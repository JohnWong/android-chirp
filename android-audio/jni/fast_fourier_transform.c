#include <math.h>
#include <stdlib.h>

double** FFT_Forward(short xr[], unsigned clipSize){

    unsigned n = clipSize;

    double *rex = (double*)malloc(sizeof(double) * n);
    double *imx = (double*)malloc(sizeof(double) * n);

    int i=0;
    for(i=0; i<n; i++){
        rex[i] = xr[i];
        imx[i] = 0.0;
    }

    int nm1 = n - 1;
    int nd2 = n / 2;
    int m = (int)(log(n)/log(2));
    int j = nd2;
    double tr, ti;
    // Bit reversal sorting
    for(i=1; i<=n-2; i++){
        if(i < j){
            tr = rex[j];
            ti = imx[j];
            rex[j] = rex[i];
            imx[j] = imx[i];
            rex[i] = tr;
            imx[i] = ti;
        }
        int k = nd2;
        while(k <= j){
            j = j - k;
            k = k / 2;
        }
        j = j + k;
    }

    // Loop for each stage
    int l;
    for(l=1; l<=m; l++){
        int le = (int)pow(2, l);
        int le2 = le / 2;
        double ur = 1;
        double ui = 0;
        double sr = cos(M_PI / le2);
        double si = -sin(M_PI / le2);
        for(j=1; j<=le2; j++){
            int jm1 = j-1;
            for(i=jm1; i<=nm1; i+=le){
                int ip = i + le2;
                tr = rex[ip] * ur - imx[ip] * ui;
                ti = rex[ip] * ui + imx[ip] * ur;
                rex[ip] = rex[i] - tr;
                imx[ip] = imx[i] - ti;
                rex[i] = rex[i] + tr;
                imx[i] = imx[i] + ti;
             } // i
             tr = ur;
             ur = tr * sr - ui * si;
             ui = tr * si + ui * sr;
        } // j
    } // l
    double **result = (double**)malloc(sizeof(double*) * 2);
    result[0] = rex;
    result[1] = imx;
    return result;
}


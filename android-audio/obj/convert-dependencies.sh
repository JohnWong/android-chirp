#!/bin/sh
# AUTO-GENERATED FILE, DO NOT EDIT!
if [ -f $1.org ]; then
  sed -e 's!^D:/develop/cygwin/lib!/usr/lib!ig;s! D:/develop/cygwin/lib! /usr/lib!ig;s!^D:/develop/cygwin/bin!/usr/bin!ig;s! D:/develop/cygwin/bin! /usr/bin!ig;s!^D:/develop/cygwin/!/!ig;s! D:/develop/cygwin/! /!ig;s!^L:!/cygdrive/l!ig;s! L:! /cygdrive/l!ig;s!^K:!/cygdrive/k!ig;s! K:! /cygdrive/k!ig;s!^E:!/cygdrive/e!ig;s! E:! /cygdrive/e!ig;s!^D:!/cygdrive/d!ig;s! D:! /cygdrive/d!ig;s!^C:!/cygdrive/c!ig;s! C:! /cygdrive/c!ig;' $1.org > $1 && rm -f $1.org
fi

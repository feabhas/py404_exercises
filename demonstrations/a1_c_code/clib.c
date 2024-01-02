#include <stdio.h>
#include <stdlib.h>

void show() {
    printf ("Hello World\n");
}

double adder(double dpar, int ipar, int* refpar) {
    *refpar = (int)(dpar + ipar);
    return dpar + ipar ;
}
    
void square(double *dst, double *src, int len) {
    int i;
    for (i=0; i<len; i++) {
        dst[i] = src[i]*src[i];
    }
}

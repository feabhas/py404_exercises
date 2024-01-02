#include <math.h>

double hero(double value) {
    double approx = -1;
    double better = value / 2.0;
    do {
        approx = better;
        better = (approx+value/approx) / 2;
    } while (fabs(better - approx) > 1e-5);
    return better;
}


    


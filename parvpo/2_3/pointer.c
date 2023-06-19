#include <stdio.h>
#include <time.h>

typedef struct Aboba
{
    int red;
    int green;
    int blue;
    int sus;
} Aboba;


int exampleFunction(Aboba *a) {
    for (int i = 0; i < 1e3; i++) {
        a->red = i;
        a->green = i;
        a->blue = i;
        a->sus = i;
    }
}

void measureExecutionTime(int (*function)(Aboba *)) {
    struct timespec startt, endt;
    double elapsed;
    clock_gettime(CLOCK_MONOTONIC, &startt);
    Aboba ab;
    for (int b=0; b < 1e6; b++) {
        exampleFunction(&ab);
    }
    // printf("Aboba?!");
    clock_gettime(CLOCK_MONOTONIC, &endt);
    elapsed = (endt.tv_sec - startt.tv_sec);
  elapsed += (endt.tv_nsec - startt.tv_nsec) / 1000000000.0;
    printf("%lf\n", elapsed);
}

int main() {
    measureExecutionTime(exampleFunction);
    return 0;
}
#include <stdio.h>
#include <time.h>

void __attribute__((stdcall)) exampleFunction(int a, int b, int c) {
    int i;
    int sum = 0;
    for (i = a; i < b; i += c) {
        sum += i;
    }
    // printf("%lld | ", sum);
}

void measureExecutionTime(void (__attribute__((stdcall)) *function)(int a, int b, int c)) {
    struct timespec startt, endt;
    double elapsed;
    clock_gettime(CLOCK_MONOTONIC, &startt);
    for (int b = 0; b < 1e6; b++) {
        function(0, 100, 1);
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

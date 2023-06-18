#include <time.h>
#include <stdio.h>
int function(int b){
    return b+1;
}
int main(){
    clock_t tic = clock();
    int a = 0;
    double b;
    double const l = 1e10;
    for(b=0; b < l; b++)
      { a = function(b); };
    clock_t toc = clock();
    printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);
    return 0;
}


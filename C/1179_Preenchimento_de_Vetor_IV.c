#include <stdio.h>

int main (){
    long long vetor[15], vPar[5], vImpar[5];
    int i, j, k, c;
    for (i = 0; i< 15; i++){
        scanf("%ld", &vetor[i]);
    }
    j = 0; k = 0;
    for (i = 0; i < 15; i++){
        if (vetor[i]%2 == 0){
            if (j < 5) {
                vPar[j] = vetor[i];
                j++;
            }
            else{
                for (c = 0; c < 5; c++){
                    printf("par [%d] = %ld\n", c, vPar[c]);
                }
                j = 0;
                vPar[j] = vetor[i];
                j ++;
            }
        }
        else{
            if (k < 5){
                vImpar[k] = vetor[i];
                k++;
            }
            else{
                for (c = 0; c < 5; c ++){
                    printf("impar [%d] = %ld\n", c, vImpar[c]);
                }
                k = 0;
                vImpar[k] = vetor[i];
                k ++;
            }
        }
    }
    if (k != 4){
        for (c = 0; c < k; c++)
            printf("impar [%d] = %ld\n", c, vImpar[c]);
    }
    if (j != 4) {
        for (c = 0; c < j; c++)
            printf("par [%d] = %ld\n", c, vPar[c]);
    }
    return 0;
}

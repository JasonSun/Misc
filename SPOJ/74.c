#include <stdio.h>
#include <math.h>

int summation[500001];

int main()
{
    int i, j;
    int nCase, num;

    summation[1] = 0;
    for (i = 2; i < 500001; i++)
        summation[i] = 1;
    for (i = 2; i <= sqrt(500000); i++) {
        summation[i * i] += i;
        for (j = i + 1; j <= 500000 / i; j++) {
            summation[i * j] += (i + j);
        }
    }
    scanf("%d", &nCase);
    for (i = 0; i < nCase; i++) {
        scanf("%d", &num);
        printf("%d\n", summation[num]);
    }
    return 0;
}

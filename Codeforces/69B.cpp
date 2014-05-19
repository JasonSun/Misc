#include <iostream>
using namespace std;

int main()
{
    int matrix[101][101];
    int profit[101];
    int max = 0, comp, index;
    int i, j, n, m, l, r, t, c;

    for (i = 1; i <= 100; i++)
        for (j = 1; j <= 100; j++)
            matrix[i][j] = 999999;
    cin >> n >> m;
    for (i = 1; i <= m; i++) {
        cin >> l >> r >> t >> c;
        for (j = l; j <= r; j++)
            matrix[i][j] = t;
        profit[i] = c;
    }
    profit[0] = 0;
    for (j = 1; j <= n; j++) {
        comp = 999999;
        index = 0;
        for (i = 1; i <= m; i++) {
            if (matrix[i][j] < comp) {
                comp = matrix[i][j];
                index = i;
            }
        }
        max += profit[index];
    }
    cout << max << endl;
    return 0;
}


#include <cstdio>
#include <map>
/*
 * In C++, STL set: Internally elements are sorted from lower to higher 
 * following specific strict weak ordering criterion set on container construction.
 *
 *
 * But in Python, built-in type SET is unordered collection of unique elements.
 *
 */
#include <set>
using namespace std;

int sequence[100001];
map<int, int> cnt; // count number of sequence[i]
set<int> record;

int main()
{
    int n, k, i;
    scanf("%d %d", &n, &k);
    for (i = 1; i <= k; i++) {
        scanf("%d", &sequence[i]);
        cnt[sequence[i]] += 1;
    }
    for (i = 1; i <= k; i++) {
        if (cnt[sequence[i]] == 1)
            record.insert(sequence[i]);
    }
    if (record.empty())
        puts("Nothing");
    else
        printf("%d\n", *record.rbegin());
    for (i = k + 1; i <= n; i++) {
        cnt[sequence[i - k]] -= 1;
        if (cnt[sequence[i - k]] == 0)
            record.erase(sequence[i - k]);
        if (cnt[sequence[i - k]] == 1)
            record.insert(sequence[i - k]);
        scanf("%d", &sequence[i]);
        cnt[sequence[i]] += 1;
        if (cnt[sequence[i]] == 1)
            record.insert(sequence[i]);
        if (cnt[sequence[i]] == 2)
            record.erase(sequence[i]);
        if (record.empty())
            puts("Nothing");
        else
            printf("%d\n", *record.rbegin());
    }

    return 0;
}

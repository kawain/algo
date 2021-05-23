/*
10進数を2進数に変換するには、スタックを用意して  

10進数を2で割り算する
余りをスタックにpush  
10進数＝先程の商　　
を繰り返し  
10進数が0になったら終了  

その後、スタックからpopしながら並べると2進数になる
*/
#include <stdio.h>
#include <stdlib.h>
int main()
{
    printf("Decimal input: ");
    int decimalNum;
    if (scanf("%d", &decimalNum) != 1)
    {
        fprintf(stderr, "err\n");
        exit(1);
    }
    // 求めたい2進数の最大桁数分の配列
    int arr[256];
    int i = 0;
    while (decimalNum > 0)
    {
        // 余り(2の割り算なので0か1しかない)
        int amari = decimalNum % 2;
        // 余りを配列にpush
        arr[i] = amari;
        // 商(小数点以下は切り捨て)
        int shou = decimalNum / 2;
        // 商を代入
        decimalNum = shou;

        i++;
    }
    // 後ろから表示
    i--;
    while (i >= 0)
    {
        printf("%d", arr[i]);
        i--;
    }
    printf("\n");
}
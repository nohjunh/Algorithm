#include <iostream>
using namespace std;

#define MAX 500

int multiply(int x, int res[], int res_size);

void factorial(int n)
{
   int result[MAX]; // 계산 결과 1자릿수를 계속 저장해줄 배열

   result[0] = 1; // 시작은 1부터 
   int result_size = 1; // 1부터 시작이니 당연히 result_size도 1부터

   for (int x = 2; x <= n; x++) // n!= 1*2...*n
       // result값은 배열에 각 자리수마다 저장될 것
       // result_size는 매 multiply마다 자릿수에 따라 수 업데이트 시켜야 함.
       result_size = multiply(x, result, result_size);

      // 계산결과 총 몇자리가 되는지 result_size로 리턴 받음    

   for (int i = result_size -1;  i >= 0;  i--) // 맨뒤부터 저장되므로 반대로 출력하기 위함.
       cout << result[i];
}

int multiply(int x, int result[], int result_size){
   int carry = 0; // Initialize carry

   for (int i = 0; i < result_size; i++) {
       int prod = result[i] * x + carry; // 자리올림 수까지 더해야 함.

       result[i] = prod % 10; // 자리 올림하고 남은 수가 당연히 밑에 내려올 것이다.

       carry = prod / 10; // 자리 올림 수
   }

   // 연산이 모두 끝난후 result_size를 넘어간 carry가 있다면
   // 그 carry를 처리해주기 위함.
   while (carry) {
       result[result_size] = carry % 10;
       carry = carry / 10;
       result_size++;
   }
   return result_size;
}

int main()
{
   int n;
   cin >> n;

   factorial(n);
   return 0;
}
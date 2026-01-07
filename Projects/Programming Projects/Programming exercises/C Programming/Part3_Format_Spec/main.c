#include <stdio.h>

int main() {
  // Format Specifier = Special tokens that begin with a % symbol
  //                    followed by a character that specifies the data type
  //                    and optional modifier (width,precision,flags).
  //                    They control how data is displayed or interpreted

  int age = 25;
  float price = 19.99;
  double pi = 3.1415926535;
  char currency = '$';
  char name[] = "Benedict Angelo";

  printf("%d\n", age);
  printf("%f\n", price);
  printf("%lf\n", pi);
  printf("%c\n", currency);
  printf("%s\n", name);

  // width = specifies the minimum numbers to print
  //          it includes the spaces

  int num1 = 1;
  int num2 = 10;
  int num3 = 100;
  int num4 = +1000;
  int num5 = -10000;

  printf("%4d\n", num1);  // left justified
  printf("%-4d\n", num2);  // right justified
  printf("%04d\n", num3);  // Lead zero instead of spaces
  printf("%+4d\n", num4);  // positive
  printf("%+4d\n", num5);  // still negative
  
  // precision
  // floats default to displaying 6 decimals points
  float price1 = 19.99;
  float price2 = 1.50;
  float price3 = -100.00;

  printf("%.1f\n", price1);
  printf("%+.2f\n", price2);
  printf("%+6.2f\n", price3);





  return 0;
}

#include <stdio.h>
#include <string.h>

int main() {

  // Shopping Cart  
  char item[50] = "";
  float price = 0.0f;
  int quantity = 0;
  char currency = '$';
  float total = 0.0f;

  printf("What item would you like to buy?: ");
  fgets(item, sizeof(item), stdin);
  item[strlen(item) -1] = '\0';

  printf("What is the price of item?: ");
  scanf("%f", &price);

  printf("How many would you like to buy?: ");
  scanf("%d", &quantity);

  total = price * quantity;

  printf("You have bought: %d %s", quantity, item);

  printf("\nYou total is: \n");
  printf("%c%.2f", currency, total);

  







  return 0;
}

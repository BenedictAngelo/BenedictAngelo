#include <stdio.h>
#include <stdbool.h> // for boolean

int main(void){

    // Variables = A reusable container for a value
    // int = whole numbers (4 bytes in modern systems)
    // float = single-precision decimal number (4 bytes)
  // double = double-precision decimal number (8 bytes)
  // char = single character (1 byte)
  // char[] = array of characters or string (size varies)
  // bool = true or false (1 byte and requires #include <stdbool.h>)
  
  
    // integers sample
    // "%d" means decimal
    int age = 24;
    int year = 2026;
    printf("I am %d years old\n", age); // "\n" for new line
    printf("It is year %d\n", year);

    // float examples
    // "%f" for float
    // defaults to displaying 6 digits
    float money = 50.5;
    float gpa = 2.5;
    printf("I only have %fAED in my pocket\n", money);
    printf("My GPA is %.1f\n", gpa); // specify how many decimal value to display
  
    // double examples
    // "%lf" means long float
    // long float deals deals with 15 to 16 decimal points
    double pi = 3.14159265358979;
    printf("The value of pi is: %.15lf\n", pi);

    // char examples
    // "%c" means character
    char grade = 'A'; // must be enclosed with ''
    printf("Your grade is '%c' on the test\n", grade);

    // Arrays also called strings, examples
    // "%s" means string
    char name[] = "Benedict Angelo"; //must be enclosed with ""
    printf("Hi, my name is %s\n", name);

    // boolean examples
    //  "%d" means bool
    bool isOnline = true; // can also be '1' for true or '0' for false
    printf("%d\n", isOnline);
    if(isOnline){
        printf("You are ONLINE\n");
  }
    else{
        printf("You are OFFLINE\n");
  }

    return 0;
}

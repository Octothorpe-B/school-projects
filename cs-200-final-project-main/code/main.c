/* Main C file to store and convert binary, decimal, and hexadecimal values by calling convert to functions in separate C files. */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "convert_hexadecimal.c"
#include "convert_binary.c"
#include "convert_decimal.c"

int b_to_decimal(int[]);
int b_to_hexadecimal(int[]);
int d_array_to_binary(int[]);
int d_int_to_binary(int);
int d_to_hexadecimal(int[]);
unsigned long h_to_binary(char[]);
int h_to_decimal(char[]);

/*
Function to run all of the conversion functions in their separate corresponding C files.
*/
int main() {
    // Initialize variables that control the size of the dynamic array, the inputted number, convert to decisions, etc.
    int array_size, conversion_decision, conversion_to_decision, input_number, input_conversion_number = 4;
    // Get the array size from the user to dynamically increase the size of the array.
    printf("Enter the size of the digits of your number as an int value!\n(Dev Note: Enter 8 to get working output, 4 for hexadecimal) ");
    scanf("%d", &array_size);
    // Create a dynamic array based on the malloc function, which is the most memory efficient dynamic array implementation in C!.
    int *input = (int *)malloc(array_size * sizeof(int));
    printf("Enter:\n[1] Convert a binary number.\n[2] Convert a decimal number.\n[3] Convert a hexadecimal number.\n[4] exit.\n");
    scanf("%d", &conversion_decision);
    // Check if the user chooses to convert a binary number.
    if (conversion_decision == 1) {
        // collect user's binary number
        printf("\nBinary Number Selected!\n\nEnter an eight bit binary number:");
        scanf("%d", &input_number);

        input_conversion_number = input_number;
        // Convert number into input array.
        for (int i = 0; i < array_size; i++) {
            *(input+i) = input_number % 10;
            input_number /= 10;
        }
        // Reverse the array to match the correct order that the user inputted.
        for (int i = 0; i < array_size/2; i++) {
            int temp_array_value = input[i];
            input[i] = input[array_size - 1 - i];
            input[array_size - 1 - i] = temp_array_value;
        }
        // Check what the user will convert binary number to
        printf("\nHow should your binary number be converted?\nEnter:\n[1] Convert to decimal.\n[2] Convert to hexadecimal.\n[ ] or any other number to exit.");
        scanf("%d", &conversion_to_decision);
        // Check if user chooses to convert binary number to decimal
        if (conversion_to_decision == 1) {
            printf("\nConverting to decimal...");
            int output = b_to_decimal(input);
            printf("\nThe converted binary number = %d\n", output);
        }
         // Check if user chooses to convert binary number to hexadecimal
        if (conversion_to_decision == 2) {
            printf("\nConverting to hexadecimal...");
            int output = b_to_hexadecimal(input);
            // printf("\nThe converted binary number = %d\n", output);
        }
        // Check if user chooses to exit program
        else {
            return 0;
        }
    }
    // Check if the user chooses to convert a decimal number.
    else if (conversion_decision == 2) {
        // collect user's decimal number
        printf("\nDecimal Number Selected!\n\nEnter a decimal number:");
        scanf("%d", &input_number);

        input_conversion_number = input_number;
        // Convert number into input array.
        for (int i = 0; i < array_size; i++) {
            *(input+i) = input_conversion_number % 10;
            input_conversion_number /= 10;
        }
        // Reverse the array to match the correct order that the user inputted.
        for (int i = 0; i < array_size/2; i++) {
            int temp_array_value = input[i];
            input[i] = input[array_size - 1 - i];
            input[array_size - 1 - i] = temp_array_value;
        }
        // Check what the user will convert decimal number to.
        printf("\nHow should your decimal number be converted? Enter:\n[1] Convert to binary.\n[2] Convert to hexadecimal.\n[ ] or any other number to exit.");
        scanf("%d", &conversion_to_decision);
        if (conversion_to_decision == 1) {
            printf("\nConverting to binary...");
            int output = d_array_to_binary(input);
            printf("\nThe converted decimal number = %d\n", output);
        }
        if (conversion_to_decision == 2) {
            printf("\nConverting to hexadecimal...");
            int output = d_to_hexadecimal(input);
            // printf("\nThe converted decimal number = %d\n", output);
        }
        else {
            return 0;
        }
    }
    // Check if the user chooses to convert a hexadecimal number.
    else if (conversion_decision == 3) {
        char hexadecimal_input[5];
        char temp_value;
        // collect user's hexadecimal number.
        printf("\nHexadecimal Number Selected!\n\nEnter a hexadecimal number (Most Significant Digit First):\n");
        for (int i = 0; i < array_size; i++) {
            printf("Enter digit %d: ", i);
            scanf(" %c", &temp_value);
            hexadecimal_input[i] = temp_value;
            printf("You entered: %c\n", hexadecimal_input[i]);
        }
        // Check what the user will convert hexadecimal number to.
        printf("\nHow should your hexadecimal number be converted? Enter:\n[1] Convert to binary.\n[2] Convert to decimal.\n[] or any other number to exit. ");
        scanf("%d", &conversion_to_decision);
        if (conversion_to_decision == 1) {
            printf("\nConverting to binary...");
            long output = h_to_binary(hexadecimal_input);
            printf("\nThe converted hexadecimal number = %ld\n", output);
        }
        if (conversion_to_decision == 2) {
            printf("\nConverting to decimal...");
            long output = h_to_decimal(hexadecimal_input);
            printf("\nThe converted hexadecimal number = %ld\n", output);
        }
        else {
            return 0;
        }
    }
    // If any other number is first chosen then the program will stop.
    else {
        return 0;
    }
}
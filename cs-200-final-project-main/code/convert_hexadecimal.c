/* C program to convert a hexadecimal number to binary or decimal. */
int d_int_to_binary(int);

/* 
Function to convert a hexadecimal number into a binary number.
Note: This currently only works for a char array with a length of 4 elements.
*/
unsigned long h_to_binary(char input[]) {
    unsigned long hexadecimal_num = 0;
    char binary_array[32];
    int temp_array[4];
    int binary_num;

    for (int i = 0; i < 4; i++) {
        // Check for uppercase A-F numbers.
        if (input[i] >= 'A' && input[i] <= 'F') {
            temp_array[i] = input[i] - 55;
        }
        // Check for lowercase A-F numbers. 
        else if (input[i] >= 'a' && input[i] <= 'f') {
            temp_array[i] = input[i] - 87;
        }
        // Check for if the inputted digit is 0-9.
        else if (input[i]-48 >= 0 && input[i]-48 < 10) {
            temp_array[i] = input[i] - 48;
        }
    }
    // Perform the conversion for hexadecimal to decimal.
    for (int i = 0; i < 4; i++) {
        binary_num = temp_array[i];
        binary_num = d_int_to_binary(binary_num);
        // Break down the converted binary number into an array of type char.
        for (int i = 0; i < 4; i++) {
            binary_array[i] = binary_num % 10;
            binary_num /= 10;
        }
        // Reverse the array.
        for (int i = 0; i < 4/2; i++) {
            int temp_array_value = binary_array[i];
            binary_array[i] = binary_array[4 - 1 - i];
            binary_array[4 - 1 - i] = temp_array_value;
        }
        // Concatenate the digits in the char array into one variable of type long.
        for (int i = 0; i < 4; i++) {
            hexadecimal_num *= 10;
            hexadecimal_num += binary_array[i];
        }
    }
    return hexadecimal_num;
}

/* 
Function to convert a hexadecimal number into a decimal number.
Note: This currently only works for a char array with a length of 4 elements.
*/
int h_to_decimal(char i_input[]){
    int hexadecimal_num = 0;
    int value = 0;
    char input[4];
    int length = 3;

    for (int i = 0; i < 4; i++) {
        input[i] = (char) i_input[i];
    }
    // Initial implementation of capturing hexadecimal number.
        for (int i = 0; i < 4; i++) {
            // Check for uppercase A-F numbers.
            if (input[i] >= 'A' && input[i] <= 'F') {
                value = input[i] - 55;
            }
            // Check for lowercase A-F numbers. 
            else if (input[i] >= 'a' && input[i] <= 'f') {
                value = input[i] - 87;
            }
            // Check for if the inputted digit is 0-9.
            else if (input[i]-48 >= 0 && input[i]-48 < 10) {
                value = input[i] - 48;
            }
            hexadecimal_num += value * pow(16, length);
            length--;
        }
    //4660 :-)
    return hexadecimal_num;
}

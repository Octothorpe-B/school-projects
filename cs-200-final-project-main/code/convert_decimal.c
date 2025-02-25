/* C program to convert a decimal number to binary or hexadecimal. */

/* Function to convert a decimal number stored in an array of type int into a binary number. */
int d_array_to_binary(int input[]) {
    int decimal_num = 0;
    // Convert array contents into int variable decimal_num.
    for (int i = 0; i < 8; i++) {
        decimal_num *= 10;
        decimal_num += input[i];
    }
    printf("%d", decimal_num);
    int bit = 0;
    unsigned long binary_num = 0;
    int remain = 1;
    // convert decimal_num to binary
    while(decimal_num) {
        bit = decimal_num % 2;
        decimal_num = decimal_num / 2;
        binary_num += bit * remain;
        remain = remain * 10;
    }
    printf("%lu", binary_num);
    return binary_num;
}

/*
Function to convert a decimal int variable into a binary number. 
*/
int d_int_to_binary(int decimal_num) {
    int bit = 0;
    unsigned long binary_num = 0;
    int remain = 1;
    int binary_array[4];
    // convert decimal_num to binary
    while(decimal_num) {
        bit = decimal_num % 2;
        decimal_num = decimal_num / 2;
        binary_num += bit * remain;
        remain = remain * 10;
    }
    //printf("Binary Number: %lu\n", binary_num);
    //printf("\nBN %lu\n", binary_num);
    return binary_num;
}

/*
Function to convert a decimal number into a hexadecimal number.
*/
int d_to_hexadecimal(int input[]) {
    int decimal_num = 0;
    // Convert array contents into int variable decimal_num.
    for (int i = 0; i < 8; i++) {
        decimal_num *= 10;
        decimal_num += input[i];
    }
    
    int q, remain;
    int i, j = 0;
    char hex_num[100];

    q = decimal_num;
    while (q != 0) {
        remain = q % 16;
        if (remain < 10)
            hex_num[j++] = 48 + remain;
        else 
            hex_num[j++] = 55 + remain;
        q = q / 16;        
    }
    printf("\n");
    printf("The converted decimal number = ");
    for (i = j; i >= 0; i--) {
        printf("%c", hex_num[i]);
    }
    return 0;
}
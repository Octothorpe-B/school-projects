/* C program to convert a binary number to decimal or hexadecimal. */

/*
Function to convert a binary number into a decimal number.
*/
int b_to_decimal(int input[]) {
    int binary_num = 0;
    // Convert array contents into int variable binary_num.
    for (int i = 0; i < 8; i++) {
        binary_num *= 10;
        binary_num += input[i];
    }
    // convert binary_num to decimal
    int bit = 0;
    int remain = 0;
    unsigned long decimal_num = 0;
    int temp = binary_num;
    while(temp != 0) {
        bit = temp % 10;
        if (bit) {
            decimal_num += pow(2, remain);
        }
        temp = temp / 10;
        remain++;
    }
    return decimal_num;
}

/*
Function to convert a binary number into a hexadecimal number.
*/
int b_to_hexadecimal(int input[]) {
    int decimal_num = b_to_decimal(input);
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
    printf("The converted binary number = ");
    for (i = j; i >= 0; i--) {
        printf("%c", hex_num[i]);
    }
    return 0; //how to return hex_num[i] ??
}
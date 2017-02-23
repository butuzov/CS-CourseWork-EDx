/****************************************************************************
 * credit.c
 *
 * The objective of this application is  to use the greedy algorithm to display
 * the least amount of coins that can be used in USD for change owed.
 *
 * Usage        : ./credit
 * Description  : http://docs.cs50.net/problems/credit/credit.html
 * Testing      : check50 2016.credit credit.c
 ***************************************************************************/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int is_valid_luhn( char *card_number_as_string, int card_digits);
int ancii_2_int( int ancii_code_of_number );

int main(void){

    //Get card number from user
    printf("Number: ");
    long long number = GetLongLong();

    // Checking how long is the number (in chars!)
    int card_digits = (int) log10( number ) + 1;
    // Creating array of chars (string)
    char card_number_as_string[ card_digits +1 ];
    // Assigning/Converting number to string
    sprintf(card_number_as_string, "%lld", number);

    if ( is_valid_luhn( card_number_as_string, card_digits ) == 1 ) {

        int amex[2] = {37, 34};
        int mastercard[5] = {51, 52, 53, 54, 55};

        // First to Numbers of card as summ of first number multiplied by 10 and second number.
        int first_two = ancii_2_int( card_number_as_string[0] ) * 10
            + ancii_2_int( card_number_as_string[1] );

        // IS AMEX?
        for ( int i = 0; i < sizeof(amex); i++) {
            if ( first_two == amex[i] && card_digits == 15 ) {
                printf("AMEX\n");
                return 0;
            }
        }

        // IS MASTERCARD?
        for ( int i = 0; i < sizeof(mastercard); i++) {
            if ( first_two == mastercard[i] && card_digits == 16 ) {
                printf("MASTERCARD\n");
                return 0;
            }
        }

        // IS VISA?
        if ( ancii_2_int( card_number_as_string[0] ) == 4
                && ( card_digits == 16 || card_digits == 13 ) ) {
            printf("VISA\n");
            return 0;
        }
    }

    printf( "INVALID\n" );
    return 0;
}

// Validating Credit Card Number using Luhn algoritm
// https://en.wikipedia.org/wiki/Luhn_algorithm
int is_valid_luhn( char *card_number_as_string, int card_digits) {

    // Declaring even and odd variables.
    int odd = 0, even = 0;

    // iterating card number in reverse order.
    for ( int i = card_digits - 1, j = 2; i >= 0; i--, j++ ) {

        int num = ancii_2_int( card_number_as_string[i] );

        if ( j % 2 == 1) {
            num *= 2;
            even += ( num / 10 >= 1 ) ? ( 1 + ( num % 10 ) ) : num;
        } else {
            odd += num;
        }
    }

    return ( odd + even ) % 10 == 0 ? 1 : 0;
}

// Convert char (ansii code) to actual int (in range 0..9)
int ancii_2_int ( int ancii_code_of_number ) {
    return ( ancii_code_of_number + 2 ) % 10;
}

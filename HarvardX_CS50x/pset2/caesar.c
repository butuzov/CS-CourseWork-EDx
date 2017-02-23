/****************************************************************************
 * caeser.c
 *
 * Implement a program that encrypts messages using Caesar’s cipher.
 *
 * Usage        : ./caesar n
 * Description  : http://docs.cs50.net/problems/caesar/caesar.html
 * Testing      : check50 2016.caesar caesar.c
 ***************************************************************************/

#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main( int argc, string argv[] ) {

    int num;

    // Everything that require input, gonna be tested with preenterd values.
    // Change `debug` to 0 in `production`
    int debug = 0;

    // Getting Data from User.
    if ( debug == 0 ) {

        if ( argc == 2 ) {
            // Using sscanf to assign variable to num
            sscanf( argv[1], "%d", &num);
        } else {
            printf("Usage: ./caesar k\n");
            return 1;
        }

    } else {
        num = 25;
    }

    // Shifting Num back to correct number (less than 26 )
    num = num % 26;

    // Creating Array for substitutes.
    char ABC[26], abc[26];

    // Filling aour array by values.
    for ( int i = 0; i < 26; i++) {
        ABC[i] = 65 + i;
        abc[i] = 97 + i;
    }

    printf("plaintext:");
    string s = GetString();
    int n = strlen(s);

    char encrypted[n];
    int encrypted_index = 0;

    // Lets encrypt it!
    for ( int i = 0; i < n; i++ ) {
        int found = 0;

        for (int j = 0; j < 26; j++ ) {
            int index = j + num;

            // rewind
            if ( index >= 26 ) {
                index  -= 26;
            }

            // Encrypting UPPERCASED char
            if ( s[i] == (char) 65 + j  ) {
                found = 1;
                encrypted[ ( encrypted_index++ ) ] = (char) 65 + index;
            }

            // Encrypting LOWERCASED char
            if ( s[i] == (char) 97 + j ) {
                found = 1;
                encrypted[ ( encrypted_index++ ) ] = (char) 97 + index;
            }
        }

        // char doesn't require to be encrypted.
        if ( found == 0 ) {
            encrypted[ ( encrypted_index++ ) ] = s[i];
        }
    }

    // Print result
    printf("ciphertext: %s\n", encrypted);
    return 0;
}

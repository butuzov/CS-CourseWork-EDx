/****************************************************************************
 * vigenere.c
 *
 * Implement a program that encrypts messages using Vigenère’s cipher.
 *
 * Usage        : ./vigenere codeword
 * Description  : https://cdn.cs50.net/2014/x/psets/2/pset2/pset2.html#_parlez_vous_fran_ais
 * Testing      : check50 2014/x/pset2/vigenere vigenere.c
 ***************************************************************************/

#include <stdio.h>
#include <string.h>
#include <cs50.h>

// Kinda hack, kinda global pointer.
// memory allocation after we know the length of the
// chipher.
int * codes;

int main( int argc, string argv[] ) {

    // Debug related variables.
    int debug = 0;
    char word[] = "baz";

    // terminating program.
    if ( debug == 0 && argc != 2 ) {
        printf("Usage: ./vigenere k\n");
        return 1;
    }

    // Computing "steps"

    int cipherlenght = strlen( debug == 0 ? argv[1] : word );
    codes = malloc( sizeof(char) *  cipherlenght );

    for ( int i = 0; i < cipherlenght; i++ ) {

        int code = debug == 0 ? argv[1][i] : word[i];

        // If code not in range of a..z or A..Z, de terminating execution.
        // ane exiting pro
        if (  code < 65 || code > 122 || ( code > 90 && code < 97 ) ) {
            // but first lets free some memory.
            free(codes);
            // error message
            printf("Usage: ./vigenere k\n");
            return 1;
        }

        for (int j = 0; j < 26; j++ ) {
            // createing "steps"
            if ( code == (char) ( 65 + j ) || code == (char) ( 97 + j ) ) {
                codes[i] = j;
            }
        }
    }

    // Getting From User ( with debug enabled feature!!! )
    // printf("plaintext: "); // 2016 CS50 version
    string s = ( debug == 0 ) ? GetString() : "world, say hello!";

    if ( debug == 1 ) {
        printf("%s\n", s);
    }

    // Length of String
    int palintext_lenght = strlen(s);

    // Array of encrypted chars
    char * encrypted = malloc( sizeof(char) * palintext_lenght );

    // Inital indexes
    int encrypted_index = 0, index = 0;

    // Crypting String
    for ( int i = 0; i < palintext_lenght ; i++ ) {
        int found = 0;

        for (int j = 0; j < 26; j++ ) {

            // Encrypting UPPERCASED char
            if ( s[i] == (char) 65 +j  ) {
                found = 1;
                encrypted[ ( encrypted_index++ ) ] = (char) 65 + ( codes[index] + j ) % 26 ;
            }

            // Encrypting LOWERCASED char
            if ( s[i] == (char) 97 + j ) {
                found = 1;
                encrypted[ ( encrypted_index++ ) ] = (char) 97 + ( codes[index] + j ) % 26;
            }
        }

        if ( found == 0 ) {
            // Do not encrypt this char.
             encrypted[ ( encrypted_index++ ) ] = s[i];
        } else {
            // incrementing index or receting it to zero in case if cipher ended.
            index = ++index >= cipherlenght ? 0 : index;
        }
    }

    // Print result
    printf("%s\n", encrypted );

    free(encrypted);

    return 0;
}

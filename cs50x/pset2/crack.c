/****************************************************************************
 * crack.c
 *
 * Cracks passwords that have been encrypted with C’s DES-based crypt function
 *
 * Usage        : ./crack hash
 *
 * Description  : http://docs.cs50.net/problems/crack/crack.html
 ***************************************************************************/

#define _XOPEN_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <cs50.h>


// Length of the checked password/
int max_password_ln = 4;

// Declaring global index of dictionary
// work as array index but for string.
int password_str_index = 0;

/**************************************************************************
 *	Function Prototypes
 *************************************************************************/

// Return a length of array of symbols used to generate password.
int dictionary_of_chars_length( int isUp, int isLow, int isNum );

// Return array of chars that can be used to generate password.
// Used to simplify password.
// in production can use a-zA-Z0-9+ other special characters.
void dictionary_of_chars( int Chars[], int isUp, int isLow, int isNum  );

// Create a String Of Passwords.
// Guess I willnever get used to passing array only as Pointer in C
 void dictionary_fill_with_words( char Dictionary[], int Chars[],
        int Chars_ln, int password_ln,
            int cur_sub_index, string word );

int main( int argc, char *argv[] ) {

    // In case of debug = 0, script will accept and cehck input hash password.
    int debug = 0;

    // Pre Definition of password generating patterns.
    int isUp = 0, isLow = 0, isNum = 0;

    // Password Placeholder
    char * Password;
    if ( debug == 0 && argc != 2 ) {
        printf("Usage: ./crack hash\n");
        return 1;
    } else if ( debug == 0 ) {
        // debug mode of
        isLow = 1; // All Uppercase
        isUp = 1; // All lowercase
        isNum = 0; // all Numbers
        // Pouring water from glass to other glass.
        // Just to fit dev env.
        Password = malloc( ( sizeof( char ) * strlen( argv[1] ) ) + 1 );
        strncpy(Password, argv[1], (int)  strlen( argv[1] ) + 1 );
        Password[ (int) strlen( argv[1] ) ] = (char)0;
    } else {
        // debug mode on
        isLow = 1;
        isUp = 1;
        isNum = 0;
        // Storing Pass to debug var...
        char debug_password_string[] = "50QvlJWn2qJGE";
        Password = malloc( ( sizeof( char ) * strlen( debug_password_string ) ) + 1 );
        strncpy(Password, debug_password_string, (int) strlen( debug_password_string ) + 1 );
        Password[ (int) strlen( debug_password_string ) ] = (char)0;
    }


    // Init
    char * Salt;
    Salt = (char*) malloc( 3 );
    strncpy(Salt, Password, 2 );
    Salt[2] = (char)0;

    // Calculating Length of array of symbols we can use to generate password.
    // We can add additional symbols without huge problem.
    int Chars_ln  = dictionary_of_chars_length( isUp, isLow, isNum );
    int *Chars;
    Chars = malloc( sizeof( int ) * ( Chars_ln ) );
    dictionary_of_chars( Chars,isUp,isLow,isNum );
    // chekc this symbols
    // for( int i =0; i < Chars_ln ; i++) {
    //     printf("%c ", Chars[i]);
    // }
    // printf("\n");

    for ( int password_ln = 1; password_ln <= max_password_ln; password_ln++ ) {

        password_str_index = 0;

        // Number of "words" in "wordlist".
        int32_t total_passwords = (int) pow( (float) Chars_ln, (float) password_ln );

        // Length of dictionary string
        int dictionary_string_ln = total_passwords * password_ln;
        //printf("\nlen of word list is %i\n", dictionary_string_ln);
        //
        // // Init
        char * Dictionary = 0;
        Dictionary = (char*) malloc( dictionary_string_ln );
        // //
        // // // empty string
        string init_pass = "";
        // // Creating String of passwords
        dictionary_fill_with_words( Dictionary, Chars, Chars_ln, password_ln, 0,  init_pass);

        // /***************************************************************
        //   Now after we have a nice super long string of passwords lets
        //   read it one by one, and compare it to input.
        // ****************************************************************/

        int n = password_ln +  1;
        //
        //
        for ( int i =0; i < total_passwords; i++) {
            char * Word = 0;
            Word = (char*) malloc( password_ln + 1 );
            strncpy(Word, Dictionary+(i*password_ln), password_ln);
            Word[password_ln] = (char)0;

            if ( strcmp( crypt(Word, Salt), Password) == 0 ) {

                /*
                 * In case if you going to run this script for different
                 * login:pass lists here is sexy bash one liner for you.
                 *  `cat crack.txt | awk '{split($0,a,":"); print  a[2]}' | xargs -L1 ./crack`
                 *  and use this printf function instead a one used by conditions of
                 *  task - printf("Pass %s is - %s\n", Password, Word);
                 */
                printf("%s\n", Word);

                // Free Resources.
                free( Chars );
                free( Dictionary );
                free( Password );
                free( Word );
                free( Salt );

                return 0;
            }

            free( Word );
        }

        free( Dictionary );
    }

    free( Chars );
    free( Password );
    free( Salt );

    printf("Pass Not Found");
    return 1;
}

/*
 * Dictionary generation.
 * its actually pain in a ass, so we using only array of chars
 * due we shecking the words of fixed length its not the issue)
 */

void dictionary_fill_with_words( char Dictionary[], int Chars[],
        int Chars_ln, int password_ln,
        int cur_sub_index, string word ) {

   if ( cur_sub_index == password_ln ) {
        // password_str_index is our global variable.
        for ( int i = password_str_index * password_ln, j = 0;
                i < ( password_str_index * password_ln) + password_ln ; i++, j++ ){
          Dictionary[i] = word[j];
        }

        // incrementing.
        password_str_index++;
	 } else {
        // incrementing for NEXT level...
        int next_sub_index = cur_sub_index + 1;

        // For All characters in array.
        char new_word[next_sub_index];
        for( int i = 0; i < Chars_ln; i++ ) {

              char new_word[next_sub_index];
              int word_i = 0;

              if ( strlen(word) != 0 ) {
                  for( word_i = 0; word_i < next_sub_index; word_i++ ){
                      new_word[word_i] = word[word_i];
                  }
              }
            new_word[cur_sub_index] = Chars[i];
            dictionary_fill_with_words( Dictionary, Chars, Chars_ln, password_ln, next_sub_index, new_word );
        }
	}
}


void dictionary_of_chars( int Chars[], int isUp, int isLow, int isNum ) {
    int length = dictionary_of_chars_length ( isUp, isLow, isNum );
    int index = 0;

    if ( isUp ) {
        // printf("Adding Uppercase Chars \n");
        for (int i = 0; i <= 25 ; i++ ) {
            Chars[ index++ ] = 65 + i; // 48 is 0 in ancii
        }
    }
    if ( isLow ) {
        // printf("Adding Lowercase Chars \n");
        for (int i = 0; i <= 25 ; i++ ){
            Chars[ index++ ] = 97 + i; // 48 is 0 in ancii
        }
    }
    if ( isNum ) {
        for (int i = 0; i <= 9 ; i++ ){
            Chars[ index++ ] = 48 + i; // 48 is 0 in ancii
        }
    }
}


int dictionary_of_chars_length ( int isUp, int isLow, int isNum ) {
    // initial placeholder for
    int dictionary_chars_length = 0;

    if ( isUp )
        dictionary_chars_length += 26;
    if ( isLow )
        dictionary_chars_length += 26;
    if ( isNum )
        dictionary_chars_length += 10;

    return dictionary_chars_length;
}

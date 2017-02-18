/*****************************************************************
 * generate.c
 *
 * Generates pseudorandom numbers in [0,MAX), one per line.
 *
 * Usage: generate n [s]
 *
 * where n is number of pseudorandom numbers to print
 * and s is an optional seed
 ****************************************************************/

#define _XOPEN_SOURCE

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// upper limit on range of integers that can be generated
#define LIMIT 65536

int main(int argc, string argv[]) {
    // We can accept 1 or 2 arguments (assuming that program name isn't argument)
    // if we have just a program name as argument or we have more then 2 additional
    // arguments - exiting with an error.
    if (argc != 2 && argc != 3) {
        printf("Usage: ./generate n [s]\n");
        return 1;
    }

    // A correct way to convert string/char to number.
    int n = atoi(argv[1]);

    // if provided second argument (3rd if count program name).
    // we usign it as a seed instead time for our RNG
    if ( argc == 3 ) {
        srand48( (long) atoi(argv[2]) );
    } else {
        srand48( (long) time(NULL));
    }

    // Generate n numbers using RNG and print it to screen
    for ( int i = 0; i < n; i++ ) {
        printf("%i\n", (int) ( drand48() * LIMIT ) );
    }

    // success
    return 0;
}

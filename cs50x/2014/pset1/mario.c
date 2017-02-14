/****************************************************************************
 * mario.c
 *
 * Printing One size of mario pyramide.
 * Usage        : ./mario
 * Description  : http://docs.cs50.net/problems/mario/more/mario.html
 * Testing      : check50 2014.fall.pset1.mario mario.c
 ***************************************************************************/

#include <stdio.h>
#include <cs50.h>

// declaring a function for printing.
void print( char CharToPrint, int Times );

int main( void ) {
    int n;

    do {
        printf("Height: ");
        n = GetInt();
    } while ( n < 0 || n > 23 );

    // Printing Pyramid.
    for ( int line = 1; line <= n; line++ ) {
        print( ' ',  n - line);
        print( '#',  line + 1);
        print( '\n',  1);
    }

    return 0;
}

void print( char CharToPrint, int Times ) {
    for ( int i = 0; i < Times; i++ ){
        printf( "%c", CharToPrint );
    }
}

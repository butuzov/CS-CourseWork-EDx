/****************************************************************************
 * mari.c
 *
 * Printing of custom Mario pyramide.
 * Usage        : ./mario
 * Description  : http://docs.cs50.net/problems/mario/more/mario.html
 * Testing      : check50 2016.mario.more mario.c
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
        print( ' ',  n - line );
        print( '#',  line);
        print( ' ',  2);
        print( '#',  line);
        print( '\n',  1);
    }

    return 0;
}

void print( char CharToPrint, int Times ) {
    for ( int i = 0; i < Times; i++ ){
        printf( "%c", CharToPrint );
    }
}

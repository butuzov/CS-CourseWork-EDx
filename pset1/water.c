/****************************************************************************
 * water.c
 *
 * Ask user for a number of minutes and prints number of bottles .
 *
 * Usage        : ./water
 * Description  : http://docs.cs50.net/problems/water/water.html
 * Testing      : check50 2016.water water.c
 ***************************************************************************/

#include <stdio.h>
#include <cs50.h>

int main( void ) {
    int n;
    printf( "Minutes: " );
    n =  GetInt();

    if ( n > 0 ) {
        printf( "Bottles: %i\n", n * 12 );
        return 0;
    }

    printf( "User failed to enter minutes number. Bad User!\n" );
    return 1;
}

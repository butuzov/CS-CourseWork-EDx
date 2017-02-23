/****************************************************************************
 * greedy.c
 *
 * The objective of this application is  to use the greedy algorithm to display
 * the least amount of coins that can be used in USD for change owed.
 * 
 * Usage        : ./greedy
 * Description  : http://docs.cs50.net/problems/greedy/greedy.html
 * Testing      : check50 2016.greedy greedy.c
 ***************************************************************************/

#include <stdio.h>
#include <cs50.h>

int main( void ) {

    float num; // Input Amount of money
    int left; // How much money left?

    do {
        printf( "O hai! How much change is owed?\n" );
        num = GetDouble();
    } while ( num < 0.0 );

    // Well, its a way to convert float to to int.
    left = (int) ( num * 1000 ) / 10;

    int coins[4] = { 25, 10, 5, 1 };
    int result   = 0; // Storing coins number here.

    // Going in for loop
    for ( int i = 0; i < sizeof( coins ) / sizeof ( int ) ; i++ ) {
        result += left / coins[i]; // so how many coins do we need for this?
        left = left % coins[i]; // adn assigning to left what is left after division
    }

    printf( "%i\n", result ); // output result.
}

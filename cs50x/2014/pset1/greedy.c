/****************************************************************************
 * greedy.c
 *
 * The objective of this application is  to use the greedy algorithm to display
 * the least amount of coins that can be used in USD for change owed.
 *
 * Note         : This is alternative solution for greedy.c problem.
 * Usage        : ./greedy
 * Description  : https://cdn.cs50.net/2014/x/psets/1/pset1/pset1.html#_time_for_change
 * Testing      : check50 2014/x/pset1/greedy greedy.c
 ***************************************************************************/

#include <stdio.h>
#include <cs50.h>

int main( void ) {

    float num; // Input Amount of money
    int left; // How much money left?

    do {
      printf("O hai! How much change is owed?\n");
      num = GetDouble();
    } while( num < -0.0 );

    // Well, its a way to convert float to to int.
    left = (int) (num * 100);

    // we adding few variables that represent amount of coins.
    int n_25, n_10, n_1, n_5 = 0;

    // Saving amount of 25 cents we need.
    n_25 = left / 25;
    left = left % 25;
    if ( left > 0 ) {
        n_10 = left / 10;
        left = left % 10;
        if ( left > 0 ) {
            n_5 = left / 5;
            n_1 = left % 5;
        }
    }
    printf("%i\n", n_25 + n_10 + n_5 + n_1 );
}

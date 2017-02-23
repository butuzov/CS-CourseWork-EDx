/****************************************************************************
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 * Implement a program that finds a number among numbers.
 *
 * Description  : http://docs.cs50.net/problems/find/less/find.html
 * Testing      : check50 2016.find.less helpers.c
 ***************************************************************************/

#include <cs50.h>

#include "helpers.h"

/**
 * Binary search.
 *
 * https://en.wikipedia.org/wiki/Binary_search_algorithm
 * http://bigocheatsheet.com/
 *
 * Returns true if value is in array of n values, else false.
 * Will work only for positive numbers (ones that bigger than 0 )
 */
bool search( int value, int values[], int n){

    // If this negative number (but 0 is OK) terminating program.
    if ( value < 0)
        return false;

    // Determining the middle of array.
    int middle_of_the_array =  n / 2;

    // initiating indexes amd lenght variables.
    int array_index_start, array_index_end, array_length;

    // FOUND!
    if ( values[ middle_of_the_array ] == value ) {
        // Found
        return true;
    } else if ( middle_of_the_array == 0 && values[ middle_of_the_array] != value) {
        // Not found
        return false;
    } else if ( values[ middle_of_the_array] < value ) {
        // Searching in left part of array.
        array_index_start = middle_of_the_array + 1;
        array_index_end = n;
        array_length = (array_index_end - array_index_start);
    } else {
        // Searching in right part of array.
        array_index_start = 0;
        array_index_end = middle_of_the_array - 1;
        array_length = array_index_end + 1;
    }

    // allocating memory for new array to search in.
    int * array = malloc( array_length * sizeof( int ) );

    // and creating index.
    int array_index = 0;

    // and finally creating array.
    for( int i = array_index_start; i <= array_index_end; i++ ){
        array[ array_index++ ] = values[i];
    }

    // and storing result in status variable.
    bool status = search( value, array, array_length );

    // free memory.
    free(array);

    // return result of search.
    return status;
}

/**
 * Sorts array of n values.
 * @implements Bubble Sort, with a worst case scenario as O(n^2)
 * @see        https://en.wikipedia.org/wiki/Bubble_sort
 */
void  sort( int values[], int n ) {
    for( int i = 0; i < n; i ++ ) {
        for( int j = 1; j < n; j ++ ) {
            if ( values[ j - 1 ] > values[ j ] ) {
                int tmp = values[ j - 1 ];
                values[ j - 1 ] = values[ j ];
                values[ j ] = tmp;
            }
        }
    }
}

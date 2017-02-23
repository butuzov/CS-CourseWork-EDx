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
 * @implements Merge Sort
 * @see        https://en.wikipedia.org/wiki/Merge_sort
 */
void sort(int values[], int n) {

    if ( n != 1 ) {

        // Size of Left array
        int left_Size  = n / 2;

        // Size of the Right array
        int right_Size = n - left_Size;

        // Allocating memory for Left and Right arrays.
        int *left  = malloc( left_Size  * sizeof( int ) );
        int *right = malloc( right_Size * sizeof( int ) );

        // Initial Indexes.
        int left_Index = 0, right_Index = 0;

        // Dividing original array in two.
        for( int i = 0; i < n; i++ ) {
            if ( i < left_Size ) {
                left[ left_Index++ ] = values[ i ];
             } else {
                right[ right_Index++ ] = values[ i ];
            }
        }

        // recursive calls to sort left array...
        sort( left,  left_Size );

        // ... and right arrays
        sort( right, right_Size);

        // Reseting indexes for left and right array.
        left_Index = 0, right_Index = 0;

        // Original array index.
        int index = 0;

        // Merging values while sorting it.
        while( left_Index < left_Size && index < right_Size ) {
            if ( left[ left_Index ] < right[ right_Index ] ) {
                values[ index  ] = left[ left_Index++ ];
            } else {
                values[ index  ] = right[ right_Index++ ];
            }
            index++;
        }

        // If we have something left from left array, appending
        // it value to end of array.
        if ( left_Index < left_Size ) {
            for ( int j = left_Index; j < left_Size; j++){
                values[ index ++ ] = left[ j ];
            }
        }

        // If something left from right array, appending it value
        // to end of result array.
        if ( right_Index < right_Size ) {
            for ( int j = right_Index; j < right_Size; j++){
                values[ index ++ ] = right[ j ];
            }
        }

        // Free allocated memory.
        free(left);
        free(right);
    }
}

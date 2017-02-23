/****************************************************************************
 * initials.c
 *
 * Implement a program that, given a person’s name, prints a person’s
 * initials, per the below.
 *
 * Usage        : ./initials
 *
 * Description  : http://docs.cs50.net/problems/initials/less/initials.html
 * Testing      : check50 2016.initials.less initials.c
 *
 * Description  : http://docs.cs50.net/problems/initials/more/initials.html
 * Testing      : check50 2016.initials.more initials.c
 ***************************************************************************/


#include <stdio.h>
#include <string.h>
#include <cs50.h>


int  main(void){

    // Obtaining string from user.
    string name =  GetString();

    // We need this variable for filtering as indicator of previous char.
    char previous = 0; // NUL

    for ( int i = 0, n = strlen( name ); i < n; i++ ) {
        //
        if ( ( name[i] >= 65 && name[i] <= 90 ) || ( name[i] >= 97 && name[i] <= 122 ) ) {
            if ( previous == 0 || previous == 32 ) {
                printf("%c", name[i] > 90 ? name[i] - 32 : name[i] );
            }
        }

        previous = name[i];
    }
    printf ( "\n" );
    return 0;
}

/****************************************************************************
 * recover.c
 *
 * Implement a program that recovers JPEGs from a forensic image
 *
 * Usage        : ./recover card.raw
 * Description  : http://docs.cs50.net/problems/recover/recover.html
 * Test         : check50 2016.recover recover.c
 ***************************************************************************/

#include <stdio.h>

// test code with
// check50 2016.recover recover.c


int main( int argc, char *argv[] ) {

    // DO we have enoghts arguments?
    if ( argc != 2 ){
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Can we open image?
    FILE * fp;
    fp = fopen( argv[1], "r" );
    if( fp == NULL ) {
        fclose( fp );
        fprintf(stderr, "Wasn't able to open the cardfile.\n");
        return 2;
    }

    // memory chunk we using, assuming that filesystem is FAT.
    char block[512];

    // Sourcerer Bit for jpeg.
    char bits[3] = {0xff, 0xd8, 0xff}; // Start bits.

    // file numerator.
    int  n = 0;

    // holder for image filename.
    char filename[8];

    // filepointer for "recovered image".
    FILE * jpeg;

    // indicator varaible.
    int is_it_started = 0;

    // while we can read info from image
    while( fread(block, 512, 1, fp) > 0 ) {

        // Perhaps its stupid but we checking first 3 bits of every memory chunk.
        if ( block[0] == bits[0] && block[1] == bits[1] && block[2] == bits[2] ) {

            // And special 4th bite.
            if ( 239 >= (block[3] + 0) && (block[3] + 0) <= 225 ) {

                // Closing file that we already opening or indicating that
                // we start opening files for writing.
                if ( is_it_started == 1 ) {
                    fclose( jpeg );
                } else {
                    is_it_started = 1;
                }

                // Forming filename.
                sprintf(filename, "%03d.jpg", n );
                // and incrementing itterator.
                ++n;

                // opening file for writing.
                jpeg = fopen( filename , "w" );
                if( jpeg == NULL ) {
                    // and also closing already opened files.
                    fclose( jpeg );
                    fclose( fp );

                    // Error message
                    fprintf(stderr, "Wasn't able to create image file.\n");
                    return 3;
                }

                fwrite( block, 1, sizeof( block ), jpeg );

            }
        } else if ( is_it_started == 1 ) {
            fwrite( block, 1, sizeof( block ), jpeg );
        }
    }


    if( jpeg != NULL ) {
        fclose( jpeg );
    }

    if( fp != NULL ) {
        fclose( fp );
    }

    return 0;
}

/****************************************************************************
 * resize.c
 *
 * Implement a program that resizes BMPs
 *
 * Usage        : ./resize .5 large.bmp middle-sized.bmp
 * Usage        : ./resize 2  small.bmp middle-sized.bmp
 *
 * Description  : http://docs.cs50.net/problems/resize/more/resize.html
 * Test         : check50 2016.resize.more bmp.h resize.c
 *
 * Description  : http://docs.cs50.net/problems/resize/less/resize.html
 * Test         : check50 2016.resize.less bmp.h resize.c
 ***************************************************************************/

/**
 * Copies a BMP piece by piece, just because.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "bmp.h"


int main( int argc, char *argv[] ) {

    int debug = 0; // For direct run on Cmd + R

    // Ensure proper usage.
    if ( debug == 0 && argc != 4 ) {
        fprintf(stderr, "Usage: ./resize factor infile.bmp outfile.bmp\n");
        return 1;
    }

    // Multiplier Factor.
     float factor =  (float) ( debug == 0 ? atof(argv[1]) : .5) ;

    // In and Out file names.
    char *infile;
    char *outfile;

    // Remember filenames
    if ( debug != 1 ) {
        infile = argv[2];
        outfile = argv[3];
    } else {
        infile = "4x4.bmp";
        outfile = "3x3.bmp";
    }

    // Open input file
    FILE *inptr = fopen( infile, "r" );
    if ( inptr == NULL ) {
         fprintf(stderr, "Could not open %s.\n", infile);
         return 3;
    }

    // Open output file
    FILE *outptr = fopen( outfile, "w" );
    if ( outptr == NULL ) {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    int BMFH_Size        = sizeof(BITMAPFILEHEADER);
    int BMIH_Size       = sizeof(BITMAPINFOHEADER);
    int RGBTriple_Size    = sizeof(RGBTRIPLE);

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, BMFH_Size, 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, BMIH_Size, 1, inptr);


    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0) {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }


    // New file generation - new size..

    // Preserving width of original image - we need it.
    int _width  = bi.biWidth;
    // ... and padding.
    int _padding = ( 4 -  ( ( bi.biWidth * RGBTriple_Size ) % 4 ) ) % 4 ;

    // New Sizes
    bi.biWidth  = (int) ( (float) factor * bi.biWidth );
    bi.biHeight = (int) ( (float) factor * bi.biHeight);

    // determine padding for scanlines
    int padding =  ( 4 -  ( ( bi.biWidth * RGBTriple_Size ) % 4 ) ) % 4 ;

    bi.biSizeImage     = ( ( bi.biWidth * RGBTriple_Size ) + padding ) * abs(bi.biHeight);
    bf.bfSize         = bi.biSizeImage + BMIH_Size + BMFH_Size ;

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, BMFH_Size, 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, BMIH_Size, 1, outptr);

    // Here we go!
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++) {

        // iterate over pixels in scanline
        for (int j = 0; j < bi.biWidth; j++) {

            // temporary storage
            RGBTRIPLE triple;

            // Calculating ColorPicker Position.

            // Row?
            int picker_row = (int) ( (float) i / factor );
            // Pixel or Column
            int picker_col = (int) ( (float) j / factor );

            // Actuall Position.
            int picker_pos = ( picker_row * ( ( _width * RGBTriple_Size ) + _padding ) ) //
                    + ( picker_col * RGBTriple_Size ) + BMFH_Size + BMIH_Size  ;

            fseek(inptr, picker_pos, SEEK_SET);

            // read RGB triple from infile
            fread( &triple, RGBTriple_Size, 1, inptr);

            // fprintf( stderr, "Picker from row %i and col %i (position - %i)\n",
            //    picker_row, picker_col, picker_pos);

            fwrite( &triple, sizeof(RGBTRIPLE), 1, outptr );
        }

        // then add it back (to demonstrate how)
        for (int k = 0; k < padding; k++) {
            fputc(0x00, outptr);
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}

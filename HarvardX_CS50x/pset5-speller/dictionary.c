 /****************************************************************************
  * dictionary.c
  *
  * Implements a dictionary's functionality.
  *
  * Test         : check50 2016.speller dictionary.c dictionary.h Makefile
  * Description  : http://docs.cs50.net/problems/speller/speller.html
  ***************************************************************************/

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


#include "dictionary.h"


// This is our Dictionary structure.
toc *rootPtr = NULL;

// Words Don't Come Easy
// words counter.
int len = 0;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word) {

    toc *curr = NULL;
    curr = rootPtr;

    for ( int i = 0, str_len=strlen(word); i <= str_len; i++) {
        if ( word[i] == '\0') {
            if ( curr->eow == true ){
                // Found end of word marker.
                // Terminating execution and returning result true (found)
                return true;
            }

            // This is end of searched word, but marker that this is the word in
            // out dictionary not found.
            return false;

        } else if ( isalpha( word[i] ) || word[i] == 0x27 ) {
            // If its letter or ' sign
            // index 0 for '
            // index 1-26 for every letter of latin alphabet,
            int index = word[i] == 0x27 ? 0 : tolower( word[i] ) - 96;

            // There is no such char on current node
            // so there is no such word.
            if ( curr->letters[ index ] == NULL ){
                return false;
            }

            // switching node.
            curr = curr->letters[ index ];
        } else {

            // this is never should happen.
            // just for test
            printf("Wtf?");
        }

    }

    return false;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary) {

    // Creating File Pointer
    FILE *DirFP;

    // Open Dictionary...
    DirFP = fopen( dictionary, "r");

    // Can't? Too bad for us!
    if ( DirFP == NULL ) {
    	fclose( DirFP );
    	return false;
    }

    // Creating Root and Current TOC pointes.
    // Then copy pointer of Root to Current

    toc *curr = NULL;
    rootPtr = toc_create();
    curr = rootPtr;


	for ( int c = fgetc( DirFP ); c != EOF; c = fgetc( DirFP ) ) {
		if ( c == 0xA ) {
			len += 1;
			// End Of Word
			curr->eow = true;
			// And Tree Reset
			curr=rootPtr;
		} else if ( isalpha( c ) || c == 0x27 ) {
			// If its letter or ' sign
			// index 0 for '
			// index 1-26 for every letter of latin alphabet,
			int index = c == 0x27 ? 0 : tolower( c ) - 96;
			// There is no such char on current node
			// so we gonna create new toc for thsi node.
			if ( curr->letters[index] == NULL ) {
				 curr->letters[index] = toc_create();
			}
			curr = curr->letters[index];
		}
	}

	fclose( DirFP );

	return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size( void ) {
    return len;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void){
    toc_free( rootPtr );
    return true;
}


// Create a TOC witha 26 pointers.
toc* toc_create() {
    toc *dict;
    dict = malloc( sizeof( toc ) );
    // BY Default IS_WORD is FALSE!.
    dict->eow = NULL;

    // creating 27 entries for abc.
    for ( int i = 0; i < 27; i++ ) {
        dict->letters[i] = NULL;
    };

    return dict;
}

// Free Memory from root node to the end of leafes
void toc_free( toc* freeable ) {
   for ( int i = 0; i < 27; i++ ) {
       if ( freeable->letters[i] != NULL ) {
            toc_free( freeable->letters[i] );
       }
   }
   free(freeable);
}

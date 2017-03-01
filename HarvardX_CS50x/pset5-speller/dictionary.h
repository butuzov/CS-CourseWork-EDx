/**
 * Declares a dictionary's functionality.
 */

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdio.h>
#include <stdbool.h>

// maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45


// Struct for Letters.
typedef struct toc {
    // End of word.
    bool eow;
    // 26 letters + ' sign
    struct toc *letters[27];
} toc;


/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word);

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary);

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void);

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void);

/**
 * Free resources allocated for dictionary in memory.
 */
void toc_free( toc* freeable );

/**
 * Create new TOC entry.
 */
toc* toc_create();

#endif // DICTIONARY_H

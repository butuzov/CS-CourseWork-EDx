/************************************************************************
 * fifteen.c
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * Description  : http://docs.cs50.net/problems/fifteen/fifteen.html
 * Testing      : ./fifteen 3 < ~cs50/pset3/3x3.txt
 *                ./fifteen 3 < ~cs50/pset3/4x4.txt
 *                check50 2016.fifteen fifteen.c
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that //usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man //usleep` for more.
 ************************************************************************/

#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[]) {
    // ensure proper usage
    if ( argc != 2 ) {
        printf("Usage: fifteen d\n");
        return 1;
    }

    // ensure valid dimensions
    d = atoi(argv[1]);
    if ( d < DIM_MIN || d > DIM_MAX) {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL) {
        return 3;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while ( true ) {
        // clear the screen
        clear();

        // draw the current state of the board
        draw();

        // log the current state of the board (for testing)
        for ( int i = 0; i < d; i++) {
            for ( int j = 0; j < d; j++) {
                fprintf( file, "%i", board[i][j]);
                if ( j < d - 1) {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // check for win
        if ( won() ) {
            printf("ftw!\n");
            break;
        }

        // prompt for move
        printf( "Tile to move: ");
        int tile = GetInt();

        // quit if user inputs 0 (for testing)
        if (tile == 0) {
            break;
        }

        // log move (for testing)
        fprintf( file, "%i\n", tile );
        fflush( file );

        // move if possible, else report illegality
        if ( ! move( tile ) ) {
            printf("\nIllegal move.\n");
            //usleep( 500000 );
        }

        // sleep thread for animation's sake
        //usleep( 500000 );
    }

    // close log
    fclose(file);

    // success
    return 0;
}

/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void) {
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    //usleep(2000000);
}

/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).
 */
void init(void) {

    // This is a last element suppose to be number.
    int TotalCells = d * d;

    // Easy Mode.
    for ( int row = 0; row < d; row++){
        for ( int col = 0; col < d; col++){
            int current_cell = (TotalCells) - (row * d + col + 1) ;

            if ( current_cell != TotalCells ) {
               board[row][col] = current_cell;
            } else {
               board[row][col] = 0;
            }
        }
    }

    if ( d % 2 == 0 ) {
        int tmp = board[(d-1)][(d-3)];
        board[(d-1)][(d-3)] = board[(d-1)][(d-2)];
        board[(d-1)][(d-2)] = tmp;
    }


    /*
        Nightmade (almost) mode.
    */
    bool nightmare = false;
    if ( nightmare ) {
        // Nightmare
        // enable time.h for MORE effect
        // srand48( (long) time(NULL));
        srand48( (long) 0);

        int * Numbers = (int*) malloc( TotalCells );
        for (int i = 0; i < TotalCells; i++ ) {
            Numbers[i] = 0;
        }

        for ( int row = 0; row < d; row++){
            for ( int col = 0; col < d; col++){

                // Generate Random Number that not on our
                // Going to slow and nightmare.
                bool uniq;
                int number;

                do {

                    // generating random number.
                    number = (int) ( drand48() * TotalCells  );
                    uniq = true;

                    if ( number == 0 ) {
                        // Do It Again Condition
                        uniq = false;
                        // This the end... so yeah its uniq.
                        if ( row == (d-1) && col == (d-1) ){
                            uniq = true;;
                        }
                    } else {
                        // Checkign for duplicate.
                        for (int i = 0; i < TotalCells; i++ ) {
                            if ( uniq == true ) {
                                if ( Numbers[i] == number ) {
                                    uniq = false;
                                    break;
                                }
                            }
                        }

                        // Updating refference array.
                        if ( uniq == true ) {
                            for (int i = 0; i < TotalCells; i++ ) {
                                if ( Numbers[i] == 0 ) {
                                    Numbers[i] = number;
                                    break;
                                }
                            }
                        }
                    }
                } while( ! uniq );

                if ( number != TotalCells ) {
                 	board[row][col] = number;
                } else {
                    board[row][col] = 0;
                }
            }
        }

        free(Numbers);
    }
}

/**
 * Prints the board in its current state.
 */
void draw(void) {

    // This is a last element suppose to be number.
    int TotalCells = d * d;

    // Size of the cell
    int size = (TotalCells / 10 >= 1 ? 4 : 3 ) ;

    // print header
    for (int pad = 0, end = size * d; pad < end; pad++) {
        printf("=");
    }
    printf("\n");

    for ( int row = 0; row < d; row++) {
        for ( int col = 0; col < d; col++) {
            if ( board[row][col] == 0) {
                printf( "\x1b[31m" );
                printf( size == 4 ? "  _ " : " _ ");
                printf( "\x1b[0m" ); // Color reset
            } else if ( size == 4 ) {
                printf( board[row][col] / 10 >= 1 ? " %i " : "  %i ", board[row][col]);
            } else {
                printf( " %i " , board[row][col]);
            }
        }
        printf("\n");
    }

}

/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false.
 */
bool move(int tile) {
    int current_row;
    int current_col;
    int found;

    // getting possition of the tile
    for ( int row = 0; row < d; row++) {
        for ( int col = 0; col < d; col++) {
            if ( board[row][col] == tile ) {
                found = true;
                current_row = row;
                current_col = col;
                //printf("Found %i at (row:%i):(col:%i)\n", tile, row, col);
                break;
            }
        }
    }

    if ( found != true ) {
        return false;
    }

    // Move Right.
    if ( current_col < (d-1) && board[current_row][(current_col+1)] == 0 ) {
        //printf( "Moving %i Right \n", board[current_row][current_col]);
        board[current_row][ (current_col + 1) ] = board[current_row][current_col];
        board[current_row][ current_col ] = 0;
        return true;
    }

    // Move Left.
    if ( current_col > 0 && board[current_row][current_col-1] == 0 ) {
        //printf( "Moving %i Left \n", board[current_row][current_col]);
        board[current_row][current_col - 1] = board[current_row][current_col];
        board[current_row][current_col] = 0;
        return true;
    }

    // Move Down.
    if ( current_row < (d-1) && board[current_row+1][current_col] == 0 ) {
        //printf( "Moving %i Down \n", board[current_row][current_col]);
        board[current_row + 1][current_col] = board[current_row][current_col];
        board[current_row][current_col] = 0;
        return true;
    }

    // Move Up.
    if ( current_row > 0 && board[current_row-1][current_col] == 0 ) {
        //printf( "Moving %i Up \n", board[current_row][current_col]);
        board[current_row - 1][current_col] = board[current_row][current_col];
        board[current_row][current_col] = 0;
        return true;
    }

    return false;
}

/**
 * Returns true if game is won (i.e., board is in winning configuration),
 * else false.
 */
bool won(void) {
    int last = d * d;
    for ( int row = 0; row < d; row++){
        for ( int col = 0; col < d; col++){
            // suppose to be in this cell.
            int current_cell_number = row * d + col + 1 ;

            if ( current_cell_number != last && current_cell_number != board[row][col] ) {
                return false;
            }
        }
    }
    return true;
}

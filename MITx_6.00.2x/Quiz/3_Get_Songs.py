"""
You are creating a song playlist for your next party. You have a collection of songs that can be represented as a list of tuples. Each tuple has the following elements:

    name: the first element, representing the song name (non-empty string)
    song_length: the second, element representing the song duration (float >= 0)
    song_size: the third, element representing the size on disk (float >= 0)

You want to try to optimize your playlist to play songs for as long as possible while making sure that the songs you pick do not take up more than a given amount of space on disk (the sizes should be less than or equal to the max_disk_size).

You decide the best way to achieve your goal is to start with the first song in the given song list. If the first song doesn't fit on disk, return an empty list. If there is enough space for this song, add it to the playlist.

For subsequent songs, you choose the next song such that its size on disk is smallest and that the song hasn't already been chosen. You do this until you cannot fit any more songs on the disk.

Write a function implementing this algorithm, that returns a list of the song names in the order in which they were chosen, with the first element in the list being the song chosen first. Assume song names are unique and all the songs have different sizes on disk and different durations.

You may not mutate any of the arguments.
"""


def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    playlist = [];

    song_one = songs[0:1];
    if len(song_one) == 0 or song_one[0][2] > max_size:
        return []

    max_size -= song_one[0][2];
    playlist.append( song_one[0] );

    # technicaly its not muting argument.
    # and we usigng only n lon n (see TimSort)
    sortedSongs = sorted(songs[1:], key=lambda x: x[2], reverse=False)

    for index in range(len(sortedSongs)):
        if  sortedSongs[index][2] < max_size:
            max_size -= sortedSongs[index][2];
            playlist.append( sortedSongs[index] );

    return [x[0] for x in playlist]



if __name__ == '__main__':
    print( song_playlist( [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], 12.2 ) )

    print( song_playlist( [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], 11 ) )

    print( song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 20) )

    print( song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 12.2) )

    print( song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 11) )

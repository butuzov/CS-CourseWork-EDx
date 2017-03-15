"""
You are given the following definitions:

 * A run of monotonically increasing numbers means that a number at position
   k+1 in the sequence is greater than or equal to the number at position k
   in the sequence.

 * A run of monotonically decreasing numbers means that a number at position
   k+1 in the sequence is less than or equal to the number at position k in
   the sequence.

"""

def longest_run( L ):
	"""
	Assumes L is a list of integers containing at least 2 elements.
	Finds the longest run of numbers in L, where the longest run can
	either be monotonically increasing or monotonically decreasing.
	In case of a tie for the longest run, choose the longest run
	that occurs first.
	Does not modify the list.
	Returns the sum of the longest run.
	"""

	List = L[:]
	length_Of_The_List = len(List);

	Directions = {
		'increasing': {},
		'decreasing': {},
	}

	final_Sequenses = {};

	for sequenses, direction in enumerate( Directions ) :
		if direction is 'decreasing':
			List.reverse();

		index_start = 0
		index_end = 0
		index_cur = 0

		while True:
			index_cur += 1


			if List[index_cur] >= List[index_cur - 1]:
				index_end = index_cur;
				sequenses = Directions.get(direction);
				Position_At_The_Start = index_start;
				sequense_length = (index_cur - index_start) + 1
				sequense = ( index_start, index_cur, sequense_length )

				if direction is 'decreasing':
					Position_At_The_Start = length_Of_The_List - index_start - 1
					sequense = (
						length_Of_The_List - 1 - index_cur,
						length_Of_The_List - 1 - index_start,
						sequense_length )
				"""
				Key of sequens IS NOT A Index of Sequense Start, its jsut
				uniqe key for this Sequense.
				"""
				sequenses.update({ Position_At_The_Start : sequense } )

			else:
				# Break Sequense.
				index_start = index_cur

			# exit the loop.
			if (length_Of_The_List - 1) == index_cur:
				break;

		if direction is 'decreasing':
			List.reverse();

		sequenses = Directions.get(direction);
		for key in sequenses:

			seq_Last = sequenses.get( key )
			if final_Sequenses.get( direction, None) is None:
				final_Sequenses.update({ direction: seq_Last })

			seq_Longest = final_Sequenses.get(direction)

			# Comparing length of sequenses.
			if seq_Longest[2] < seq_Last[2]:
				#Updateing longest sequense
				final_Sequenses.update({ direction: seq_Last })
			elif seq_Longest[2] == seq_Last[2] and seq_Longest[0] > seq_Last[0]:
				final_Sequenses.update({ direction: seq_Last })

	def sequense_compare_and_return( Sequense_A, Sequense_B ) :
		"""
		Compare two sequenses, first by length, second by position
		"""
		if Sequense_A[2] == Sequense_B[2]:
			if Sequense_A[0] > Sequense_B[0]:
				return Sequense_B;
			return Sequense_A;
		else :
			if Sequense_A[2] > Sequense_B[2]:
				return Sequense_A;
			return Sequense_B;


	longest_Run = sequense_compare_and_return(
					final_Sequenses.get( 'decreasing', (0,0,0) ),
					final_Sequenses.get( 'increasing', (0,0,0) ) )

	return sum( List[ longest_Run[0] : longest_Run[1] + 1 ] );


"""
	Testing our Code
"""

Expectations = [
  ( 26, [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] ),
  ( 9, [5, 4, 10] ),
  ( 9, [5, 4, 5] ),
]

for Item in Expectations:
	longest_run_sum = longest_run( Item[1] )
	Message = ' {} is sum of longest run "{}" '.format( Item[0], Item[1] )

	if longest_run_sum == Item[0]:
		print( f'\033[1;102;30m (Test Passed) \033[0;102;30m {Message} \033[0m' )
	else:
		print( f'\033[1;101;30m (Test Failed) \033[0;101;30m {Message} \033[0m' )

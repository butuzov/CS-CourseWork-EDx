import nltk

class Analyzer():
	"""Implements sentiment analysis."""

	def __init__(self, positives, negatives):
		"""Initialize Analyzer."""

		self.words_positive = self.read( positives );
		self.words_negative = self.read( negatives );

	def analyze(self, text):


		rate = 0

		tknzr = nltk.tokenize.TweetTokenizer( strip_handles=True, reduce_len=True )
		words = tknzr.tokenize( text )
		for word in words :
			if word in self.words_positive :
				rate += 1;
			if word in self.words_negative :
				rate -= 1;

		return rate


	def read( __self__ , source ):
		"""
			Read and returns positive and negative words from provided lists.
		"""
		f = open( source, 'r')
		lines = f.readlines()
		f.close()

		lines = [ line.strip() for line in lines ]
		return lines[35:]

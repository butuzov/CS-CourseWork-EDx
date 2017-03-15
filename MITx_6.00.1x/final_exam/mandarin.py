"""
This dictionary is respresent mandarin names for basic numbers used to
form a large ones.
"""
trans = {
	'0':'ling',
	'1':'yi',
	'2':'er',
	'3':'san',
	'4': 'si',
	'5':'wu',
	'6':'liu',
	'7':'qi',
	'8':'ba',
	'9':'jiu',
	'10': 'shi'
}


def convert_to_mandarin(us_num) :
	'''
	us_num, a string representing a US number 0 to 99
	returns the string mandarin representation of us_num

	we using '{}'.format() to proccess response for requested int.

	'''
	if int(us_num) <= 10 :
		return '{}'.format(
				trans.get( str( us_num ) )
		)
	elif int(us_num) < 20 :
		return '{} {}'.format(
				trans.get('10'),
				trans.get( str( int(us_num) % 10 ) )
		)
	elif int(us_num) % 10 is 0 :
		return '{} {}'.format(
				trans.get( str( int(us_num) // 10 ) ),
				trans.get('10')
		)
	else :
		return '{} {} {}'.format(
				trans.get( str( int(us_num) // 10 ) ),
				trans.get('10'),
				trans.get( str( int(us_num) % 10 ) )
		)

"""
	Testing our Code
"""

Expectations = [
  (0, 'ling'), (9, 'jiu'), (10, 'shi'),
  (11, 'shi yi'), (19, 'shi jiu'), (20, 'er shi'),
  (61, 'liu shi yi'), (70, 'qi shi'),
  (71, 'qi shi yi')
]

for Item in Expectations:
	Mandarin = convert_to_mandarin( Item[0] );
	if Item[1] != Mandarin:
		Message = ' "{}" is expected to be "{}", but we get {} '.format( Item[0], Item[1], Mandarin)
	else:
		Message = ' "{}" is expected to be and is "{}" '.format( Item[0], Item[1])

	if Mandarin == Item[1]:
		print( f'\033[1;102;30m (Test Passed) \033[0;102;30m {Message} \033[0m' )
	else:
		print( f'\033[1;101;30m (Test Failed) \033[0;101;30m {Message} \033[0m' )

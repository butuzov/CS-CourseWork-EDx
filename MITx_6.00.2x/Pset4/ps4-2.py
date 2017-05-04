from ps4 import *

Expectations = [
    ( ( [-3.1, -4.1, -9.2, 10.1, 9.1, 4.5], [-1.1, -2.1, -7.2, 11.1, 11.1, 5.5] ), 0.9414),
    ( ( [-3.1, -4.1, -9.2, 10.1], [-2.1, -6.1, 9.2, 20.1] ), -1.1834 ),
    ( ( [4.4, 5.5, 6.6], [4.4, 5.5, 6.6] ), 1.0 ),
    ( ( [32.0, 42.0, 31.3, 22.0, 33.0], [32.3, 42.1, 31.2, 22.1, 34.0] ), 0.9944 )
]

for expectation in Expectations:
    test = []
    test.append( r_squared( *expectation[0] ) );
    test.append( expectation[1] );
    test = np.around(test, 3);

    if  test[0] == test[1] :
        print( "OK!" );
    else :
        print( "Failed" )

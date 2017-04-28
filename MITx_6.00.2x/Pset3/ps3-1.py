from ps3b import *

# Few Tests from Pset3b-Problem1

# Test
print( 'Create a Patient with virus that is never cleared and always reproduces' );
print( 'patient = Patient([ SimpleVirus(1.0, 0.0) ], 100)' );
patient = Patient([ SimpleVirus(1.0, 0.0) ], 100)
print( 'Updating the patient for 100 trials...' );

for i in range(100):
    patient.update();

print( 'patient.getTotalPop() expected to be >= 100' )
assert patient.getTotalPop() >= 100
print( 'Test successfully completed' )
print();
print();
# Test
print( 'Create a Patient with virus that is always cleared and always reproduces' );
print( 'patient = Patient([ SimpleVirus(1.0, 1.0) ], 100)' );
patient = Patient([ SimpleVirus(1.0, 1.0) ], 100)
print( 'Updating the patient for 100 trials...' );

for i in range(100):
    patient.update();

print( 'patient.getTotalPop() expected to = 0' )
assert patient.getTotalPop() == 0
print( 'Test successfully completed' )
print();
print();


exit(1)

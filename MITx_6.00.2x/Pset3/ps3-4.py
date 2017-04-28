from ps3b import *

# Few Tests from Pset3b-Problem4

# Create a TreatedPatient with virus that is never cleared and always reproduces.

patient = TreatedPatient([ ResistantVirus(1.0, 0.0, {}, 0.0) ], 100)
print( 'patient = TreatedPatient([ ResistantVirus(1.0, 0.0, {}, 0.0) ], 100)' );
print( 'Updating the patient for 100 trials...' );

for i in range(100):
    patient.update();

print( 'patient.getTotalPop() expected to be >= 100' )
assert patient.getTotalPop() >= 100
print( 'Test successfully completed' )
print();
print();

# Create a TreatedPatient with virus that is always cleared and always reproduces.

patient = TreatedPatient([ ResistantVirus(1.0, 1.0, {}, 0.0) ], 100)
print( 'patient = TreatedPatient([ ResistantVirus(1.0, 0.0, {}, 0.0) ], 100)' );
print( 'Updating the patient for 100 trials...' );

for i in range(100):
    patient.update();

print( 'patient.getTotalPop() expected to be == 0' )
assert patient.getTotalPop() == 0
print( 'Test successfully completed' )
print();
print();


# Test of getting TreatedPatient's resistant pop

virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
patient = TreatedPatient([virus1, virus2, virus3], 100)

assert patient.getResistPop(['drug1']) == 2
assert patient.getResistPop(['drug2']) == 2
assert patient.getResistPop(['drug1','drug2']) == 1
assert patient.getResistPop(['drug3']) == 0
assert patient.getResistPop(['drug1', 'drug3']) == 0
assert patient.getResistPop(['drug1','drug2', 'drug3']) == 0

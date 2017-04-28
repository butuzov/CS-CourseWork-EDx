from ps3b import *

# Few Tests from Pset3b-Problem3

virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
print( virus.reproduce(0, ["drug1"]) )
print( virus.reproduce(0, ["drug2"]) )

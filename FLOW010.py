T = input()
A=[]

for i in range (T):
    C = raw_input()
    C=C.upper()

    if C=="B":
        A.append("BattleShip")
    if C=="C":
        A.append("Cruiser")
    if C=="D":
        A.append("Destroyer")
    if C == "F":
        A.append("Frigate")

for x in A:
    print x

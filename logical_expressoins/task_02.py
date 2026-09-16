for A in (0,1):
    for B in (0,1):
        for C in (0,1):
            e1 = (not (A and B)) or (not (A or C))
            e2 = (A and B) or ((not B) and C)
            e3 = (A and B) or (not C)
            # битовые операции
            b1 = ~(A & B) | ~(A | C) & 1
            b2 = (A & B) | (~B & C) & 1
            b3 = (A & B) | (~C & 1)
            print(A,B,C, int(e1), int(e2), int(e3), "|", b1, b2, b3)
class B:    
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B, C, D]:
    print "-" * 50
    try:
        raise c()
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"
# c02:testable:BlackBoxTest.py (Eckel, B. page 44)

class BlackBoxTest(UnitTest):
    Testable tst = Testable()
    def test1(self):
        #! tst.f2() # Nope!
        #! tst.f3() # Nope!
        tst.f4() # Only public methods available
        
#:~

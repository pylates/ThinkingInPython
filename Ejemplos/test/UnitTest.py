# <<Para crear un set de pruebas, hay que empezar haciendo  una clase 'static' interna dentro de la clase que desea probar>>
# Eckel, B. (Pagina 38) no funciona independientemente.

# test:UnitTest.py
# The basic unit testing class
import String

class UnitTest:
    static String testID
    static List errors = ArrayList()

    #Override cleanup() if test object
    #creation allocates non-memory
    #resources that must be cleaned up:
    def cleanup(self):
        #Verify the truth of a condition:
        protected final void affirm(boolean condition){
            if(!condition)
                errors.add("failed: "+testID)
        }
#:~

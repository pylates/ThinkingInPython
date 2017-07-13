#%Este Ejemplo no funciona con Python 2.7 ni Python3! >o<

#  test:UnitTest.py 
# The basic unit testing class 
class UnitTest: 

  static String testID 
  static List errors = ArrayList() 
  # Override cleanup() if test object  
  # creation allocates non-memory  
  # resources that must be cleaned up: 
  def cleanup(self): 
  # Verify the truth of a condition: 
  protected final void affirm(boolean condition){ 
    if(!condition) 
      errors.add("failed: " + testID) 

# :~ 

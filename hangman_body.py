from typing import Optional

def draw_hangman_body(incorrect: int) -> Optional[str]:

    if incorrect == 1:
        return """
 ------
 |    
 |    
 |
 |
 |
 |
 |
 |
----------
"""

    if incorrect == 2:
        return  """
 ------
 |    |
 |    
 |
 |
 |
 |
 |
 |
----------
"""

    if incorrect == 3:
        return """
 ------
 |    |
 |    O
 |   
 | 
 |   
 |   
 |   
 |   
----------
"""

    if incorrect == 4:
        return """
 ------
 |    |
 |    O
 |   -+-
 |   
 |   
 |   
 |   
 |   
----------
"""

    if incorrect == 5:
        return """
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
"""

    if incorrect == 6:
        return """
 ------
 |    |
 |    O
 |  /-+-/
 |    
 |   
 |   
 |   
 |   
----------
"""
    if incorrect == 7:
        return """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 | 
 |    
 |   
----------
"""

    if incorrect == 8:
        return """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |  
----------
"""
    
    if incorrect == 9:
        return """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
"""

    
# letters come from http://patorjk.com/software/taag/#p=display&f=Slant&t=Q

letters = {}

letters[" "] = r"""
   
   
   
   
   
"""

letters["A"] = r"""
    ___ 
   /   |
  / /| |
 / ___ |
/_/  |_|
"""

letters["B"] = r"""
    ____ 
   / __ )
  / __  |
 / /_/ / 
/_____/  
"""

letters["C"] = r"""
   ______
  / ____/
 / /     
/ /___   
\____/   
"""

letters["D"] = r"""
    ____ 
   / __ \
  / / / /
 / /_/ / 
/_____/  
"""

letters["E"] = r"""
    ______
   / ____/
  / __/   
 / /___   
/_____/   
"""

letters["F"] = r"""
    ______
   / ____/
  / /_    
 / __/    
/_/       
"""

letters["G"] = r"""
   ______
  / ____/
 / / _   
/ /_/ /  
\____/   
"""

letters["H"] = r"""
    __  __
   / / / /
  / /_/ / 
 / __  /  
/_/ /_/   
"""

letters["I"] = r"""
    ____
   /  _/
   / /  
 _/ /   
/___/   
"""

letters["J"] = r"""
       __
      / /
 __  / / 
/ /_/ /  
\____/   
"""

letters["K"] = r"""
    __ __
   / //_/
  / ,<   
 / /| |  
/_/ |_|  
"""

letters["L"] = r"""
    __ 
   / / 
  / /  
 / /___
/_____/
"""

letters["M"] = r"""
    __  ___
   /  |/  /
  / /|_/ / 
 / /  / /  
/_/  /_/   
"""

letters["N"] = r"""
    _   __
   / | / /
  /  |/ / 
 / /|  /  
/_/ |_/   
"""

letters["O"] = r"""
   ____ 
  / __ \
 / / / /
/ /_/ / 
\____/  
"""

letters["P"] = r"""
    ____ 
   / __ \
  / /_/ /
 / ____/ 
/_/      
"""

letters["Q"] = r"""
   ____ 
  / __ \
 / / / /
/ /_/ / 
\___\_\ 
"""

letters["R"] = r"""
    ____ 
   / __ \
  / /_/ /
 / _, _/ 
/_/ |_|  
"""

letters["S"] = r"""
   _____
  / ___/
  \__ \ 
 ___/ / 
/____/  
"""

letters["T"] = r"""
  ______
 /_  __/
  / /   
 / /    
/_/     
"""

letters["U"] = r"""
   __  __
  / / / /
 / / / / 
/ /_/ /  
\____/   
"""

letters["V"] = r"""
 _    __
| |  / /
| | / / 
| |/ /  
|___/   
"""

letters["W"] = r"""
 _       __
| |     / /
| | /| / / 
| |/ |/ /  
|__/|__/   
"""

letters["X"] = r"""
   _  __
  | |/ /
  |   / 
 /   |  
/_/|_|  
"""

letters["Y"] = r"""
__  __
\ \/ /
 \  / 
 / /  
/_/   
"""

letters["Z"] = r"""
 _____
/__  /
  / / 
 / /__
/____/
"""


def get_letter(l):
    rows = letters[l].split("\n")
    return "\n".join(rows[1:-1])


if __name__ == "__main__":
    print(get_letter('A'), get_letter(" "))
    # print(get_letter('C'))

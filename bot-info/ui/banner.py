from pystyle import Colorate, Colors

ASCII_ART = r"""
  _______   ___  ___  ____  ____  __   ___       __      
 /"      \ |"  \/"  |("  _||_ " ||/"| /  ")     /""\     
|:        | \   \  / |   (  ) : |(: |/   /     /    \    
|_____/   )  \\  \/  (:  |  | . )|    __/     /' /\  \   
 //      /   /   /    \\ \__/ // (// _  \    //  __'  \  
|:  __   \  /   /     /\\ __ //\ |: | \  \  /   /  \\  \ 
|__|  \___)|___/     (__________)(__|  \__)(___/    \___)
                                                         
                                                                
"""

def print_banner():
    print(Colorate.Horizontal(Colors.blue_to_purple, ASCII_ART, 1))

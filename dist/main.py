true=True; false=False; null=None
import os 
import time 
import datetime 

import config 
import digits 

now =datetime .datetime .now ()

os .system ("tput reset");
time .sleep (1)
if (not config .rainbow ):
    base_characters =["","","","",""]
    
else :
    base_characters =["\033[31m","\033[33m","\033[32m","\033[34m","\033[35m"]
    



print ("\n"*int (os .get_terminal_size ().lines /2));
while (1):
    characters =[
    base_characters [0],
    base_characters [1],
    base_characters [2],
    base_characters [3],
    base_characters [4]
    ]
    
    formatstring ="%h:%m:%s"
    now =datetime .datetime .now ()
    
    formatstring =formatstring .replace ("%h",str (now .hour ).rjust (2,'0'))
    formatstring =formatstring .replace ("%m",str (now .minute ).rjust (2,'0'))
    formatstring =formatstring .replace ("%s",str (now .second ).rjust (2,'0'))
    
    
    for i in formatstring :
        if (i ==":"):
            i =10;
            
        elif (i =="-"):
            i =11;
            
        
        
        number =int (i )
        characters [0]+=digits .digits [number ][0]+"  "
        characters [1]+=digits .digits [number ][1]+"  "
        characters [2]+=digits .digits [number ][2]+"  "
        characters [3]+=digits .digits [number ][3]+"  "
        characters [4]+=digits .digits [number ][4]+"  "
        
        
    
    
    print ("\033[0m \033[A"*6)
    
    for i in characters :
        print (f"{i}".center (os .get_terminal_size ().columns ))
        
    
    time .sleep (1)
    


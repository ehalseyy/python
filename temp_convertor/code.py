from asyncore import loop
import os
from os import system
system("clear")

name = input("Whats your name ") 
print("Hello " + name )
question = input("Enter c for celcius or f for fahrenheit ")

while question != ('c', 'f'):
  print('pleease enter C or F ')
  break
if question == "c":
    cel = input("What is the tempture? ")
    cel = int(cel)
    cel2 = (cel / 5)* 9 + 32
    cel2 = str(cel2)
    print(name +" The temputare is "+ cel2)

elif question == "f":
    far = input("What is the tempture? ")
    far = int(far)
    far2 = (far - 32) * 5 / 92
    far2 = str(far2)
    print(name +" the tempature is " + far2)
else:
    print("Nah")
    
    ## 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SS
A=input("enter the string")
numberOfCharacters=0
numberOfWords=1
for I in A :
    numberOfCharacters=numberOfCharacters+1
    if (I==' '): 
        numberOfWords=numberOfWords+1
print("totalNumberofWordsinString=",numberOfWords)
print("totalNumberofCharactersinString=",numberOfCharacters)

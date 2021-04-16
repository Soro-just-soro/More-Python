def countWords():
    filename=input("enter the file name")
    words=0
    file=open(filename,'r')
    for x in file:
        w=x.split()
        words=words+len(w)
    print("number of words",words)
countWords()
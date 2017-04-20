f1=open("file1.txt","r")
f2=open("file2.txt","w")
key=input("Enter key : ")
key2=input("Confirm key : ")
if key != key2:
    exit ()
    
strkey=str(key)

cycle=0

for line in f1:
    for car1 in line:
        offset=int(strkey[cycle])
        car2=car1
        if (car1 != '\n'):
            car2=chr(ord(car1)+offset)
        print(car2,end="")
        f2.write(car2)
        cycle=cycle+1
        if (cycle==len(strkey)):
            cycle=0

    

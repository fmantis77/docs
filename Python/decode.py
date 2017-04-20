f2=open("/sdcard/Download/file2.txt","r")
f3=open("/sdcard/Download/file3.txt","w")
key=input("Enter key : ")

strkey=str(key)

cycle=0

for line in f2:
    for car1 in line:
        offset=int(strkey[cycle])
        car2=car1
        if (car1 != '\n'):
            car2=chr(ord(car1)-offset)
        print(car2,end="")
        f3.write(car2)
        cycle=cycle+1
        if (cycle==len(strkey)):
            cycle=0

    
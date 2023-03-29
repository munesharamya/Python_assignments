import fileinput

with open("text.txt",'w') as f:
    f.write("hello python \n")
    f.write("hello python students \n")
    f.writelines("let's learn filehandling....at the end\n")

with open("text.txt",'a') as f:
    f.write("appending text \n")
    f.write("appended successfully \n")

with open("text.txt",'r') as f:
    print(f.read(50))
    position=f.tell()
    print(position)

with open("text.txt",'r') as f:
    print(f.read(5))
    f.seek(0,0)
    p=f.tell()
    print(f.read(50))

fileinput.close()
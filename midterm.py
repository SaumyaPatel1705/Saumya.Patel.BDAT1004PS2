f = open("file.txt", "a")
f.write("Hi, Now the file has more content!")
f.close()

f = open("file.txt", "r")
print(f.read())
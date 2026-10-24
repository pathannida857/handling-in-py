# f=open('anam1.py','a')
# f.write("print('hello world')")
# f=open('anam1.py','ab+')
# f.write(b "thi is python class\n" )

# f=open("test.txt","ab+")
# f.write(b"hello world\n")
# f.write(b"hello python\n")
# f.close()

f=open("test.txt","rb+")
data=f.read()
print(data)
f.close()
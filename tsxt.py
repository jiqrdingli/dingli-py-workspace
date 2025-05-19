with open('file.txt','w') as f:
    f.write("这是一个新文件")

while open('file.txt','r')as f:
    content = f.read()
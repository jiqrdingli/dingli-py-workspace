with open("hellow.py","w",encoding="utf-8")as f:
    f.write("hellow\n")
    f.write("yoooo")
    f.close()

with open("hellow.py", "r", encoding="utf-8") as f:

    f.close()

with open("hellow.py","a",encoding="utf-8")as f:
    f.write("hellow\n")
    f.write("yoooo")
    f.close()

with open("hellow.py", "r+", encoding="utf-8") as f:
    f.write("hellow\n")
    f.write("yoooo")
    f.close()
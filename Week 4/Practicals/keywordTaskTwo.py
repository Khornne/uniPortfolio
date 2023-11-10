def showMsg(title, body="", prefix="INFO", suffix="."):
    print(prefix,title,body,suffix,sep='\t')

results = showMsg("File missing", body="Insert Disk", suffix="Press return")

print(results)
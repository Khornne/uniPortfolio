f = open(r"E:\Coding Projects\Portfolio\uniPortfolio\Week 8\Practicals\info.txt", "a")
f.write("This is an extra line")
f.close()

f = open(r"E:\Coding Projects\Portfolio\uniPortfolio\Week 8\Practicals\info.txt", "r")
print(f.read())
import time
lines_st = set() #lines stored 
outputfile = open("output.txt", "w") #output file  and file name
filename=input("Input the face name: ") #take your file name as input
for line in open(filename, "r"):
    if line not in lines_st: # Unique line check
        outputfile.write(line.replace('\n',", ")) # replace new line with comma
        lines_st.add(line)

print("Working....")
time.sleep(4)
outputfile.close()
print("its done")

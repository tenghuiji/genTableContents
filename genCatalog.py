import re
def setp1(line):
	return re.sub(".\n",".",line)
def setp2(line):
	return re.sub("<span id","\n<span id",line)
def setp3(line):
	all = ""
	for l in re.findall("bookPageNum=\d+.*\>",line):
		all += '\n'+l.replace(">","")
	return all
def setp4(line):
	return line.replace("bookPageNum=","")
def setp5(line):
	return line.replace( "one-link-mark=\"yes","")
def setp6(line):
	return line.replace( "target=\"_blank\" style=\"display: none","")
def setp7(line):
	return line.replace( " target=\"_blank\" style=\"\" title=","")
def setp8(line):
	line = line.split('\n')
	all=""
	cur=""
	ind = ""
	for c in line:
		l = re.findall( "\d+\"",c) 
		if len(l) < 1:
			continue
		l[0].replace("\"","")
		cur = re.sub("\d+\"","",c).replace("\n","")
		cur += "\t"+l[0]+"\n"
		if cur.count(".") == 1:
			all+="\t"+cur.replace("\"","")
			strNumList = re.findall( "\d+\.\d+",all)[-1].split(".")
			#print(strNumList)
			ind = strNumList[0]+"."+str(int(strNumList[1])+1) #为“参考文献”添加标号
		elif cur.count(".") == 2:
			all+="\t\t"+cur.replace("\"","")
		elif cur.count(".") == 3:
			all+="\t\t\t"+cur.replace("\"","")
		elif cur.count(".") == 4:
			all+="\t\t\t\t"+cur.replace("\"","")
		elif cur.count(".") == 5:
			all+="\t\t\t\t\t"+cur.replace("\"","")
		elif cur.find("参考文献") != -1:
			all+="\t"+ind+cur.replace("\"","")
		else:
			all+=cur.replace("\"","")
	return all.replace(" ; title=目录","目录").replace(" ; title=","")
def getFile(path):
	file_object = open(path,'r',encoding='utf-8')
	allLine=""
	try: 
	    for line in file_object:
	    	allLine +=line
	       #do_somthing_with(line)
	finally:
	     file_object.close()
	return allLine
def main():
	path = r"D:/myProject/sciencereading/test.txt"
	s1 = setp1(getFile(path))
	s2 = setp2(s1)
	s3 = setp3(s2)
	s4 = setp4(s3)
	s5 = setp5(s4)
	s6 = setp6(s5)
	s7 = setp7(s6)
	s8 = setp8(s7)
	s9 = "封面\t1\n"+"书名页\t2\n"+"简介\t3\n"+"前言\t\n"+s8
	print(s9)
	f = open("catlog.txt", "w")
	f.write(s9)
	f.close()

if __name__=="__main__":
    main()

# phones.txt 파일에 아래의 2줄 쓰고 저장하시오. 
# 최무선  010-1111-2222")
# 정중부  010-2222-3333

outfile = open("./phones.txt", "a")

outfile.write("최무선  010-1111-2222")
outfile.write("정중부  010-2222-3333")

outfile.close() 

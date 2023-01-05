'''
Name:余波
Time:2020年10月14日15:30:20
'''
data = []
fr = open('111.txt',encoding='utf-8')
for line in fr.readlines():
    line = line.strip()
    data_line = line.split(',')

    data.append(data_line)
print(data[-1])

fr.close()
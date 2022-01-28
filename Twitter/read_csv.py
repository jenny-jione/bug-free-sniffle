import csv
import my_info

f = open(my_info.my_path+'/Twitter/BTS_twt_100.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)

for line in rdr:
    print(line[0])
    print(line[1])
    # print(line[1].split('https')[0])
    print()
    print()

f.close()

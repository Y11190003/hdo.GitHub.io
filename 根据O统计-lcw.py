#  S4-0.3.out     S5-0.3.out    S6-0.3.out
#  S4-0.9.out     S5-0.9.out    S6-0.9.out
#  mop.out    moph2.out    mopni.out
def cal(name_list):
    name_list_Cnum = []
    for molecule_name in name_list:
        num_C = []
        str_num = ''
        flag = 0
        for i in range(len(molecule_name)):
            if molecule_name[i] == 'O':
                if i == len(molecule_name) - 1:
                    num_C.append('1')
                else:
                    for k in range(i+1, len(molecule_name)):
                        if '0' <= molecule_name[k] <= '9':
                            str_num += molecule_name[k]
                        else:
                            if k == i+1:
                                str_num += '1'
                            i = k
                            num_C.append(str_num)
                            str_num = ''
                            break
            else:
                continue

        num_C.append(str_num)
        sum_C = 0
        for i in num_C:
            if i == '':
                num_C.remove(i)
            else:
                sum_C += int(i)

        if sum_C == 0:
            name_list_Cnum.append(0)
        elif sum_C > 20:
            name_list_Cnum.append(21)
        else:
            name_list_Cnum.append(sum_C)

    return name_list_Cnum


f1 = open('E:/shengwuzhineng/lcw-0909/sus-shujufenxi/S6-0.9.out','r')
f2 = open('E:/shengwuzhineng/lcw-0909/sus-shujufenxi/O-S6-1-0.9.txt', 'w')
z = 0
name = []
num = []
for line in f1:
    if line == '\n':
        continue
    else:
        linelist = line.strip().split()
        #print(linelist)
        if linelist[0] == '#':
            name_list = linelist[4:]
            name_list = cal(name_list)
           # print(name_list)
            for name_in in name_list:
                if name_in in name:
                    continue
                else:
                    name.append(name_in)
                #print(name)

name = sorted(name)
f1.seek(0)

if name[0] == 0:
    flag = 0
    name_write = name[1:]
else:
    flag = 1

f2.write('step ')
for na in name_write:
    #print(na)
    f2.write('%s '%('O' + str(na)))
f2.write('\n')
for line1 in f1:
    num_cal = []
    for i in range(len(name)):
        num_cal.append(int(0))
    if line1 == '\n':
        continue
    else:
        linelist = line1.strip().split()
        if linelist[0] == '#':
            name_list = linelist[4:]
            name_list = cal(name_list)
        else:
            z += 1
            f2.write('%d '%z)
            num = linelist[3:]
            for id,n in enumerate(name_list):
                coor = name.index(n)
                num_cal[coor] += int(num[id])

            if flag == 0:
                num_cal = num_cal[1:]

            for j in range(len(num_cal)):
                f2.write('%d '%num_cal[j])
            f2.write('\n')
f1.close()
f2.close()

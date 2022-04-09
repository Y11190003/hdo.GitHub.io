#  S4-0.3.out     S5-0.3.out    S6-0.3.out
#  S4-0.9.out     S5-0.9.out    S6-0.9.out
#  mop.out    moph2.out    mopni.out
#  S4-0.3.out(2)     S5-0.3.out(2)    S6-0.3.out(2)
#  S4-0.9.out(2)     S5-0.9.out(2)    S6-0.9.out(2)
#  mop.out    moph2.out    mopni.out
names = locals()
f_rd = open('E:/lyn/ISO/xo-MOP-species.out-1', 'r')
rd_lines = f_rd.readlines()
f2 = open('E:/lyn/ISO/species.txt','w')
#file_name = '121.out-1'
#s1.out0.9
target = ['No_Specs','No_Moles','HO', 'O', 'H2O', 'HOH', 'OH', 'H6C6', 'H5C6', 'H4C6', 'C', 'O', 'H', 'C2', 'C3', 'C4', 'C5', 'C6']
###'H8C6OC', 'H9C6OC', 'H6C6OC', 'H5C6OC', 'H7C6OC', 'H4C6OC'
###'H4C','H3C','H2C','HC','H7C6OOCH','H6C6OOCH','H7C6OC','H4C6OH','H5C6OOH', 'H4C2','H3OCH','H6C6','H5C6','H4C6','H2','HH','H','H3OC'

###'HO','O','H2O','HOH','OH'
###苯酚系列：'H4C6OH','H5C6O','H6C6O','H7C6O'

###'H2','HH','HO','O','H','H2O','HOH','H4C','H3C','H2C','HC2','H4C6','H5C6OOH','H7C6OOCH','H6C6OOCH','H8C6OOCH','H4C6OOH','H7C6OC','H4C6OH'
###,'H6C6OH','H6C6O','H5C6O','H3OC','H2OC','H6C6C','H6C6','H3C5','H4C2'

b =' '.join(target)      ### 不带[]的列表输出
print ("frame", b)
f2.write("frame" + ' ' + ' '.join(target))
f2.write('\n')

for i in target:

    names['orr_' + i] = []
    names['num_' + i] = 0

# Read coordinate from dump file 
z=[]
type=[]

#f_rd = open(file_name, 'r')
#rd_lines = f_rd.readlines()

count_0 = 0

for line in rd_lines:
    ls = line.split()
    count_1 = 0
    line_new = ''
    if ls[0] == '#':
        for i in target:
            names['orr_' + i] = []
            names['num_' + i] = 0
        for li in ls:
            count_1 += 1
            for tar in target:
                if li == tar:
                    names['orr_' + tar].append(str(count_1 - 1))

    else:
        for li in ls:
            count_1 += 1
            for tar in target:
                if str(count_1) in names['orr_' + tar]:
                    names['num_' + tar] += float(li)
        count_0 += 1
        line_new += str(count_0)

        for tar in target:
            line_new +=  ' ' + str(names['num_' + tar])
        #print(line_new)
        f2.write(line_new + '\n')











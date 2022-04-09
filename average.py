with open('10.txt','r') as f:
    the = f.readlines()
    #print(the)
num_count = 0
sum = 0
g = open('1.txt','w')
step = 10
list = []
for i in the:
    th = i.split()
    #print(th[1])
    #t2 = th[1]
    #print(t2)
    for j in th[1:]:
        #print(j)
        sum = int(sum) + int(j)
        num_count +=1
        print(num_count)
        if int(num_count) % 10 == 0:
            ave = int(sum)/10
            #print(ave)
            g.write('%d ' % num_count)
            g.write(str(ave))
            g.write('\n')
            sum = 0



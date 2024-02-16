t1 = ['00', '01', '02', '03','04','05','06','07','08','09','10','20','30','40','50','60','70','80','90','91', '92','93','94','95','96','97','98','99','19','29','39','49','59','69','79','89']
t2 = ['11','12','13','14','15','16','17','81','82','83','84','85','86','87','88','21','31','41','51','61','71','81','18','28','38','48','58','68','78','88']
t3 = ['22','23','24','25','26','27','72','73','74','75','76','77','32','42','52','62','37','47','57','67']
t4 = ['33','34','35','36','43','53','63','64','65','66','46','56']
t5 = ['44','45','54','55']
#o = []
#for z in t1:
 #   o.append(z)
#for z in t2:
    #o.append(z)
#for z in t3:
 #   o.append(z)
#for z in t4:
 #   o.append(z)
#for z in t5:
 #   o.append(z)
#o.sort()
#print(o)
for b in range(int(input())):
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    s5 = input()
    s6 = input()
    s7 = input()
    s8 = input()
    s9 = input()
    s10 = input()
    a = list()
    a.append(s1)
    a.append(s2)
    a.append(s3)
    a.append(s4)
    a.append(s5)
    a.append(s6)
    a.append(s7)
    a.append(s8)
    a.append(s9)
    a.append(s10)
    p = []
    y = []
    kol = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "X":
                p.append(i)
                y.append(j)
    for h in range(len(p)):
        if str(p[h])+str(y[h]) in t1:
            kol+=1
        elif str(p[h])+str(y[h]) in t2:
            kol+=2
        elif str(p[h])+str(y[h]) in t3:
            kol+=3
        elif str(p[h])+str(y[h]) in t4:
            kol+=4
        elif str(p[h])+str(y[h]) in t5:
            kol+=5
    print(kol)


#!/usr/bin/env python3

import sys
import configparser


for i in range(1,len(sys.argv)):
    if sys.argv[i] == '-c':
        peizhi_filename = sys.argv[i+1]
    if sys.argv[i] == '-d':
        yuangong_filename = sys.argv[i+1]
    if sys.argv[i] == '-o':
        shuchu_filename = sys.argv[i+1]



filename = peizhi_filename
cf = configparser.ConfigParser()
cf.read(filename)
JiShuL = float(cf.get("default","JiShuL"))
JiShuH = float(cf.get("default","JiShuH"))
YangLao = float(cf.get("default","YangLao"))
YiLiao = float(cf.get("default","YiLiao"))
ShiYe = float(cf.get("default","ShiYe"))
GongShang = float(cf.get("default","GongShang"))
ShengYu = float(cf.get("default","ShengYu"))
GongJiJin = float(cf.get("default","GongJiJin"))
SheBaoJiShu = YangLao + YiLiao + ShiYe + GongShang + ShengYu + GongJiJin
def shebao(gongzi):
    if gongzi > JiShuH:
        shebao = JiShuH * SheBaoJiShu
    elif gongzi > JiShuL:
        shebao = gongzi * SheBaoJiShu
    elif gongzi > 0:
        shebao = JiShuL * SheBaoJiShu
    else:
        shebao = 0
    return shebao


def jisuan_ynse(ynssdr):
    if ynssdr > 80000:
        ynse = ynssdr * 0.45 -13505
    elif ynssdr > 55000:
        ynse = ynssdr * 0.35 - 5505
    elif ynssdr > 35000:
        ynse = ynssdr * 0.30 -2755
    elif ynssdr > 9000:
        ynse = ynssdr * 0.25 -1005
    elif ynssdr > 4500:
        ynse = ynssdr * 0.20 -555
    elif ynssdr > 1500:
        ynse = ynssdr * 0.10 -105
    elif ynssdr > 0:
        ynse = ynssdr * 0.03
    else:
        ynse = 0
    return ynse
    

try:
    
    #yuangong_filename = '/home/shiyanlou/user.csv'
    with open(yuangong_filename,'r') as f:
        alist = f.readlines()
    for i in alist:
        gonghao = i.split(",")[0]
        #print(gonghao)
        gzje = int(float(i.split(",")[1]))
        #print(gzje)
        SheBao = shebao(gzje)
        #print(SheBao)
        #gzje = gzje * (1 - wuxianyijin)
        ynssdr = gzje - 3500 - SheBao
        
        ynse = jisuan_ynse(ynssdr)
        shgz = gzje -ynse - SheBao
        #print(ynse)
        #print(shgz)
        #print('{} : {:.2f}'.format(gonghao,(gzje - ynse )))
        #print('{},{},{:.2f},{:.2f},{:.2f}'.format(gonghao,gzje,SheBao,ynse,shgz))
        with open(shuchu_filename, 'a') as f:
            f.write(('{},{},{:.2f},{:.2f},{:.2f}'.format (gonghao,gzje,SheBao,ynse,shgz)) + '\n')
except:
    print("Parameter Error")
    


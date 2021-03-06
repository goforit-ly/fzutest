import jieba
import jieba.analyse
from math import sqrt
from functools import reduce

class getText():
    def __init__(txts,f11,f22,K=500):
        txts.f1 = f11
        txts.f2 = f22
        txts.vector1 = {}
        txts.vector2 = {}
        txts.topK = K
    #去除文本中的符号
    def delsim(txts):
        for ch in '！？《》，。、|-@#%：；.=【】{}~':
            txts.f1 = txts.f1.replace(ch, '')
            txts.f2 = txts.f2.replace(ch, '')

    #构建向量，以（词，权重）的形式存在
    def vector(txts):
        cut1 = jieba.analyse.extract_tags(txts.f1,topK = txts.topK, withWeight = True)
        cut2 = jieba.analyse.extract_tags(txts.f2,topK = txts.topK, withWeight = True)
        for key,value in cut1:
            txts.vector1[key] = value
        for key,value in cut2:
            txts.vector2[key] = value
        for key in txts.vector1:
            txts.vector2[key] = txts.vector2.get(key, 0)
        for key in txts.vector2:
            txts.vector1[key] = txts.vector1.get(key, 0)
    #计算向量余弦相似值
    def similar(txts):
        txts.vector()
        txts.delsim()
        sum = 0
        for key in txts.vector1:
            sum += txts.vector1[key]*txts.vector2[key]
        a = sqrt(reduce(lambda x,y: x+y, map(lambda x: x*x, txts.vector1.values())))
        b = sqrt(reduce(lambda x,y: x+y, map(lambda x: x*x, txts.vector2.values())))
        sum = sum/(a*b)
        return sum
        
if __name__ == '__main__':
    otxt = sys.argv[1]
    ctxt = sys.argv[2]
    atxt = sys.argv[3]
    #读入文件
    try:
        with open(otxt,encoding = 'utf-8') as file1:
            f1 = file1.read()
        with open(ctxt,encoding ='utf-8') as file2:
            f2 = file2.read()
    except:
        print('路径有错')
    K = int(len(f1)*0.8)
    s = getText(f1,f2,K)
    sim = round(s.similar(),2)
    #输出文件
    try:
        with open(atxt,'w+',encoding = 'utf-8') as file3:
            file3.write(str(sim))
    except:
        print('路径有错')
    import sys
    s.similar()

# Profundidad
import re 
patron=re.compile(r'\W')

def bla(F,V,ni):
    nodos={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7} 
    S=[]
    vi=nodos[ni]
    V=patron.split(V)
    v1=V[vi]
    S=[v1]
    Vp=[v1]
    Ep=[]
    S1=[]
    while True:
        boo = True
        for x in S:
            diferenciar(V,Vp)
            for y in Vaux:
                z=(x,y)
                if z in E:
                    Ep.append(z)
                    Vp.append(y)
                    S1.append(y)
                    boo = False
        if boo:
            print(Vp)
            print(Ep)
        S=S1
        S1=[]
        
def diferenciar(A,B):
    for i in B:
        for i in A:
            if i in Vaux:
                Vaux.remove(i)

vi='a'
V=('a b c d e f g h')

E={('a','b'),('a','c'),('a','g'),('b','a'),('b','d'),('b','g'),('c','a'),('c','d'),('c','e'),
    ('d','b'),('d','c'),('d','f'),('e','c'),('e','f'),('e','g'),('f','d'),('f','e'),('f','h'),
    ('g','a'),('g','b'),('g','e'),('h','f')} 

Vaux=()

bla(E,V,vi)
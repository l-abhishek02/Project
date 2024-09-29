import json

def resetfunct():
    data=[{'no':1,'name':"player1",'score':30},
          {'no':2,'name':"player2",'score':20},
          {'no':3,'name':"player3",'score':10}
        ]
    with open("data.json",'w') as txfl:
        json.dump(data,txfl)
'''
with open("data.json",'r')as rd:
    hs=json.load(rd)

    nm=input("nm=")
    n=int(input("no="))
    nv=[]
    cnt=0
    for each in hs:
        if n>each['score'] and cnt==0:
            print("hii")
            new={}
            new['no']=each['no']
            new['name']=nm
            new['score']=n
            nv.append(new)
            cnt+=1
        else:
            new={}
            new['no']=each['no']
            new['name']=each['name']
            new['score']=each['score']
            nv.append(new)
with open('data.json','w') as f:
    f.write(json.dumps(nv))
with open("data.json",'r')as tl:
    ha=json.load(tl)
    print(ha)
    '''

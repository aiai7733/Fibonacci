#coding:utf-8
import rhinoscriptsyntax as rs

def fib(n,a,b):
    oriPt = [0,0,0]
    moveVec =[0,0,0]
    for i in range(n):
        
        
        #出力
        str ='i={},a={},b={}'.format(i,a,b)
        print (str)
        
        #四角描写
        id = makeSrfPt(b,b)
        index = i%4
        
        if (index == 0):
            moveVec =[0,-b,0]
        elif(index == 1):
            moveVec =[a,0,0]
        elif(index == 2):
            moveVec =[-(b-a),a,0]
        elif(index == 3):
            moveVec =[-b,-(b-a),0]
        
        oriPt = rs.VectorAdd(oriPt,moveVec)
        rs.MoveObject(id,oriPt)
        
        
        # 次の繰り返しのための準備
        c = a+b
        a = b 
        b = c
def makeSrfPt(width,height):
    pts =[  [0,0,0],
            [width,0,0],
            [width,height,0],
            [0,height,0]
        ]
    id = rs.AddSrfPt(pts)
    return (id)
    
fib(7,0,1)
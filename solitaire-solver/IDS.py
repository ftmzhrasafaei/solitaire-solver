from Node import Node
from DLS import DLS

def IDS(inpcard ,firstlimit, n , m):
    limit = firstlimit
    d = DLS(inpcard , limit , n , m)
    if len(d)>1:
        s = d[0]
        step = d[1]
        borned =d[2]
        totalborn = borned
        sp = step
        if s:
            return s,step,borned , step
        limit = limit + 1 
        print('limit increased to ',limit)
        while True:
            d = DLS(inpcard , limit , n , m , sp)
            if len(d)>1:
                s = d[0]
                step = d[1]
                borned =d[2]
                sp = step
                totalborn = borned +  totalborn
                if not s :
                    limit = limit + 1
                    print('limit increased to ',limit)
                else:
                    return s,step,totalborn,step
            else:
                print('Failure')
                return False ,
    else:
        print('Failure ! ')
import copy 
from Node import Node

def ListValue(lv):
    val = []
    for n in lv:
        val.append(n.Value())
    return val

def PrintStep(step):
    if step < 11:
        print('---------- step--',step,'------------')
    if step > 10 and step < 101:
        if step%10 == 0:
            print('---------- step--',step,'-----------')
    if step > 100 and step < 1000:
        if step%100 == 0 :
            print('---------- step--',step,'----------')    
    if step >1000 and step <10000:
        if step%500 ==0:
            print('---------- step--',step,'----------')
    if step >10000:
        if step%1000 ==0:
            print('---------- step--',step,'----------')
            
def equality_test(sublist):
    for i in range(len(sublist) - 1):
        if sublist[i][len(sublist[i])-1] != sublist[i + 1][len(sublist[i + 1])-1]:
            return False      
    return True



def arrangement(sublist , n):
    cur = 0
    k0 = len(sublist)
    if n == k0:
        for i in range(n):
            cur = n - i
            numb = int(sublist[i][0:len(str(cur))])
            if cur != numb : 
              #  print('at i = ' , i)
                return False
        return True    
    else:
        return False


def Goal_test(mainlist , n , m):
    copy_list = copy.deepcopy(mainlist)
    while ['#'] in copy_list:
        copy_list.remove(['#'])
    if len(copy_list) != m:
        return False
    #print('pure list : ' , copy_list)
    else:
       # print('atleat equal size')
        for i in range(len(copy_list)):
            if not equality_test(copy_list[i]):
           # print('not equal')
                return False
            if not arrangement(copy_list[i] , n):
           # print('not arrang')
            #print(copy_list)
                return False
    return True

def child(inpstate , action):
    if inpstate[action] == ['#']:
        return []
    else:
        hstate = copy.deepcopy(inpstate)
        state = copy.deepcopy(hstate)
        sa = hstate[action][len(hstate[action])-1] ; 
      #  print('last state is',sa,'num is',sa[0:len(sa) -1],'state is',hstate)
        numsa = int(sa[0:len(sa) -1])
        children1 = []
        k = len(hstate)
        for i in range(k):
            state = copy.deepcopy(hstate)
            if i != action :
                curs = state[i][len(state[i])-1]; 
                if curs == '#':
                    state[i] = [sa]
                    state[action].remove(sa)
                    if len(state[action]) == 0:
                        state[action] = ['#']
                    children1.append(state)
                else :
                    if numsa <= int(curs[0:len(curs)-1]):
                        state[i].append(sa)
                        state[action].remove(sa)
                        if len(state[action]) == 0:
                            state[action] = ['#']
                        children1.append(state)

        return children1

def children(cstate):
    all_children = []
    wstate = copy.deepcopy(cstate)
    for i in range(len(wstate)):
        c = copy.deepcopy(child(wstate , i))
        if c != []:
            all_children = c + all_children
  #  print('len children is : ',len(all_children))
   # print('children are : ' , all_children)
    return all_children


def absence_check(ls , elm):
    #print('absence check : ',ls)
    if elm in ls:
        return False
    else:
        return True
    

def arrangementN(sublist, n , N):
    cur = 0
    total = 0
    for i in range(n):
        if(i < N):
            cur = n - i
            numb = int(sublist[i][0:len(str(cur))])
           # print(numb)
            if cur != numb :
                return i
            else :
                total = i + 1
        else:
            break
    return total


def h(inpstate , n , m): 
    inx = 0
    state = copy.deepcopy(inpstate)
    inds = [0 for i in range(len(state))]
    goality_list = [0 for i in range(len(state))]
    while ['#'] in state:
        state.remove(['#'])
    for place in state : 
        if len(place) == 1:
            inds[inx] = 1
        else:
            inds[inx] = 1
            for i in range(len(place) - 1):
               # print(place , place[i][len(place[i])-1] , place[i + 1][len(place[i + 1])-1])
                if place[i][len(place[i])-1] != place[i + 1][len(place[i + 1])-1]:
                    if i == 0:
                        inds[inx] = 0
                    break
                inds[inx] = inds[inx] + 1
        goality_list[inx]=  arrangementN(place , n , inds[inx])
        inx = inx + 1
    
    return (n*m -sum(goality_list))
def g(node):
    return node.Depth()
def H(nodelist , n ,m):
    val = ListValue(nodelist)
    goal_val = [0 for i in range(len(val))]
    for i in range(len(val)):
        goal_val[i] = h(val[i] , n , m) + g(nodelist[i])
    rnode = nodelist[goal_val.index(min(goal_val))]
    nodelist.remove(rnode)
    return rnode
    
def Hg(nodelist , n ,m):
    val = ListValue(nodelist)
    goal_val = [0 for i in range(len(val))]
    for i in range(len(val)):
        goal_val[i] = h(val[i] , n , m)
    rnode = nodelist[goal_val.index(min(goal_val))]
    nodelist.remove(rnode)
    return rnode
def HowMuch10(x):
    y = 0
    while x >= 10:
        x = x / 10
        y = y + 1
    return y

def SpaceCreator(length):
    strg = ''
    for i in range(length):
        strg = strg + ' '
    return strg


def OneSideDiff(l1 , l2 , state =False):
    one_diffrence = []
    if state:
        length = min(len(l1) , len(l2))
        for i in range(length):
            if l1[i] != l2[i]:
              #  if l1[i] == ['#']:
               #     one_diffrence.append([])
                #else:
                    one_diffrence.append(l1[i])
    else:
        for item in l1:
            if item not in l2:
                    one_diffrence.append(item)
    return one_diffrence
def Diff2D(l1 , l2 ,state =False):
    return OneSideDiff(l1 , l2 , state) , OneSideDiff(l2 , l1,state)


def index2D(ls , item , iflist=False):
    glist = []
    for subl in ls:
        if item in subl:
            glist = subl
            break
    ind = ls.index(glist)
    if iflist:
        return glist , ind
    else:
        return ind

def Movement(path):
    maxlevel = len(path)
    max10 = HowMuch10(maxlevel)
    for i in range(len(path) - 1):
        d = Diff2D(path[i].Value() , path[i + 1].Value(), True)
        m = list(Diff2D(d[0][0] , d[1][0]))
        if [] in m:
            m.remove([])
        item = m[0][0]
        #print('item : ',item)
        if item == '#':
            m = list(Diff2D(d[0][1] , d[1][1]))
            if [] in m:
                m.remove([])
            item = m[0][0]
        i1 = index2D(path[i].Value() , item , iflist=False)
        i2 = index2D(path[i + 1].Value() , item , iflist=False)
        PrintState(path[i])
        PrintState(path[i+1])
        print('level :' , i + 1 ,SpaceCreator(max10 - HowMuch10(i+ 1)) ,'move',item,' from column ',i1 + 1 , ' to column',i2 + 1 )
        print('======================================================')
        print('\n')
        
def PrintState(node):
    print('-------------- ' ,node.Depth(),'th State --------------' )
    x  = 0 
    state = node.Value()
    for col in state:
        x = x + 1
        print('column ',x ,' : ', col)
    print('\n')       
def get_params():
    inp = input('Please Enter n , m , k :')
    inp = inp.split()
    n = int(inp[0])
    m = int(inp[1])
    k = int(inp[2])
    return n , m , k

def get_cards(n , k):
    cards = [['' for i in range(n)] for j in range(k)]
    for i1 in range(k):
        print('Pleas Enter statment of ',i1+1,'th place')
        inp = input()
        if inp == '#':
            cards[i1] = ['#']
        else : 
                cards[i1] = inp.split()
    return cards

def SearchType():
    print('We can solve your problem using these three ways : ')
    print('1 - BFS(Breadth-first search)')
    print('2 - IDS(Iterative deepening depth-first search)')
    print('3 - A*')
    print('4 - Greedy (if you want to save time)')
    stype = int(input('Pleas Enter 1 or 2 or 3 or 4 to choose search type : '))
    if stype == 1:
        print('OK , we will solve your problem using BFS')
        print('Please Wait')
        return stype,
    if stype == 2:
        flimit = input('Please Enter first depth for IDS : ')
        if flimit:
            flimit = int(flimit)
        else : 
            flimit = 1
        
        print('OK , we will solve your problem using IDS')
        print('Please Wait')
        return stype , flimit
    if stype == 3:
        print('OK , we will solve your problem using A*')
        print('Please Wait')
        return stype,
    if stype == 4:
        print('OK , we will solve your problem using greedy search')
        print('Please Wait')
        return stype,
    
    
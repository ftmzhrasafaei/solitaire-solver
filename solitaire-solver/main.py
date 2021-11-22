import time
from Node import Node
from BFS import BFS
from IDS import IDS
from Greedy import Greedy
from Astar import Astar
from Functions import get_params , Movement , get_cards, SearchType 



#---------main----------
n , m , k = get_params()
while k<m :
    print('k must be greater than m, Try again')
    n , m , k = get_params()
    
c = get_cards(n , k)
stype = SearchType()
search = stype[0]
if len(stype) == 2:
    lim = stype[1]
if search == 1 :
    tstart = time.perf_counter()
    r = BFS(c , n ,m)
    tfinal = time.perf_counter()

if search == 2 :
    tstart = time.perf_counter()
    r = IDS(c , lim , n ,m)
    tfinal = time.perf_counter()

if search == 3:
    tstart = time.perf_counter()
    r = Astar(c , n , m)
    tfinal = time.perf_counter()

if search == 4:
    tstart = time.perf_counter()
    r = Greedy(c , n , m)
    tfinal = time.perf_counter()

if len(r)>1:
    if r[0]:
        step = r[1]
        result = r[0]
        born = r[2]
        exp = r[3]
        t = tfinal - tstart
        if t>60:
            print('The chosen search takes ',t/60,' minutes to solve this problem ')
        else:
            print('The chosen search takes ',t,' seconds to solve this problem ')
        print('Total steps to acheice the goal is ' , step)
        print('The number of expanded nodes is ', r[3] , 'and the number of borned nodes is ' , born)
        print('======================================================')
        print('\n')
        print('Solution .... ')
        path = result.Path()
        Movement(path)


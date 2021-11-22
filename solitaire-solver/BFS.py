from Node import Node
from Functions import PrintStep , Goal_test , ListValue , children , absence_check



def BFS(inpcard , n , m):
    borned = 1
    n1 = Node(inpcard)
    node = Node(0)
    explored = []
    frontier = [n1]
    step = 0
    while True:
        PrintStep(step)
        step = step + 1
        if len(frontier) == 0:
            print('Failure ! ')
            return False , 
        else:
            node = frontier.pop(0)
           # if Goal_test(node , n,m):
            #    return node ,step
           # node.PrintNode()
            explored.append(node)
            newchildren = children(node.Value())
            node.SetChildren(newchildren)
            for x in newchildren:
                if  absence_check(ListValue(frontier) , x) and absence_check(ListValue(explored) ,x):
                    borned = borned +1 
                    frontier.append(Node(x , node))
                    if Goal_test(x , n,m):
                        g = Node(x , node)
                        print('---------- step--',step,'------------')
                        print('Gooooall!')
                        return g ,step , borned , len(explored)
            

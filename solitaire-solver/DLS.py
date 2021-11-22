from Node import Node
from Functions import PrintStep , Goal_test  , ListValue , children , absence_check

def DLS(inpcard , limit , n ,m , step =0):
    n1 = Node(inpcard)
    node = Node(0)
    borned = 1
    frontier = [n1]
    while True:
        PrintStep(step)
        step = step + 1
        if len(frontier) == 0:
            print('Failure ! ')
            return False,
        else:
            node = frontier.pop()
         #   print('Depth : ',node.Depth())
            if node.Depth() > limit:
                while node.Depth() > limit:
                    if len(frontier) == 0:
                        print('There is no solution in this depth')
                        return False,step ,borned
                    else:
                        node = frontier.pop()

             #   if not UpperNode(frontier , node.Depth()):
              #      print('There is no solution in this depth')
               #     return node
                #else : 
                 #   node = UpperNode(frontier , node.Depth())
            if Goal_test(node.Value() , n,m):
                print('---------- step--',step,'------------')
                print('Gooooal!')
                return node ,step ,borned
           # node.PrintNode()
            newchildren = children(node.Value())
            node.SetChildren(newchildren)
            for x in newchildren:
                if  absence_check(ListValue(frontier) , x):
                    borned = borned + 1 
                    frontier.append(Node(x , node))
                    #if Goal_test(x , n,m):
                     #   g = Node(x , node)
                      #  return g ,step
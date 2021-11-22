

class Node:
    def __init__(self , value , parent = None , children = []):
        self.value = value
        self.parent = parent
        self.children = children

    def Parent(self):
        return self.parent
    def Children(self):
        return self.children
    def Value(self):
        return self.value
    def PrintNode(self):
        print('.',self.value ,'.' , end = ' ' )
    def PrintAll(self):
        if self.parent:
            self.parent.PrintAll()
            print('\n')
        self.PrintNode()
        print('\n')
        if self.children:
            for child in self.children:
                child.PrintNode()
                
    def SetParent(self , pNode):
        self.parent = pNode
    def SetChildren(self , childrenNodes):
        self.children = self.children + childrenNodes
        
    def Path(self):
        path2root = [self]
        temp = Node(0)
        temp = self
        while True:
            if temp.Parent() == None:
                break
            temp = temp.Parent()
            path2root.append(temp)
        path2root.reverse()
        return path2root

    def Depth(self):
        depth = 0
        temp = Node(0)
        temp = self
        while True:
            if temp.Parent() == None:
                break
            temp = temp.Parent()
            depth = depth + 1

        return depth
    

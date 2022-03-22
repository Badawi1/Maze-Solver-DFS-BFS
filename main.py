## Class Node to save board nodes and possible moves

import queue


class Node:
    id = None  # Unique value for each node, the 1D index of node in the board game
    up = None  # Represents value of neighbors (up, down, left, right), e.g. Index of up node is ..
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of previous Node.

    def __init__(self, value):
        self.value = value  #set the value of the current node (either S or . or # or E)


class SearchAlgorithms:
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.

    ## Update the neighbors 1D index according to my place
    def update_Indeces(self,count):
        #initialize all values with None
        up = None
        down = None
        left = None
        right = None

        if count ==0:   #if I am at index 0, then no up and no left, my right is index 1 and my down is index 7
            right = 1
            down = 7
        elif count == 1:
            left =0
            right =2
            down = 8
        elif count ==2:
            left =1
            right =3
            down =9
        elif count == 3:
            left =2
            right =4
            down=10
        elif count ==4:
            left = 3
            right = 5
            down = 11
        elif count ==5:
            left =4
            right = 6
            down =12
        elif count == 6:
            left = 5
            down = 13
        elif count == 7:
            up =0
            right = 8
            down = 14
        elif count ==8:
            up =1
            down = 15
            left = 7
            right =9
        elif count == 9:
            up = 2
            down = 16
            left = 8
            right = 10
        elif count ==10:
            up = 3
            down = 17
            left = 9
            right = 11
        elif count == 11:
            up = 4
            down = 18
            left = 10
            right = 12
        elif count ==12:
            up = 5
            down = 19
            left = 11
            right = 13
        elif count ==13:
            up = 6
            down = 20
            left = 12
        elif count ==14:
            up =7
            down = 21
            right =15
        elif count == 15:
            up =8
            down = 22
            left = 14
            right = 16
        elif count == 16:
            up = 9
            down = 23
            left = 15
            right = 17
        elif count == 17:
            up = 10
            down = 24
            left = 16
            right = 18
        elif count ==18:
            up = 11
            down = 25
            left = 17
            right = 19
        elif count == 19:
            up = 12
            down = 26
            left = 18
            right = 20
        elif count == 20:
            up = 13
            down = 27
            left = 19
        elif count == 21:
            up =14
            down = 28
            right =22
        elif count == 22:
            up =15
            down = 29
            left = 21
            right = 23
        elif count == 23:
            up = 16
            down = 30
            left = 22
            right = 24
        elif count == 24:
            up = 17
            down = 31
            left = 23
            right = 25
        elif count == 25:
            up = 18
            down = 32
            left = 24
            right = 26
        elif count == 26:
            up = 19
            down = 33
            left = 25
            right = 27
        elif count == 27:
            up = 20
            down = 34
            left = 26
        elif count == 28:
            up = 21
            right = 29
        elif count == 29:
            up = 22
            right = 30
            left = 28
        elif  count == 30:
            up = 23
            right = 31
            left = 29
        elif count == 31:
            up = 24
            right = 32
            left =30
        elif count == 32:
            up = 25
            right = 33
            left = 31
        elif count == 33:
            up = 26
            right = 34
            left = 32
        elif count == 34:
            up = 27
            left = 33
        return up, down, left, right

    def __init__(self, mazeStr):        # mazeStr is the string that build my board game by S and . and # and E
        maze = mazeStr.split(" ")       #each row in maze is separated by space
        self.board = list()
        counter = 0
        for lineindex in range(len(maze)):
            singlenode= maze[lineindex].split(",")  #each node in the row is separated by ","
            for nde in singlenode:      # nde contains node value either S or . or # or E
                N = Node(nde)
                N.id = counter          # this node 1D index
                N.up, N.down, N.left, N.right = self.update_Indeces(counter)        # update this node with indeces of all neighbors

                self.board.append(N)
                counter = counter +1

    def getavilabemoves(self,Nde):

        avilablemoveslise = list()
        avilablemovesliseNodes = list()

        if Nde.up != None:      # if I can move up, then up will have a 1D index not None
            avilablemoveslise.append(Nde.up)
        if Nde.down != None :
            avilablemoveslise.append(Nde.down)
        if Nde.left != None :
            avilablemoveslise.append(Nde.left)
        if Nde.right != None:
            avilablemoveslise.append(Nde.right)

        for i in avilablemoveslise:
            for N in self.board:
                if N.id == i and N.value != "#":
                    avilablemovesliseNodes.append(N)


        return avilablemovesliseNodes

    def BFS(self):
        # TODO 1.1 write implementation code for the BFS (Breadth First Search) algorithm
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        N = Node(self.board[0])
        self.bfs2(self.board[0])

        self.path = []
        val = self.fullPath[len(self.fullPath)-1]
        for x in range(len(self.board)):
            if (val == self.board[x].id):
                N = self.board[x]

        while 1==1:
            if (N.id==0):
                self.path.append(N.id)
                break
            self.path.append(N.id)
            N = N.previousNode

        self.path.reverse()




        return self.path, self.fullPath

    def bfs2(self,Node):
        q = queue.Queue()
        q.put(Node)
        visited = set()
        while q.empty()!=1:
            Node = q.get()
            if Node not in visited:
                self.fullPath.append(Node.id)
                if Node.value == 'E':
                    return self.path
                visited.add(Node)
                for neighbor in self.getavilabemoves(Node):
                    if(neighbor.previousNode==None):
                        neighbor.previousNode = Node
                    q.put(neighbor)



    def DFS(self):
        # TODO 1.2 write implementation code for the DFS (Depth First Search) algorithm
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.fullPath.clear()
        self.path.clear()

        self.dfs2(self.board[0])
        return self.path, self.fullPath

    def dfs2(self,Node):

        """ if(Node.value=='E'):
            self.fullPath.append(Node.id)
            return self.path,self.fullPath

        elif(Node.value!='v'):
           Node.value = 'v'
           self.fullPath.append(Node.id)
           l = self.getavilabemoves(Node)
           for x in l:
               self.dfs2(x)"""

        stack = [(Node, [Node.id])]
        visited = set()
        while len(stack) != 0:
            (Node, self.path) = stack.pop()
            if Node not in visited:
                self.fullPath.append(Node.id)
                if Node.value == 'E':
                    return self.path
                visited.add(Node)
                for neighbor in self.getavilabemoves(Node):
                    stack.append((neighbor, self.path + [neighbor.id]))



# Main function that solve the problem
def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('BFS Path is: [' + str(path) + ']\nFull Path is: [' + str(fullPath) + ']\n\n')

                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('DFS Path is: [' + str(path) + ']\nFull Path is: [' + str(fullPath) + ']\n\n')

                #######################################################################################



main()

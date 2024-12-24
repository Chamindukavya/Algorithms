import sys

class Graph:

    def __init__(self,numberOfVertices):
        
        self.V = numberOfVertices
        self.g = []
        for i in range(self.V):
            self.g.append([0]*self.V)


    def getMinIndex(self,visited,distance):

        min = sys.maxsize
        minIndex = 0
        for i in range(self.V):            
            temp = distance[i]
            #print(temp)
            if(temp<min and visited[i] == False):
                min = temp
                minIndex = i
                #print("minIndex",minIndex)

        return minIndex             


    def dijkstra(self,source):

        visited = [False]*self.V
        distance = [sys.maxsize]*self.V
        distance[source] = 0

        for i in range(self.V):

            #get the node with minimum distance
            x = self.getMinIndex(visited,distance)
            print("X is", x)

            visited[x] = True

            for j in range(self.V):
                if(visited[j] == False and self.g[x][j] != 0 and distance[j]>=(self.g[x][j] + distance[x])):
                    distance[j] = self.g[x][j] + distance[x]


        print(distance)            
        

if __name__ == "__main__":
    
    graph = Graph(9)

    graph.g = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
    
    graph.dijkstra(0)
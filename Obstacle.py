import Node

class Obstacle:
    
    aVert = Node()
    bVert = Node()
    cVert = Node()

    def getKey(self):
        return str(aVert.x)+str(aVert.y)+str(bVert.x)+str(bVert.y)+str(cVert.x)+str(cVert.y)

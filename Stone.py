import random
class Stone:

    stoneX = 0
    stoneY = 0
    pic1 = (r'stone.png')
    #def __init__(self):
       # self.stoneX = 0
       # self.stoneY = 0
       # self.pic = (r'stone.png')
    def __init__(self, stoneX=None, stoneY=None):
        if stoneX is None:
            stoneX = random.randint(40, 1170)
        if stoneY is None:
            stoneY = random.randint(60, 720)
        self.stoneX = stoneX
        self.stoneY = stoneY
        self.pic = r'stone.png'
        #return self.stoneX, self.stoneY
        #self.mask = pygame.mask.from_surface(self.pic)

     

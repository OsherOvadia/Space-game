import pygame
import Stone
import random
class Star:
    star_x = 0
    star_y = 0
    pic = pygame.image.load(r"star.png")
    pic1 = pygame.transform.scale(pic,(30,30))
    need_to_search = True
    def __init__(self,stone_arr):
        need_to_search = True
        star_x, star_y  = random.randint(30,1170) , random.randint(50,750)
        self.star_x =  star_x
        self.star_y = star_y
        if(len(stone_arr)==0):
            self.star_x, self.star_y  = random.randint(30,1170) , random.randint(50,750)
            return 
        while(need_to_search):
            counter =0
            for i in stone_arr:
                if abs(i.stoneX-star_x)<100 and abs(i.stoneY-star_y)<100 and star_x<0 and star_x>1150 and star_y<0 and star_y>750:
                    Star(stone_arr)
                if i==stone_arr[counter]:
                    self.star_x =  star_x
                    self.star_y = star_y
                    need_to_search = False
                    return
                
                counter+=1

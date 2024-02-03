#flying spaceship Project
import pygame
from Stone import Stone
from Star import Star
from pygame.locals import KEYDOWN,K_d,K_w,K_s,K_a,K_SPACE,K_ESCAPE,KMOD_NONE,K_DOWN,K_UP,K_RIGHT,K_LEFT
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
game_over_pic = pygame.image.load(r"gameOver.jpg")
playerScoreX = 1200
playerScoreY =50
black = (255,255,255)
blue = (0,0,255)
white = (0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def level10f(arr,points):
    level10=True
    for stone in arr:
        if arr.index(stone)<5:
            stone.stoneY+=5
        else:
            stone.stoneY+=arr.index(stone)
        if(stone.stoneY>750):
            stone.stoneY=5
    createStone(Star,arr,points-10,level10)
def is_crashed(x,y,arr,points):
    if  x>1150 or x<-5 or y>760 or y<-5:
            Main.gameOver(points)
            return True
    for stone in arr:        
        if((abs(stone.stoneX-x)<65 and abs(stone.stoneY-y)<35)):
            Main.gameOver(points)
            return True
def createStone(star,arr,points,level10):
    created = False
    i=0
    while(len(arr)<points and not created):
        k = Stone()
        if(abs(k.stoneX-star.star_x)>40 and abs(k.stoneY-star.star_y)>40):
            created==True
            i+=1
            print(len(arr), points ,created)
            if(level10):
                return add_stone(k.stoneX,0,arr)
            else:
                return add_stone(k.stoneX,k.stoneY,arr)
        if(abs(k.stoneX-star.star_x)<40 or abs(k.stoneY-star.star_y)<40):
            createStone(star,arr,points,level10) 
            created == True   
        
def add_stone(stoneX, stoneY, arr):
    k = Stone(stoneX, stoneY)  
    arr.append(k)

class Main: 
    def play():
            movement=True
            global points 
            points = 0
            arr = []
            arr1 = []
            level10 = False
            dir1 = False
            x, y = 100, 400
            black, white = (255, 255, 255), (0, 0, 0)
            Xvelocity, yVelocity = 0, 0
            stoneCounter=0
            captured=False
            run = True
        
            pygame.init()  
            pygame.display.set_caption('flying spaceship')
            clock = pygame.time.Clock()
            player1 = pygame.image.load(r'spaceShip.png').convert_alpha()
            player = pygame.transform.scale(player1, (60, 40)).convert_alpha()
            boost1 = pygame.image.load(r'boosing.png').convert_alpha()
            boost = pygame.transform.scale(boost1, (60, 40)).convert_alpha()
            stone = pygame.image.load(r'stone.png').convert_alpha()
            star = Star(arr)
            #star1 = pygame.image.load(r'star.png').convert_alpha()
            #star = pygame.transform.scale(star1,(30,30)).convert_alpha()
            
            
            
            
            font = pygame.font.Font('freesansbold.ttf', 30)
            stoneBool=False
            while run:
                #score
                playerText = "Score: "  + str(points)
                score1 = font.render(playerText, True, black , white ) 
                points = int(points)
                score1Rect = score1.get_rect()
                score1Rect.center = (playerScoreX//2 , playerScoreY//2)

                # reduce speedOf spaceship
                Xvelocity=Xvelocity/1.05 
                yVelocity=yVelocity/1.05
                #main loop
                for event in pygame.event.get():
                    #Quit
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        quit()
                #if the spaceShip is on star?  
                #get input + movement
                keys = pygame.key.get_pressed()
                if(movement):
                    if keys[K_a] or keys[K_LEFT] and Xvelocity > -10:
                        Xvelocity -= 0.6
                        dir1=True
                    if keys[K_d] or keys[K_RIGHT]  and Xvelocity < 10:
                        Xvelocity += 0.6
                        dir1=True
                    if keys[K_w] or keys[K_UP] and yVelocity > -10:
                        yVelocity -= 0.6
                        dir1=True
                    if keys[K_s] or keys[K_DOWN] and yVelocity < 10:
                        yVelocity += 0.6
                        dir1=True
                    if not keys[K_s] and not keys[K_w] and not keys[K_d] and not keys[K_a]:
                        dir1=False  
                #change the location of spaceShip
                x += Xvelocity
                y += yVelocity
                #Screen fill
                screen.fill((0,0,40))
                screen.blit(score1, score1Rect)
                #add fire to the Spaceship
                if(not dir1):
                    screen.blit(player, (x, y))
                if(dir1):
                    screen.blit(boost, (x,y))
                #change gameModes
                screen.blit(star.pic1,(star.star_x,star.star_y))
                if abs(x-star.star_x)<20 and abs(y-star.star_y)<20:
                    captured=True
                if(points>0 and points<10):
                    stoneBool = True
                if(points>=10):
                    level10 = True
                    stoneBool = False
                if(level10):
                    level10f(arr1,points)
                if(stoneBool):
                    createStone(star,arr,points,level10)
                    
                #check if the SpaceShip not on Stone
                if(stoneBool):
                    for stone in arr:
                        pic = pygame.image.load(r"stone.png").convert_alpha()
                        screen.blit(pic, (stone.stoneX, stone.stoneY))
                if(level10):
                    for stone in arr1:
                        pic = pygame.image.load(r"stone.png").convert_alpha()
                        screen.blit(pic, (stone.stoneX, stone.stoneY))
                    
                #If the SpaceShip is on Star
                if(captured):
                    star = Star(arr)
                    captured=False
                    points+=1
                if(points == 18):
                    print("VICTORY")
                #Check if Crashed
                if(stoneBool or level10):
                    if is_crashed(x,y,arr,points):
                        movement=False
                        Xvelocity=0
                        yVelocity=0
                pygame.display.update()
                clock.tick(30)
    #show Score
    def gameOver(points):
        playerText = "Score: "  + str(points)
        font = pygame.font.Font('freesansbold.ttf', 30)
        score1 = font.render(playerText, True, black , blue ) 
        score1Rect = score1.get_rect()
        
        score1Rect.center = (playerScoreX//2 , playerScoreY//2)
        screen.blit(game_over_pic,(0,0))
        screen.blit(score1, score1Rect)
        
        keys = pygame.key.get_pressed()
        #Quit
        if keys[K_ESCAPE]:
            pygame.quit()
            quit()
        #Rematch
        if keys[K_SPACE]:
                Main.play()
        pygame.display.update()
Main.play()





        

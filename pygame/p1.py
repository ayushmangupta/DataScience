import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((1180,780))
#screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen.fill((3, 125, 11))
done = False
clock = pygame.time.Clock()
sq_height = 93
sq_width  = 93
x = 40
y = 40
disc_color = [(225,225,225),(0,0,0)]


class Board:
    
    def __init__(self):
        self.board_array = np.zeros(shape=([8,8]))+9
        

    def get_board(self):
        return self.board_array
    
    def move(self,pos,player):
        self.board_array[pos] = int(player)



# create new board
board  = Board()
# display board
#print("board ",board.get_board())



while not done:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Esc")
                done = True


        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(str((int(pos[0]/96)+1)),str((int(pos[1]/96)+1)))
            sq_row = int(pos[0]/96)+1
            sq_col = int(pos[1]/96)+1

            print(pos[0],pos[1])
            xx= int(pos[0]/96)
            yy= int(pos[1]/96)
            
            #pygame.draw.circle(screen,(225,225,225),(int(pos[0]),int(pos[1])),36)
            if(sq_col<9 and sq_row<9):
                pygame.draw.circle(screen,disc_color[np.random.choice(2)],(int(96*(xx+.1)+(sq_width/2)),int(96*(yy+.1)+(sq_height/2))),36)
                board.move((yy,xx),0)
                #print("board ",board.get_board())
                #print("Update scoreboard called")
                #text = updateScoreboard()
                


    
    

    for x in range(8):
        for y in range(8):
            pygame.draw.rect(screen,(225,225,225),pygame.Rect(96*(x+.1),96*(y+.1),sq_width,sq_height),5)
        
    pygame.display.flip()
import pygame
import os
import numpy as np

width, height = 1200, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Chess v0.0")

background_colour = (255, 204, 229)
light_square_colour = (255, 153, 204)
dark_square_colour = (102, 0, 51)

fps = 60

wk = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wk.png')), (100, 100))
wq = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wq.png')), (100, 100))
wr = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wr.png')), (100, 100))
wb = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wb.png')), (100, 100))
wn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wn.png')), (100, 100))
wp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wp.png')), (100, 100))
bk = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bk.png')), (100, 100))
bq = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bq.png')), (100, 100))
br = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'br.png')), (100, 100))
bb = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bb.png')), (100, 100))
bn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bn.png')), (100, 100))
bp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bp.png')), (100, 100))

offset = np.empty(shape = (8, 4, 4)) #ij0 = x, ij1 = y, ij2 = 0/1 where 0 is captured, ij3 = 0/1/2/3/4 -> not promoted, Q, R, B, N
for i in range(8):
    for j in range(4):
        offset[i, j, 0], offset[i, j, 1], offset[i, j, 2] = 0, 0, 1
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        window.fill(background_colour)
        pygame.draw.rect(window, light_square_colour, pygame.Rect(50, 50, 800, 800))
        for i in range(8):
            for j in range(8):
                if ((i + j)%2 == 1):
                    pygame.draw.rect(window, dark_square_colour, pygame.Rect(50 + i * 100, 50 + j * 100, 100, 100))
        
        for i in range(8):
            for j in range(8):
                if (j == 0):
                    if i == 0:
                        window.blit(br, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                    elif i == 7:
                        window.blit(br, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                    elif i == 1:
                        window.blit(bn, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                    elif i == 6:
                        window.blit(bn, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                    elif i == 2:
                        window.blit(bb, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                    elif i == 5:
                        window.blit(bb, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                    elif i == 3:
                        window.blit(bq, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                    elif i == 4:
                        window.blit(bk, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                elif (j == 1):
                    window.blit(bp, (50 + i * 100 + offset[i, j, 0], 50 + j * 100 + offset[i, j, 1]))
                elif (j == 6):
                    window.blit(wp, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
                elif (j == 7):
                    if i == 0:
                        window.blit(wr, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
                    elif i == 7:
                        window.blit(wr, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
                    elif i == 1:
                        window.blit(wn, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
                    elif i == 6:
                        window.blit(wn, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
                    elif i == 2:
                        window.blit(wb, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
                    elif i == 5:
                        window.blit(wb, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
                    elif i == 3:
                        window.blit(wq, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
                    elif i == 4:
                        window.blit(wk, (50 + i * 100 + offset[i, j-4, 0], 50 + j * 100 + offset[i, j-4, 1]))
        pygame.display.update()
    
    pygame.quit()

if __name__ == '__main__':
    main()
    
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

wk = pygame.image.load(os.path.join('Assets', 'wk.png'))
wk = pygame.transform.scale(wk, (100, 100))
wq = pygame.image.load(os.path.join('Assets', 'wq.png'))
wq = pygame.transform.scale(wq, (100, 100))
wr = pygame.image.load(os.path.join('Assets', 'wr.png'))
wr = pygame.transform.scale(wr, (100, 100))
wb = pygame.image.load(os.path.join('Assets', 'wb.png'))
wb = pygame.transform.scale(wb, (100, 100))
wn = pygame.image.load(os.path.join('Assets', 'wn.png'))
wn = pygame.transform.scale(wn, (100, 100))
wp = pygame.image.load(os.path.join('Assets', 'wp.png'))
wp = pygame.transform.scale(wp, (100, 100))
bk = pygame.image.load(os.path.join('Assets', 'bk.png'))
bk = pygame.transform.scale(bk, (100, 100))
bq = pygame.image.load(os.path.join('Assets', 'bq.png'))
bq = pygame.transform.scale(bq, (100, 100))
br = pygame.image.load(os.path.join('Assets', 'br.png'))
br = pygame.transform.scale(br, (100, 100))
bb = pygame.image.load(os.path.join('Assets', 'bb.png'))
bb = pygame.transform.scale(bb, (100, 100))
bn = pygame.image.load(os.path.join('Assets', 'bn.png'))
bn = pygame.transform.scale(bn, (100, 100))
bp = pygame.image.load(os.path.join('Assets', 'bp.png'))
bp = pygame.transform.scale(bp, (100, 100))

offset_br1_x, offset_br1_y = 0, 0
offset_br2_x, offset_br2_y = 0, 0
offset_bn1_x, offset_bn1_y = 0, 0
offset_bn2_x, offset_bn2_y = 0, 0
offset_bb1_x, offset_bb1_y = 0, 0
offset_bb2_x, offset_bb2_y = 0, 0
offset_bq_x, offset_bq_y = 0, 0
offset_bk_x, offset_bk_y = 0, 0
offset_wr1_x, offset_wr1_y = 0, 0
offset_wr2_x, offset_wr2_y = 0, 0
offset_wn1_x, offset_wn1_y = 0, 0
offset_wn2_x, offset_wn2_y = 0, 0
offset_wb1_x, offset_wb1_y = 0, 0
offset_wb2_x, offset_wb2_y = 0, 0
offset_wq_x, offset_wq_y = 0, 0
offset_wk_x, offset_wk_y = 0, 0

offset = np.empty(shape = (8, 4, 3))
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
    
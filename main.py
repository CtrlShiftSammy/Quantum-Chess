import pygame
import os
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

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
        offset[i, j, 0], offset[i, j, 1], offset[i, j, 2],  offset[i, j, 3] = 0, 0, 1, 0
def main():
    clock = pygame.time.Clock()
    run = True
    drag =  False
    drag_i = 0
    drag_j = 0
    click_x = 0
    click_y = 0
    pick_i = 0
    pick_j = 0
    while run:
        clock.tick(fps)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == MOUSEBUTTONDOWN:
                for i in range(8):
                    for j in range(4):
                        if (mouse_x > 50 + i * 100 + offset[i, j, 0]) and (mouse_x < 50 + (i + 1) * 100 + offset[i, j, 0]) and (mouse_y > 50 + ((j + ((4) if (j > 1) else 0)) * 100 + offset[i, j, 1]) and (mouse_y < 50 + (j + ((5) if (j > 1) else 1)) * 100 + offset[i, j, 1]) and offset[i, j, 2] == 1):
                            drag = True
                            drag_i = i
                            drag_j = j
                            pick_i = i + offset[i, j, 0] / 100
                            pick_j = (j if j <= 1 else j + 4) + offset[i, j, 1] / 100
                            click_x = mouse_x
                            click_y = mouse_y
            elif event.type == MOUSEBUTTONUP:
                for i in range(8):
                    for j in range(8):
                        if drag and (mouse_x > 50 + i * 100) and (mouse_x < 50 + (i + 1) * 100) and (mouse_y > 50 + j * 100) and (mouse_y < 50 + (j + 1) * 100):
                            for k in range(8):
                                for l in range(4):
                                    if k * 100 + offset[k, l, 0] == i * 100 and (l + (4 if l > 1 else 0)) * 100 + offset[k, l, 1] == j * 100:
                                        if k * 100 + offset[k, l, 0] != pick_i * 100 or (l + (4 if l > 1 else 0)) * 100 + offset[k, l, 1] != pick_j * 100: #remove after adding legal check
                                            offset[k, l, 2] = 0
                            drag = False
                            offset[drag_i, drag_j, 0] = offset[drag_i, drag_j, 0] + (i - pick_i) * 100
                            offset[drag_i, drag_j, 1] = offset[drag_i, drag_j, 1] + (j - pick_j) * 100
        window.fill(background_colour)
        pygame.draw.rect(window, light_square_colour, pygame.Rect(50, 50, 800, 800))
        for i in range(8):
            for j in range(8):
                if ((i + j)%2 == 1):
                    pygame.draw.rect(window, dark_square_colour, pygame.Rect(50 + i * 100, 50 + j * 100, 100, 100))
        
        for i in range(8):
            for j in range(4):
                if offset[i, j, 2] == 1:
                            piece = (br if (i == 0 or i == 7) else (bn if (i == 1 or i == 6) else (bb if (i == 2 or i == 5) else (bq if i == 3 else bk)))) if (j == 0) else (bp if j == 1 else (wp if j == 2 else (wr if (i == 0 or i == 7) else (wn if (i == 1 or i == 6) else (wb if (i == 2 or i == 5) else (wq if i == 3 else wk))))))
                            window.blit(piece, (50 + i * 100 + offset[i, j, 0] + ((mouse_x - click_x) if (drag and drag_i == i and drag_j == j) else (0)), 50 + (j + (4 if j > 1 else 0)) * 100 + offset[i, j, 1] + ((mouse_y - click_y) if (drag and drag_i == i and drag_j == j) else (0))))
        pygame.display.update()
    
    pygame.quit()

if __name__ == '__main__':
    main()

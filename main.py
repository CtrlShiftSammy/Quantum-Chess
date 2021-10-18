import pygame
import os
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

width, height = 1200, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Chess v0.0")

background_colour = (132, 86, 60)
light_square_colour = (255, 255, 204)
dark_square_colour = (194, 139, 109)

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

def check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
    if drag_j == 1:
        if pick_i == i: #forward
            for a in range(8):
                for b in range(4):
                    if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                        return False
        elif abs(pick_i - i) == 1: #diagonal
            for a in range(8):
                for b in range(4):
                    if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                        return (False if b <= 1 else True)
            return False
        else:
            return False
    elif drag_j == 2:
        if pick_i == i: #forward
            for a in range(8):
                for b in range(4):
                    if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                        return False
        elif abs(pick_i - i) == 1: #diagonal
            for a in range(8):
                for b in range(4):
                    if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                        return (False if b > 1 else True)
            return False
        else:
            return False
    elif drag_j == 3: # white pieces
        if drag_i == 0 or drag_i == 7: # rooks
            if pick_i == i: # vertical
                if pick_j < j: # top to bottom
                    for a in range(8):
                        for b in range(4):
                            #for k in (pick_j + 1, j): #no piece in between
                            k = pick_j + 1
                            while k < j:
                                if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == k and offset[a, b, 2] == 1: #if piece
                                    return False
                                k += 1
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if whie piece at end
                                return False
                else: # bottom to top
                    for a in range(8):
                        for b in range(4):
                            #for k in (j + 1, pick_j): #no piece in between
                            k = j + 1
                            while k < pick_j:
                                if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == k and offset[a, b, 2] == 1: #if piece
                                    return False
                                k += 1
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if whie piece at end
                                return False
            elif pick_j == j: # horizontal
                if pick_i < i: # left to right
                    for a in range(8):
                        for b in range(4):
                            #for k in (pick_i + 1, i): #no piece in between
                            k = pick_i + 1
                            while k < i:
                                if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                                    return False
                                k += 1
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if whie piece at end
                                return False
                else: # right to left
                    for a in range(8):
                        for b in range(4):
                            #for k in (i + 1, pick_i): #no piece in between
                            k = i + 1
                            while k < pick_i:
                                if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                                    return False
                                k += 1
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if whie piece at end
                                return False
                    #if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                    #    return False
        elif drag_i == 1 or drag_i == 6: # knights
            
    return True

def legal(whites_turn, drag_i, drag_j, pick_i, pick_j, i, j):
        # pick ij -> ij
        if pick_i == i and pick_j == j:
            return False
        if whites_turn:
            if drag_j == 2:
                if (pick_j == j + 1) and (pick_i == i or pick_i == i + 1 or pick_i == i - 1) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                    return True
                elif (pick_j == 6) and (j == 4) and (pick_i == i) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j+1) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                    return True
            elif drag_j == 3:
                if drag_i == 0 or drag_i == 7:
                    if (pick_i == i or pick_j == j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif drag_i == 1 or drag_i == 6:
                    if abs(pick_i - i) == 2:
                        if abs(pick_j - j) == 1:
                            return True
                    elif abs(pick_j - j) == 2:
                        if abs(pick_i - i) == 1:
                            return True
                elif drag_i == 2 or drag_i == 5:
                    if abs(pick_i - i) == abs(pick_j - j):
                        return True
                elif drag_i == 3:
                    if abs(pick_i - i) == abs(pick_j - j):
                        return True
                    elif pick_i == i:
                        return True
                    elif pick_j == j:
                        return True
                elif drag_i == 4:
                    if abs(pick_i - i) <= 1 and abs(pick_j - j) <= 1:
                        if abs(pick_i - i) == abs(pick_j - j):
                            return True
                        elif pick_i == i:
                            return True
                        elif pick_j == j:
                            return True
            return False
        else:
            if drag_j == 1:
                if (pick_j == j - 1) and (pick_i == i or pick_i == i + 1 or pick_i == i - 1) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                    return True
                elif (pick_j == 1) and (j == 3) and (pick_i == i) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j-1) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                    return True
            elif drag_j == 0:
                if drag_i == 0 or drag_i == 7:
                    if pick_i == i:
                        return True
                    elif pick_j == j:
                        return True
                elif drag_i == 1 or drag_i == 6:
                    if abs(pick_i - i) == 2:
                        if abs(pick_j - j) == 1:
                            return True
                    elif abs(pick_j - j) == 2:
                        if abs(pick_i - i) == 1:
                            return True
                elif drag_i == 2 or drag_i == 5:
                    if abs(pick_i - i) == abs(pick_j - j):
                        return True
                elif drag_i == 3:
                    if abs(pick_i - i) == abs(pick_j - j):
                        return True
                    elif pick_i == i:
                        return True
                    elif pick_j == j:
                        return True
                elif drag_i == 4:
                    if abs(pick_i - i) <= 1 and abs(pick_j - j) <= 1:
                        if abs(pick_i - i) == abs(pick_j - j):
                            return True
                        elif pick_i == i:
                            return True
                        elif pick_j == j:
                            return True
            return False

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
    whites_turn = True
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
                            # drag i ang j are picked piece numbers in 8x4
                            pick_i = i + offset[i, j, 0] / 100
                            pick_j = (j if j <= 1 else j + 4) + offset[i, j, 1] / 100
                            # pick i and j are picked piece current coords in 8x8
                            click_x = mouse_x
                            click_y = mouse_y
            elif event.type == MOUSEBUTTONUP:
                for i in range(8):
                    for j in range(8):
                        if drag and legal(whites_turn, drag_i, drag_j, pick_i, pick_j, i, j) and (mouse_x > 50 + i * 100) and (mouse_x < 50 + (i + 1) * 100) and (mouse_y > 50 + j * 100) and (mouse_y < 50 + (j + 1) * 100):
                            for k in range(8):
                                for l in range(4):
                                    if k * 100 + offset[k, l, 0] == i * 100 and (l + (4 if l > 1 else 0)) * 100 + offset[k, l, 1] == j * 100:
                                        if k * 100 + offset[k, l, 0] != pick_i * 100 or (l + (4 if l > 1 else 0)) * 100 + offset[k, l, 1] != pick_j * 100: #remove after adding legal check
                                            offset[k, l, 2] = 0
                            drag = False
                            if whites_turn:
                                whites_turn = False
                            else:
                                whites_turn = True
                            offset[drag_i, drag_j, 0] = offset[drag_i, drag_j, 0] + (i - pick_i) * 100
                            offset[drag_i, drag_j, 1] = offset[drag_i, drag_j, 1] + (j - pick_j) * 100
                        elif drag and (mouse_x > 50 + i * 100) and (mouse_x < 50 + (i + 1) * 100) and (mouse_y > 50 + j * 100) and (mouse_y < 50 + (j + 1) * 100):
                            drag = False
        window.fill(background_colour)
        pygame.draw.rect(window, light_square_colour, pygame.Rect(50, 50, 800, 800))
        for i in range(8):
            for j in range(8):
                if ((i + j)%2 == 1):
                    pygame.draw.rect(window, dark_square_colour, pygame.Rect(50 + i * 100, 50 + j * 100, 100, 100))
        
        for i in range(8):
            for j in range(4):
                if offset[i, j, 2] == 1 and (drag_i != i or drag_j != j):
                            piece = (br if (i == 0 or i == 7) else (bn if (i == 1 or i == 6) else (bb if (i == 2 or i == 5) else (bq if i == 3 else bk)))) if (j == 0) else (bp if j == 1 else (wp if j == 2 else (wr if (i == 0 or i == 7) else (wn if (i == 1 or i == 6) else (wb if (i == 2 or i == 5) else (wq if i == 3 else wk))))))
                            window.blit(piece, (50 + i * 100 + offset[i, j, 0] + ((mouse_x - click_x) if (drag and drag_i == i and drag_j == j) else (0)), 50 + (j + (4 if j > 1 else 0)) * 100 + offset[i, j, 1] + ((mouse_y - click_y) if (drag and drag_i == i and drag_j == j) else (0))))
        for i in range(8):
            for j in range(4):
                if offset[i, j, 2] == 1 and drag_i == i and drag_j == j:
                            piece = (br if (i == 0 or i == 7) else (bn if (i == 1 or i == 6) else (bb if (i == 2 or i == 5) else (bq if i == 3 else bk)))) if (j == 0) else (bp if j == 1 else (wp if j == 2 else (wr if (i == 0 or i == 7) else (wn if (i == 1 or i == 6) else (wb if (i == 2 or i == 5) else (wq if i == 3 else wk))))))
                            window.blit(piece, (50 + i * 100 + offset[i, j, 0] + ((mouse_x - click_x) if (drag and drag_i == i and drag_j == j) else (0)), 50 + (j + (4 if j > 1 else 0)) * 100 + offset[i, j, 1] + ((mouse_y - click_y) if (drag and drag_i == i and drag_j == j) else (0))))
        pygame.display.update()
    
    pygame.quit()

if __name__ == '__main__':
    main()

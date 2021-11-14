import pygame
import os
import numpy as np
import random
from pygame.constants import BUTTON_RIGHT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from qiskit import QuantumRegister, ClassicalRegister,QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
IBMQ.save_account('6b5dce45561a72edd27ccd67f0a724eb1466ef5b1af9b927afe5dd2314d236f79db0b775ac8fabeadb56b669594e79cdf73c728e3b007c525761c85879401a3a', overwrite=True)
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')

pygame.font.init()
qchess_font = pygame.font.SysFont('timesnewroman', 60)

arr = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

width, height = 1200, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Chess v1.0")

background_colour = (0, 51, 102)
light_square_colour = (201,223,254)
dark_square_colour = (107,151,185)
font_colour = (255, 255, 255)
fps = 60

background = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.jpg')), (1200, 900))

wk = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wk.png')), (100, 100))
wq = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wq.png')), (100, 100))
wr = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wr.png')), (100, 100))
wb = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wb.png')), (100, 100))
wn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wn.png')), (100, 100))
wp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wp.png')), (100, 100))

wqr = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wqr.png')), (100, 100))
wqb = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wqb.png')), (100, 100))
wqn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wqn.png')), (100, 100))
wqp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wqp.png')), (100, 100))
wrb = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wrb.png')), (100, 100))
wrn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wrn.png')), (100, 100))
wrp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wrp.png')), (100, 100))
wbn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wbn.png')), (100, 100))
wbp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wbp.png')), (100, 100))
wnp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wnp.png')), (100, 100))

bk = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bk.png')), (100, 100))
bq = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bq.png')), (100, 100))
br = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'br.png')), (100, 100))
bb = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bb.png')), (100, 100))
bn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bn.png')), (100, 100))
bp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bp.png')), (100, 100))

bqr = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bqr.png')), (100, 100))
bqb = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bqb.png')), (100, 100))
bqn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bqn.png')), (100, 100))
bqp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bqp.png')), (100, 100))
brb = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'brb.png')), (100, 100))
brn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'brn.png')), (100, 100))
brp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'brp.png')), (100, 100))
bbn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bbn.png')), (100, 100))
bbp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bbp.png')), (100, 100))
bnp = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bnp.png')), (100, 100))

rep = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'replay.png')), (100, 100))

offset = np.empty(shape = (8, 4, 9)) 
# ij0 = x, ij1 = y, 
# ij2 = 0/1 where 0 is captured, 
# ij3 = 0/1/2/3/4 -> not promoted, R/ N/ B/ Q
# ij4 = 0/1 -> cant castle, castle short 
# ij5 = 0/1 -> cant castle, castle long, 
# ij6 = 0, 1, 2, 3, 4, 5, 6 -> option 1 R/ N/ B/ Q/ P/ K
# ij7 = 0, 1, 2, 3, 4, 5, 6 -> option 2 R/ N/ B/ Q/ P/ K 
# ij8 = 0, 1 -> current state choice 1/ 2

def qrandom(n1):
    q = QuantumRegister(n1,'q')
    c = ClassicalRegister(n1,'c')
    circuit = QuantumCircuit(q,c) 
    circuit.h(q) # Applies hadamard gate to all qubits
    circuit.measure(q,c) # Measures all qubits 
    backend = provider.get_backend('ibmq_qasm_simulator')
    job = execute(circuit, backend, shots=1)                 
    counts = job.result().get_counts()
    return counts
def choosepair(numarray,n,result):
    #numarray is a 2D list of n pairs
    a = qrandom(n)
    akey = ''
    i = 0
    for key in a.keys():
        akey = key
    for i in range(n):
        if akey[i] == '0':
            result[i] = numarray[i][0]
        else:
            result[i] = numarray[i][1]
    return result
def q_choice(num5):
    a = qrandom(3)
    if '000' in a.keys():
        return num5[0]
    elif '001' in a.keys():
        return num5[1]
    elif '010' in a.keys():
        return num5[2]
    elif '011' in a.keys():
        return num5[3]
    elif '100' in a.keys():
        return num5[4]
    else:
        q_choice(num5)
def q_choice_minus_pawn(a, i, j, num5):
    if j > 1:
        j =  3 - j
    a = a[i + 8 * j:i + 8 * j + 2]
    if a == '00':
        return num5[0]
    elif a == '01':
        return num5[1]
    elif a == '10':
        return num5[2]
    else:
        return num5[3]
def piece_still(drag_i, drag_j):
    if drag_j > 1:
        if offset[drag_i, drag_j, 6] == 0:
            if offset[drag_i, drag_j, 7] == 0:
                return wr
            elif offset[drag_i, drag_j, 7] == 1:
                if offset[drag_i, drag_j, 8] == 1:
                    return wrn
                else:
                    return wrn
            elif offset[drag_i, drag_j, 7] == 2:
                return wrb
            elif offset[drag_i, drag_j, 7] == 3:
                return wqr
            elif offset[drag_i, drag_j, 7] == 4:
                return wrp
        elif offset[drag_i, drag_j, 6] == 1:
            if offset[drag_i, drag_j, 7] == 0:
                return wrn
            elif offset[drag_i, drag_j, 7] == 1:
                return wn
            elif offset[drag_i, drag_j, 7] == 2:
                return wbn
            elif offset[drag_i, drag_j, 7] == 3:
                return wqn
            elif offset[drag_i, drag_j, 7] == 4:
                return wnp
        elif offset[drag_i, drag_j, 6] == 2:
            if offset[drag_i, drag_j, 7] == 0:
                return wrb
            elif offset[drag_i, drag_j, 7] == 1:
                return wbn
            elif offset[drag_i, drag_j, 7] == 2:
                return wb
            elif offset[drag_i, drag_j, 7] == 3:
                return wqb
            elif offset[drag_i, drag_j, 7] == 4:
                return wbp
        elif offset[drag_i, drag_j, 6] == 3:
            if offset[drag_i, drag_j, 7] == 0:
                return wqr
            elif offset[drag_i, drag_j, 7] == 1:
                return wqn
            elif offset[drag_i, drag_j, 7] == 2:
                return wqb
            elif offset[drag_i, drag_j, 7] == 3:
                return wq
            elif offset[drag_i, drag_j, 7] == 4:
                return wqp
        elif offset[drag_i, drag_j, 6] == 4:
            if offset[drag_i, drag_j, 7] == 0:
                return wrp
            elif offset[drag_i, drag_j, 7] == 1:
                return wnp
            elif offset[drag_i, drag_j, 7] == 2:
                return wbp
            elif offset[drag_i, drag_j, 7] == 3:
                return wqp
            elif offset[drag_i, drag_j, 7] == 4:
                return wp
        else:
            return wk            
    else:
        if offset[drag_i, drag_j, 6] == 0:
            if offset[drag_i, drag_j, 7] == 0:
                return br
            elif offset[drag_i, drag_j, 7] == 1:
                return brn
            elif offset[drag_i, drag_j, 7] == 2:
                return brb
            elif offset[drag_i, drag_j, 7] == 3:
                return bqr
            elif offset[drag_i, drag_j, 7] == 4:
                return brp
        elif offset[drag_i, drag_j, 6] == 1:
            if offset[drag_i, drag_j, 7] == 0:
                return brn
            elif offset[drag_i, drag_j, 7] == 1:
                return bn
            elif offset[drag_i, drag_j, 7] == 2:
                return bbn
            elif offset[drag_i, drag_j, 7] == 3:
                return bqn
            elif offset[drag_i, drag_j, 7] == 4:
                return bnp
        elif offset[drag_i, drag_j, 6] == 2:
            if offset[drag_i, drag_j, 7] == 0:
                return brb
            elif offset[drag_i, drag_j, 7] == 1:
                return bbn
            elif offset[drag_i, drag_j, 7] == 2:
                return bb
            elif offset[drag_i, drag_j, 7] == 3:
                return bqb
            elif offset[drag_i, drag_j, 7] == 4:
                return bbp
        elif offset[drag_i, drag_j, 6] == 3:
            if offset[drag_i, drag_j, 7] == 0:
                return bqr
            elif offset[drag_i, drag_j, 7] == 1:
                return bqn
            elif offset[drag_i, drag_j, 7] == 2:
                return bqb
            elif offset[drag_i, drag_j, 7] == 3:
                return bq
            elif offset[drag_i, drag_j, 7] == 4:
                return bqp
        elif offset[drag_i, drag_j, 6] == 4:
            if offset[drag_i, drag_j, 7] == 0:
                return brp
            elif offset[drag_i, drag_j, 7] == 1:
                return bnp
            elif offset[drag_i, drag_j, 7] == 2:
                return bbp
            elif offset[drag_i, drag_j, 7] == 3:
                return bqp
            elif offset[drag_i, drag_j, 7] == 4:
                return bp
        else:
            return bk            
def piece_dragging(drag_i, drag_j):
    if drag_j > 1:
        return (wr if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 0 else (wn if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 1 else (wb if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 2 else (wq if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 3 else (wp if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 4 else (wk))))))
    else:
        return (br if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 0 else (bn if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 1 else (bb if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 2 else (bq if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 3 else (bp if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 4 else (bk))))))
def check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
    if drag_j >= 2: # white pieces
        if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 0: # rooks
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                                return False
                    #if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                    #    return False
        elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 1: # knights
            for a in range(8):
                for b in range(4):
                    if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                        return (False if b > 1 else True)
        elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 2: # bishops
            #print(i, j, pick_i, pick_j)
            if pick_i > i and pick_j > j: # NW
                for a in range(8):
                    for b in range(4):
                        #for k in (pick_j + 1, j): #no piece in between
                        k = pick_i - 1
                        l = pick_j - 1
                        while l > j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k -= 1
                            l -= 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                            return False
            elif pick_i > i and pick_j < j: # SW
                for a in range(8):
                    for b in range(4):
                        #for k in (j + 1, pick_j): #no piece in between
                        k = pick_i - 1
                        l = pick_j + 1
                        while l < j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k -= 1
                            l += 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                            return False
            elif pick_i < i and pick_j > j: # NE
                for a in range(8):
                    for b in range(4):
                        #for k in (pick_i + 1, i): #no piece in between
                        k = pick_i + 1
                        l = pick_j - 1
                        while l > j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k += 1
                            l -= 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                            return False
            else: # SE
                for a in range(8):
                    for b in range(4):
                        #for k in (i + 1, pick_i): #no piece in between
                        k = pick_i + 1
                        l = pick_j + 1
                        while l < j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k += 1
                            l += 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                            return False
        elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 3: #queen
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                                return False
            elif pick_i > i and pick_j > j: # NW
                for a in range(8):
                    for b in range(4):
                        #for k in (pick_j + 1, j): #no piece in between
                        k = pick_i - 1
                        l = pick_j - 1
                        while l > j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k -= 1
                            l -= 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                            return False
            elif pick_i > i and pick_j < j: # SW
                for a in range(8):
                    for b in range(4):
                        #for k in (j + 1, pick_j): #no piece in between
                        k = pick_i - 1
                        l = pick_j + 1
                        while l < j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k -= 1
                            l += 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                            return False
            elif pick_i < i and pick_j > j: # NE
                for a in range(8):
                    for b in range(4):
                        #for k in (pick_i + 1, i): #no piece in between
                        k = pick_i + 1
                        l = pick_j - 1
                        while l > j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k += 1
                            l -= 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                            return False
            else: # SE
                for a in range(8):
                    for b in range(4):
                        #for k in (i + 1, pick_i): #no piece in between
                        k = pick_i + 1
                        l = pick_j + 1
                        while l < j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k += 1
                            l += 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1: #if white piece at end
                            return False
        elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 4: # pawn
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
        else: #king
            for a in range(8):
                for b in range(4):
                    if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b > 1 and offset[a, b, 2] == 1:
                        return False
    elif drag_j <= 1: # black pieces
        if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 0: # rooks
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                                return False
                    #if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                    #    return False
        elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 1: # knights
            for a in range(8):
                for b in range(4):
                    if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                        return (False if b <= 1 else True)
        elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 2: # bishops
            if pick_i > i and pick_j > j: # NW
                for a in range(8):
                    for b in range(4):
                        #for k in (pick_j + 1, j): #no piece in between
                        k = pick_i - 1
                        l = pick_j - 1
                        while l > j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k -= 1
                            l -= 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                            return False
            elif pick_i > i and pick_j < j: # SW
                for a in range(8):
                    for b in range(4):
                        #for k in (j + 1, pick_j): #no piece in between
                        k = pick_i - 1
                        l = pick_j + 1
                        while l < j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k -= 1
                            l += 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                            return False
            elif pick_i < i and pick_j > j: # NE
                for a in range(8):
                    for b in range(4):
                        #for k in (pick_i + 1, i): #no piece in between
                        k = pick_i + 1
                        l = pick_j - 1
                        while l > j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k += 1
                            l -= 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                            return False
            else: # SE
                for a in range(8):
                    for b in range(4):
                        #for k in (i + 1, pick_i): #no piece in between
                        k = pick_i + 1
                        l = pick_j + 1
                        while l < j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k += 1
                            l += 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                            return False
        elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 3: #queen
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
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
                            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                                return False
            elif pick_i > i and pick_j > j: # NW
                for a in range(8):
                    for b in range(4):
                        #for k in (pick_j + 1, j): #no piece in between
                        k = pick_i - 1
                        l = pick_j - 1
                        while l > j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k -= 1
                            l -= 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                            return False
            elif pick_i > i and pick_j < j: # SW
                for a in range(8):
                    for b in range(4):
                        #for k in (j + 1, pick_j): #no piece in between
                        k = pick_i - 1
                        l = pick_j + 1
                        while l < j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k -= 1
                            l += 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                            return False
            elif pick_i < i and pick_j > j: # NE
                for a in range(8):
                    for b in range(4):
                        #for k in (pick_i + 1, i): #no piece in between
                        k = pick_i + 1
                        l = pick_j - 1
                        while l > j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k += 1
                            l -= 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                            return False
            else: # SE
                for a in range(8):
                    for b in range(4):
                        #for k in (i + 1, pick_i): #no piece in between
                        k = pick_i + 1
                        l = pick_j + 1
                        while l < j:
                            if a + offset[a, b, 0] / 100 == k and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == l and offset[a, b, 2] == 1: #if piece
                                return False
                            k += 1
                            l += 1
                        if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1: #if black piece at end
                            return False
        elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 4: #pawn
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
        else: #king
            for a in range(8):
                for b in range(4):
                    if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and b <= 1 and offset[a, b, 2] == 1:
                        return False
    return True
def can_castle(drag_i, drag_j, pick_i, pick_j, i, j):
    a = 0
    while a < 8:
        b = 0
        while b < 4:
            if a + offset[a, b, 0] / 100 == i and b + (4 if b > 1 else 0) + offset[a, b, 1] / 100 == j and offset[a, b, 2] == 1: #if piece
                return False
            b += 1
        a += 1
    return True
def legal(whites_turn, drag_i, drag_j, pick_i, pick_j, i, j):
        # pick ij -> ij
        if pick_i == i and pick_j == j:
            return False
        if whites_turn:
            if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 4:
                if (pick_j == j + 1) and (pick_i == i or pick_i == i + 1 or pick_i == i - 1) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                    return True
                elif (pick_j == 6) and (j == 4) and (pick_i == i) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j+1) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                    return True
            elif drag_j > 1:
                if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 0:
                    if (pick_i == i or pick_j == j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 1:
                    if ((abs(pick_i - i) == 2 and abs(pick_j - j) == 1) or (abs(pick_i - i) == 1 and abs(pick_j - j) == 2)) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 2:
                    #print(i, j, check_empty(drag_i, drag_j, pick_i, pick_j, i, j))
                    if abs(pick_i - i) == abs(pick_j - j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 3:
                    if (abs(pick_i - i) == abs(pick_j - j) or pick_i == i or pick_j == j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 5:
                    if (abs(pick_i - i) <= 1 and abs(pick_j - j) <= 1) and (abs(pick_i - i) == abs(pick_j - j) or pick_i == i or pick_j == j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                    elif offset[drag_i, drag_j, 4] == 1 and (pick_j == j) and i == 6 and can_castle(drag_i, drag_j, pick_i, pick_j, i, j) and can_castle(drag_i, drag_j, pick_i, pick_j, i-1, j):
                        return True
                    elif offset[drag_i, drag_j, 4] == 1 and (pick_j == j) and i == 2 and can_castle(drag_i, drag_j, pick_i, pick_j, i, j) and can_castle(drag_i, drag_j, pick_i, pick_j, i-1, j) and can_castle(drag_i, drag_j, pick_i, pick_j, i+1, j):
                        return True
            return False
        else:
            if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 4:
                if (pick_j == j - 1) and (pick_i == i or pick_i == i + 1 or pick_i == i - 1) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                    return True
                elif (pick_j == 1) and (j == 3) and (pick_i == i) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j-1) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                    return True
            elif drag_j <= 1:
                if offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 0:
                    if (pick_i == i or pick_j == j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 1:
                    if ((abs(pick_i - i) == 2 and abs(pick_j - j) == 1) or (abs(pick_i - i) == 1 and abs(pick_j - j) == 2)) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 2:
                    if abs(pick_i - i) == abs(pick_j - j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 3:
                    if (abs(pick_i - i) == abs(pick_j - j) or pick_i == i or pick_j == j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                elif offset[drag_i, drag_j, int(6 + offset[drag_i, drag_j, 8])] == 5:
                    if (abs(pick_i - i) <= 1 and abs(pick_j - j) <= 1) and (abs(pick_i - i) == abs(pick_j - j) or pick_i == i or pick_j == j) and check_empty(drag_i, drag_j, pick_i, pick_j, i, j):
                        return True
                    elif offset[drag_i, drag_j, 4] == 1 and (pick_j == j) and i == 6 and can_castle(drag_i, drag_j, pick_i, pick_j, i, j) and can_castle(drag_i, drag_j, pick_i, pick_j, i-1, j):
                        return True
                    elif offset[drag_i, drag_j, 4] == 1 and (pick_j == j) and i == 2 and can_castle(drag_i, drag_j, pick_i, pick_j, i, j) and can_castle(drag_i, drag_j, pick_i, pick_j, i-1, j) and can_castle(drag_i, drag_j, pick_i, pick_j, i+1, j):
                        return True
            return False
def main():
    clock = pygame.time.Clock()
    run = True
    drag =  False
    drag_i = -1
    drag_j = -1
    click_x = 0
    click_y = 0
    pick_i = 0
    pick_j = 0
    unmated = True
    replay = False
    list01x32 = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
    a = qrandom(32)
    for i in range(8):
        for j in range(4):
            list01 = [0, 1]
            offset[i, j, 0], offset[i, j, 1], offset[i, j, 2], offset[i, j, 3],  offset[i, j, 4], offset[i, j, 5] = 0, 0, 1, 0, (1 if i == 4 else 0), (1 if i == 4 else 0)
            offset[i, j, 8] = (random.choice(list01)) # classical randomize between 0 and 1
            if j == 1 or j == 2:
                offset[i, j, 6] = 4
            else:
                if i == 0 or i == 7:
                    offset[i, j, 6] = 0
                elif i == 1 or i == 6:
                    offset[i, j, 6] = 1
                elif i == 2 or i == 5:
                    offset[i, j, 6] = 2
                elif i == 3:
                    offset[i, j, 6] = 3
                else:
                    offset[i, j, 6] = 5
            if i == 4 and (j == 0 or j == 3):
               offset[i, j, 7] = 5 # keeping the king classical
            else:
                list01234 = [0, 1, 2, 3, 4]
                #print(str(a)[8 * j + i: 8 * j + i + 2])
                #offset[i, j, 7] = (random.choice(list01234)) # classical randomize pieces associated here 0/ 1/ 2/ 3/ 4
                #offset[i, j, 7] = q_choice(list01234) # quantum randomize pieces associated here 0/ 1/ 2/ 3/ 4
                offset[i, j, 7] = q_choice_minus_pawn(str(a), i, j, list01234) # quantum randomize pieces associated here 0/ 1/ 2/ 3
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
                if (mouse_x > 975 ) and (mouse_x < 1075 ) and (mouse_y > 250 ) and (mouse_y < 350):
                    replay = True
                else:
                    replay = True
            elif event.type == MOUSEBUTTONUP:
                for i in range(8):
                    for j in range(8):
                        if drag and unmated and legal(whites_turn, drag_i, drag_j, pick_i, pick_j, i, j) and (mouse_x > 50 + i * 100) and (mouse_x < 50 + (i + 1) * 100) and (mouse_y > 50 + j * 100) and (mouse_y < 50 + (j + 1) * 100):
                            for k in range(8):
                                for l in range(4):
                                    if k * 100 + offset[k, l, 0] == i * 100 and (l + (4 if l > 1 else 0)) * 100 + offset[k, l, 1] == j * 100:
                                        if k * 100 + offset[k, l, 0] != pick_i * 100 or (l + (4 if l > 1 else 0)) * 100 + offset[k, l, 1] != pick_j * 100: #remove after adding legal check
                                            offset[k, l, 2] = 0
                                            if j == 0 and (k == 0 or k == 7):
                                                offset[4, (0 if drag_j <= 1 else 3), 5] == 0
                                            if j == 7 and (k == 0 or k == 7):
                                                offset[4, (0 if drag_j <= 1 else 3), 4] == 0
                                            if k == 4 and (l == 0 or l == 3):
                                                unmated = False
                                drag = False
                            if whites_turn:
                                whites_turn = False
                            else:
                                whites_turn = True
                            #chosen32 = [0 for m in range(32)]
                            #chosen32 = choosepair(list01x32, 32, chosen32)
                            if whites_turn:
                                for a in range(8):
                                    for b in range(4):
                                        list01 = [0, 1]
                                        offset[a, b, 8] = (random.choice(list01)) # classical randomize between 0 and 1
                                        #offset[a, b, 8] = chosen32[int(4 * a + b)] # quantum randomize between 0 and 1
                            offset[drag_i, drag_j, 0] = offset[drag_i, drag_j, 0] + (i - pick_i) * 100
                            offset[drag_i, drag_j, 1] = offset[drag_i, drag_j, 1] + (j - pick_j) * 100
                            if drag_i == 4 and (drag_j == 0 or drag_j == 3):
                                offset[4, (0 if drag_j <= 1 else 3), 4] == 0
                                offset[4, (0 if drag_j <= 1 else 3), 5] == 0
                            elif drag_i == 0 and (drag_j == 0 or drag_j == 3):
                                offset[4, (0 if drag_j <= 1 else 3), 5] == 0
                            elif drag_i == 7 and (drag_j == 0 or drag_j == 3):
                                offset[4, (0 if drag_j <= 1 else 3), 4] == 0
                            if pick_j == j and drag_i == 4 and abs(pick_i - i) == 2: # move the rook while castling
                                offset[4, (0 if drag_j <= 1 else 3), 4] == 0
                                offset[4, (0 if drag_j <= 1 else 3), 5] == 0
                                if pick_i > i:
                                    offset[0, drag_j, 0] = offset[0, drag_j, 0] + 300
                                else:
                                    offset[7, drag_j, 0] = offset[7, drag_j, 0] - 200
                        elif drag and (mouse_x > 50 + i * 100) and (mouse_x < 50 + (i + 1) * 100) and (mouse_y > 50 + j * 100) and (mouse_y < 50 + (j + 1) * 100):
                            drag = False
                if (mouse_x > 975 ) and (mouse_x < 1075 ) and (mouse_y > 250 ) and (mouse_y < 350) and replay:
                    main()
                else:
                    replay == False
        #window.fill(background_colour)
        window.blit(background, (0, 0))
        l = pygame.Surface((800,800))
        l.set_alpha(229)
        l.fill(light_square_colour)
        window.blit(l, (50,50))
        #pygame.draw.rect(window, light_square_colour, pygame.Rect(50, 50, 800, 800))
        for i in range(8):
            for j in range(8):
                if ((i + j)%2 == 1):
                    d = pygame.Surface((100,100))
                    d.set_alpha(229)
                    d.fill(dark_square_colour)
                    window.blit(d, (50 + i * 100, 50 + j * 100))
                    #pygame.draw.rect(window, dark_square_colour, pygame.Rect(50 + i * 100, 50 + j * 100, 100, 100))
        
        for i in range(8):
            for j in range(4):
                if offset[i, j, 2] == 1 and (drag_i != i or drag_j != j):
                    #piece = (br if (i == 0 or i == 7) else (bn if (i == 1 or i == 6) else (bb if (i == 2 or i == 5) else (bq if i == 3 else bk)))) if (j == 0) else (bp if j == 1 else (wp if j == 2 else (wr if (i == 0 or i == 7) else (wn if (i == 1 or i == 6) else (wb if (i == 2 or i == 5) else (wq if i == 3 else wk))))))
                    window.blit(piece_still(i, j), (50 + i * 100 + offset[i, j, 0] + ((mouse_x - click_x) if (drag and drag_i == i and drag_j == j) else (0)), 50 + (j + (4 if j > 1 else 0)) * 100 + offset[i, j, 1] + ((mouse_y - click_y) if (drag and drag_i == i and drag_j == j) else (0))))
        for i in range(8):
            for j in range(4):
                if offset[i, j, 2] == 1 and drag_i == i and drag_j == j:
                    #piece = (br if (i == 0 or i == 7) else (bn if (i == 1 or i == 6) else (bb if (i == 2 or i == 5) else (bq if i == 3 else bk)))) if (j == 0) else (bp if j == 1 else (wp if j == 2 else (wr if (i == 0 or i == 7) else (wn if (i == 1 or i == 6) else (wb if (i == 2 or i == 5) else (wq if i == 3 else wk))))))
                    window.blit(piece_dragging(drag_i, drag_j), (50 + i * 100 + offset[i, j, 0] + ((mouse_x - click_x) if (drag and drag_i == i and drag_j == j) else (0)), 50 + (j + (4 if j > 1 else 0)) * 100 + offset[i, j, 1] + ((mouse_y - click_y) if (drag and drag_i == i and drag_j == j) else (0))))
        quantum = qchess_font.render("QUANTUM", 1, font_colour)
        chess = qchess_font.render("CHESS", 1, font_colour)
        window.blit(quantum, (1025 - (quantum.get_width() / 2), 70))
        window.blit(chess, (1025 - (chess.get_width() / 2), 80 + quantum.get_height()))
        window.blit(rep, (975, 250))
        pygame.display.update()
    
    pygame.quit()
IBMQ.disable_account()

if __name__ == '__main__':
    main()

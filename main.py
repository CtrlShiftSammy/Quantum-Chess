import pygame

width, height = 1600, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Chess v0.0")

background_colour = (255, 204, 229)
light_square_colour = (255, 153, 204)
dark_square_colour = (102, 0, 51)

fps = 60

def draw():
    window.fill(background_colour)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    pygame.quit()

if __name__ == '__main__':
    main()
    
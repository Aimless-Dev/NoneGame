import pygame, sys
from button import Button
from level import Level

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NoneGame")

BG = pygame.image.load("assets/Background.png")

score = 0

melody     = pygame.mixer.Sound("assets/molody.mp3")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


while True:
    SCREEN.blit(BG, (0, 0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(60).render("NoneGame", True, "#1B2631")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

    PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), 
                        text_input="PLAY", font=get_font(40), base_color="white", hovering_color="#1B2631")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 400), 
                        text_input="QUIT", font=get_font(40), base_color="white", hovering_color="#1B2631")

    SCREEN.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                melody.play(-1)
                level = True
                while level:
                    level, score = Level('MapaUno', score).run()
                    if level:
                        level, score = Level('MapaDos', score).run()
                        if not level:
                            melody.stop()
                            break
                    if level:
                        level, score = Level('MapaTres', score).run()
                        if not level:
                            melody.stop()
                            break
                    if not level:
                        melody.stop()
                        break
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()

    pygame.display.update()
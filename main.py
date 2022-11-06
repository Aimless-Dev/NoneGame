import pygame, sys
from button import Button
from level_one import LevelOne

pygame.init()

SCREEN = pygame.display.set_mode((960, 640))
pygame.display.set_caption("NoneGame")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("NoneGame", True, "#1B2631")
        MENU_RECT = MENU_TEXT.get_rect(center=(480, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(480, 250), 
                            text_input="PLAY", font=get_font(75), base_color="white", hovering_color="#1B2631")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(480, 400), 
                            text_input="QUIT", font=get_font(75), base_color="white", hovering_color="#1B2631")

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
                    LevelOne().run()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
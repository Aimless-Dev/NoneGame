import pygame, sys
from player import Player
class Level:

    def __init__ (self, mapa, score):
        pygame.init()
        pygame.display.set_caption('NoneGame')
        self.screen             = pygame.display.set_mode((800, 600))
        self.clock              = pygame.time.Clock()
        self.sprites            = pygame.sprite.Group()
        self.player_run_r       = Player('Run_right', 12, 384, 32, 1)
        self.sprites.add(self.player_run_r)
        self.player_jump_r     = Player('Jump_r', 1, 32, 32, 1)
        self.sprites.add(self.player_jump_r)

        self.player_hit      = Player('Hit', 7, 224, 32, 1)
        self.sprites.add(self.player_hit)

        self.enemy  = Player('Enemy_Run', 12, 384, 32, 0)
        self.sprites.add(self.enemy)
        self.enemys = pygame.sprite.Group()
        self.enemys.add(self.enemy)

        self.enemyDos  = Player('Enemy_Run', 12, 384, 32, 0)
        self.sprites.add(self.enemyDos)
        self.enemys.add(self.enemyDos)

        self.jump   = False
        self.salto  = 6
        self.speed  = 0
        self.score  = score
        self.final_score  = 0
        self.scores = [300, 600, 900, 1200, 1500, 1700, 2100, 2400, 2700, 3000]

        self.junpfx     = pygame.mixer.Sound("assets/salto.wav")
        self.damage     = pygame.mixer.Sound("assets/damage.mp3")

        self.background = pygame.image.load(f'sprites/backgrounds/{mapa}.png').convert()
        self.game_over = False

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def update(self):
        MENU_TEXT = self.get_font(10).render(f"Score: {self.score}", True, "#1B2631")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 20))
        self.screen.blit(MENU_TEXT, MENU_RECT)

    def gameOver(self):
        self.screen.fill('white')
        gameover = self.get_font(50).render(f"GAME OVER", True, "#1B2631")
        gameover_rect = gameover.get_rect(center=(400, 100))
        score =  self.get_font(45).render(f'Score: {self.final_score}', True, "#1B2631")
        score_rect = score.get_rect(center=(400, 200))

        back =  self.get_font(15).render(f'Pulsa [Esc] para salir al menu principal', True, "#1B2631")
        back_rect = back.get_rect(center=(400, 300))

        self.screen.blit(gameover, gameover_rect)
        self.screen.blit(score, score_rect)
        self.screen.blit(back, back_rect)
        

    def run(self):
        enemyX = 800
        enemyY = 545
        enemyDosX = 900
        x = 60
        y = 545
        __x = 60
        while True:
            x_falsa = __x % self.background.get_rect().width
            self.screen.blit(self.background, [x_falsa - self.background.get_rect().width, 0])
            if x_falsa < 800:
                self.screen.blit(self.background, [x_falsa, 0])
            __x -= 10
            enemyX -= 10
            enemyDosX -= 20

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.jump = True
                        self.junpfx.play(0)
                    if event.key == pygame.K_ESCAPE:
                        return False, self.score
                    
            if self.jump:
                if self.salto >= -6:
                    y -= (self.salto * abs(self.salto)) * 0.5
                    self.salto -= 1
                else:
                    self.salto = 6
                    self.jump = False

            self.player_run_r.update(self.screen, x, y)

            self.enemy.update(self.screen, enemyX, enemyY)
            self.enemyDos.update(self.screen, enemyDosX, enemyY)

            if self.score == 1200:
                return False, self.score

            if not self.game_over:
                if self.player_run_r.area.colliderect(self.enemy.area) or self.player_run_r.area.colliderect(self.enemyDos.area):
                    self.game_over = True
                    self.final_score = self.score
                    self.player_hit.update(self.screen, x, y)
                    self.damage.play(0)
                else:
                    self.game_over = False

            if enemyX < 0:
                enemyX = 800

            if enemyDosX < 0:
                enemyDosX = 900

            if not self.game_over:
                self.score += 1

            for i in self.scores:
                if self.score == i:
                    return True, self.score

            if self.game_over:
                self.gameOver()
            else:
                self.update()

            self.clock.tick(15)
            pygame.display.update()
            pygame.display.flip()

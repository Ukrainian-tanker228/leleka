import pygame
from random import randint
import pygame.freetype

pygame.init()
pygame.mixer.music.load("muzuka.wav")
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("leleka")
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 40)
bg = pygame.image.load("bg.png")
leleka = pygame.image.load("lek.png")
leleka = pygame.transform.scale(leleka, (300, 200))
cactus = pygame.image.load("gh.png")
cactus = pygame.transform.scale(cactus, (60, 130))
bg = pygame.transform.scale(bg, (800, 142))



bg_group = pygame.sprite.Group()
gh_group = pygame.sprite.Group()
bg_event = pygame.USEREVENT
gh_event = pygame.USEREVENT +1
pygame.time.set_timer(bg_event, 2000)
pygame.time.set_timer(gh_event, randint(1000, 6000))
class Bg(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        self.rect.x -= 3
        if self.rect.right<0:
            self.kill()
            
class Gh(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        self.rect.x -= 3
        if self.rect.right<0:
            self.kill()
            lek.score +=1
        if self.rect.colliderect(lek.rect):
            lek.game_status = "Menu"
class Lek():
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.y = 0
        self.step = 8
        self.max_jump = 25
        self.in_jump = False
        self.score = 0
        self.game_status = "Game"
    def jump(self):
        if self.in_jump:
            if self.y < self.max_jump:
                self.y +=1
                self.rect.y -=self.step
            elif self.y < self.max_jump * 2:
                self.y +=1
                self.rect.y +=self.step
            else:
                self.in_jump = False
                self.y = False
    def draw(self):
        screen.blit(self.image, self.rect)

lek = Lek(leleka, (100, 400))
g = Bg(bg, (400, 500))
bg_group.add(g)
g = Bg(bg, (800, 500))
bg_group.add(g)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            lek.in_jump = True
        if event.type == bg_event:
            g = Bg(bg, (700, 500))
            bg_group.add(g)
        if event.type == gh_event:
            pygame.time.set_timer(gh_event, randint(1000, 6000))
            c = Gh(cactus, (910, 450))
            gh_group.add(c)
    screen.fill((0, 127 ,255))
    if lek.game_status == "Game":
        bg_group.update()
        bg_group.draw(screen)
        gh_group.update()
        gh_group.draw(screen)
        font.render_to(screen, (850, 50), str(lek.score), (0, 0, 0))
        lek.jump()
        lek.draw()
    else:
        font.render_to(screen, (330, 200), "Гра завершена!", (0,0,0))
    pygame.display.flip()
    clock.tick(60)
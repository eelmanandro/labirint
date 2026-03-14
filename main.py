import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, width, height, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self, win: pygame.Surface):
        win.blit(self.image, (self.rect.x, self.rect.y))

        

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("assets/jungles.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

win_size = (700, 500)
win = pygame.display.set_mode(win_size)
pygame.display.set_caption("Maze")

clock = pygame.time.Clock()
fps = 60

background = pygame.transform.scale(pygame.image.load("assets/background.jpg"), win_size)

player = GameSprite("assets/hero.png", 5, win_size[1]-80, 65, 65, 5)
enemy = GameSprite("assets/cyborg.png", win_size[0]-80, 280, 65, 65, 2)
finish = GameSprite("assets/treasure.png", win_size[0]-120, win_size[1]-80, 65, 65, 0)

run = True
while run:
    win.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.reset(win)
    enemy.reset(win)
    finish.reset(win)
    pygame.display.update()
    clock.tick(fps)

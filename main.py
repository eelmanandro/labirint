import pygame
from typing import Tuple

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
    


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < win_size[0] - self.rect.width:
            self.rect.x += self.speed
        if keys [pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [pygame.K_DOWN] and self.rect.y < win_size[1] - self.rect.width:
            self.rect.y += self.speed


class Enemy(GameSprite):
    def __init__(self, filename, x, y, width, height, speed):
        super().__init__(filename, x, y, width, height, speed)
        self.direction = "LEFT"
    

    def update(self):
        if self.rect.x <= win_size[0] - 250: 
            self.direction = "RIGHT"
        if self.rect.x >= win_size[0] - self.rect.width:
            self.direction = "LEFT"
        if self.direction == "LEFT":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    

class Wall(pygame.sprite.Sprite):
    def __init__(self, x:float, y:float, width:float, height:float, color:Tuple[int,int,int]):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


        

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("assets/jungles.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

kick = pygame.mixer.Sound("assets/kick.ogg")
groshi = pygame.mixer.Sound("assets/money.ogg")

win_size = (700, 500)
win = pygame.display.set_mode(win_size)
pygame.display.set_caption("Maze")

clock = pygame.time.Clock()
fps = 60
wall_color = (255,0,0)

background = pygame.transform.scale(pygame.image.load("assets/background.jpg"), win_size)

player = Player("assets/hero.png", 5, win_size[1]-80, 65, 65, 5)
enemy = Enemy("assets/cyborg.png", win_size[0]-80, 280, 65, 65, 2)
finish = GameSprite("assets/treasure.png", win_size[0]-120, win_size[1]-80, 65, 65, 0)
w1 = Wall(150, 0, 10, 400, wall_color)
w2 = Wall(150, 150, 150, 10, wall_color)
w3 = Wall(300, 150, 10, 100, wall_color)
w4 = Wall(300, 250, 50, 10, wall_color)
w5 = Wall(350, 150, 10, 110, wall_color)
w6 = Wall(350, 150, 100, 10, wall_color)
w7 = Wall(225, 225, 10, 300, wall_color)
w8 = Wall(225, 330, 210, 10, wall_color)
w9 = Wall(425, 225, 10, 110, wall_color)

font = pygame.font.SysFont("Arial", 30, bold=True)
font_big = pygame.font.Font(None, 70)

walls = [w1,w2,w3,w4,w5, w6, w7, w8, w9]
run = True
end = False
restart = False
attempts = 1
win_label = font_big.render("YOU WIN:3", True, (0,255,200))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not end:
        win.blit(background, (0, 0))
        player.update()
        player.reset(win)
        enemy.update()
        enemy.reset(win)
        for wall in walls:
            wall.reset()
        finish.reset(win)
        
        attempts_label = font.render(f"attempt: {attempts}", True, (255,255,255))
        attempts_rect = attempts_label.get_rect()
        attempts_rect.x, attempts_rect.y = (win_size[0] - 225, 20)
        pygame.draw.rect(win, (0,0,0), attempts_rect)
        win.blit(attempts_label, (win_size[0] - 225, 20))

        for wall in walls:
            if pygame.sprite.collide_rect(player, wall):
                end = True
                restart = True
                kick.play()
                attempts += 1
        if pygame.sprite.collide_rect(player, enemy):
            end = True
            restart = True
            kick.play()
            attempts += 1

        if pygame.sprite.collide_rect(player, finish):
            end = True
            groshi.play()
            win.blit(win_label, (200,200))
            

    if restart:
        player.rect.x, player.rect.y = 5, win_size[1]-80
        enemy.rect.x, enemy.rect.y = win_size[0]-80, 280
        restart = False
        end = False
    
    
    pygame.display.update()
    clock.tick(fps)
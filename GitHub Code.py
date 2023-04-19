
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()    
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()    
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
sp_Player = Player('Kapibaara.jpg', 0, 420, 65, 65, 10)
sp_Player2 = Player2('Kapibaara.jpg', 635, 420, 65, 65, 10)
display.set_caption("Kapibara")
background = transform.scale(image.load('Kapibaara.jpg'), (700, 500))

game = True
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    sp_Player.update()
    sp_Player.reset()
    sp_Player2.update()
    sp_Player2.reset()
    display.update()
    clock.tick(60)

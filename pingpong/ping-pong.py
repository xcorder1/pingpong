from pygame import * 
window = display.set_mode((700,500))
display.set_caption("Ping-pong")
background = transform.scale(image.load("cityskyline.png"),(700,500))
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self,image1,speed,x,y,width,height):
        super().__init__()
        self.image = transform.scale(image.load(image1), (width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))




class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed        

speed_x = 3
speed_y = 3
win_height = 500

platform = Player('platform.png',5,10,100,15,75)
platform2 = Player('platform.png',5,670,10,15,75)

ball = GameSprite('newball.png',0,200,150,50,50)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True,(180,0,0))
font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSE!', True,(180,0,0))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        platform.update_l()
        platform.reset()
        platform2.update_r()
        platform2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(platform,ball) or sprite.collide_rect(platform2,ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))   
    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200,200))         
    clock.tick(FPS)
    display.update()

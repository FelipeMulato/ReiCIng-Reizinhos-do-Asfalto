import pygame

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("ReiCIng")
running = True

clock = pygame.time.Clock()
road = pygame.image.load("background-1.png")
car_surf = pygame.image.load("CarRed.png")
car_rec  = car_surf.get_rect(midbottom=(235,300))
x_car = 200
y_car = 200
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_rec.x -= 5
    if keys[pygame.K_RIGHT]:
        car_rec.x += 5


    if car_rec.x>800: car_rec.x=0
    if car_rec.y<-200: car_rec.y=400    
    screen.blit(road,(0,0))
    screen.blit(car_surf,car_rec)
    pygame.display.update()
    clock.tick(60)

pygame.quit()


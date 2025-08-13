import pygame as pg

class Explosao(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.images = []

        for i in range(1, 6):
            img = pg.image.load(f'Imagens/explosao/exp{i}.png').convert_alpha()
            img = pg.transform.scale(img, (100, 100))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.count = 0 

    def update(self):
        explosion_speed = 5
        self.count += 1
        if self.count >= explosion_speed and self.index < len(self.images) - 1:
            self.count = 0
            self.index += 1
            if self.index >= len(self.images) and self.index > len(self.images) - 1:
                self.kill()
            else:
                self.image = self.images[self.index]
                self.rect = self.image.get_rect(center=self.rect.center)
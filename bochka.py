import  pygame

class Bochka():
    def __init__(self,window,x,y,stat):
        self.screen = window
        self.image = pygame.image.load("botl.png")
        self.rect = self.image.get_rect()#get_rect - получение кординат
        # - прямоугольника в который виписано наше изаброжение
        self.rect.centerx = x
        self.rect.centery = y
        self.iscoin = False#изначально у нас везде тараканы
        self.stat = stat
        self.isopen = False

    def art_bochka(self):
        self.screen.blit(self.image,self.rect)#blit - это прорисовка обьекта

    def change_image(self,last_key):
        if self.iscoin == True:
            self.stat.add_wins()
            self.image = pygame.image.load("gold.png")
        else:
            if last_key == True:
               self.stat.add_lose()
            self.image = pygame.image.load("tarakan.png")

    def close_bochka(self):
        self.image = pygame.image.load("botl.png")
        self.isopen = False
        self.iscoin = False

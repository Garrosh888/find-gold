import pygame
class Key():

    def __init__(self,window,x,y,key_number):
        self.screen = window
        self.image = pygame.image.load("key.png")
        self.rect = self.image.get_rect()  # get_rect - получение кординат
        # - прямоугольника в который виписано наше изаброжение
        self.rect.centerx = x
        self.rect.centery = y
        self.key_number = key_number
        self.show = True# ключик отресововыеться
    def art_key(self):
        if self.show == True:
            self.screen.blit(self.image, self.rect)  # blit - это прорисовка обьекта



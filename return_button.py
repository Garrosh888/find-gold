import pygame
class Return():
    def __init__(self,window):
        self.screen = window
        self.image = pygame.image.load("return.png")
        self.rect = self.image.get_rect()  # get_rect - получение кординат
        self.rect.right = 780
        self.rect.top = 20
    def art_return(self):
        self.screen.blit(self.image,self.rect)
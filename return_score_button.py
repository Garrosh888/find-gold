import pygame

class Score_button():
    def __init__(self,window,stat):
        self.screen = window
        self.image = pygame.image.load("return_score.png")
        self.rect = self.image.get_rect()
        self.rect.left = 100
        self.rect.top = -15
        self.stat = stat
    def art_score_button(self):
        self.screen.blit(self.image,self.rect)

    def click_score_button(self):
        self.stat.clean_score()





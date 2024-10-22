import pygame.font

class Statistic():
    def __init__(self,window):
        self.win = 0
        self.lose = 0
        self.load_statistic()
        self.screen = window
        self.font = pygame.font.SysFont(None,35)
        self.prepare_image()
    def load_statistic(self):
        with open("win.txt") as win_file:
            self.win = int(win_file.read())
        with open("lose.txt") as lose_file:
            self.lose = int(lose_file.read())
    def save_stat(self):
        with open("win.txt","w") as win_file:
            win_file.write(str(self.win))
        with open("lose.txt", "w") as lose_file:
            lose_file.write(str(self.lose))

    def prepare_image(self):# обновления графического отображения статистики
        self.image_win = self.font.render(f"wins: {self.win}",True,(0,145,41),(0,0,0))
        self.image_win_rect = self.image_win.get_rect()
        self.image_win_rect.left = 10
        self.image_win_rect.top = 10
        self.image_lose = self.font.render(f"lost: {self.lose}",True, (97, 8, 36), (0, 0, 0))
        self.image_lose_rect = self.image_lose.get_rect()
        self.image_lose_rect.left = 10
        self.image_lose_rect.top = 35

    def art_statistic(self):
        self.screen.blit(self.image_win,self.image_win_rect)
        self.screen.blit(self.image_lose,self.image_lose_rect)

    def add_wins(self):
        self.win += 1
        self.prepare_image()
        self.save_stat()

    def add_lose(self):
        self.lose += 1
        self.prepare_image()
        self.save_stat()
    def clean_score(self):
        self.win = 0
        self.lose = 0
        self.prepare_image()
        self.save_stat()






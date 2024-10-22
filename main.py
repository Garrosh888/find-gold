import sys
import pygame
from bochka import Bochka
from random import randint
from key import Key
from return_button import Return
from statistic import Statistic
from return_score_button import Score_button

def return_work():
    global isgoldfine
    if isgoldfine == False and key2.show == False and key1.show == True:
        stat.add_lose()
    isgoldfine = False
    bochka1.close_bochka()
    bochka2.close_bochka()
    bochka3.close_bochka()
    choose_gold()
    key1.show = True
    key2.show = True



def try_open_bochka(bochka):
    global isgoldfine
    if isgoldfine == True:
        return
    if bochka.iscoin == True:
        isgoldfine = True

    if key2.show == True:
        bochka.isopen = True
        key2.show = False
        bochka.change_image(False)


    elif key1.show == True:
        bochka.isopen = True
        key1.show = False
        bochka.change_image(True)

def choose_gold():
    x = randint(1,3)
    if x == 1:
        bochka1.iscoin = True
    elif x == 2:
        bochka2.iscoin = True
    else:
        bochka3.iscoin = True

pygame.init()
isgoldfine = False #найдено ли золото?
window = pygame.display.set_mode((800,600))
stat = Statistic(window)
score_btn = Score_button(window,stat)
bochka1 = Bochka(window,133,300,stat)
bochka2 = Bochka(window,399,300,stat)
bochka3 = Bochka(window,666,300,stat)
key1 = Key(window,80,550,2)
key2 = Key(window,150,550,1)
return_btn = Return(window)
choose_gold()#это функция есть сверху она выберает бочку в которой будет золото

while True:
    window.fill((0,0,0))
    score_btn.art_score_button()
    bochka1.art_bochka()#вызов  функции отресовки
    bochka2.art_bochka()
    bochka3.art_bochka()
    key1.art_key()
    key2.art_key()
    return_btn.art_return()
    stat.art_statistic()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#QUIT - это нажатие на крестик
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:#событие что мы кликнули мышкой
            if event.button == 1: #проверяем что нажали именно левую кнопку
                print("click")
                mousepoz = pygame.mouse.get_pos()#позиция мишки
                if bochka1.rect.collidepoint(mousepoz) and bochka1.isopen == False:
                    #collidepoint - проверяет наличие точки внутри кординат обэкта
                    try_open_bochka(bochka1)

                    print("bochka1")
                elif bochka2.rect.collidepoint(mousepoz):#collidepoint - проверяет наличие точки внутри кординат обэкта
                    print("bochka2")
                    try_open_bochka(bochka2)

                elif bochka3.rect.collidepoint(mousepoz):#collidepoint - проверяет наличие точки внутри кординат обэкта
                    print("bochka3")
                    try_open_bochka(bochka3)
                elif return_btn.rect.collidepoint(mousepoz):
                    return_work()
                elif score_btn.rect.collidepoint(mousepoz):
                    score_btn.click_score_button()







    pygame.display.flip()# flip - зацикливание всего


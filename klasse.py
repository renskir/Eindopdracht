import numpy as np
from itertools import combinations

from random import shuffle
import pygame
import time

class SETkaart:
    def __init__(self, aantal, kleur, vorm, dichtheid):
        self.vector = np.array([aantal, kleur, vorm, dichtheid])

        self.aantal = str(aantal + 1)

        if kleur == 0:
            self.kleur = 'green'
        elif kleur == 1:
            self.kleur = 'purple'
        elif kleur == 2:
            self.kleur = 'red'
        else:
            raise ValueError

        if vorm == 0:
            self.vorm = 'diamond'
        elif vorm == 1:
            self.vorm = 'oval'
        elif vorm == 2:
            self.vorm = 'squiggle'
        else:
            print(vorm)
            raise ValueError

        if dichtheid == 0:
            self.dichtheid = 'empty'
        elif dichtheid == 1:
            self.dichtheid = 'shaded'
        elif dichtheid == 2:
            self.dichtheid = 'filled'
        else:
            raise ValueError

    def __str__(self):
        return 'kaarten/' + self.kleur + self.vorm + self.dichtheid + self.aantal + '.gif'


class SET:
    def __init__(self):
        self.setkaarten = [SETkaart(i, j, k, l) for i in range(3) for j in range(3)
                           for k in range(3) for l in range(3)]

        shuffle(self.setkaarten)
        self.settafel = self.setkaarten[:12]
        self.setstapel = self.setkaarten[12:]

    def nieuwe_kaarten_set_gevonden(self, a, b, c):
        if len(self.setstapel) == 0:
            self.settafel[self.settafel.index(a)], \
            self.settafel[self.settafel.index(b)], \
            self.settafel[self.settafel.index(c)] = None, None, None
        else:
            # leg ze op tafel
            self.settafel[self.settafel.index(a)], \
            self.settafel[self.settafel.index(b)], \
            self.settafel[self.settafel.index(c)] = self.setstapel[:3]

            # haal ze van de stapel
            self.setstapel = self.setstapel[3:]

    def nieuwe_kaarten_geen_set_gevonden(self):
        if len(self.setstapel) == 0:
            return True
        else:
            # leg ze op tafel
            self.settafel[0], \
            self.settafel[1], \
            self.settafel[2] = self.setstapel[:3]

            # haal ze van de stapel
            self.setstapel = self.setstapel[3:]
            return False

    def vind_set(self):
        for comb in combinations(self.settafel, 3):
            if self.compare(*comb):
                return comb
        else:
            return None

    def vind_alle_sets(self):
        sets = []
        for comb in combinations(self.settafel, 3):
            if self.compare(*comb):
                sets.append(comb)
        return sets

    @staticmethod
    def compare(a, b, c):
        if a is None or b is None or c is None:
            return False
        else:
            return (np.remainder(a.vector + b.vector + c.vector, 3) == 0).all()


set = SET()
klaar = False
klaar2 = False
score_computer, score_player = 0, 0

SIZE = (100, 200)
WINDOW_SIZE = (SIZE[0]*4, SIZE[1]*3)
vierkanten = [(j*SIZE[0], i*SIZE[1]) for i in range(3) for j in range(4)]
tijd_om_set_te_vinden = 30 #TIJD IN SECONDEN
kaarten = list() # DIT IS DE LIJST MET KAARTEN WAARMEE JE EEN SET PROBEERT TE MAKEN

pygame.init()
pygame.display.set_caption('SET')
screen = pygame.display.set_mode(WINDOW_SIZE)

start_time = time.time()
while not klaar2:
    if time.time() - start_time > tijd_om_set_te_vinden:
        kaarten = list()
        alle_sets = set.vind_alle_sets()
        if len(alle_sets) > 0:
            set.nieuwe_kaarten_set_gevonden(*alle_sets[0])
            score_computer += 1
        else:
            klaar = set.nieuwe_kaarten_geen_set_gevonden()
        start_time = time.time()

    if not klaar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                klaar2 = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, vierkant in enumerate(vierkanten):
                    if vierkant[0] <= event.pos[0] < vierkant[0]+SIZE[0] and vierkant[1] <= event.pos[1] < vierkant[1]+SIZE[1]:
                        if set.settafel[i] not in kaarten:
                            kaarten.append(set.settafel[i])
                            if len(kaarten) == 3:
                                if set.compare(*kaarten):
                                    score_player += 1
                                    set.nieuwe_kaarten_set_gevonden(*kaarten)
                                    start_time = time.time()
                                kaarten = list()
                        else:
                            kaarten.remove(set.settafel[i])
    if klaar:
        screen.fill((0,0,0))
        if score_computer > score_player:
            winst1 = 'De computer heeft gewonnen... :('
        elif score_player > score_computer:
            winst1 = 'Jij hebt gewonnen! :)'
        else:
            winst1 = 'Gelijkspel! :/'

        winst2 =  'Computer: ' + str(score_computer) + '     Jij: ' + str(score_player)
        winst3 = 'Klik om opnieuw te spelen!'

        font = pygame.font.Font('freesansbold.ttf', 20)
        text1 = font.render(winst1, True, (255,255,255), (0, 0, 0))
        textRect1 = text1.get_rect()
        textRect1.center = (WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2 - 20)
        screen.blit(text1, textRect1)

        text2 = font.render(winst2, True, (255, 255, 255), (0, 0, 0))
        textRect2 = text2.get_rect()
        textRect2.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
        screen.blit(text2, textRect2)

        text3 = font.render(winst3, True, (255, 255, 255), (0, 0, 0))
        textRect3 = text3.get_rect()
        textRect3.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 20)
        screen.blit(text3, textRect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                klaar2 = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                klaar = False
                set = SET()
                score_computer, score_player = 0, 0
    else:
        # TEKEN NIEUW SCHERM
        screen.fill((0, 0, 0))
        for i in range(len(set.settafel)):
            if set.settafel[i] is not None:
                image = pygame.image.load(str(set.settafel[i]))
                screen.blit(image, vierkanten[i])

        for i in range(0, WINDOW_SIZE[0], SIZE[0]):
            pygame.draw.line(screen, (0,0,0), (i, 0), (i, WINDOW_SIZE[1]), 1)
        for j in range(0, WINDOW_SIZE[1], SIZE[1]):
            pygame.draw.line(screen, (0,0,0), (0, j), (WINDOW_SIZE[0], j), 1)

        for kaart in kaarten:
            plek = vierkanten[set.settafel.index(kaart)]
            pygame.draw.circle(screen, (85, 107, 217), (plek[0]+15, plek[1]+15), 10)

    pygame.display.flip()

#infinite loop
#timer is afgelopen:
    # bestaat er een set?
        #nieuwe_kaarten_set_gevonden(set) EN score_computer += 1
        #nieuwe_kaarten_geen_set_gevonden
#je klikt op het scherm
    # welke heb je aangeklikt?
    # stop in een kaarten ALS NOG NIET IN DE LIJST (anders doen we weg uit lijst halen)
    # kaarten LENGTE 3?
        # check of lijst een set is -> score_player += 1, kaarten = set(), timer = 0, kaarten aanvullen
# teken kaarten, inclusief teken highlights


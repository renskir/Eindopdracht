import numpy as np
from itertools import combinations
from random import shuffle

class SETkaart:
    def __init__(self, aantal, kleur, vorm, dichtheid):
        '''
        :param aantal: het aantal figuurtjes op de kaart
        :param kleur: de kleur van de figuurtjes op de kaart
        :param vorm: de vorm van de figuurtjes op de kaart
        :param dichtheid: de mate waarin de figuurtjes zijn ingekleurd

        De klasse SETkaart bestaat uit een array die de kaarten beschrijft, en een methode
        om later de afbeeldingen terug te vinden.
        '''

        self.vector = np.array([aantal, kleur, vorm, dichtheid])

        # om straks te afbeeldingen te vinden
        self.aantal = str(aantal + 1)

        if kleur == 0:
            self.kleur = 'green'
        elif kleur == 1:
            self.kleur = 'purple'
        elif kleur == 2:
            self.kleur = 'red'

        if vorm == 0:
            self.vorm = 'diamond'
        elif vorm == 1:
            self.vorm = 'oval'
        elif vorm == 2:
            self.vorm = 'squiggle'


        if dichtheid == 0:
            self.dichtheid = 'empty'
        elif dichtheid == 1:
            self.dichtheid = 'shaded'
        elif dichtheid == 2:
            self.dichtheid = 'filled'

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


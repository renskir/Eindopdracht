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


class Set:
    def __init__(self):
        '''
        De klasse SET creëert het spelletje SET door alle mogelijke kaarten te
        genereren, deze stapel kaarten te schudden, en twaalf kaarten op tafel
        te leggen. 
        '''
        
        self.setkaarten = [SETkaart(i, j, k, l) for i in range(3) for j in range(3)
                           for k in range(3) for l in range(3)]

        shuffle(self.setkaarten)
        self.settafel = self.setkaarten[:12]
        self.setstapel = self.setkaarten[12:]
        self.score_computer = 0
        self.score_speler = 0

    def nieuwe_kaarten_set_gevonden(self, a, b, c):
        '''
        :param a: de eerste kaart die bij een set hoort
        :param b: de tweede kaart die bij een set hoort
        :param c: de derde kaart die bij een set hoort

        Deze methode vervangt drie kaarten in de gevonden set
        door drie nieuwe kaarten van de stapel, als er nog kaarten
        op de stapel liggen. Anders worden de kaarten weggehaald.
        '''
        if len(self.setstapel) == 0:
            self.settafel[self.settafel.index(a)], \
            self.settafel[self.settafel.index(b)], \
            self.settafel[self.settafel.index(c)] = None, None, None
        else:
            # leg de kaarten op tafel
            self.settafel[self.settafel.index(a)], \
            self.settafel[self.settafel.index(b)], \
            self.settafel[self.settafel.index(c)] = self.setstapel[:3]

            # haal de kaarten van de stapel
            self.setstapel = self.setstapel[3:]

    def nieuwe_kaarten_geen_set_gevonden(self):
        '''
        Als er geen kaarten zijn gevonden door de computer, worden
        de bovenste drie kaarten vervangen door drie nieuwe kaarten
        van de stapel, als er nog kaarten op de stapel liggen, anders
        is het spel afgelopen.
        '''
        if len(self.setstapel) == 0:
            return True
        else:
            # leg de kaarten op tafel
            self.settafel[0], \
            self.settafel[1], \
            self.settafel[2] = self.setstapel[:3]

            # haal de kaarten van de stapel
            self.setstapel = self.setstapel[3:]
            return False

    def vind_set(self):
        '''
        Deze methode zoekt een set uit de kaarten die op tafel liggen.
        '''
        for comb in combinations(self.settafel, 3):
            if self.compare(*comb):
                return comb
        else:
            return None

    def vind_alle_sets(self):
        '''
        Deze methode zoekt alle mogelijke sets uit
        de kaarten die op tafel liggen.
        '''
        sets = []
        for comb in combinations(self.settafel, 3):
            if self.compare(*comb):
                sets.append(comb)
        return sets

    @staticmethod
    def compare(a, b, c):
        '''
        :param a: de eerste kaart die bij een mogelijke set hoort
        :param b: de tweede kaart die bij een mogelijke set hoort
        :param c: de derde kaart die bij een mogelijke set hoort

        Deze methode bekijkt van drie kaarten of deze een set vormen.
        '''
        if a is None or b is None or c is None:
            return False
        else:
            return (np.remainder(a.vector + b.vector + c.vector, 3) == 0).all()




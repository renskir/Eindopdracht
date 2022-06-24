from set import Set
import pygame
import time



set_spelletje = Set()  # maakt het spelletje set aan
klaar = False  # houdt bij of het spelletje is afgelopen
afgesloten = False  # houdt bij of het spelletje is afgesloten

SIZE = (100, 200) # geeft de grootte van de kaarten aan
WINDOW_SIZE = (SIZE[0]*4, SIZE[1]*3)  # geeft de grootte van het scherm aan
vierkanten = [(j*SIZE[0], i*SIZE[1]) for i in range(3) for j in range(4)] # geeft alle linkerbovenhoeken van de kaarten
tijd_om_set_te_vinden = 30  # tijd in seconden
kaarten = list()  # dit is de lijst met de kaarten die een set zouden moeten vormen

# maakt het scherm aan in pygame
pygame.init()
pygame.display.set_caption('SET')
screen = pygame.display.set_mode(WINDOW_SIZE)

# houdt bij hoelang het duurt om een set te vinden
start_time = time.time()

while not afgesloten:
    # kijkt of het langer heeft geduurd om een set te vinden dan de maximaal gegeven tijd
    if time.time() - start_time > tijd_om_set_te_vinden:
        # deselecteert de geselecteerde kaarten
        kaarten = list()
        # zoekt alle sets
        # als er sets zijn, dan wordt de eerste set vervangen en krijgt de computer een punt
        # als er geen sets zijn, worden de eerste drie kaarten vervangen
        alle_sets = set_spelletje.vind_alle_sets()
        if len(alle_sets) > 0: 
            set_spelletje.nieuwe_kaarten_set_gevonden(*alle_sets[0])
            set_spelletje.score_computer += 1
        else:
            klaar = set_spelletje.nieuwe_kaarten_geen_set_gevonden()
        start_time = time.time()

    # zolang het spelletje nog niet is afgelopen
    if not klaar:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                afgesloten = True

            # als er op een kaart is geklikt, wordt er gekeken welke kaart dit was en wordt deze kaart geselecteerd
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, vierkant in enumerate(vierkanten):
                    if vierkant[0] <= event.pos[0] < vierkant[0]+SIZE[0] and vierkant[1] <= event.pos[1] < vierkant[1]+SIZE[1]:
                        if set_spelletje.settafel[i] not in kaarten:
                            kaarten.append(set_spelletje.settafel[i])

                            # als er drie kaarten zijn geselecteerd wordt er gekeken of deze een set vormen
                            if len(kaarten) == 3:
                                if set_spelletje.compare(*kaarten):
                                    # de set wordt vervangen en de speler krijgt een punt
                                    set_spelletje.score_speler += 1
                                    set_spelletje.nieuwe_kaarten_set_gevonden(*kaarten)
                                    start_time = time.time()
                                kaarten = list()
                        else:
                            # de kaart wordt gedeselecteerd als deze al geselecteerd was
                            kaarten.remove(set_spelletje.settafel[i])

    # als het spelletje is afgelopen, staat er wie er gewonnen heeft, en is er de mogelijkheid om opnieuw te spelen
    if klaar:
        screen.fill((0,0,0))
        if set_spelletje.score_computer > set_spelletje.score_speler:
            winst1 = 'De computer heeft gewonnen... :('
        elif set_spelletje.score_speler > set_spelletje.score_computer:
            winst1 = 'Jij hebt gewonnen! :)'
        else:
            winst1 = 'Gelijkspel! :/'

        winst2 =  'Computer: ' + str(set_spelletje.score_computer) + '     Jij: ' + str(set_spelletje.score_speler)
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

        # als er geklikt wordt op het scherm wordt er opnieuw gespeeld
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                afgesloten = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                klaar = False
                set_spelletje = Set()
    else:
        # als het spelletje nog niet klaar is, worden de kaarten op het scherm getekend
        screen.fill((0, 0, 0))
        for i in range(len(set_spelletje.settafel)):
            if set_spelletje.settafel[i] is not None:
                image = pygame.image.load(str(set_spelletje.settafel[i]))
                screen.blit(image, vierkanten[i])

        for i in range(0, WINDOW_SIZE[0], SIZE[0]):
            pygame.draw.line(screen, (0,0,0), (i, 0), (i, WINDOW_SIZE[1]), 1)
        for j in range(0, WINDOW_SIZE[1], SIZE[1]):
            pygame.draw.line(screen, (0,0,0), (0, j), (WINDOW_SIZE[0], j), 1)

        for kaart in kaarten:
            plek = vierkanten[set_spelletje.settafel.index(kaart)]
            pygame.draw.circle(screen, (85, 107, 217), (plek[0]+15, plek[1]+15), 10)

    pygame.display.flip()


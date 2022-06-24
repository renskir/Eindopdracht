# Eindopdracht SET
## Toelichting bij de code
In het bestand set.py staan twee klassen, namelijk de klasse SetKaart en Set. De klasse SetKaart weergeeft een kaart in
het spelletje Set, zowel als numpy array en als tekst, om later de gegeven afbeeldingen makkelijk terug te kunnen vinden, 
met de _str_ methode. De klasse Set weergeeft het spelletje Set, als stapel waar nieuwe kaarten van gepakt kunnen worden,
de kaarten die 'op tafel' liggen en de kaarten die uit het spel zijn, en de scores van de speler en de computer.
Er is een methode om nieuwe kaarten op tafel te leggen als er een set is gevonden (deze set wordt vervangen door de bovenste drie kaarten op de stapel) en 
om nieuwe kaarten op tafel te leggen als er geen kaarten zijn gevonden (de eerste drie kaarten worden vervangen door de bovenste drie kaarten op de stapel).
Ook zijn er methodes om één set te vinden en om alle sets in het spelletje te vinden, zodat er gecontroleerd kan worden of 
er sets te vormen zijn op tafel, als de speler er geen kan vinden. Deze methodes proberen alle mogelijke combinaties van 
drie kaarten uit de twaalf kaarten die op tafel liggen, en controleren of deze drie kaarten een set vormen. De methode 
_vind_set_ stopt als er een set is gevonden, terwijl de methode _vind_alle_sets_ doorgaat tot alle combinaties zijn gecontroleerd.
Ten slotte is er een _static_ methode om te controleren of drie gegeven kaarten een set vormen, wat gedaan wordt door de 
vectoren die de kaarten weergeven componentsgewijs bij elkaar op te tellen en te controleren of alle componenten na deling door drie
geen rest meer hebben. In dat geval weten we voor iedere eigenschap dat deze of gelijk was in alle drie de kaarten, 
of verschilde in alle drie de kaarten.

In het bestand _game.py_ staat de _main loop_ voor het spelletje set. Er wordt een instantie van het spelletje aangemaakt. Er wordt een lege lijst gemaakt die bijhoudt welke kaarten er geselecteerd zijn, omdat het makkelijk is om elementen toe te voegen en weg te halen aan een lijst. De indeling van het scherm wordt bepaald aan de hand van constantes en een lijst _vierkanten_ (omdat een lijst geïndexeerd is) met de linkerbovenhoeken van waar de kaarten komen te liggen, en het scherm wordt aangemaakt. Dan start de timer om bij te houden hoe lang de speler erover doet om een set te vinden. Zolang het spelletje niet is afgelopen, wordt er gecontroleerd of de speler er langer dan de maximale tijd over heeft gedaan. In dat geval zoekt de computer een set, en als de computer deze kan vinden, krijgt de computer een punt. Dan worden zoals eerder genoemd de kaarten die de eerst gevonden set opmaken vervangen door kaarten van de stapel. Als de computer geen set kan vinden, worden de bovenste kaarten vervangen (als er nog een stapel over is, anders is het spel afgelopen). De timer begint nu opnieuw. Zolang de speler er niet langer dan de maximale tijd over heeft gedaan en het spelletje niet is afgelopen, wordt er gekeken of het scherm wordt afgesloten, en of er op het scherm wordt geklikt. In dat laatste geval wordt er uitgezocht waar er wordt geklikt aan de hand van de eerder genoemde lijst _vierkanten_. De bijbehorende kaart wordt toegevoegd aan de lijst met kaarten die mogelijk een set vormen (als deze nog niet geselecteerd was), en als deze lengte 3 heeft wordt er gecontroleerd of deze een set vormen. Als dat zo is wordt de set vervangen en een punt toegekend aan de speler. Als de kaart al geselecteerd was, dan wordt deze nu gedeselecteerd, door de kaart uit de lijst te halen. Als het spel is afgelopen worden de scores op het scherm weergegeven en de winnaar benoemd. Er is dan de mogelijkheid om opnieuw te spelen als er op het scherm wordt geklikt. Dan wordt er een nieuwe instantie gemaakt van de klasse Set.


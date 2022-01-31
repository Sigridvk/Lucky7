# Lucky7
Programmeertheorie

## Case Rush Hour
Rush Hour is een ogenschijnlijk eenvoudig puzzeltje met een verrassend uitdagend karakter. In een veld van dezelfde hoogte en breedte staat een rode auto, de jouwe, en die moet naar de uitgang, die recht voor je ligt. Maar andere voertuigen versperren de weg; auto’s van twee eenheden lang en trucks van drie eenheden lang, die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien. De opdracht is simpel: beweeg je auto naar buiten.

6x6: game 1, game 2, game 3          
<img src="https://theorie.mprog.nl/course/cases/Rush%20Hour/Rushhour6x6_1.jpg" width="150" />
<img src="https://theorie.mprog.nl/course/cases/Rush%20Hour/Rushhour6x6_2.jpg" width="150" />
<img src="https://theorie.mprog.nl/course/cases/Rush%20Hour/Rushhour6x6_3.jpg" width="150" />

9x9: game 4, game 5, game 6    
<img src="https://theorie.mprog.nl/course/cases/Rush%20Hour/Rushhour9x9_1.jpg" width="150" />
<img src="https://theorie.mprog.nl/course/cases/Rush%20Hour/Rushhour9x9_2.jpg" width="150" />
<img src="https://theorie.mprog.nl/course/cases/Rush%20Hour/Rushhour9x9_3.jpg" width="150" />

12x12: game 7                                      
<img src="https://theorie.mprog.nl/course/cases/Rush%20Hour/Rushhour12x12_1.jpg" width="250" />


## Run the program
Roep het programma op deze manier aan:
`python3 rushhour.py -g GAME -o OUTPUT -a ALGORITHM [-n NUMER_OF_RUNS]`

De beschikbare algoritmes zijn:
- Random solver: 
   - Met behulp van ‘random.choice’ wordt er een voertuig op het bord gekozen. Vervolgens
    wordt met de functie check_move bepaald welke stappen het voertuig kan zetten. Als het
    voertuig: een stap naar voren, een stap naar achter, maar ook twee stappen naar achter kan
    maken, dan wordt deze lijst gegenereerd: [-2, -1, 1]. Uit de lijst wordt daarna, weer met
    random.choice , een stap gekozen en wordt deze gezet.

- Greedy solver:
   - Er wordt random een voertuig op het bord gekozen. Als een voertuig geen stappen kan zetten wordt dit voertuig verwijderd uit lijst met mogelijke voertuigen. Mocht er een stap 
    worden gezet door een ander voertuig, dan kan voor de daaropvolgende move weer uit alle 
    voertuigen gekozen worden.
    - Een move van een voertuig kan niet meer ongedaan worden gemaakt door het voertuig gelijk weer terug te bewegen naar zijn vorige positie. Door de 
    laatste stap op te slaan kan er nu gecontroleerd worden of dit het geval is. Indien deze stap
    geselecteerd wordt, voeren we deze niet uit. En wordt opnieuw een voertuig gekozen.
    - Er wordt gecontroleerd of de rode auto naar voren kan worden gezet of door welk voertuig deze wordt geblokkeerd. Indien de rode auto naar voren kan, wordt deze stap uitgevoerd. Indien de rode auto wordt geblokkeerd, wordt onthouden welk voertuig dit is. Pas nadat dit voertuig een stap heeft gezet, wordt gecheckt of de rode auto naar voren kan bewegen. Tussendoor vindt het random-algoritme plaats zoals voorheen. De rode auto kan worden terug bewogen wanneer deze wordt geselecteerd door het random algoritme. Als de rode auto nooit wordt teruggeplaatst, is het probleem niet oplosbaar.

- Breadth first search:
    - Een belangrijk kenmerk van dit algoritme is, dat als er een oplossing gevonden wordt, dit de optimale (zomin mogelijk zetten) oplossing is. Echter, een breadth-first algoritme gebruikt ontzettend veel geheugen, dus hoe groter het bord, hoe langer het duurt. Ook kan het zelfs zijn dat het teveel geheugen kost en het algoritme bepaalde borden niet kan oplossen hierdoor Helaas heeft ons algoritme tot nu toe alleen de optimale oplossing gevonden voor borden van 6x6 en het eerste spelbord van 9x9. 

Deze zijn respectievelijk aan te roepen in de command line als volgt: 
`random`
`greedy`
`breadth`

Bijvoorbeeld:
`python3 rushhour.py -g Rushhour6x6_1 -o runs_per_game.csv -a random -n 1000`

Het aantal stappen dat wordt genomen om tot een oplossing van de game te komen wordt voor alle runs naar het output-bestand geschreven waarvan de naam op de commandline kan worden meegegeven hetzelfde gebeurt met de daadwerkelijke verplaatsingen van de voertuigen op het spelbord.




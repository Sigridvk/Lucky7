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

## Aan de slag
### Vereisten
In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de Rushhour class
  - **/code/visualisation**: bevat de code om een oplossing the visualiseren in Turtle en om de output te visualiseren
- **/gameboards**: bevat de verschillende gameboards die hierboven zijn benoemd
- **/output**: bevat voor ieder algoritme een mapje met alle gevonden resultaten

## Run the program
Roep het programma op deze manier aan:
`python3 main.py -g GAME -a ALGORITHM [-n NUMER_OF_RUNS]`

Bijvoorbeeld:
`python3 main.py -g Rushhour6x6_1 -a random -n 1000`

De verschillende games staan in de map Lucky7/gameboards.

De beschikbare algoritmes zijn:
- Random solver (`-a random`): 
   - Met behulp van ‘random.choice’ wordt er een voertuig op het bord gekozen. Vervolgens
    wordt met de functie check_move bepaald welke stappen het voertuig kan zetten. Als het
    voertuig: een stap naar voren, een stap naar achter, maar ook twee stappen naar achter kan
    maken, dan wordt deze lijst gegenereerd: [-2, -1, 1]. Uit de lijst wordt daarna, weer met
    random.choice , een stap gekozen en wordt deze gezet.

- Greedy1 solver (`-a greedy1`):
   - Er wordt random een voertuig op het bord gekozen. Als een voertuig geen stappen kan zetten wordt dit voertuig verwijderd uit lijst met mogelijke voertuigen. Mocht er een stap 
    worden gezet door een ander voertuig, dan kan voor de daaropvolgende move weer uit alle 
    voertuigen gekozen worden.
    - Een move van een voertuig kan niet meer ongedaan worden gemaakt door het voertuig gelijk weer terug te bewegen naar zijn vorige positie. Door de 
    laatste stap op te slaan kan er nu gecontroleerd worden of dit het geval is. Indien deze stap
    geselecteerd wordt, voeren we deze niet uit. En wordt opnieuw een voertuig gekozen.

- Greedy2 solver (`-a greedy2`):
    - Hetzelfde als de Greedy1 solver met als toevoeging dat er wordt gecontroleerd of de rode auto naar voren kan worden gezet of door welk voertuig deze wordt geblokkeerd. Indien de rode auto naar voren kan, wordt deze stap uitgevoerd. Indien de rode auto wordt geblokkeerd, wordt onthouden welk voertuig dit is. Pas nadat dit voertuig een stap heeft gezet, wordt gecheckt of de rode auto naar voren kan bewegen. Tussendoor vindt het random-algoritme plaats zoals voorheen. De rode auto kan worden terug bewogen wanneer deze wordt geselecteerd door het random algoritme. Als de rode auto nooit wordt teruggeplaatst, is het probleem niet oplosbaar.

- Breadth first search (`-a breadth`):
    - Een belangrijk kenmerk van dit algoritme is, dat als er een oplossing gevonden wordt, dit de optimale (zomin mogelijk zetten) oplossing is. Echter, een breadth-first algoritme gebruikt ontzettend veel geheugen, dus hoe groter het bord, hoe langer het duurt. Ook kan het zelfs zijn dat het teveel geheugen kost en het algoritme bepaalde borden niet kan oplossen hierdoor Helaas heeft ons algoritme tot nu toe alleen de optimale oplossing gevonden voor borden van 6x6 en het eerste spelbord van 9x9. 

Deze zijn respectievelijk aan te roepen in de command line als volgt: 
`random`
`greedy1`
`greedy2`
`breadth`


## Output
Het aantal zetten dat wordt genomen om tot een oplossing van de game te komen, wordt voor alle runs naar een output-bestand geschreven in de map 'Lucky7/output/{algoritme}'. Het bestand wordt opgeslagen met behulp van de game-naam: 'output_moves_{algoritme}_{game_naam}.csv'. Bijvoorbeeld: 'output_moves_greedy1_Rushhour6x6_2.csv'.

Alle zetten die genomen worden in de best gevonden oplossing, worden opgeslagen in de output-map van het desbetreffende algoritme onder de naam: 'output_moves_{algortime}_{game_naam}.csv'. Bijvoorbeeld: 'output_moves_random_Rushhour6x6_1.csv'.

## Visualise data
Om de data te visualiseren kunnen de programma's 'draw.py' en 'data_visualisation.py' gebruikt worden. Deze staan in de map Lucky7/code/visualisation.

## Run draw.py or data_visualisation.py
Deze programma's moeten beiden via Visual Studio Code worden aangeroepen. Rechtsbovenin staat een soort playbutton/driehoekje, 'Run Python File'. Als men daarop klikt onstaat er een soortgelijk pad in de terminal: `/opt/homebrew/bin/python3 "/Users/sigridvanklaveren/Documenten/Uva minor programmeren/Programmeertheorie/Lucky7/code/visualisation/draw.py"`. Dit is een voorbeeld van het bestand draw.py. Hieraan voegt men nog het volgende aan toe: `-f FOLDER -i INPUT_FILE -g GAME`. Bijvoorbeeld: `-f greedy1 -i output_moves_greedy1_Rushhour6x6_1 -g Rushhour6x6_1`.


### draw.py
draw.py creëert met behulp van de een tool genaamd 'Turtle' een spelbord waarin de voertuigen worden aangegeven met kleuren.
Hiervoor wordt het bestand gebruikt waarin de moves staan die tot een oplossing leiden. Dit bestand wordt gegenereerd wanneer het hoofdprogramma (main.py) met een van de algoritmes wordt aangeroepen.
Wanneer 'random' 'greedy1' of 'greedy2' wordt aangeroepen krijgt het bestand de naam: `output_moves_{algoritme}_{spel}.csv`. Bijvoorbeeld: `output_moves_greedy1_Rushhour6x6_2.csv`. 

Naar dit bestand worden automatisch de moves van de kortste oplossing geschreven.
Wanneer 'breadth' wordt aangeroepen krijgt het bestand de naam: 'best_solution_{game}.csv. Bijvoorbeeld: 'best_solution_Rushhour6x6_2.csv'. Naar dit bestand worden altijd de moves van de (de eerste) en de beste oplossing geschreven.

Een voorbeeld van een spelbord in Turtle:
<img src="file:///Users/lunaellinger/Dropbox%20(HEADHUNTERZ)/Programmeertheorie/turtle_draw.png" width="250" />

### data_visualisation.py
data_visualisation.py creëert met behulp van Matplotlib twee staafdiagrammen en een bestand waarin de mediaan, het gemiddelde en het maximaal/minimaal aantal stappen.
Hiervoor wordt het bestand gebruikt waarin het aantal stappen tot een oplossing per run van het algoritme. Dit bestand wordt alleen gegenereerd wanneer 'greedy1', 'greedy2' of 'random' het spel oplost. 
Het bestand heeft de naam: 'amount_steps_{algoritme}_{spel}.csv'. Bijvoorbeeld: 'amount_steps_greedy1_Rushhour6x6_2.csv'.

Op de x-as van de staafdiagrammen staat de frequentie van het aantal stappen, en op de y-as staan bins met het aantal stappen. 
Er worden automatisch twee verschillende bestanden gegenereerd. Een waarvan de bin-spreiding loopt van het 0 tot aan het maximaal aantal stappen en een ander waarin deze spreiding door vier is gedeeld. Deze keuze is gemaakt omdat het dan beter zichtbaar is hoe de werkelijke verdeling van stappen is.

Deze bestanden worden allemaal geschreven naar de map van het algoritme in de map output met de naam: 'data_visualisation - {algoritme}_{game}'. Bijvoorbeeld 'data_visualisation - greedy1_Rushhour6x6_2'.

Voorbeeld van een staafdiagram met een grote bin-spreiding:
<img src="https://github.com/Sigridvk/Lucky7/blob/main/doc/large_range_bins_greedy1_greedy1_Rushhour6x6_2.png" width="250" />

Voorbeeld van een staafdiagram met een kleine bin-spreiding:
<img src="file:///Users/lunaellinger/Dropbox%20(HEADHUNTERZ)/Programmeertheorie/data_visualisation%20-%20greedy1_Rushhour6x6_3/small_range_bins_greedy1_greedy1_Rushhour6x6_3.png" />

Voorbeeld van bestand met de mediaan, het gemiddelde en het maximaal/minimaal aantal stappen:
<img src="file:///Users/lunaellinger/Dropbox%20(HEADHUNTERZ)/Programmeertheorie/run_informatie.png" width="250" />

## Auteurs
- Luna Ellinger
- Vanja Misuric-Ramljak
- Sigrid van Klaveren

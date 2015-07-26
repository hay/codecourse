# -*- coding: utf-8 -*-
# In Python begint commentaar met een hekje (#)
# Alles waar een hekje voorstaat wordt door Python overgeslagen

print "Hallo, wereld!" # Ook als het niet aan het begin van een zin staat

# De gouden tip: tik 'python' (zonder bestandsnaam) en je komt in de REPL
# Waar je dit soort dingen allemaal zelf kan uitproberen

# Een variabele moet je declareren met elke naam die je wilt
getal = 42 # Een integer is een heel getal zonder punt
breuk = 4.2 # Een float is een getal met een punt
leuk = True # Een boolean is waar
niet_leuk = False # Of niet waar
niks = None # En je hebt ook nog de 'niks' waarde

# Een variabele is.. variabel, ergo: je kan het aanpassen
getal = getal * 2 # 'getal' is nu dus 84
breuk = getal / breuk # Een integer kan je delen door een float
getal = getal + 1 # Je kan optellen
getal = getal - 1 # Aftrekken
getal = getal * getal # Veremnigvuldigen
getal = getal / getal # En delen

# Een vergelijking is altijd True of False
getal = 42
check = getal == 42 # check is nu dus True
check = getal == 84 # check is nu dus False
check = getal != 84 # check is nu dus..True!

# Je kan ook checken of iets groter of kleiner is
check = getal > 20 # True, want 42 is groter dan 20
check = getal < 20 # False, want 42 is niet kleiner dan 20

# Je kan dingen combineren met and en or, let op de haakjes!
check = (getal > 20) or (getal < 20) # True, een van beide is waar
check = (getal > 20) and (getal < 20) # False, moeten beide waar zijn

# Vergelijkingen staan aan de basis van if, elif en else
if getal > 20: # Altijd een : na een if statement!
    print "Het getal is groter dan 20" # En statements in een if-blok altijd indenten!
else: # Weer een :
    print "Het getal is niet groter dan 20" # En een indent

# Eigenlijk is:
if getal > 20:
    print "Het getal is groter dan 20"

# Precies hetzelfde als
if (getal > 20) == True:
    print "Het getal is groter dan 20!"

# Met 'elif' (else if) kun je ook andere condities checken
if getal > 20:
    print "Het getal is groter dan 20"
elif getal < 10:
    print "Het getal is groter dan 20"
else:
    print "Het getal zit tussen 10 en 20"

# Dan hebben we nog strings
zin = "Hallo, wereld!" # Altijd tussen dubbele quotes
zin = 'Hallo, "Wereld"!' # Of enkele, als je bijvoorbeeld dubbele quotes wilt gebruiken

# Strings kun je, net als getallen, optellen. Dat noem je 'concatineren'
zin1 = "Hallo, "
zin2 = "Wereld!"
zin = zin1 + zin2

# Maar makkelijker is het om gebruik te maken van 'string interpolation'
zin = "Hallo, %s!" % "wereld" # De procent vervangt de '%s' door de string "wereld"

# Als je meer dan één string wilt vervangen moeten de strings tussen haakjes
zin = "%s, %s!" % ("Hallo, ", "Wereld")

# Uiteraard kunnen die strings ook weer variabelen zijn
ding = "wereld"
zin = "Hallo, %s!" % ding

# Strings kun je 'slicen' als je één of meerdere karakters wilt
print zin[0] # 'H', tellen begint bij 0
print zin[-1] # '!', het laatste karakter is dus -1, niet -0!
print zin[1:5] # Print vanaf karakter 1 tot (niet tot en met!) 5, dus "allo"
print zin[:5] # Print vanaf het begin tot karakter 5, dus "Hallo"
print zin[5:] # Print vanaf karakter 5 tot het einde van de string, dus ", wereld"

# Om te checken of een string in een andere string zit gebruik je de 'in' operator
zin = "Hallo, wereld!"
print "Hallo" in zin # True, "Hallo" zit in de zin
print "Doei" in zin # False, zit er niet in

# En strings hebben een hoop methodes om de string te manipuleren
zin.upper() # Converteert naar HOOFDLETTERS
zin.lower() # Converteert naar onderkast
zin.strip() # Verwijder alle spaties aan het begin en einde van de zin
zin.split(" ") # Opsplitsen naar een list op basis van een andere string

# Strings werken net zoals andere waardes in vergelijkingen
naam = "Barrie"
if naam == "Barrie":
    print "De naam is Barrie"
else:
    print "De naam is niet Barrie, maar %s" % naam

# Als je meerdere variabelen bij elkaar wilt stoppen gebruik je een lijst
names = ["Barrie", "Tinus", "Hans"]

# Die kun je ook weer 'slicen'
print names[0] # Barrie
print "%s en %s" % (names[0], names[2]) # "Barrie en Hans"

# Je kan alle soorten waardes in een lijst opnemen
dingen = ["Tinus", 1, True, 5.2]

# En hier werkt de 'in' operator ook
print "Tinus" in names # True
print "Nellie" in names # False
print "tinus" in names # 'in' is case-sensitive, dus dit is False

# De 'in' operator gebruik je ook om door een lijstje heen te loopen, dat doe
# je met het 'for' commando. Je definieert ook een variabele die je gebruikt
# om de variabele tijdelijk op te slaan
for item in names: # Let op, weer een dubbele punt!
    print "En hier is %s" % item # En een indent!

# Bovenstaande for-loop is identiek aan
print "En hier is %s" % names[0]
print "En hier is %s" % names[1]
print "En hier is %s" % names[2]

# Met het range() commando kun je tellen door een lijst. Dit stukje code
# Print 'Dit is nummer 0' tot en met 'Dit is nummer 9'
for x in range(10):
    print "Dit is nummer %s" % x

# Ook een list heeft methodes, zoals 'append', waarmee je een item toevoegt
# aan een bestaande lijst
names = ["Tinus"]
names.append("Barrie")
print len(names) # 'len' geeft de lengte van een lijst. Dit is dus nu 2

# Een korte reminder: je kan in methodes, zoals 'append' ook weer variabelen
# stoppen.
names = [] # Een lege lijst
name = "Barrie"
names.append(name)

# Naast de list heb je ook de dict. Daar ga je altijd uit van key-value pairs
item = { # Let op de accolades (curly braces).
    "naam" : "Barrie", # Let op de komma. Indenten hoeft niet, mag wel.
    "soort" : "aap" # Geen komma, want het is de laatste
}

print "naam:" + item["naam"] # "Barrie"
print "soort:" + item["soort"] # "aap"

# Als je door keys en values wil loopen moet je gebruik maken van de
# iteritems() methode.
# De code hieronder doet precies hetzelfde als de twee print regels boven
for key, val in item.iteritems():
    print "%s:%s" % (key, val)

# Je kan lists en dicts combineren
dieren = [ # Blokhaken, van de list
    { # Accolades van de dict
        "naam" : "Barrie",
        "soort" : "aap"
    }, # En dus weer een komma
    {
        "naam" : "Tinus",
        "soort" : "bever"
    }  # En hier niet, want laatste item van de list
]

# En zo loop je daar doorheen met twee for-loops, een zogenaamde geneste for-loop
for item in dieren: # Hier geen iteritems(), want het is een lijst
    for key, val in item.iteritems(): # Maar hier wel, want het is een dict!
        print "%s:%s" % (key, val)

# Als je ook wilt tellen bij welk item je bent kun je gebruik maken van de
# enumerate functie
for index, item in enumerate(dieren): # 'index' en 'item' mogen elke naam hebben
    print "%s:%s" % (index, item["naam"]) # Hier gebruiken we de waarde direct

# Je kan door veel meer dingen 'itereren', zoals bijvoorbeeld bestanden
f = open("bestandsnaam.txt") # met 'open' kun je een bestand openen in read-only modus
for line in f:
    print line # 'line' is dus nu weer een string

# Om je code beter te structeren kun je gebruik maken van functies. Een functie
# definieer je altijd met 'def' een naam en dan twee haakjes
def hoi(): # Weer een dubbele punt
    print "Hallo, wereld!" # Alle code in een functie is altijd geindent

# Je kan dan vervolgens de functie aanroepen met de naam die je hebt gegeven
# en de twee haakjes
hoi() # "Hallo, wereld!"

# Je kan er alles mee doen wat je wilt
for x in range(3):
    hoi() # Drie keer "Hallo, wereld!"

# Een functie kan ook een argument krijgen. Hiermee kun je een stukje code
# wat je vaak gebruikt hergebruiken en configueerbaar maken
def hoi(wat):
    print "Hallo, %s!" % wat

hoi("wereld")    # 'Hallo, wereld!'
hoi("buurvrouw") # 'Hallo, buurvrouw!'
hoi("daar")      # 'Hallo, daar!'

# Je kan een functie zoveel argumenten geven als je wilt
def hoi(hoe, wat):
    print "%s, %s!" % (hoe, wat)

hoi("Hallo", "wereld")
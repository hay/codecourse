films = [
    {
        "titel" : "The Third Man",
        "jaar" : 1949
    },
    {
        "titel" : "Ace Ventura: Pet Detective",
        "jaar" : 1994
    }
]

titel3 = raw_input("Wat vind je een toffe film?")
jaar3 = raw_input("Uit welk jaar komt deze film?")

film3 = {}
film3["titel"] = titel3
film3["jaar"] = int(jaar3)

films.append(film3)

print "////////////////////////////////////"
print "De dicts in deze list ofwel de films die in de lijst staan zijn"
print "////////////////////////////////////"

for film in films:
    titel = film["titel"]
    jaar = film["jaar"]

    print titel.upper()
    print "%s is uitgekomen in %s" % (titel, jaar)
    jaargeleden = str(2015 - jaar) #Lotte heeft hier gecheat
    print "Dat is maar liefst %s jaar geleden" % jaargeleden
    print "------------------------------------"
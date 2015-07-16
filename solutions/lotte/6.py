name1 = raw_input("Hoe heet je?")
name2 = raw_input("Wat vind je nog meer een leuke naam?")
name3 = raw_input("Ok, noem nog een mooie naam.")
fruit = raw_input("En wat vind je een lekkere vrucht?")

names = [name1, name2, name3]

for name in names:
    if name[0].isupper():
        print "Aangenaam, %s" % (name)
    else:
        print "Hoi, %s" % (name)

for name in names:
    if "te" in name:
        print "Te gek! %s" % (name)

for name in names:
    print "%s is een %s" % (name, fruit.upper())
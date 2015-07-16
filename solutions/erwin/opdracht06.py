# -*- coding: utf-8 -*-

names = []
for name in range(3):
    print name
    name = raw_input("Noem een naam: ")
    names.append(name)

fruit = raw_input("Vertel me je lievelingsvrucht: ")

for name in names:
	if name[0].isupper():
		print "Aangenaam, " + name
	else:
		print "Hoi " + name

print "De lettercombinatie 'te' komt voor:"
for name in names:
	print "te" in name

print "%s is een %s" % (name, fruit.upper())

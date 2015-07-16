people = open("people.txt").readlines()
twitter = open("twitter.txt").readlines()

for index in range(len(people)):
    person = people[index].strip()
    date = twitter[index].strip()
    combination = "%s zit sinds %s op Twitter" % (person, date)
    print combination

people.close()
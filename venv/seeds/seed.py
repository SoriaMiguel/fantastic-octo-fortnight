import csv

users = []
with open("seeds/users.tsv") as data:
    rd = csv.DictReader(data, delimiter="\t", quotechar='"')
    for row in rd:
        users.append(row)

experiences = []
with open("seeds/experience.tsv") as data:
    rd = csv.DictReader(data, delimiter="\t", quotechar='"')
    for row in rd:
        experiences.append(row)

ids = []
for user in users:
    ids.append(user["id"])
for experience in experiences:
    ids.append(experience["id"])
ids = list(set(ids))

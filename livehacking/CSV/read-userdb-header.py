import sys
import csv

f = open(sys.argv[1], encoding='cp1252')
rdr = csv.DictReader(f, delimiter=';', quotechar='"')
for user in rdr:
    id = user['ID']
    firstname = user['First name']
    lastname = user['Last name']
    birth = user['Date of Birth']

    print(f'ID:{id}, Firstname:{firstname}, Lastname:{lastname}, Date of birth: {birth}')

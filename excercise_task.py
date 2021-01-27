import csv

with open('people2.csv', mode='w') as file:
    headers = ['firstname', 'lastname', 'age']
    writer = csv.DictWriter(file, delimiter=',')
    writer.header([])
    writer.writerow(['Joe', 'Bloggs', 40])  
    writer.writerow(['Jane', 'Smith', 50])
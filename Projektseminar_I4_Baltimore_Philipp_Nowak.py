# -*- coding: utf-8 -*-


import csv


#Listen definieren
baltimore_complete = []

#CSV-Datei öffnen & einlesen
with open ('Crime___Safety__2010-2014_.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		baltimore_complete.append(row)

#test
print baltimore_complete

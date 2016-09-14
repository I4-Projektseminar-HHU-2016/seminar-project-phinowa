# -*- coding: utf-8 -*-


import csv


#Im Folgenden befinden sich Funktionen, die für die (grafische) Auswertung benötigt werden
#Funktion 1: Summe einer Liste berechnen
def sum_function(my_list):
	list_sum = 0
	for i in my_list:
		list_sum += i
	return list_sum
	
#Funktion 2: Durchschnitt berechnen
def average_function(my_list):
	list_sum = 0
	for i in my_list:
		list_sum += i
	return list_sum/len(my_list)


#Listen definieren
baltimore_complete = []


#CSV-Datei öffnen & einlesen
with open ('Crime___Safety__2010-2014_.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		baltimore_complete.append(row)


#test
print baltimore_complete

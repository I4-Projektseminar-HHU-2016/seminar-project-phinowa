# -*- coding: utf-8 -*-


import csv


"""
Im Folgenden befinden sich Funktionen, die für die (grafische) Auswertung benötigt werden
"""
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
neighborhood_name = []
crime_10 = []
crime_11 = []
crime_12 = []
crime_13 = []
crime_14 = []


#CSV-Datei öffnen & einlesen
with open ('Crime___Safety__2010-2014_.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		baltimore_complete.append(row)


#Listen füttern: Richtige Spalte der CSV-Grunddatei der richtigen Liste zuordnen
for entry in baltimore_complete:
	neighborhood_name.append(entry[0])
	crime_10.append(entry[1])
	crime_11.append(entry[2])
	crime_12.append(entry[3])
	crime_13.append(entry[4])
	crime_14.append(entry[5])


#Die allgemeinen Spaltenüberschriften stören bei den neuen Listen und werden daher rausgeschmissen
neighborhood_name.pop(0)
crime_10.pop(0)
crime_11.pop(0)
crime_12.pop(0)
crime_13.pop(0)
crime_14.pop(0)


#Strings in Gleitkommazahl umwandeln, damit mit ihnen gearbeitet werden kann
crime_10 = map(float, crime_10)
crime_11 = map(float, crime_11)
crime_12 = map(float, crime_12)
crime_13 = map(float, crime_13)
crime_14 = map(float, crime_14)


#Crime-Rate pro Jahr berechnen
crime_average_2010 = average_function(crime_10)
crime_average_2011 = average_function(crime_11)
crime_average_2012 = average_function(crime_12)
crime_average_2013 = average_function(crime_13)
crime_average_2014 = average_function(crime_14)


#test
#print baltimore_complete
print crime_average_2010, crime_average_2011, crime_average_2012, crime_average_2013, crime_average_2014


"""
Im Folgenden werden die Diagramme erstellt
"""
import numpy as np
#Seaborn installieren in cmd per "pip install seaborn"
import seaborn as sns
import matplotlib.pyplot as plt


#Figur anlegen
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

#X-Labels und Werte definieren
x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_average_2010, crime_average_2011, crime_average_2012, crime_average_2013, crime_average_2014]

#Diagramm generieren
x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["red", "orange", "yellow", "green", "blue"])
ax.set_ylabel("Baltimore Verbrechensrate")

#Endeinstellungen
sns.despine(bottom=True)
plt.tight_layout()

plt.show()

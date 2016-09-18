# -*- coding: utf-8 -*-


import csv


"""
Im Folgenden befinden sich Funktionen, die für die (grafische) Auswertung benötigt werden
"""
#Funktion 1: Durchschnitt berechnen
def average_function(my_list):
	list_sum = 0
	for i in my_list:
		list_sum += i
	return list_sum/len(my_list)

#Funktion 2: Top-10 der Bezirke
def top_10_function(values, neighborhoods):
	top_10_list = []
	i = 0
	while i < 10:
		top_10_list.append(max(values)) 
		top_10_list.append(neighborhoods[values.index(max(values))])
		values[values.index(max(values))] = 0
		i = i+1
	return top_10_list

#Funktion 3: Flop-10 der Bezirke
def flop_10_function(values, neighborhoods):
	flop_10_list = []
	i = 0
	while i < 10:
		flop_10_list.append(min(values)) 
		flop_10_list.append(neighborhoods[values.index(min(values))])
		values[values.index(min(values))] = 100000
		i = i+1
	return flop_10_list


#Listen definieren
baltimore_complete = []
neighborhood_name = []
crime_10 = []
crime_11 = []
crime_12 = []
crime_13 = []
crime_14 = []
crime_10_top = []
crime_12_top = []
crime_14_top = []
crime_10_flop = []
crime_12_flop = []
crime_14_flop = []
crime_11_top = []
crime_13_top = []
crime_11_flop = []
crime_13_flop = []
viol_14_top = []
viol_14_flop = []
viol_10_top = []
viol_11_top = []
viol_12_top = []
viol_13_top = []
viol_10_flop = []
viol_11_flop = []
viol_12_flop = []
viol_13_flop = []
prop_14_top = []
prop_14_flop = []


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
	crime_10_top.append(entry[1])
	crime_12_top.append(entry[3])
	crime_14_top.append(entry[5])
	crime_10_flop.append(entry[1])
	crime_12_flop.append(entry[3])
	crime_14_flop.append(entry[5])
	crime_11_top.append(entry[2])
	crime_13_top.append(entry[4])
	crime_11_flop.append(entry[2])
	crime_13_flop.append(entry[4])
	viol_14_top.append(entry[10])
	viol_14_flop.append(entry[10])
	viol_10_top.append(entry[6])
	viol_11_top.append(entry[7])
	viol_12_top.append(entry[8])
	viol_13_top.append(entry[9])
	viol_10_flop.append(entry[6])
	viol_11_flop.append(entry[7])
	viol_12_flop.append(entry[8])
	viol_13_flop.append(entry[9])
	prop_14_top.append(entry[14])
	prop_14_flop.append(entry[14])


#Die allgemeinen Spaltenüberschriften stören bei den neuen Listen und werden daher rausgeschmissen
neighborhood_name.pop(0)
crime_10.pop(0)
crime_11.pop(0)
crime_12.pop(0)
crime_13.pop(0)
crime_14.pop(0)
crime_10_top.pop(0)
crime_12_top.pop(0)
crime_14_top.pop(0)
crime_10_flop.pop(0)
crime_12_flop.pop(0)
crime_14_flop.pop(0)
crime_11_top.pop(0)
crime_13_top.pop(0)
crime_11_flop.pop(0)
crime_13_flop.pop(0)
viol_14_top.pop(0)
viol_14_flop.pop(0)
viol_10_top.pop(0)
viol_11_top.pop(0)
viol_12_top.pop(0)
viol_13_top.pop(0)
viol_10_flop.pop(0)
viol_11_flop.pop(0)
viol_12_flop.pop(0)
viol_13_flop.pop(0)
prop_14_top.pop(0)
prop_14_flop.pop(0)


#Namen in Neighborhoods kürzen, damit Diagramme lesbarer werden
neighborhood_name = [i.split("/")[0] for i in neighborhood_name]
neighborhood_name = [i.split("&")[0] for i in neighborhood_name]


#Strings in Gleitkommazahl umwandeln, damit mit ihnen gearbeitet werden kann
crime_10 = map(float, crime_10)
crime_11 = map(float, crime_11)
crime_12 = map(float, crime_12)
crime_13 = map(float, crime_13)
crime_14 = map(float, crime_14)
crime_10_top = map(float, crime_10_top)
crime_12_top = map(float, crime_12_top)
crime_14_top = map(float, crime_14_top)
crime_10_flop = map(float, crime_10_flop)
crime_12_flop = map(float, crime_12_flop)
crime_14_flop = map(float, crime_14_flop)
crime_11_top = map(float, crime_11_top)
crime_13_top = map(float, crime_13_top)
crime_11_flop = map(float, crime_11_flop)
crime_13_flop = map(float, crime_13_flop)
viol_14_top = map(float, viol_14_top)
viol_14_flop = map(float, viol_14_flop)
viol_10_top = map(float, viol_10_top)
viol_11_top = map(float, viol_11_top)
viol_12_top = map(float, viol_12_top)
viol_13_top = map(float, viol_13_top)
viol_10_flop = map(float, viol_10_flop)
viol_11_flop = map(float, viol_11_flop)
viol_12_flop = map(float, viol_12_flop)
viol_13_flop = map(float, viol_13_flop)
prop_14_top = map(float, prop_14_top)
prop_14_flop = map(float, prop_14_flop)


#Crime-Rate pro Jahr berechnen
crime_average_2010 = average_function(crime_10)
crime_average_2011 = average_function(crime_11)
crime_average_2012 = average_function(crime_12)
crime_average_2013 = average_function(crime_13)
crime_average_2014 = average_function(crime_14)


#Top-10 der Crime-Rate berechnen
crime_top_10_2010 = top_10_function(crime_10_top, neighborhood_name)
crime_top_10_2012 = top_10_function(crime_12_top, neighborhood_name)
crime_top_10_2014 = top_10_function(crime_14_top, neighborhood_name)
crime_top_10_2011 = top_10_function(crime_11_top, neighborhood_name)
crime_top_10_2013 = top_10_function(crime_13_top, neighborhood_name)


#Flop-10 der Crime-Rate berechnen
crime_flop_10_2010 = flop_10_function(crime_10_flop, neighborhood_name)
crime_flop_10_2012 = flop_10_function(crime_12_flop, neighborhood_name)
crime_flop_10_2014 = flop_10_function(crime_14_flop, neighborhood_name)
crime_flop_10_2011 = flop_10_function(crime_11_flop, neighborhood_name)
crime_flop_10_2013 = flop_10_function(crime_13_flop, neighborhood_name)

#Top & Flop Nr. 1 der Crime-Rate aus den Jahren 2010 bis 2014
crime_top_1 = crime_top_10_2010[0], crime_top_10_2011[0], crime_top_10_2012[0], crime_top_10_2013[0], crime_top_10_2014[0]
crime_flop_1 = crime_flop_10_2010[0], crime_flop_10_2011[0], crime_flop_10_2012[0], crime_flop_10_2013[0], crime_flop_10_2014[0]

#Top-10 der Violence-Rate berechnen
viol_top_10_2014 = top_10_function(viol_14_top, neighborhood_name)
viol_top_10_2010 = top_10_function(viol_10_top, neighborhood_name)
viol_top_10_2011 = top_10_function(viol_11_top, neighborhood_name)
viol_top_10_2012 = top_10_function(viol_12_top, neighborhood_name)
viol_top_10_2013 = top_10_function(viol_13_top, neighborhood_name)

#Flop-10 der Violence-Rate berechnen
viol_flop_10_2014 = flop_10_function(viol_14_flop, neighborhood_name)
viol_flop_10_2010 = flop_10_function(viol_10_flop, neighborhood_name)
viol_flop_10_2011 = flop_10_function(viol_11_flop, neighborhood_name)
viol_flop_10_2012 = flop_10_function(viol_12_flop, neighborhood_name)
viol_flop_10_2013 = flop_10_function(viol_13_flop, neighborhood_name)

#Top & Flop Nr. 1 der Violence-Rate aus den Jahren 2010 bis 2014
viol_top_1 = viol_top_10_2010[0], viol_top_10_2011[0], viol_top_10_2012[0], viol_top_10_2013[0], viol_top_10_2014[0]
viol_flop_1 = viol_flop_10_2010[0], viol_flop_10_2011[0], viol_flop_10_2012[0], viol_flop_10_2013[0], viol_flop_10_2014[0]

#Top-10 der Property-Crime-Rate berechnen
prop_top_10_2014 = top_10_function(prop_14_top, neighborhood_name)

#Flop-10 der Property-Crime-Rate berechnen
prop_flop_10_2014 = flop_10_function(prop_14_flop, neighborhood_name)


#test
#print baltimore_complete
#print crime_average_2010, crime_average_2011, crime_average_2012, crime_average_2013, crime_average_2014
#print crime_top_10_2010, crime_top_10_2012, crime_top_10_2014
#print crime_flop_10_2010, crime_flop_10_2012, crime_flop_10_2014
#print crime_top_1, crime_flop_1
#print viol_top_10_2014, viol_flop_10_2014
#print neighborhood_name

"""
Im Folgenden werden die Diagramme erstellt
"""
import numpy as np
#Seaborn installieren in cmd per "pip install seaborn"
import seaborn as sns
import matplotlib.pyplot as plt

#Diagramm Durchschnitt Verbrechenquotient der Jahre 2010-2014 in Baltimore absolut (x-Achse: Jahre)
#Diagramm anlegen
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

#X-Labels und Werte definieren
x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_average_2010, crime_average_2011, crime_average_2012, crime_average_2013, crime_average_2014]

#Diagramm generieren
x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore Verbrechensrate")
ax.xaxis.set_label_position("top")

#Endeinstellungen
sns.despine(bottom=True)
plt.tight_layout()


#Diagramm Top 10 Verbrechen in 2010 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_top_10_2010[1], crime_top_10_2010[3], crime_top_10_2010[5], crime_top_10_2010[7], crime_top_10_2010[9], crime_top_10_2010[11], crime_top_10_2010[13], crime_top_10_2010[15], crime_top_10_2010[17], crime_top_10_2010[19]]
x_values = [crime_top_10_2010[0], crime_top_10_2010[2], crime_top_10_2010[4], crime_top_10_2010[6], crime_top_10_2010[8], crime_top_10_2010[10], crime_top_10_2010[12], crime_top_10_2010[14], crime_top_10_2010[16], crime_top_10_2010[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000"])
ax.set_xlabel("Baltimore Top 10 Verbrechen 2010")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Top 10 Verbrechen in 2012 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_top_10_2012[1], crime_top_10_2012[3], crime_top_10_2012[5], crime_top_10_2012[7], crime_top_10_2012[9], crime_top_10_2012[11], crime_top_10_2012[13], crime_top_10_2012[15], crime_top_10_2012[17], crime_top_10_2012[19]]
x_values = [crime_top_10_2012[0], crime_top_10_2012[2], crime_top_10_2012[4], crime_top_10_2012[6], crime_top_10_2012[8], crime_top_10_2012[10], crime_top_10_2012[12], crime_top_10_2012[14], crime_top_10_2012[16], crime_top_10_2012[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF0000"])
ax.set_xlabel("Baltimore Top 10 Verbrechen 2012")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Top 10 Verbrechen in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_top_10_2014[1], crime_top_10_2014[3], crime_top_10_2014[5], crime_top_10_2014[7], crime_top_10_2014[9], crime_top_10_2014[11], crime_top_10_2014[13], crime_top_10_2014[15], crime_top_10_2014[17], crime_top_10_2014[19]]
x_values = [crime_top_10_2014[0], crime_top_10_2014[2], crime_top_10_2014[4], crime_top_10_2014[6], crime_top_10_2014[8], crime_top_10_2014[10], crime_top_10_2014[12], crime_top_10_2014[14], crime_top_10_2014[16], crime_top_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF6666"])
ax.set_xlabel("Baltimore Top 10 Verbrechen 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Flop 10 Verbrechen in 2010 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_flop_10_2010[1], crime_flop_10_2010[3], crime_flop_10_2010[5], crime_flop_10_2010[7], crime_flop_10_2010[9], crime_flop_10_2010[11], crime_flop_10_2010[13], crime_flop_10_2010[15], crime_flop_10_2010[17], crime_flop_10_2010[19]]
x_values = [crime_flop_10_2010[0], crime_flop_10_2010[2], crime_flop_10_2010[4], crime_flop_10_2010[6], crime_flop_10_2010[8], crime_flop_10_2010[10], crime_flop_10_2010[12], crime_flop_10_2010[14], crime_flop_10_2010[16], crime_flop_10_2010[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000"])
ax.set_xlabel("Baltimore Flop 10 Verbrechen 2010")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Flop 10 Verbrechen in 2012 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_flop_10_2012[1], crime_flop_10_2012[3], crime_flop_10_2012[5], crime_flop_10_2012[7], crime_flop_10_2012[9], crime_flop_10_2012[11], crime_flop_10_2012[13], crime_flop_10_2012[15], crime_flop_10_2012[17], crime_flop_10_2012[19]]
x_values = [crime_flop_10_2012[0], crime_flop_10_2012[2], crime_flop_10_2012[4], crime_flop_10_2012[6], crime_flop_10_2012[8], crime_flop_10_2012[10], crime_flop_10_2012[12], crime_flop_10_2012[14], crime_flop_10_2012[16], crime_flop_10_2012[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF0000"])
ax.set_xlabel("Baltimore Flop 10 Verbrechen 2012")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Flop 10 Verbrechen in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_flop_10_2014[1], crime_flop_10_2014[3], crime_flop_10_2014[5], crime_flop_10_2014[7], crime_flop_10_2014[9], crime_flop_10_2014[11], crime_flop_10_2014[13], crime_flop_10_2014[15], crime_flop_10_2014[17], crime_flop_10_2014[19]]
x_values = [crime_flop_10_2014[0], crime_flop_10_2014[2], crime_flop_10_2014[4], crime_flop_10_2014[6], crime_flop_10_2014[8], crime_flop_10_2014[10], crime_flop_10_2014[12], crime_flop_10_2014[14], crime_flop_10_2014[16], crime_flop_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF6666"])
ax.set_xlabel("Baltimore Flop 10 Verbrechen 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Top 1 Verbrechen von 2010 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_top_1[0], crime_top_1[1], crime_top_1[2], crime_top_1[3], crime_top_1[4]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore Veraenderung von Top-Verbrechen ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Diagramm Flop 1 Verbrechen von 2010 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_flop_1[0], crime_flop_1[1], crime_flop_1[2], crime_flop_1[3], crime_flop_1[4]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore Veraenderung von Flop-Verbrechen ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Diagramm Top 10 Gewalt in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [viol_top_10_2014[1], viol_top_10_2014[3], viol_top_10_2014[5], viol_top_10_2014[7], viol_top_10_2014[9], viol_top_10_2014[11], viol_top_10_2014[13], viol_top_10_2014[15], viol_top_10_2014[17], viol_top_10_2014[19]]
x_values = [viol_top_10_2014[0], viol_top_10_2014[2], viol_top_10_2014[4], viol_top_10_2014[6], viol_top_10_2014[8], viol_top_10_2014[10], viol_top_10_2014[12], viol_top_10_2014[14], viol_top_10_2014[16], viol_top_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#6666FF"])
ax.set_xlabel("Baltimore Top 10 Gewalt 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Flop 10 Gewalt in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [viol_flop_10_2014[1], viol_flop_10_2014[3], viol_flop_10_2014[5], viol_flop_10_2014[7], viol_flop_10_2014[9], viol_flop_10_2014[11], viol_flop_10_2014[13], viol_flop_10_2014[15], viol_flop_10_2014[17], viol_flop_10_2014[19]]
x_values = [viol_flop_10_2014[0], viol_flop_10_2014[2], viol_flop_10_2014[4], viol_flop_10_2014[6], viol_flop_10_2014[8], viol_flop_10_2014[10], viol_flop_10_2014[12], viol_flop_10_2014[14], viol_flop_10_2014[16], viol_flop_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#6666FF"])
ax.set_xlabel("Baltimore Flop 10 Gewalt 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Top 1 Gewalt von 2010 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [viol_top_1[0], viol_top_1[1], viol_top_1[2], viol_top_1[3], viol_top_1[4]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#0000CD", "#0000E6", "#0000FF", "#3333FF", "#6666FF"])
ax.set_xlabel("Baltimore Veraenderung von Top-Gewalt ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Diagramm Flop 1 Gewalt von 2010 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [viol_flop_1[0], viol_flop_1[1], viol_flop_1[2], viol_flop_1[3], viol_flop_1[4]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#0000CD", "#0000E6", "#0000FF", "#3333FF", "#6666FF"])
ax.set_xlabel("Baltimore Veraenderung von Flop-Gewalt ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Diagramm Top 10 Diebstahl in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [prop_top_10_2014[1], prop_top_10_2014[3], prop_top_10_2014[5], prop_top_10_2014[7], prop_top_10_2014[9], prop_top_10_2014[11], prop_top_10_2014[13], prop_top_10_2014[15], prop_top_10_2014[17], prop_top_10_2014[19]]
x_values = [prop_top_10_2014[0], prop_top_10_2014[2], prop_top_10_2014[4], prop_top_10_2014[6], prop_top_10_2014[8], prop_top_10_2014[10], prop_top_10_2014[12], prop_top_10_2014[14], prop_top_10_2014[16], prop_top_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#66FF66"])
ax.set_xlabel("Baltimore Top 10 Diebstahl 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Diagramm Flop 10 Diebstahl in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [prop_flop_10_2014[1], prop_flop_10_2014[3], prop_flop_10_2014[5], prop_flop_10_2014[7], prop_flop_10_2014[9], prop_flop_10_2014[11], prop_flop_10_2014[13], prop_flop_10_2014[15], prop_flop_10_2014[17], prop_flop_10_2014[19]]
x_values = [prop_flop_10_2014[0], prop_flop_10_2014[2], prop_flop_10_2014[4], prop_flop_10_2014[6], prop_flop_10_2014[8], prop_flop_10_2014[10], prop_flop_10_2014[12], prop_flop_10_2014[14], prop_flop_10_2014[16], prop_flop_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#66FF66"])
ax.set_xlabel("Baltimore Flop 10 Diebstahl 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)



plt.show()

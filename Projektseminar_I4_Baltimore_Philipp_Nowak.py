# -*- coding: utf-8 -*-


import csv


"""
Im Folgenden befinden sich Funktionen, die für die (grafische) Auswertung benötigt werden
"""
#Funktion 1: Durchschnitt berechnen
def average_function(my_list):
	list_sum = 0
	for i in my_list:
		list_sum = list_sum + i
	return list_sum/len(my_list)
	
#Funktion 2: Median berechnen
def median_function(my_list):
	my_list_len = len(my_list)
	sorted_list = sorted(my_list)
	median_index = (my_list_len - 1) / 2
	if (my_list_len % 2):
		return sorted_list[median_index]
	else:
		return (sorted_list[median_index] + sorted_list[median_index + 1]) / 2

#Funktion 3: Modalwert berechnen
def modal_value_function(my_list):
	list_modal = max(set(my_list), key=my_list.count)
	return list_modal

#Funktion 4: Varianz berechnen
def variance_function(my_list):
	list_sum = 0
	for i in my_list:
		list_sum = list_sum + i
	average = list_sum/len(my_list)
	variance = sum(((i - average)**2 for i in my_list)) / (len(my_list) - 1)
	return variance

#Funktion 5: Standardabweichung berechnen
def standard_deviation_function(my_list):
	list_sum = 0
	for i in my_list:
		list_sum = list_sum + i
	average = list_sum/len(my_list)
	variance = sum(((i - average)**2 for i in my_list)) / (len(my_list) - 1)
	standard_deviation = variance**(0.5)
	return standard_deviation

#Funktion 6: Spannweite berechnen
def span_function(my_list):
	span = max(my_list) - min(my_list)
	return span

#Funktion 7: Prozentzahl der Werte einer Liste unter Wert "50" berechnen
def percent_list_50_function(my_list):
	length_list = 0
	counter = 0.0
	while length_list < len(my_list):
		for i in my_list:
			if i < 50:
				counter = counter+1
			length_list = length_list+1
	counter_percent = (counter / (len(my_list)))*100
	return counter_percent

#Funktion 8: Top-10 der Bezirke
#In Zusammenarbeit entwickelt mit Karoline Jüttner
def top_10_function(values, neighborhoods):
	top_10_list = []
	i = 0
	while i < 10:
		top_10_list.append(max(values)) 
		top_10_list.append(neighborhoods[values.index(max(values))])
		values[values.index(max(values))] = 0
		i = i + 1
	return top_10_list

#Funktion 9: Flop-10 der Bezirke
#In Zusammenarbeit entwickelt mit Karoline Jüttner
def flop_10_function(values, neighborhoods):
	flop_10_list = []
	i = 0
	while i < 10:
		flop_10_list.append(min(values)) 
		flop_10_list.append(neighborhoods[values.index(min(values))])
		values[values.index(min(values))] = 100000
		i = i + 1
	return flop_10_list

#Funktion 10: Verbrechensrate der Bezirke gestiegen
def rise_function(values_10, values_11, values_12, values_13, values_14):
	i = 0
	x = 0
	rise_list = []
	while i < len(values_10):
		if values_10[i] - values_11[i] < 0:
			x = x + 1
		if values_11[i] - values_12[i] < 0:
			x = x + 1
		if values_12[i] - values_13[i] < 0:
			x = x + 1
		if values_13[i] - values_14[i] < 0:
			x = x + 1
		i = i + 1
		rise_list.append(x)
		x = 0
	return rise_list

#Funktion 11: Verbrechensrate der Bezirke gesunken
def drop_function(values_10, values_11, values_12, values_13, values_14):
	i = 0
	x = 0
	drop_list = []
	while i < len(values_10):
		if values_10[i] - values_11[i] > 0:
			x = x + 1
		if values_11[i] - values_12[i] > 0:
			x = x + 1
		if values_12[i] - values_13[i] > 0:
			x = x + 1
		if values_13[i] - values_14[i] > 0:
			x = x + 1
		i = i+1
		drop_list.append(x)
		x = 0
	return drop_list

#Funktion 12: Prozentuale Veränderung berechnen
def percentage_function(my_list_1, my_list_2):
	i = 0
	percentage = 0
	percentage_list = []
	while i < len(my_list_1):
		percentage = int(100-((my_list_1[i]/my_list_2[i])*100))
		i = i + 1
		percentage_list.append(percentage)
	return percentage_list


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
prop_11_top = []
prop_12_top = []
prop_13_top = []
prop_11_flop = []
prop_12_flop = []
prop_13_flop = []
crime_10_median = []
crime_11_median = []
crime_12_median = []
crime_13_median = []
crime_14_median = []
viol_11 = []
viol_12 = []
viol_13 = []
viol_14 = []
prop_11 = []
prop_12 = []
prop_13 = []
prop_14 = []
domvio_11 = []
domvio_12 = []
gunhom_11 = []
gunhom_12 = []
gunhom_13 = []
gunhom_14 = []


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
	prop_11_top.append(entry[11])
	prop_12_top.append(entry[12])
	prop_13_top.append(entry[13])
	prop_11_flop.append(entry[11])
	prop_12_flop.append(entry[12])
	prop_13_flop.append(entry[13])
	crime_10_median.append(entry[1])
	crime_11_median.append(entry[2])
	crime_12_median.append(entry[3])
	crime_13_median.append(entry[4])
	crime_14_median.append(entry[5])
	viol_11.append(entry[7])
	viol_12.append(entry[8])
	viol_13.append(entry[9])
	viol_14.append(entry[10])
	prop_11.append(entry[11])
	prop_12.append(entry[12])
	prop_13.append(entry[13])
	prop_14.append(entry[14])
	domvio_11.append(entry[19])
	domvio_12.append(entry[20])
	gunhom_11.append(entry[29])
	gunhom_12.append(entry[30])
	gunhom_13.append(entry[31])
	gunhom_14.append(entry[32])
	

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
prop_11_top.pop(0)
prop_12_top.pop(0)
prop_13_top.pop(0)
prop_11_flop.pop(0)
prop_12_flop.pop(0)
prop_13_flop.pop(0)
crime_10_median.pop(0)
crime_11_median.pop(0)
crime_12_median.pop(0)
crime_13_median.pop(0)
crime_14_median.pop(0)
viol_11.pop(0)
viol_12.pop(0)
viol_13.pop(0)
viol_14.pop(0)
prop_11.pop(0)
prop_12.pop(0)
prop_13.pop(0)
prop_14.pop(0)
domvio_11.pop(0)
domvio_12.pop(0)
gunhom_11.pop(0)
gunhom_12.pop(0)
gunhom_13.pop(0)
gunhom_14.pop(0)


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
prop_11_top = map(float, prop_11_top)
prop_12_top = map(float, prop_12_top)
prop_13_top = map(float, prop_13_top)
prop_11_flop = map(float, prop_11_flop)
prop_12_flop = map(float, prop_12_flop)
prop_13_flop = map(float, prop_13_flop)
crime_10_median = map(float, crime_10_median)
crime_11_median = map(float, crime_11_median)
crime_12_median = map(float, crime_12_median)
crime_13_median = map(float, crime_13_median)
crime_14_median = map(float, crime_14_median)
viol_11 = map(float, viol_11)
viol_12 = map(float, viol_12)
viol_13 = map(float, viol_13)
viol_14 = map(float, viol_14)
prop_11 = map(float, prop_11)
prop_12 = map(float, prop_12)
prop_13 = map(float, prop_13)
prop_14 = map(float, prop_14)
domvio_11 = map(float, domvio_11)
domvio_12 = map(float, domvio_12)
gunhom_11 = map(float, gunhom_11)
gunhom_12 = map(float, gunhom_12)
gunhom_13 = map(float, gunhom_13)
gunhom_14 = map(float, gunhom_14)
#Strings in Integer umwandeln, damit mit ihnen für den Modalwert gearbeitet werden kann
crime_10_int = map(int, crime_10)
crime_11_int = map(int, crime_11)
crime_12_int = map(int, crime_12)
crime_13_int = map(int, crime_13)
crime_14_int = map(int, crime_14)


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
prop_top_10_2011 = top_10_function(prop_11_top, neighborhood_name)
prop_top_10_2012 = top_10_function(prop_12_top, neighborhood_name)
prop_top_10_2013 = top_10_function(prop_13_top, neighborhood_name)

#Flop-10 der Property-Crime-Rate berechnen
prop_flop_10_2014 = flop_10_function(prop_14_flop, neighborhood_name)
prop_flop_10_2011 = flop_10_function(prop_11_flop, neighborhood_name)
prop_flop_10_2012 = flop_10_function(prop_12_flop, neighborhood_name)
prop_flop_10_2013 = flop_10_function(prop_13_flop, neighborhood_name)

#Top & Flop Nr. 1 der Property-Crime-Rate aus den Jahren 2011 bis 2014
prop_top_1 = prop_top_10_2011[0], prop_top_10_2012[0], prop_top_10_2013[0], prop_top_10_2014[0]
prop_flop_1 = prop_flop_10_2011[0], prop_flop_10_2012[0], prop_flop_10_2013[0], prop_flop_10_2014[0]

#Verbrechensrate der Bezirke gestiegen berechnen
crime_rise = rise_function(crime_10, crime_11, crime_12, crime_13, crime_14)

#Top-10 Verbrechensrate der Bezirke gestiegen berechnen
crime_rise_top_10 = top_10_function(crime_rise, neighborhood_name)

#Verbrechensrate der Bezirke gesunken berechnen
crime_drop = drop_function(crime_10, crime_11, crime_12, crime_13, crime_14)

#Top-10 Verbrechensrate der Bezirke gesunken berechnen
crime_drop_top_10 = top_10_function(crime_drop, neighborhood_name)

#Prozentuale Veränderung berechnen
percentage_change = percentage_function(crime_10, crime_14)

#Top-10 prozentuale Steigerung berechnen
crime_percentage_change_rise_top_10 = top_10_function(percentage_change, neighborhood_name)

#Top-10 prozentuale Senkung berechnen
crime_percentage_change_drop_top_10 = flop_10_function(percentage_change, neighborhood_name)

#Median der Crime-Rate pro Jahr berechnen
crime_median_2010 = median_function(crime_10_median)
crime_median_2011 = median_function(crime_11_median)
crime_median_2012 = median_function(crime_12_median)
crime_median_2013 = median_function(crime_13_median)
crime_median_2014 = median_function(crime_14_median)

#Modalwert der Crime-Rate pro Jahr berechnen
crime_modal_value_2010 = modal_value_function(crime_10_int)
crime_modal_value_2011 = modal_value_function(crime_11_int)
crime_modal_value_2012 = modal_value_function(crime_12_int)
crime_modal_value_2013 = modal_value_function(crime_13_int)
crime_modal_value_2014 = modal_value_function(crime_14_int)

#Varianz der Crime-Rate pro Jahr berechnen
crime_variance_2010 = variance_function(crime_10)
crime_variance_2011 = variance_function(crime_11)
crime_variance_2012 = variance_function(crime_12)
crime_variance_2013 = variance_function(crime_13)
crime_variance_2014 = variance_function(crime_14)

#Standardabweichung der Crime-Rate pro Jahr berechnen
crime_standard_devitation_2010 = standard_deviation_function(crime_10)
crime_standard_devitation_2011 = standard_deviation_function(crime_11)
crime_standard_devitation_2012 = standard_deviation_function(crime_12)
crime_standard_devitation_2013 = standard_deviation_function(crime_13)
crime_standard_devitation_2014 = standard_deviation_function(crime_14)

#Spannweite der Crime-Rate pro Jahr berechnen
crime_span_2010 = span_function(crime_10)
crime_span_2011 = span_function(crime_11)
crime_span_2012 = span_function(crime_12)
crime_span_2013 = span_function(crime_13)
crime_span_2014 = span_function(crime_14)

#Prozentzahl, wie viele Bezirke unter Wert 50 der Crime-Rate pro Jahr liegen, berechnen
crime_percent_list_50_2010 = percent_list_50_function(crime_10)
crime_percent_list_50_2011 = percent_list_50_function(crime_11)
crime_percent_list_50_2012 = percent_list_50_function(crime_12)
crime_percent_list_50_2013 = percent_list_50_function(crime_13)
crime_percent_list_50_2014 = percent_list_50_function(crime_14)

#Violence-Rate pro Jahr berechnen
violence_average_2011 = average_function(viol_11)
violence_average_2012 = average_function(viol_12)
violence_average_2013 = average_function(viol_13)
violence_average_2014 = average_function(viol_14)

#Property-Crime-Rate pro Jahr berechnen
property_average_2011 = average_function(prop_11)
property_average_2012 = average_function(prop_12)
property_average_2013 = average_function(prop_13)
property_average_2014 = average_function(prop_14)

#Domestic-Violence-Rate pro Jahr berechnen
domestic_average_2011 = average_function(domvio_11)
domestic_average_2012 = average_function(domvio_12)

#Gun-Homicide-Rate pro Jahr berechnen
gun_average_2011 = average_function(gunhom_11)
gun_average_2012 = average_function(gunhom_12)
gun_average_2013 = average_function(gunhom_13)
gun_average_2014 = average_function(gunhom_14)


"""
#Im Folgenden werden die Diagramme erstellt
"""
import numpy as np
#Seaborn installieren in cmd per "pip install seaborn"
import seaborn as sns
import matplotlib.pyplot as plt

#Figur 1: Diagramm Durchschnitt Verbrechenquotient der Jahre 2010-2014 in Baltimore absolut (x-Achse: Jahre)
#Diagramm anlegen
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

#X-Labels und Werte definieren
x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_average_2010, crime_average_2011, crime_average_2012, crime_average_2013, crime_average_2014]

#Diagramm generieren
x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Verbrechensrate")
ax.xaxis.set_label_position("top")

#Endeinstellungen
sns.despine(bottom=True)
plt.tight_layout()


#Figur 2: Diagramm Top 10 Verbrechen in 2010 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_top_10_2010[1], crime_top_10_2010[3], crime_top_10_2010[5], crime_top_10_2010[7], crime_top_10_2010[9], crime_top_10_2010[11], crime_top_10_2010[13], crime_top_10_2010[15], crime_top_10_2010[17], crime_top_10_2010[19]]
x_values = [crime_top_10_2010[0], crime_top_10_2010[2], crime_top_10_2010[4], crime_top_10_2010[6], crime_top_10_2010[8], crime_top_10_2010[10], crime_top_10_2010[12], crime_top_10_2010[14], crime_top_10_2010[16], crime_top_10_2010[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000"])
ax.set_xlabel("Baltimore - Top 10 Verbrechen 2010")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 3: Diagramm Top 10 Verbrechen in 2012 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_top_10_2012[1], crime_top_10_2012[3], crime_top_10_2012[5], crime_top_10_2012[7], crime_top_10_2012[9], crime_top_10_2012[11], crime_top_10_2012[13], crime_top_10_2012[15], crime_top_10_2012[17], crime_top_10_2012[19]]
x_values = [crime_top_10_2012[0], crime_top_10_2012[2], crime_top_10_2012[4], crime_top_10_2012[6], crime_top_10_2012[8], crime_top_10_2012[10], crime_top_10_2012[12], crime_top_10_2012[14], crime_top_10_2012[16], crime_top_10_2012[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF0000"])
ax.set_xlabel("Baltimore - Top 10 Verbrechen 2012")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 4: Diagramm Top 10 Verbrechen in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_top_10_2014[1], crime_top_10_2014[3], crime_top_10_2014[5], crime_top_10_2014[7], crime_top_10_2014[9], crime_top_10_2014[11], crime_top_10_2014[13], crime_top_10_2014[15], crime_top_10_2014[17], crime_top_10_2014[19]]
x_values = [crime_top_10_2014[0], crime_top_10_2014[2], crime_top_10_2014[4], crime_top_10_2014[6], crime_top_10_2014[8], crime_top_10_2014[10], crime_top_10_2014[12], crime_top_10_2014[14], crime_top_10_2014[16], crime_top_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF6666"])
ax.set_xlabel("Baltimore - Top 10 Verbrechen 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 5: Diagramm Flop 10 Verbrechen in 2010 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_flop_10_2010[1], crime_flop_10_2010[3], crime_flop_10_2010[5], crime_flop_10_2010[7], crime_flop_10_2010[9], crime_flop_10_2010[11], crime_flop_10_2010[13], crime_flop_10_2010[15], crime_flop_10_2010[17], crime_flop_10_2010[19]]
x_values = [crime_flop_10_2010[0], crime_flop_10_2010[2], crime_flop_10_2010[4], crime_flop_10_2010[6], crime_flop_10_2010[8], crime_flop_10_2010[10], crime_flop_10_2010[12], crime_flop_10_2010[14], crime_flop_10_2010[16], crime_flop_10_2010[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000"])
ax.set_xlabel("Baltimore - Flop 10 Verbrechen 2010")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 6: Diagramm Flop 10 Verbrechen in 2012 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_flop_10_2012[1], crime_flop_10_2012[3], crime_flop_10_2012[5], crime_flop_10_2012[7], crime_flop_10_2012[9], crime_flop_10_2012[11], crime_flop_10_2012[13], crime_flop_10_2012[15], crime_flop_10_2012[17], crime_flop_10_2012[19]]
x_values = [crime_flop_10_2012[0], crime_flop_10_2012[2], crime_flop_10_2012[4], crime_flop_10_2012[6], crime_flop_10_2012[8], crime_flop_10_2012[10], crime_flop_10_2012[12], crime_flop_10_2012[14], crime_flop_10_2012[16], crime_flop_10_2012[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF0000"])
ax.set_xlabel("Baltimore - Flop 10 Verbrechen 2012")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 7: Diagramm Flop 10 Verbrechen in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_flop_10_2014[1], crime_flop_10_2014[3], crime_flop_10_2014[5], crime_flop_10_2014[7], crime_flop_10_2014[9], crime_flop_10_2014[11], crime_flop_10_2014[13], crime_flop_10_2014[15], crime_flop_10_2014[17], crime_flop_10_2014[19]]
x_values = [crime_flop_10_2014[0], crime_flop_10_2014[2], crime_flop_10_2014[4], crime_flop_10_2014[6], crime_flop_10_2014[8], crime_flop_10_2014[10], crime_flop_10_2014[12], crime_flop_10_2014[14], crime_flop_10_2014[16], crime_flop_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF6666"])
ax.set_xlabel("Baltimore - Flop 10 Verbrechen 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 8: Diagramm Top 1 Verbrechen von 2010 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_top_1[0], crime_top_1[1], crime_top_1[2], crime_top_1[3], crime_top_1[4]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Veraenderung von Top-Verbrechen ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 9: Diagramm Flop 1 Verbrechen von 2010 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_flop_1[0], crime_flop_1[1], crime_flop_1[2], crime_flop_1[3], crime_flop_1[4]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Veraenderung von Flop-Verbrechen ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 10: Diagramm Top 10 Gewalt in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [viol_top_10_2014[1], viol_top_10_2014[3], viol_top_10_2014[5], viol_top_10_2014[7], viol_top_10_2014[9], viol_top_10_2014[11], viol_top_10_2014[13], viol_top_10_2014[15], viol_top_10_2014[17], viol_top_10_2014[19]]
x_values = [viol_top_10_2014[0], viol_top_10_2014[2], viol_top_10_2014[4], viol_top_10_2014[6], viol_top_10_2014[8], viol_top_10_2014[10], viol_top_10_2014[12], viol_top_10_2014[14], viol_top_10_2014[16], viol_top_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#6666FF"])
ax.set_xlabel("Baltimore - Top 10 Gewaltdelikt 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 11: Diagramm Flop 10 Gewalt in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [viol_flop_10_2014[1], viol_flop_10_2014[3], viol_flop_10_2014[5], viol_flop_10_2014[7], viol_flop_10_2014[9], viol_flop_10_2014[11], viol_flop_10_2014[13], viol_flop_10_2014[15], viol_flop_10_2014[17], viol_flop_10_2014[19]]
x_values = [viol_flop_10_2014[0], viol_flop_10_2014[2], viol_flop_10_2014[4], viol_flop_10_2014[6], viol_flop_10_2014[8], viol_flop_10_2014[10], viol_flop_10_2014[12], viol_flop_10_2014[14], viol_flop_10_2014[16], viol_flop_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#6666FF"])
ax.set_xlabel("Baltimore - Flop 10 Gewaltdelikt 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 12: Diagramm Top 1 Gewalt von 2010 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [viol_top_1[0], viol_top_1[1], viol_top_1[2], viol_top_1[3], viol_top_1[4]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#0000CD", "#0000E6", "#0000FF", "#3333FF", "#6666FF"])
ax.set_xlabel("Baltimore - Veraenderung von Top-Gewaltdelikt ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 13: Diagramm Flop 1 Gewalt von 2010 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [viol_flop_1[0], viol_flop_1[1], viol_flop_1[2], viol_flop_1[3], viol_flop_1[4]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#0000CD", "#0000E6", "#0000FF", "#3333FF", "#6666FF"])
ax.set_xlabel("Baltimore - Veraenderung von Flop-Gewaltdelikt ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 14: Diagramm Top 10 Diebstahl in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [prop_top_10_2014[1], prop_top_10_2014[3], prop_top_10_2014[5], prop_top_10_2014[7], prop_top_10_2014[9], prop_top_10_2014[11], prop_top_10_2014[13], prop_top_10_2014[15], prop_top_10_2014[17], prop_top_10_2014[19]]
x_values = [prop_top_10_2014[0], prop_top_10_2014[2], prop_top_10_2014[4], prop_top_10_2014[6], prop_top_10_2014[8], prop_top_10_2014[10], prop_top_10_2014[12], prop_top_10_2014[14], prop_top_10_2014[16], prop_top_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#66FF66"])
ax.set_xlabel("Baltimore - Top 10 Diebstahl 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 15: Diagramm Flop 10 Diebstahl in 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [prop_flop_10_2014[1], prop_flop_10_2014[3], prop_flop_10_2014[5], prop_flop_10_2014[7], prop_flop_10_2014[9], prop_flop_10_2014[11], prop_flop_10_2014[13], prop_flop_10_2014[15], prop_flop_10_2014[17], prop_flop_10_2014[19]]
x_values = [prop_flop_10_2014[0], prop_flop_10_2014[2], prop_flop_10_2014[4], prop_flop_10_2014[6], prop_flop_10_2014[8], prop_flop_10_2014[10], prop_flop_10_2014[12], prop_flop_10_2014[14], prop_flop_10_2014[16], prop_flop_10_2014[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#66FF66"])
ax.set_xlabel("Baltimore - Flop 10 Diebstahl 2014")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 16: Diagramm Top 1 Diebstahl von 2011 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2011", "2012", "2013", "2014"]
x_values = [viol_top_1[0], viol_top_1[1], viol_top_1[2], viol_top_1[3]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#00E600", "#00FF00", "#33FF33", "#66FF66"])
ax.set_xlabel("Baltimore - Veraenderung von Top-Diebstahl ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 17: Diagramm Flop 1 Diebstahl von 2011 bis 2014 (x-Achse: Jahre)
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2011", "2012", "2013", "2014"]
x_values = [viol_flop_1[0], viol_flop_1[1], viol_flop_1[2], viol_flop_1[3]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#00E600", "#00FF00", "#33FF33", "#66FF66"])
ax.set_xlabel("Baltimore - Veraenderung von Flop-Diebstahl ueber die Jahre")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 18: Diagramm Top 10 Wie oft sind die Verbrechenswerte (übergreifend) über die Jahre gestiegen im Vergleich zu vorher? (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_rise_top_10[1], crime_rise_top_10[3], crime_rise_top_10[5], crime_rise_top_10[7], crime_rise_top_10[9], crime_rise_top_10[11], crime_rise_top_10[13], crime_rise_top_10[15], crime_rise_top_10[17], crime_rise_top_10[19]]
x_values = [crime_rise_top_10[0], crime_rise_top_10[2], crime_rise_top_10[4], crime_rise_top_10[6], crime_rise_top_10[8], crime_rise_top_10[10], crime_rise_top_10[12], crime_rise_top_10[14], crime_rise_top_10[16], crime_rise_top_10[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF0000"])
ax.set_xlabel("Baltimore - Top 10 gestiegene Verbrechenswerte pro Jahr")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 19: Diagramm Top 10 Wie oft sind die Verbrechenswerte (übergreifend) über die Jahre gefallen im Vergleich zu vorher? (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_drop_top_10[1], crime_drop_top_10[3], crime_drop_top_10[5], crime_drop_top_10[7], crime_drop_top_10[9], crime_drop_top_10[11], crime_drop_top_10[13], crime_drop_top_10[15], crime_drop_top_10[17], crime_drop_top_10[19]]
x_values = [crime_drop_top_10[0], crime_drop_top_10[2], crime_drop_top_10[4], crime_drop_top_10[6], crime_drop_top_10[8], crime_drop_top_10[10], crime_drop_top_10[12], crime_drop_top_10[14], crime_drop_top_10[16], crime_drop_top_10[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF0000"])
ax.set_xlabel("Baltimore - Top 10 gesunkene Verbrechenswerte pro Jahr")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 20: Diagramm Top 10 Prozentuale Steigerung des Verbrechensquotients aus dem Jahre 2010 im Vergleich zum Jahre 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_percentage_change_rise_top_10[1], crime_percentage_change_rise_top_10[3], crime_percentage_change_rise_top_10[5], crime_percentage_change_rise_top_10[7], crime_percentage_change_rise_top_10[9], crime_percentage_change_rise_top_10[11], crime_percentage_change_rise_top_10[13], crime_percentage_change_rise_top_10[15], crime_percentage_change_rise_top_10[17], crime_percentage_change_rise_top_10[19]]
x_values = [crime_percentage_change_rise_top_10[0], crime_percentage_change_rise_top_10[2], crime_percentage_change_rise_top_10[4], crime_percentage_change_rise_top_10[6], crime_percentage_change_rise_top_10[8], crime_percentage_change_rise_top_10[10], crime_percentage_change_rise_top_10[12], crime_percentage_change_rise_top_10[14], crime_percentage_change_rise_top_10[16], crime_percentage_change_rise_top_10[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF0000"])
ax.set_xlabel("Baltimore - Top 10 prozentuale Steigerung")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 21: Diagramm Top 10 Prozentuale Senkung des Verbrechensquotients aus dem Jahre 2010 im Vergleich zum Jahre 2014 (x-Achse: Bezirke)
f, ax = plt.subplots(1, 1, figsize=(12, 6))

x_labels = [crime_percentage_change_drop_top_10[1], crime_percentage_change_drop_top_10[3], crime_percentage_change_drop_top_10[5], crime_percentage_change_drop_top_10[7], crime_percentage_change_drop_top_10[9], crime_percentage_change_drop_top_10[11], crime_percentage_change_drop_top_10[13], crime_percentage_change_drop_top_10[15], crime_percentage_change_drop_top_10[17], crime_percentage_change_drop_top_10[19]]
x_values = [crime_percentage_change_drop_top_10[0], crime_percentage_change_drop_top_10[2], crime_percentage_change_drop_top_10[4], crime_percentage_change_drop_top_10[6], crime_percentage_change_drop_top_10[8], crime_percentage_change_drop_top_10[10], crime_percentage_change_drop_top_10[12], crime_percentage_change_drop_top_10[14], crime_percentage_change_drop_top_10[16], crime_percentage_change_drop_top_10[18]]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#FF0000"])
ax.set_xlabel("Baltimore - Top 10 prozentuale Senkung")
ax.xaxis.set_label_position("top")
ax.set_xticklabels(x_labels, fontsize = 10)

sns.despine(bottom=True)
plt.xticks(rotation= 14)


#Figur 22: Median Verbrechenquotient der Jahre 2010-2014 (x-Achse: Jahre)
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_median_2010, crime_median_2011, crime_median_2012, crime_median_2013, crime_median_2014]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Median der Verbrechensrate")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 23: Modalwert Verbrechenquotient der Jahre 2010-2014 (x-Achse: Jahre)
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_modal_value_2010, crime_modal_value_2011, crime_modal_value_2012, crime_modal_value_2013, crime_modal_value_2014]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Modalwert der Verbrechensrate")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 24: Varianz Verbrechenquotient der Jahre 2010-2014 (x-Achse: Jahre)
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_variance_2010, crime_variance_2011, crime_variance_2012, crime_variance_2013, crime_variance_2014]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Varianz der Verbrechensrate")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 25: Standardabweichung Verbrechenquotient der Jahre 2010-2014 (x-Achse: Jahre)
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_standard_devitation_2010, crime_standard_devitation_2011, crime_standard_devitation_2012, crime_standard_devitation_2013, crime_standard_devitation_2014]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Standardabweichung der Verbrechensrate")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 26: Spannweite Verbrechenquotient der Jahre 2010-2014 (x-Achse: Jahre)
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_span_2010, crime_span_2011, crime_span_2012, crime_span_2013, crime_span_2014]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Spannweite der Verbrechensrate")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 27: Bei wie viel Prozent der Bezirke liegt die Kriminalitätsrate unter dem Wert "50" bei den Jahren 2010-2014? (x-Achse: Jahre)
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

x_labels = ["2010", "2011", "2012", "2013", "2014"]
x_values = [crime_percent_list_50_2010, crime_percent_list_50_2011, crime_percent_list_50_2012, crime_percent_list_50_2013, crime_percent_list_50_2014]

x_values_arr = np.array(x_values)
sns.barplot(x_labels, x_values_arr, palette = ["#CD0000", "#E60000", "#FF0000", "#FF3333", "#FF6666"])
ax.set_xlabel("Baltimore - Prozentzahl Bezirke unter Wert 50 der Verbrechensrate")
ax.xaxis.set_label_position("top")

sns.despine(bottom=True)
plt.tight_layout()


#Figur 28: Liniendiagramm Downtown ("gefährlichster" Bezirk) Auswertung 2011-2014: crime (Verbrechen), viol (Gewalt), prop (Diebstahl), domvio (Häusliche Gewalt), gunhom (Schusswaffentötung): Wie hat es sich verändert, gibt es Auffälligkeiten?
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

gunhom_labels = ["2011", "2012", "2013", "2014"]
gunhom_values = [gunhom_11[13], gunhom_12[13], gunhom_13[13], gunhom_14[13]]
gunhom_labels_arr = np.array(gunhom_labels)
gunhom_values_arr = np.array(gunhom_values)

prop_labels = ["2011", "2012", "2013", "2014"]
prop_values = [prop_11[13], prop_12[13], prop_13[13], prop_14[13]]
prop_labels_arr = np.array(prop_labels)
prop_values_arr = np.array(prop_values)

viol_labels = ["2011", "2012", "2013", "2014"]
viol_values = [viol_11[13], viol_12[13], viol_13[13], viol_14[13]]
viol_labels_arr = np.array(viol_labels)
viol_values_arr = np.array(viol_values)

domvio_labels = ["2011", "2012"]
domvio_values = [domvio_11[13], domvio_12[13]]
domvio_labels_arr = np.array(domvio_labels)
domvio_values_arr = np.array(domvio_values)

crime_labels = ["2011", "2012", "2013", "2014"]
crime_values = [crime_11[13], crime_12[13], crime_13[13], crime_14[13]]
crime_labels_arr = np.array(crime_labels)
crime_values_arr = np.array(crime_values)

sns.pointplot(gunhom_labels_arr, gunhom_values_arr, color = "#FF00FF")
sns.pointplot(prop_labels_arr, prop_values_arr, color = "#00FF00")
sns.pointplot(viol_labels_arr, viol_values_arr, color = "#0000FF")
sns.pointplot(domvio_labels_arr, domvio_values_arr, color = "#FFC800")
sns.pointplot(crime_labels_arr, crime_values_arr, color = "#FF0000")
ax.set_xlabel("Baltimore Downtown - gefaehrlichster Bezirk - Entwicklung")
ax.xaxis.set_label_position("top")

sns.despine()
plt.tight_layout()


#Figur 29: Liniendiagramm Cross-Country ("sicherster" Bezirk) Auswertung 2011-2014: crime (Verbrechen), viol (Gewalt), prop (Diebstahl), domvio (Häusliche Gewalt), gunhom (Schusswaffentötung): Wie hat es sich verändert, gibt es Auffälligkeiten?
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

gunhom_labels = ["2011", "2012", "2013", "2014"]
gunhom_values = [gunhom_11[10], gunhom_12[10], gunhom_13[10], gunhom_14[10]]
gunhom_labels_arr = np.array(gunhom_labels)
gunhom_values_arr = np.array(gunhom_values)

prop_labels = ["2011", "2012", "2013", "2014"]
prop_values = [prop_11[10], prop_12[10], prop_13[10], prop_14[10]]
prop_labels_arr = np.array(prop_labels)
prop_values_arr = np.array(prop_values)

viol_labels = ["2011", "2012", "2013", "2014"]
viol_values = [viol_11[10], viol_12[10], viol_13[10], viol_14[10]]
viol_labels_arr = np.array(viol_labels)
viol_values_arr = np.array(viol_values)

domvio_labels = ["2011", "2012"]
domvio_values = [domvio_11[10], domvio_12[10]]
domvio_labels_arr = np.array(domvio_labels)
domvio_values_arr = np.array(domvio_values)

crime_labels = ["2011", "2012", "2013", "2014"]
crime_values = [crime_11[10], crime_12[10], crime_13[10], crime_14[10]]
crime_labels_arr = np.array(crime_labels)
crime_values_arr = np.array(crime_values)

sns.pointplot(gunhom_labels_arr, gunhom_values_arr, color = "#FF00FF")
sns.pointplot(prop_labels_arr, prop_values_arr, color = "#00FF00")
sns.pointplot(viol_labels_arr, viol_values_arr, color = "#0000FF")
sns.pointplot(domvio_labels_arr, domvio_values_arr, color = "#FFC800")
sns.pointplot(crime_labels_arr, crime_values_arr, color = "#FF0000")
ax.set_xlabel("Baltimore Cross-Country - sicherster Bezirk - Entwicklung")
ax.xaxis.set_label_position("top")

sns.despine()
plt.tight_layout()


#Figur 30: Liniendiagramm Baltimore über Jahre 2011-2014: Durchschnittswerte crime, viol, prop, domvio, gunhom: Was hat sich wie stark verändert?
sns.set(style="white", context="talk")
f, ax = plt.subplots(1, 1, figsize=(8, 6))

gunhom_labels = ["2011", "2012", "2013", "2014"]
gunhom_values = [gun_average_2011, gun_average_2012, gun_average_2013, gun_average_2014]
gunhom_labels_arr = np.array(gunhom_labels)
gunhom_values_arr = np.array(gunhom_values)

prop_labels = ["2011", "2012", "2013", "2014"]
prop_values = [property_average_2011, property_average_2012, property_average_2013, property_average_2014]
prop_labels_arr = np.array(prop_labels)
prop_values_arr = np.array(prop_values)

viol_labels = ["2011", "2012", "2013", "2014"]
viol_values = [violence_average_2011, violence_average_2012, violence_average_2013, violence_average_2014]
viol_labels_arr = np.array(viol_labels)
viol_values_arr = np.array(viol_values)

domvio_labels = ["2011", "2012"]
domvio_values = [domestic_average_2011, domestic_average_2012]
domvio_labels_arr = np.array(domvio_labels)
domvio_values_arr = np.array(domvio_values)

crime_labels = ["2011", "2012", "2013", "2014"]
crime_values = [crime_average_2011, crime_average_2012, crime_average_2013, crime_average_2014]
crime_labels_arr = np.array(crime_labels)
crime_values_arr = np.array(crime_values)

sns.pointplot(gunhom_labels_arr, gunhom_values_arr, color = "#FF00FF")
sns.pointplot(prop_labels_arr, prop_values_arr, color = "#00FF00")
sns.pointplot(viol_labels_arr, viol_values_arr, color = "#0000FF")
sns.pointplot(domvio_labels_arr, domvio_values_arr, color = "#FFC800")
sns.pointplot(crime_labels_arr, crime_values_arr, color = "#FF0000")
ax.set_xlabel("Baltimore - Entwicklung ueber die Jahre hinweg")
ax.xaxis.set_label_position("top")

sns.despine()
plt.tight_layout()



plt.show()

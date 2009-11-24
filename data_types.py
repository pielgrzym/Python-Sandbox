#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint

# podstawowe typy:
# int
nasz_int = 33

# float
nasz_float = 0.33333

# boolean
nasz_bool = True
nie_nasz_bool = False

# string
nasz_string = "Jestem fajnym stringiem, zaskakujące, co?"
pprint(nasz_string) # nasz string jest w utf-8 - zwróć uwagę na krzaka
trzecia_litera_stringa = nasz_string[2] # trzecia, bo liczymy od 0
pprint(trzecia_litera_stringa)
ostatnie_trzy_litery = nasz_string[-3:]
pprint(ostatnie_trzy_litery)
od_trzeciej_do_osmej = nasz_string[3:8]
pprint(od_trzeciej_do_osmej)

wielo_linijkowy_string = """Hej ho
to też będzie
sensowny string.
Taki bajer się strasznie przydaje przy
zagnieżdżaniu np. SQL w zmiennej,
ponieważ można ją swobodnie formatować,
dopóki nie natrafimy na 3 x cudzysłów. """

imie = "Przemek"
string_z_podstawieniami = "Witaj %s, zmienna \"Nasz int\" to %d" % (imie, nasz_int)
print "string_z_podstawieniami:\n", string_z_podstawieniami

# sklejanie stringów
print nasz_string[:-3]+imie+"?"

# typowe błędy:
# próba sumowania nie pasujących do siebie typów:
# print nasz_float+nasz_int

# rzutowanie

string_jak_liczba = "5"
liczba_ze_stringa = int(string_jak_liczba)

##########################
# Złożone typy danych
##########################

# listy
lista_pierwsza = [ "element pierwszy", "element drugi", "element trzeci" ]
print "lista_pierwsza[0] =", lista_pierwsza[0]
print "lista_pierwsza[1] =", lista_pierwsza[1]
print "lista_pierwsza[2] =", lista_pierwsza[2]

lista_druga = [ lista_pierwsza, nasz_string, "dupa" ]

print "Zagnieżdżona lista - element trzeci:", lista_druga[0][2]
print "A tak wygląda jej reprezentacja w konsolce: ", pprint(lista_druga[0])

podlista = lista_pierwsza[1:3] # zwróć uwagę - nie ma elementu o indeksie 3!
print "Podlista z drugim i trzecim elementem listy pierwszej: ", pprint(podlista)

# dodawanie elementów do listy
# dodawanie na koniec

podlista.append("banan")
print "Podlista z nowym elementem (append): ",pprint(podlista)

podlista.extend(lista_pierwsza)
print "Podlista rozszerzona o listę \"lista_pierwsza\" (append): ",pprint(podlista)

podlista.remove("banan")
podlista.pop()


# tuple

# tupla to specyficzny rodzaj listy, jedyna różnica polega na tym,
# że po stworzeniu tupli NIE DA SIĘ JEJ ZMODYFIKOWAĆ

tupla = ("element 1", "element 2", "element 3")
# próba modyfikacji zwróci błąd:
# tupla[1] = "dupa" 

# zarówno w listach jak i w słownikach kolejność dodawanych elementów jest
# zawsze zachowywana!

# słowniki

slownik_pierwszy = {"jeden": "Tu siedzi jeden", "dwa": "Tu siedzi dwóch",
                    "trzy": "Tu siedzi trzech", }

pprint(slownik_pierwszy)
print slownik_pierwszy["dwa"]
print slownik_pierwszy["trzy"]
# klucze w słowniku są case sensitive - czyli klucz != Klucz

# nic nie stoi na przeszkodzie, żeby klucze były różnych typów:

powalony_slownik = { 2483: "Ale wał",
                    3.2: "No niezłą dupa",
                    "baton": 398438943.0, }

print powalony_slownik[3.2]

# UWAGA! W słownikach kolejność kluczy jest LOSOWA. Dzięki temu są szybkie, ale
# klucze nie są w takiej samej kolejności jak były deklarowane

slownik_udajacy_liste = {0:"element pierwszy",
                         1:"element drugi",
                         2:"element trzeci", }

print "slownik_udajacy_liste[1] =",slownik_udajacy_liste[1]

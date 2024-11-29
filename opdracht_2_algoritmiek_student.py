#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment: algoritmiek

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""
import sys
import inspect

naam = "Zulal"
klas = "V1C"
studentnummer = 1834618-1

"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die deze
        lijst aanneemt bij álle tussenstappen bij toepassing van
        bovenstaand sorteeralgoritme.
"""
def bubble_sort(lst):
    # Stap 1: Doorloop de lijst totdat er geen wisselingen meer nodig zijn
    n = len(lst)
    steps = []  # Om tussenstappen bij te houden

    while True:
        swapped = False  # Houd bij of er wisselingen zijn gemaakt in deze ronde

        for i in range(n - 1):  # Vergelijk elk paar naast elkaar
            if lst[i] > lst[i + 1]:  # Als het eerste element groter is dan het tweede
                # Wissel ze om
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True  # Er is een wisseling gemaakt

        # Voeg de huidige staat van de lijst toe aan de tussenstappen
        steps.append(lst[:])  # [:] maakt een kopie van de lijst

        if not swapped:  # Als er geen wisselingen meer zijn, is de lijst gesorteerd
            break

    return steps  # Geef alle tussenstappen terug


"""

    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie
        hieronder genaamd my_sort(lst).
        Let op: je *moet* de pseudocode volgen!
"""

def my_sort(lst):
    """
    Sorteer een lijst volgens het Bubble Sort-algoritme en retourneer een nieuwe, gesorteerde lijst.
    """
    lst_sorted = lst[:]  # Maak een kopie van de lijst zodat het origineel behouden blijft.
    while True:
        swapped = False
        for i in range(len(lst_sorted) - 1):
            if lst_sorted[i] > lst_sorted[i + 1]:  # Vergelijk buur-elementen.
                lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]  # Wissel.
                swapped = True
        if not swapped:  # Als er geen wisselingen zijn, is de lijst gesorteerd.
            break
    return lst_sorted


def my_sort_2(lst):
    """
    Sorteer een lijst volgens de frequentietabel-methode en retourneer een nieuwe, gesorteerde lijst.
    """
    if not lst:
        return []  # Retourneer een lege lijst als de invoer leeg is.

    # Stap 1 en 2: Maak een lijst van lengtes gebaseerd op het maximale element.
    max_value = max(lst)
    frequency = [0] * (max_value + 1)

    # Stap 3: Tel frequenties van elementen in de originele lijst.
    for num in lst:
        frequency[num] += 1

    # Stap 5: Maak de gesorteerde lijst op basis van de frequenties.
    sorted_lst = []
    for num, count in enumerate(frequency):
        sorted_lst.extend([num] * count)

    return sorted_lst



"""
    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke
            volgorde van de waarden in de lijst is het sorteeralgoritme
            het snelste klaar (best-case scenario)?
            Hoeveel vergelijkingen (zoals beschreven in stap 1. van de
            pseudocode) zijn nodig geweest?
"""
# Best-case scenario:
# De lijst is al gesorteerd: [1, 2, 3].
# Het algoritme doorloopt de lijst één keer en voert 2 vergelijkingen uit.
# Antwoord: Best-case volgorde = [1, 2, 3], Aantal vergelijkingen = 2
"""


        -   Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het minst snel klaar (worst-case scenario)?
            Hoeveel vergelijkingen zijn nodig geweest?
"""
# Worst-case scenario:
# De lijst staat in omgekeerde volgorde: [3, 2, 1].
# Het algoritme voert 3 vergelijkingen uit in de eerste ronde,
# en 2 vergelijkingen in de tweede ronde. Totaal: 3 + 2 = 5.
# Antwoord: Worst-case volgorde = [3, 2, 1], Aantal vergelijkingen = 5
"""


        -   Stel je hebt een lijst met de waarden 1 tot en met 4.
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
# Best-case scenario:
# De lijst is al gesorteerd: [1, 2, 3, 4].
# Het algoritme doorloopt de lijst één keer en voert 3 vergelijkingen uit.
# Antwoord: Best-case volgorde = [1, 2, 3, 4], Aantal vergelijkingen = 3

# Worst-case scenario:
# De lijst staat in omgekeerde volgorde: [4, 3, 2, 1].
# Het algoritme voert 4 + 3 + 2 + 1 = 10 vergelijkingen uit.
# Antwoord: Worst-case volgorde = [4, 3, 2, 1], Aantal vergelijkingen = 10

# De antwoorden hieronder zijn berekend met een implementatie van Bubble Sort.
# Zie onderstaande code voor details (optioneel).


def bubble_sort_analysis(lst):
    """
    Voert Bubble Sort uit op een lijst en telt het aantal vergelijkingen.

    Args:
        lst (list): De lijst die gesorteerd moet worden.

    Returns:
        tuple: Gesorteerde lijst en het aantal vergelijkingen.
    """
    lst_sorted = lst[:]  # Maak een kopie van de lijst om de originele te behouden
    n = len(lst)
    comparisons = 0  # Tel het aantal vergelijkingen

    while True:
        swapped = False
        for i in range(n - 1):
            comparisons += 1  # Tel elke vergelijking
            if lst_sorted[i] > lst_sorted[i + 1]:
                # Wissel elementen als het huidige groter is dan het volgende
                lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                swapped = True
        if not swapped:  # Stop als er geen wisselingen zijn
            break

    return lst_sorted, comparisons


# Analyse van best- en worst-case scenario's

# Voor 3 elementen
best_case_3 = [1, 2, 3]  # Al gesorteerd (best-case scenario)
worst_case_3 = [3, 2, 1]  # Omgekeerd gesorteerd (worst-case scenario)

sorted_best_3, comparisons_best_3 = bubble_sort_analysis(best_case_3)
sorted_worst_3, comparisons_worst_3 = bubble_sort_analysis(worst_case_3)

print("Best-case (3 elementen):")
print(f"Lijst: {best_case_3}, Vergelijkingen: {comparisons_best_3}")
print("Worst-case (3 elementen):")
print(f"Lijst: {worst_case_3}, Vergelijkingen: {comparisons_worst_3}")

# Voor 4 elementen
best_case_4 = [1, 2, 3, 4]  # Al gesorteerd (best-case scenario)
worst_case_4 = [4, 3, 2, 1]  # Omgekeerd gesorteerd (worst-case scenario)

sorted_best_4, comparisons_best_4 = bubble_sort_analysis(best_case_4)
sorted_worst_4, comparisons_worst_4 = bubble_sort_analysis(worst_case_4)

print("\nBest-case (4 elementen):")
print(f"Lijst: {best_case_4}, Vergelijkingen: {comparisons_best_4}")
print("Worst-case (4 elementen):")
print(f"Lijst: {worst_case_4}, Vergelijkingen: {comparisons_worst_4}")



"""
2. Linear search recursive
    Implementeer onderstaande functie om element in de gegeven lijst te zoeken door middel van recursief lineair zoeken.
"""


def linear_search_recursive(lst, target):
    """
    Zoek een element in de gegeven lijst door middel van recursief lineair zoeken.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target: Het doel dat gezocht wordt.

    Returns:
        bool: True als het element wordt gevonden, anders False.
    """
    # Basisgeval 1: als de lijst leeg is, zit het element er niet in.
    if not lst:
        return False

    # Basisgeval 2: controleer het eerste element.
    if lst[0] == target:
        return True

    # Recursieve stap: zoek verder in de rest van de lijst.
    return linear_search_recursive(lst[1:], target)

"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_my_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def test_linear_search_recursive():
    for _ in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = linear_search_recursive(lst_test, target)
        assert lst_copy == lst_test, "Fout: linear_search_recursive(lst, target) verandert de inhoud van lijst lst"
        assert outcome == found, \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"


def test_test_linear_search_recursive_recursiveness():
    limit = sys.getrecursionlimit()
    sys.setrecursionlimit(50)
    try:
        linear_search_recursive(list(range(100)), 100)
        assert False, "Fout: linear_search_recursive werkt niet recursief"
    except RecursionError:
        return
    finally:
        sys.setrecursionlimit(limit)


def test_my_sort_2():
    lst_test = [random.choice(range(10)) for _ in range(10)]
    lst_copy = lst_test.copy()
    lst_output = my_sort_2(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort_2(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort_2({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")  # Groene tekstkleur
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        test_test_linear_search_recursive_recursiveness()
        print("Je functie linear_search_recursive() werkt goed!")

        test_my_sort_2()
        print("Je functie test_my_sort_2() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")  # Reset tekstkleur


if __name__ == '__main__':
    __main()

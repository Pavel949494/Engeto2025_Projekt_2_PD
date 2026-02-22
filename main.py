"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Pavel Dostalík
email: pavel.dostalík94@gmail.com
"""


import random
import sys

def python_pozdrav(pozdrav, oddelovac, prvni_radek, druhy_radek):
    """Funkce pro grafické zobrazení úvodního pozdravu, která vizuálně odděluje text od zbytku aplikace.
    Program postupně vypíše zadané řádky a ohraničí je zvoleným oddělovačem pro lepší přehlednost uživatelského rozhraní."""

    print(pozdrav, oddelovac, prvni_radek, druhy_radek, oddelovac, sep = "\n")

def validace_cisla (cislo):
    """Funkce pro kontrolu správného formátu čísla, která ověřuje jeho délku, číselnou hodnotu a unikátnost znaků.
    Program hlídá, aby vstup tvořily čtyři různé číslice, délka byla přesně čtyři a první číslice nebyla nula."""
    
    if cislo.isnumeric() and (cislo)[0] != '0' and len(set(cislo)) == 4:
        vysledek_validace = True
    else: 
        vysledek_validace = False
    return(vysledek_validace)


def vygeneruj_validni_cislo ():
    """Funkce pro automatické generování náhodného čtyřmístného čísla, které splňuje všechna validační kritéria.
    Program v cyklu vytváří náhodné hodnoty a pomocí externí validace kontroluje, zda jsou číslice unikátní a číslo nezačíná nulou."""
    
    gerenovani_validniho_cisla =  True
    while gerenovani_validniho_cisla:
        vygenerovane_cislo = str(random.randint(1000, 9999))
        if validace_cisla (vygenerovane_cislo): 
            gerenovani_validniho_cisla = False
    return (vygenerovane_cislo)

def zadej_validni_cislo ():
    """Funkce pro interaktivní zadání čísla uživatelem, která vynucuje dodržení všech validačních pravidel.
    Program v cyklu čeká na vstup a v případě chyby uživatele upozorní, dokud není zadáno číslo se správnou délkou a unikátními ciframi."""
    
    zadani_validniho_cisla = True
    while zadani_validniho_cisla:
        zadane_cislo = str(input(">>>"))
        if validace_cisla (zadane_cislo) == False: 
            print("Use valid number")
        elif validace_cisla (zadane_cislo): 
            zadani_validniho_cisla = False
    return (zadane_cislo)
        
def shody_vyskytu_cifer(list_vygenerovane_cislo, list_zadane_cislo):
    """Funkce pro zjištění celkového počtu shodných cifer mezi dvěma seznamy bez ohledu na jejich pozici.
    Program prochází vygenerované číslo a u každé nalezené shody navýší počítadlo, přičemž použitou cifru ze seznamu odstraní pro zamezení duplicitního započítání."""

    pocet_shod_vyskytu_cifer = 0  
    for cifra in list_vygenerovane_cislo:
        if cifra in list_zadane_cislo:
            pocet_shod_vyskytu_cifer += 1; 
            list_zadane_cislo.remove(cifra)    
    return(pocet_shod_vyskytu_cifer)

def kontrola_pozice_cifer(vygenerovane_cislo, zadane_cislo):
    """Funkce pro zjištění počtu cifer, které se shodují v hodnotě i v přesném umístění v rámci obou čísel.
    Program pomocí indexů postupně porovnává jednotlivé pozice a v případě naprosté shody navýší celkové počítadlo zásahů."""

    pocet_shod_pozice_cifer = 0
    for i in range(4):
        if zadane_cislo [i] == vygenerovane_cislo [i]: 
            pocet_shod_pozice_cifer += 1
    return pocet_shod_pozice_cifer

def game():
    """Hlavní herní smyčka aplikace Bulls and Cows, která inicializuje hru a spravuje celkovou komunikaci s hráčem.
    Program generuje tajné číslo, v cyklu zpracovává uživatelské tipy, vypočítává počet zásahů a při úspěšném uhodnutí hru ukončí s výpisem statistik."""

    pozdrav ='Hi there!'; oddelovac = 47 * '-'; prvni_radek ="I've generated a random 4 digit number for you."; 
    druhy_radek = "Let's play a bulls and cows game."; oznameni_o_vyhre = "Correct, you've guessed the right number"; 
    konec = "That's amazing!"; pokusy = 0; hra_bezi = True
    python_pozdrav(pozdrav, oddelovac, prvni_radek, druhy_radek)
    vygenerovane_cislo = vygeneruj_validni_cislo ()
    while hra_bezi == True:
        zadane_cislo = zadej_validni_cislo (); pokusy += 1
        list_vygenerovane_cislo = list(vygenerovane_cislo)
        list_zadane_cislo = list(zadane_cislo)
        pocet_shod_pozice_cifer = kontrola_pozice_cifer(vygenerovane_cislo, zadane_cislo)
        if pocet_shod_pozice_cifer == 0 or pocet_shod_pozice_cifer == 1: 
            print(pocet_shod_pozice_cifer, "bulls")
        if pocet_shod_pozice_cifer > 1 and pocet_shod_pozice_cifer < 5: 
            print(pocet_shod_pozice_cifer, "bulls") 
        if pocet_shod_pozice_cifer == 4: 
            print(oznameni_o_vyhre) 
            if pokusy == 1: 
                print("in", pokusy, "guess!")
            elif pokusy > 1: 
                print("in", pokusy, "guesses!")
            print(oddelovac), 
            print(konec)
            sys.exit()
        pocet_shod_vyskytu_cifer = shody_vyskytu_cifer(list_vygenerovane_cislo, list_zadane_cislo) - pocet_shod_pozice_cifer 
        if pocet_shod_pozice_cifer == 4:
            hra_bezi = False 
        elif pocet_shod_vyskytu_cifer == 1:
            print(pocet_shod_vyskytu_cifer, "cow")
        elif pocet_shod_vyskytu_cifer == 0 or pocet_shod_vyskytu_cifer > 1 and pocet_shod_vyskytu_cifer < 5:
            print(pocet_shod_vyskytu_cifer, "cows")          

game()

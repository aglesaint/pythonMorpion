import random
from termcolor import colored

global scoreJoueur
global scoreOrdi
global scoreTotal

def result(dict):
    return dict['a1'] == dict['a4'] == dict['a7'] and dict['a1'] != " " and dict['a4'] != " " and dict['a7'] !=" "  \
            or dict['b2'] == dict['b5'] == dict['b8'] and dict['b2'] != " " and dict['b5'] != " " and dict['b8'] !=" " \
            or dict['c3'] == dict['c6'] == dict['c9'] and dict['c3'] != " " and dict['c6'] != " " and dict['c9'] !=" " \
            or dict['a1'] == dict['b2'] == dict['c3'] and dict['a1'] != " " and dict['b2'] != " " and dict['c3'] !=" " \
            or dict['a4'] == dict['b5'] == dict['c6'] and dict['a4'] != " " and dict['b5'] != " " and dict['c6'] !=" " \
            or dict['a7'] == dict['b8'] == dict['c9'] and dict['a7'] != " " and dict['b8'] != " " and dict['c9'] !=" "  \
            or dict['a1'] == dict['b5'] == dict['c9'] and dict['a1'] != " " and dict['b5'] != " " and dict['c9'] !=" "  \
            or dict['a7'] == dict['b5'] == dict['c3'] and dict['a7'] != " " and dict['b5'] != " " and dict['c3'] !=" "

# un peu d'intelligence artificielle : 8 règles définies
# @Return le choix a1, b2, c3 ....
def IA(dict, pionOrdi, pion, nbPionOnLine):

    # les 8 combinaisons gagnantes
    d1 = {'a1': dict['a1'], 'b2': dict['b2'], 'c3': dict['c3']}
    d2 = {'a4': dict['a4'], 'b5': dict['b5'], 'c6': dict['c6']}
    d3 = {'a7': dict['a7'], 'b8': dict['b8'], 'c9': dict['c9']}
    d4 = {'a1': dict['a1'], 'a4': dict['a4'], 'a7': dict['a7']}
    d5 = {'b2': dict['b2'], 'b5': dict['b5'], 'b8': dict['b8']}
    d6 = {'c3': dict['c3'], 'c6': dict['c6'], 'c9': dict['c9']}
    d7 = {'a1': dict['a1'], 'b5': dict['b5'], 'c9': dict['c9']}
    d8 = {'a7': dict['a7'], 'b5': dict['b5'], 'c3': dict['c3']}

    # 1e coup : vérifier si 2 pions identiques ORDI et gagner
    result = testSiGagne(d1, pionOrdi, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d2, pionOrdi, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d3, pionOrdi, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d4, pionOrdi, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d5, pionOrdi, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d6, pionOrdi, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d7, pionOrdi, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d8, pionOrdi, nbPionOnLine)


    # 2e coup : vérifier si 2 pions identiques JOUEUR et contrer
    if result == "vide":
        result = testSiGagne(d1, pion, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d2, pion, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d3, pion, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d4, pion, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d5, pion, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d6, pion, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d7, pion, nbPionOnLine)
    if result == "vide":
        result = testSiGagne(d8, pion, nbPionOnLine)

    return result



def afficheGrille(dict, j):
    if j == listJoueur[0]:
        color = 'yellow'
    else:
        color = 'blue'

    print(colored("\n- a - b - c -", color) + "\t\t" + colored(" - a - b - c -", 'green'))
    print(colored("| " + dict['a1'] + " | " + dict['b2']  + " | " + dict['c3'] + " |", color) + "\t\t" + colored("| " + 'a1' + " | " + 'b2'  + " | " + 'c3' + " |", 'green'))
    print(colored("-------------", color) + "\t\t" + colored("----------------", 'green'))
    print(colored("| " + dict['a4'] + " | " + dict['b5'] + " | " + dict['c6'] + " |", color) + "\t\t" + colored("| " + 'a4' + " | " + 'b5'  + " | " + 'c6' + " |", 'green'))
    print(colored("-------------", color) + "\t\t" + colored("----------------", 'green'))
    print(colored("| " + dict['a7'] + " | " + dict['b8'] + " | " + dict['c9'] + " |", color) + "\t\t" + colored("| " + 'a7' + " | " + 'b8'  + " | " + 'c9' + " |", 'green'))
    print(colored("-------------", color) + "\t\t" + colored("----------------", 'green'))


def init():
    global joueur
    global listMatriceJoue
    global pion
    global pionOrdi
    global listMatrice
    global listJoueur
    global tabIA


    # les listes
    listJoueur = ['humain', 'ordiMini']
    listMatrice = ['a1', 'a4', 'a7', 'b2', 'b5', 'b8', 'c3', 'c6', 'c9']
    listMatriceJoue = {"a1":" ", "a4":" ", "a7":" ", "b2":" ", "b5":" ", "b8":" ", "c3":" ", "c6":" ", "c9":" "}

    # personnaliser le joueur humain... ou pas
    prenom = input("votre prénom : ")
    if prenom.strip() != "":
        listJoueur[0] = prenom.upper()
    else:
        print("tant pis ! vous serez : {0} ".format(colored(listJoueur[0].upper(), 'yellow')))

    # le choix du pion : X / O
    pion = input("avec quelle lettre souhaitez-vous jouer (X/O) ? ")
    while pion != 'X' and pion != 'O':
        pion = input(colored("PLEASE : avec quelle lettre souhaitez-vous jouer {0} (X/O) ? ".format(listJoueur[0]), 'red'))

    joueur = random.choice(listJoueur)
    print(colored("vous avez choisi : " + pion + " et " + joueur.upper() + " commence à jouer", 'yellow' ))
    if pion == "X": pionOrdi = "O"
    else: pionOrdi = "X"

##  print("==> coups joués{0}".format(str(listMatriceJoue)))
def jouer():
    retry = True
    listJoueOrdi = []
    ## (re)start game if True
    while retry:
        init()
        joueurEnCours = joueur
        coup = 0

        ## play the game
        while coup < 9:
            coup += 1
            if (joueurEnCours == listJoueur[0]):
                choix = input("\n> {0} choisissez une position parmis {1}, jouer coup #{2}".format(listJoueur[0].upper(), str(listMatrice), str(coup)) + " > ")
                while not choix in listMatrice:
                    choix = input(colored("PLEASE : choisissez une position parmis {0}".format(str(listMatrice)) + " > ", 'red'))

                listMatriceJoue[choix] = pion
                joueurPrec = joueurEnCours
                joueurEnCours = listJoueur[1]
            else:
                choix = random.choice(listMatrice)
                ## un peu d'intelligence
                if coup < 2:
                    nbPionOnLine = 1
                else:
                    nbPionOnLine = 2
                newCoup = IA(listMatriceJoue, pionOrdi, pion, nbPionOnLine)

                # on écrase par la suggestion artificielle
                if newCoup != "vide" and newCoup != "":
                    choix = newCoup

                listMatriceJoue[choix] = pionOrdi
                print(colored("\n> "+ listJoueur[1].upper() + " '({})' joue : {}, jouer coup #{}".format(pionOrdi, choix, str(coup)), 'red'))
                if newCoup != "vide" and newCoup != "":
                    print("(suggestion du coup par IA " + newCoup + ")")
                joueurPrec = joueurEnCours
                joueurEnCours = listJoueur[0]

            ## affichage et maj matrice
            listMatrice.remove(choix)
            # pour plus de visibilité on affiche la grille qu'une fois
            if joueurEnCours == listJoueur[0]: afficheGrille(listMatriceJoue, joueurPrec)

            ## on sort de la boucle si True
            res = testResult(listMatriceJoue, joueurPrec)
            if res:
                coup = 10000
            ## retry again ?
            if coup >= 9:
                retry = retryGame(coup)
                if not retry:
                    print(colored("BYE {} - May the fourth ;)".format(listJoueur[0].upper()), 'green'))

# on teste si un coup est gagnant
def testSiGagne(dict, pion, nbPionOnLine):
    cptpion = 0
    pos = "vide"
    for valeur in dict.values():
        if valeur == pion:
            cptpion += 1

    for key, value in dict.items():
        if value == " " and cptpion == nbPionOnLine:
            pos = key

    return pos

# on teste le coup et on affiche le resultat si gagant
def testResult(listMatriceJoue, joueur):
    res = result(listMatriceJoue)

    if res:
        print("====================================")
        print(colored(joueur.upper() + " WINS !!! ", 'yellow'))
        afficheGrille(listMatriceJoue, joueur)
        print("====================================")


    return res

## on rejoue la partie si True
def retryGame(coup):
    if coup == 9 or coup == 10000:
        res = input(colored("GAME OVER", 'green') + " - retry (O/N)? ")
        if res == "O":
            return True
        else:
            return False
        print("====================================")
#================================================================================================

#================================================================================================
jouer()



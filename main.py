"""
Module qui construit une liste de tuples, correspondant au codage d'une chaîne de caractères
"""

#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    C = [s[0]]
    O = [1]
    n = len(s)
    I = []
    compteur = 1
    for k in range(1,n) :
        if s[k] == s[k-1] :
            O[-1]+=1
        else :
            I.append((C[-1],O[-1]))
            C.append(s[k])
            O.append(1)
    I.append((C[-1],O[-1]))
    return I


def artcode_r(s):
    """
    retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    lettre1 = s[0]
    compteur = 0
    n = len(s)
    while compteur < n and s[0] == lettre1 :# compte le nbre d'occurences du premier caractère
        compteur+=1
    I = [(lettre1,compteur)]
    return I + artcode_r(s[compteur:])
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()


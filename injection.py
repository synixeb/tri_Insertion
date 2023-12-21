#tri par insertion
import croissant

max = 100
taille = 10

def tri_Insersiton(tab : [int])->[int]:
    """
    pre: tab est un tableau d'entiers
    post: retourne le tableau trié par ordre croissant
    caractéristique: stable
    """
    i=1
    while i < len(tab):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = x
        i += 1
    return tab

def tri_Insersiton_Recursif(tab : [int], i : int)->[int]:
    """
    pre: tab est un tableau d'entiers
    post: retourne le tableau trié par ordre croissant
    caractéristique: stable
    """
    if i < len(tab):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = x
        tri_Insersiton_Recursif(tab, i+1)
    return tab

def main():
    T = croissant.generate_tab(taille, max)
    print("Avant tri: "+str(T))
    print("-----------------------------------")
    print("Recursif:"+str(tri_Insersiton_Recursif(T, 1)))
    print("-----------------------------------")
    print("Après tri: "+str(tri_Insersiton(T)))

if __name__ == "__main__":
    main()
#tri par insertion
import croissant
max = 100
taille = 10

def tri_Insersiton(tab : [int])->[int]:
    for i in range(1, len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = x
    return tab


def main():
    T = croissant.generate_tab(taille)

    print("Avant tri: "+str(T))
    print("-----------------------------------")
    print("Après tri: "+str(tri_Insersiton(T))+"\n")

if __name__ == "__main__":
    main()
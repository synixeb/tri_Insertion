# <p align="center">Tri par insertion</p>
<p align='center'><a href="https://commons.wikimedia.org/wiki/File:Insertion_sort_animation.gif#/media/Fichier:Insertion_sort_animation.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/2/25/Insertion_sort_animation.gif" alt="Insertion sort animation.gif" height="237" width="280"></a></p>

explication:
--
Le tri par injection est un algorithme de tri par comparaison qui consiste à trier un tableau en plaçant les éléments un par un dans un tableau vide. Pour ce faire, on compare l'élément à placer avec tous les éléments déjà placés dans le tableau vide, jusqu'à trouver la position qui lui correspond.

Pseudo-code:
--
```
    procédure tri_insertion(tableau T)

         pour i de 1 à taille(T) - 1    
              # mémoriser T[i] dans x
              x ← T[i]                              
              # décaler les éléments T[0]..T[i-1] qui sont plus grands que x, en partant de T[i-1]
              j ← i                               
              tant que j > 0 et T[j - 1] > x
                       T[j] ← T[j - 1]
                       j ← j - 1    
              # placer x dans le "trou" laissé par le décalage
              T[j] ← x
```



Python:
--
```py
def tri_injection(tab: [int])->[int]:
    tri = []
    for i in range(len(tab)):
        tri.append(tab[i])
        for j in range(len(tri)-1, 0, -1):
            if tri[j] < tri[j-1]:
                tri[j], tri[j-1] = tri[j-1], tri[j]
    return tri
```

Complexité:
--
```
    Meilleur cas: O(n)
    Pire cas: O(n^2)
    Cas moyen: O(n^2)

    Mémoire: O(1)
```

<p><a href="https://commons.wikimedia.org/wiki/File:Insertion-sort-example-300px.gif#/media/Fichier:Insertion-sort-example-300px.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" alt="Insertion-sort-example-300px.gif" height="180" width="300"></a></p>

exemple:
--
```
T = [9, 2, 7, 1]
trié || pas trié

1er tour :
9 || 2, 7, 1

2ème tour :
2, 9 || 7, 1

3ème tour :
2, 7, 9 || 1

4ème tour:
1, 2, 7, 9 (tableau completement trié)
```

[Wikipedia](https://fr.wikipedia.org/wiki/Tri_par_insertion)
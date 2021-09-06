from getpass import getpass

mot = getpass ("Entrez votre mot à faire deviner (attention, celui ci n'apparaitra pas) ->")

liste=[]
votre_liste=[]


for x in mot:
    liste.append(x)
    votre_liste.append('*')

print("".join(votre_liste))

nb_erreur = 0
while nb_erreur < 9 : 
    lettre = input("Entrez votre lettre")

    if len(lettre) > 1 :
        if lettre == mot:
            print("Vous avez trouvé la bonne réponse !")
            break

    if lettre in liste:
        for (index,x) in enumerate(liste):
            if x == lettre:
                votre_liste[index] = x
        v = ("".join(votre_liste))
        print("Bonne lettre !",v)

        if liste == votre_liste :
            print("Vous avez trouvé le mot !")
            break

    else: 
        nb_erreur += 1
        print('Mauvaise lettre... Il vous reste %s essais' %(9-nb_erreur))

if nb_erreur == 9:
    print('Vous avez perdu !')

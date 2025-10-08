"""
EXERCICE PYTHON #3

> Créer un programme simulant  un combat qui respecte les contraintes suivantes:
    - Deux joueurs, aux quels on demandera de choisir un pseudo
    - Les deux combattants démarrent avec 250 point de vie chacun 
    - Le combat se déroule en 4 attaques (Joueur1,joueur2,joueur1 et enfin joueur2)
    - Chaque attaque est une tentative (-Si elle réussit,le joueur infligera un nombre de dégats entre 0 et 100
                                        -Si elle échoue,l'attaque est ratée, et c'est au tour de l'autre joueur)
    - A la fin du combat (les 4 attaques), on déclare le gagnant (celui à qui il reste le plus de point de vie)
> Indications :
    - Le déroulement du combat doit être logique et annoncé à l'utilisateur (affichez du texte, décrivez ce qu'il se passe)
    - Coder dans un premier temps uniquement avec des afficharges/saisies,variables,opérations,conditions.
    - Pour les plus avancés, vous pourrez optimiser ce code ensuite en l'adaptant avec vos connaissance (boucles,fonction,classe,etc..)

"""
import random

titan1_name = ""
titan1_hp = 250

titan2_name = ""
titan2_hp = 250


random_attack = True 
random_damage = 0

titan1_name = input("joueur 1, choisissez un pseudo : ")
#print("{} est le joueur 1.".format(titan1_name)) python 3.X
print(f"{titan1_name} est le joueur 1.") # python 3.6 et +

titan2_name = input("joueur 2, choisissez un pseudo : ")
#print("{} est le joueur 1.".format(titan1_name)) python 3.X
print(f"{titan2_name} est le joueur 2.") # python 3.6 et +

print("\n LE COMBAT COMMENCE !\n")

#-----------------------------------------------------------
# 1 ére attaque
input()
print(f"{titan1_name}, à vous de commencer !")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True:
    #Si l'attaque réussit
    random_damage = random.randint(0,100)
    print(f"{titan1_name} subit une attaque de {titan1_name} qui lui inflige {random_damage} point de dégat")
    titan2_hp -= random_damage
else:
    #Si l'attaque échoue 
    print(f"{titan1_name} rate son attaque....")

#------------------------------------------------------------
# 2 éme attaque
input()
print(f"{titan2_name}, à vous de jouer !")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True:
    #Si l'attaque réussit
    random_damage = random.randint(0,100)
    print(f"{titan1_name} subit une attaque de {titan2_name} qui lui inflige {random_damage} point de dégat")
    titan1_hp -= random_damage
else:
    #Si l'attaque échoue
    print(f"{titan2_name} rate son attaque....")

#------------------------------------------------------------------------------------
# 3 éme attaque
input()
print(f"{titan1_name}, à vous de jouer !")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True:
    #Si l'attaque réussit 
    random_damage = random.randint(0,100)
    print(f"{titan1_name} subit une attaque de {titan1_name} qui lui inflige {random_damage} point de dégat")
    titan2_hp -= random_damage
else:
    #Si l'attaque échoue
    print(f"{titan1_name} rate son attaque....")

#------------------------------------------------------------------------------------
# 4 éme attaque 
input()
print(f"{titan2_name}, à vous de jouer !")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True:
    #Si l'attaque réussit
    random_damage = random.randint(0,100)
    print(f"{titan1_name} subit une attaque de {titan2_name} qui lui inflige {random_damage} point de dégat")
    titan1_hp -= random_damage
else:
    #Si l'attaque échoue 
    print(f"{titan2_name} rate son attaque....")

#----------------------------------------------------------------------------------------
#Résultat final
input()
print("\n FIN DU COMBAT ! \n")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")


if titan1_hp > titan2_hp:
    print(f"{titan1_name} remporte la victoire !")
elif titan1_hp < titan2_hp:
    print(f"{titan2_name} remporte la victoire !")
else:
    print("Match null!!!") 

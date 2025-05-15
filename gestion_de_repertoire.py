import sys
def leave():
    """
    cette fonction permet de quitter le programme

    Returns
    -------
    None.

    """
    print("Exiting the program...")
    sys.exit()
def menu():
    """
    cette fonction menu permet d'afficher le menu comme suite avec les options

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    print("\n")
    print("0-leave\n"
       "1-write in repertory\n"
       "2-search name in  repertory\n")
    print("\n")
    return input("enter your choice:")
def write_in_repertory():
    """
    cette fonction permet d'ecrire un nom dans le repertoire
    avec une boucle infini(while) qui s'arrete uniquement en entrant 0 pour retourner
    au menu

    Returns
    -------
    None.

    """
    while True:
        name=input("enter a name or 0 to finish:")
        if name== "0":
            print("returning to the menu...")
            break
        try :
            num=int(input("enter a correspondance number:")) #num est un entier
            with open('gestion_de_reperoire1.txt', 'a') as f:
                f.write(f"{name}:{num}\n")
        except ValueError:
            print("the num must be composite only the chiffre.")
    
def search_in_repertory():
    """
    cette fonction permet de rechercher si un nom existe dans le repertoire ou 
    non

    Returns
    affiche le message disant si le nom existe ou pas

    """
    search_name = input("Enter the name you want to search: ")
    found = False
    with open('gestion_de_reperoire1.txt', 'r') as f:
       lines = f.readlines()  #stocke ls elts ds lignes sous forme de list avec\n
       for line in lines:
           if search_name in line:
               print(f"Found: {line.strip()}")     #donne ligne sans \n
               found = True
               break
    if not found:
       print(f"{search_name} not found in the repertory.")

def main():
    """
    la fonction principale main qui petrmet d'appeler les autres fonctions 
    du programme en teetant les differents valeurs de choice.

    Returns
    ------
    None

    """
    while True:
        choice=menu()
        if choice== "0":
            leave()
        elif choice=="1":
             write_in_repertory()
        elif choice=="2":
             search_in_repertory()
        else:
            print("name doesn't exits:")
    
main()

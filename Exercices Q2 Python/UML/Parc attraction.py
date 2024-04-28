class parc:
    def __init__(self, billet_vendu, argent_encaisse, liste_attractions):
        self.__billet_vendu = billet_vendu
        self.__argent_encaisse = argent_encaisse
        self.__liste_attractions = liste_attractions

    def vendre_entree_attraction(self, attraction, billet):
        if attraction.en_activite:
            attraction.reduire_file_attente()
            self.billets_vendus.append(billet)
            self.argent_encaisse += billet.tarif
            print(f"Entrée vendue pour l'attraction {attraction.nom}")

    def ajouter_attraction(self, attraction):
        self.liste_attractions.append(attraction)
        print(f"Attraction {attraction.nom} a été ajoutée au parc")

    def arreter_attraction(self, attraction):
        attraction.en_activite = False
        print(f"Attraction {attraction.nom} a été arrêtée")


    def supprimer_attraction(self, attraction):
        self.liste_attractions.remove(attraction)
        print(f"Attraction {attraction.nom} a été supprimée du parc")

class Attraction:
    def __init__(self, nom, file_attente, billet_entrée, nb_places, en_activité, ):
        self.__nom = nom
        self.__file_attente = file_attente
        self.__billet_entrée = billet_entrée
        self.__nb_places = nb_places
        self.__en_activite = en_activité

    def reduire_file_attente(self):
        if self.__nb_places > self.__file_attente :
            print("Plus de places disponibles")
        else :
            print("Places disponibles")

    def afficher_statut(self):
        print(f"Attraction {self.__nom} : {self.__file_attente} personnes dans la file d'attente")

    def demarrer(self):
        self.__en_activite = True
        print(f"Attraction {self.__nom} a démarré")

    def arreter(self):
        self.__en_activite = False
        print(f"Attraction {self.__nom} est arrêté")

    def verifier_nb_places(self):
        return self.__nb_places

class












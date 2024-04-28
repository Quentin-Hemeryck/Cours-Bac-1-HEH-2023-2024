from datetime import datetime, timedelta

class Vehicule:
    def __init__(self, identifiant , marque , modele , annee , tarif_journalier, kilometrage) :
        self.__identifiant = identifiant
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__tarif_journalier = tarif_journalier
        self.__kilometrage = kilometrage

    def __str__(self) :
        return f"{self.__marque} {self.__modele} {self.__annee} ({self.__tarif_journalier} $/jour)"

    def check_odometre (self) :
        return self.__kilometrage

class Voiture (Vehicule):
    def __init__(self, identifiant , marque , modele , annee , tarif_journalier, nbr_portes, vitesse_max ):
        super().__init__(identifiant, marque, modele, annee, tarif_journalier, nbr_portes )
        self.__nbr_portes = nbr_portes
        self.__vitesse_max = vitesse_max

    def __str__(self):
        return f"Voiture : {self.__marque} {self.__modele} {self.__annee} ({self.__tarif_journalier} $/jour)"

class Camion (Vehicule):
    def __init__(self, identifiant , marque , modele ,annee , tarif_journalier , capacite_charge ,nb_essieux ) :
        super().__init__(identifiant, marque, modele, annee, tarif_journalier)
        self.__capacite_charge = capacite_charge
        self.__nb_essieux = nb_essieux

    def __str__(self):
        return f"Camion : {self.__marque} {self.__modele} {self.__année} ({self.__tarif_journalier} $/jour)"


class ContratLocation:
    def __init__(self, véhicule, date_début, date_fin, tarif_journalier):
        self.__véhicule = véhicule
        self.__date_début = date_début
        self.__date_fin = date_fin
        self.__tarif_journalier = tarif_journalier

    def cout_total(self):
        return (self.__date_fin - self.__date_début) * self.__tarif_journalier

class SystèmeLocation:
    def __init__(self):
        self.__véhicules = []
        self.__contrats = []

    def ajouter_véhicule(self,véhicule):
        self.__véhicules.append(véhicule)

    def supprimer_véhicule(self,véhicule):
        self.__contrats.remove(véhicule)

    def lister_véhicule(self):
        for véhicule in self.__véhicules:
            print(véhicule)

    def créer_contrat(self, véhicule, date_début, date_fin, tarif_journalier):
        contrat = ContratLocation(
        véhicule, date_début, date_fin, tarif_journalier)
        self.__contrats.append(contrat)

    def lister_contrats(self):
        for contrat in self.__contrats:
            print(contrat)

    def retourner_vehicule(self, vehicule):
        pass

    # Créer des instances de véhicules
    vehicule1 = Voiture("001", "Toyota", "Corolla", 2020, 50, 4, 180)
    vehicule2 = Camion("002", "Ford", "F150", 2018, 80, 2000, 2)

    # Créer une instance de contrat de location
    from datetime import datetime
    date_debut = datetime.now()
    date_fin = date_debut + timedelta(days=5)
    contrat1 = ContratLocation(vehicule1, date_debut, date_fin, vehicule1.tarif_journalier)

    # Instancier le système de location
    système_location = SystemeLocation()

    # Ajouter les véhicules au système
    système_location.ajouter_véhicule(vehicule1)
    système_location.ajouter_véhicule(vehicule2)

    # Créer un contrat de location
    date_debut = datetime.now()
    date_fin = date_debut + timedelta(days=7)
    système_location.créer_contrat(vehicule1, date_debut, date_fin, vehicule1.tarif_journalier)

    # Afficher les informations des véhicules
    print("Liste des véhicules disponibles :")
    système_location.lister_véhicule()

    # Afficher les contrats de location
    print("\nListe des contrats de location :")
    système_location.lister_contrats()











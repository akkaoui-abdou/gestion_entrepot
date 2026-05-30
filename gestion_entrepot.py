from enum import Enum


class Taille(Enum):
    PETIT = 1
    MOYEN = 2
    GRAND = 3


class Sas:
    def __init__(self, nom, taille, orientations):
        self.nom = nom
        self.taille = taille
        self.orientations = orientations
        self.occupe = False

    def compatible(self, vehicule):
        return (
            self.taille.value >= vehicule.taille.value
            and vehicule.orientation in self.orientations
            and not self.occupe
        )

    def __str__(self):
        statut = "Occupé" if self.occupe else "Libre"
        return f"{self.nom} ({self.taille.name}) - {statut}"


class Vehicule:
    def __init__(self, immatriculation, type_vehicule,
                 taille, orientation, operation):
        self.immatriculation = immatriculation
        self.type_vehicule = type_vehicule
        self.taille = taille
        self.orientation = orientation
        self.operation = operation

    def __str__(self):
        return (
            f"{self.immatriculation} | "
            f"{self.type_vehicule} | "
            f"{self.taille.name} | "
            f"{self.orientation} | "
            f"{self.operation}"
        )


class GestionEntrepot:
    def __init__(self):
        self.sas = []

    def ajouter_sas(self, sas):
        self.sas.append(sas)

    def affecter_sas(self, vehicule):
        compatibles = [
            s for s in self.sas if s.compatible(vehicule)
        ]

        if not compatibles:
            print(
                f"Aucun sas disponible pour "
                f"{vehicule.immatriculation}"
            )
            return None

        compatibles.sort(key=lambda x: x.taille.value)

        sas = compatibles[0]
        sas.occupe = True

        print(
            f"Véhicule {vehicule.immatriculation} "
            f"affecté au {sas.nom}"
        )

        return sas

    def liberer_sas(self, nom_sas):
        for sas in self.sas:
            if sas.nom == nom_sas:
                sas.occupe = False
                print(f"{nom_sas} libéré")
                return

    def afficher_etat(self):
        print("\n=== Etat des sas ===")
        for sas in self.sas:
            print(sas)


# -------------------------
# Configuration des sas
# -------------------------

entrepot = GestionEntrepot()

entrepot.ajouter_sas(
    Sas("SAS_P1", Taille.PETIT, ["NORD", "SUD"])
)

entrepot.ajouter_sas(
    Sas("SAS_P2", Taille.PETIT, ["NORD"])
)

entrepot.ajouter_sas(
    Sas("SAS_M1", Taille.MOYEN, ["NORD", "SUD", "EST"])
)

entrepot.ajouter_sas(
    Sas("SAS_G1", Taille.GRAND, ["NORD", "SUD", "EST", "OUEST"])
)

entrepot.ajouter_sas(
    Sas("SAS_G2", Taille.GRAND, ["OUEST"])
)

# -------------------------
# Arrivées de véhicules
# -------------------------

vehicules = [
    Vehicule(
        "AA-123-AA",
        "Utilitaire",
        Taille.PETIT,
        "NORD",
        "ENTREE"
    ),
    Vehicule(
        "BB-456-BB",
        "Camionnette",
        Taille.MOYEN,
        "EST",
        "ENTREE"
    ),
    Vehicule(
        "CC-789-CC",
        "Semi-remorque",
        Taille.GRAND,
        "OUEST",
        "SORTIE"
    ),
]

for v in vehicules:
    entrepot.affecter_sas(v)

entrepot.afficher_etat()

# Exemple : libération d'un sas
entrepot.liberer_sas("SAS_P1")

entrepot.afficher_etat()

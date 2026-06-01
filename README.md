# Gestion Automatique des Sas d'Entrée/Sortie d'Entrepôt

## Description

Ce projet permet de gérer automatiquement l'affectation des véhicules aux sas d'entrée et de sortie d'un entrepôt.

L'objectif est de :

* Identifier le véhicule à son arrivée.
* Déterminer la taille de sas nécessaire.
* Vérifier l'orientation du véhicule.
* Contrôler la disponibilité des sas.
* Affecter automatiquement le sas le plus adapté.
* Libérer les sas après utilisation.
* Afficher l'état des sas en temps réel.

---

## Fonctionnalités

### Gestion des véhicules

Chaque véhicule possède :

* Une immatriculation
* Un type de véhicule
* Une taille
* Une orientation
* Une opération (Entrée ou Sortie)

Exemple :

| Immatriculation | Type          | Taille | Orientation | Opération |
| --------------- | ------------- | ------ | ----------- | --------- |
| AA-123-AA       | Utilitaire    | Petit  | Nord        | Entrée    |
| BB-456-BB       | Camionnette   | Moyen  | Est         | Entrée    |
| CC-789-CC       | Semi-remorque | Grand  | Ouest       | Sortie    |

---

## Gestion des sas

Le système gère trois catégories de sas :

### Petit

Adapté aux :

* Véhicules légers
* Utilitaires

### Moyen

Adapté aux :

* Camionnettes
* Petits camions

### Grand

Adapté aux :

* Poids lourds
* Semi-remorques

---

## Architecture

### Classe Taille

Représente les tailles disponibles :

```python
PETIT
MOYEN
GRAND
```

### Classe Sas

Représente un sas de contrôle.

Attributs :

```python
nom
taille
orientations
occupe
```

Exemple :

```python
SAS_P1
SAS_M1
SAS_G1
```

---

### Classe Vehicule

Représente un véhicule entrant ou sortant.

Attributs :

```python
immatriculation
type_vehicule
taille
orientation
operation
```

---

### Classe GestionEntrepot

Responsable de :

* Ajouter des sas
* Affecter les véhicules
* Libérer les sas
* Afficher l'état des sas

---

## Algorithme d'Affectation

### Étape 1

Le véhicule arrive au sas d'entrée.

### Étape 2

Le système récupère :

* Taille du véhicule
* Orientation
* Type d'opération

### Étape 3

Recherche des sas compatibles :

```text
taille sas >= taille véhicule
orientation compatible
sas libre
```

### Étape 4

Sélection du plus petit sas compatible disponible.

### Étape 5

Réservation du sas.

### Étape 6

Transmission des consignes au chauffeur.

Exemple :

```text
Dirigez-vous vers SAS_M1
```

---

## Exemple de Configuration

### Sas disponibles

| Sas    | Taille | Orientations          |
| ------ | ------ | --------------------- |
| SAS_P1 | Petit  | Nord, Sud             |
| SAS_P2 | Petit  | Nord                  |
| SAS_M1 | Moyen  | Nord, Sud, Est        |
| SAS_G1 | Grand  | Nord, Sud, Est, Ouest |
| SAS_G2 | Grand  | Ouest                 |

---

## Exemple d'Exécution

Entrées :

```text
AA-123-AA
Utilitaire
Petit
Nord
Entrée
```

Résultat :

```text
Véhicule AA-123-AA affecté au SAS_P1
```

---

## Gestion de l'Occupation

### Occupation

Lorsqu'un véhicule est affecté :

```python
sas.occupe = True
```

### Libération

Après validation :

```python
sas.occupe = False
```

---

## Exemple de Sortie

```text
=== Etat des sas ===

SAS_P1 (PETIT) - Occupé
SAS_P2 (PETIT) - Libre

SAS_M1 (MOYEN) - Occupé

SAS_G1 (GRAND) - Occupé
SAS_G2 (GRAND) - Libre
```

---

## Améliorations Futures

### Gestion des files d'attente

Créer une file FIFO :

```text
Premier arrivé
Premier servi
```

---

### Lecture Automatique des Plaques

Intégration possible :

* Caméra IP
* OCR
* Reconnaissance de plaques

---

### Interface Web

Technologies possibles :

* Flask
* Django
* FastAPI

Fonctionnalités :

* Tableau de bord
* Visualisation des sas
* Historique des passages
* Alertes temps réel

---

### Base de Données

Tables recommandées :

#### Vehicules

```sql
id
immatriculation
type
taille
```

#### Sas

```sql
id
nom
taille
orientation
statut
```

#### Affectations

```sql
id
vehicule_id
sas_id
heure_arrivee
heure_depart
```

---

### Affichage Temps Réel

Possibilités :

* Écrans LED
* Application mobile
* Tableau de supervision

Exemple :

```text
AA-123-AA → SAS_P1
BB-456-BB → SAS_M1
CC-789-CC → SAS_G1
```

---

## Cas d'Usage Industriel

### Entrée

1. Arrivée du véhicule
2. Lecture de plaque
3. Vérification des autorisations
4. Attribution du sas
5. Contrôle documentaire

### Sortie

1. Contrôle du chargement
2. Validation des documents
3. Libération du sas
4. Autorisation de sortie

---

## Objectif Final

Réduire :

* Les temps d'attente
* Les erreurs d'affectation
* Les embouteillages internes

Améliorer :

* La sécurité
* La traçabilité
* La productivité de l'entrepôt

---

## Auteur

Projet de gestion intelligente des sas d'entrée et de sortie pour entrepôt logistique.

```python

from abc import ABC, abstractmethod


class Taille:
    PETIT = 1
    MOYEN = 2
    GRAND = 3


# =====================================
# Véhicules
# =====================================

class Vehicule(ABC):

    def __init__(self, immatriculation, orientation, operation):
        self.immatriculation = immatriculation
        self.orientation = orientation
        self.operation = operation

    @property
    @abstractmethod
    def taille(self):
        pass

    @property
    @abstractmethod
    def type_vehicule(self):
        pass

    def __str__(self):
        return (
            f"{self.immatriculation} | "
            f"{self.type_vehicule} | "
            f"{self.orientation} | "
            f"{self.operation}"
        )


class Utilitaire(Vehicule):

    @property
    def taille(self):
        return Taille.PETIT

    @property
    def type_vehicule(self):
        return "Utilitaire"


class Camionnette(Vehicule):

    @property
    def taille(self):
        return Taille.MOYEN

    @property
    def type_vehicule(self):
        return "Camionnette"


class SemiRemorque(Vehicule):

    @property
    def taille(self):
        return Taille.GRAND

    @property
    def type_vehicule(self):
        return "Semi-remorque"


# =====================================
# Sas
# =====================================

class Sas:

    def __init__(
        self,
        nom,
        taille,
        orientations,
        capacite_max
    ):
        self.nom = nom
        self.taille = taille
        self.orientations = orientations
        self.capacite_max = capacite_max
        self.vehicules = []

    @property
    def dispo(self):
        return len(self.vehicules) < self.capacite_max

    def is_compatible(self, vehicule):

        return (
            self.taille >= vehicule.taille
            and vehicule.orientation in self.orientations
            and self.dispo
        )

    def ajouter_vehicule(self, vehicule):

        if not self.dispo:
            raise ValueError(
                f"Le sas {self.nom} est plein"
            )

        self.vehicules.append(vehicule)

    def retirer_vehicule(self, immatriculation):

        for vehicule in self.vehicules:

            if vehicule.immatriculation == immatriculation:
                self.vehicules.remove(vehicule)
                return True

        return False

    def __str__(self):

        etat = (
            "Disponible"
            if self.dispo
            else "Complet"
        )

        return (
            f"{self.nom} | "
            f"Capacité {len(self.vehicules)}/"
            f"{self.capacite_max} | "
            f"{etat}"
        )


# =====================================
# Gestion entrepôt
# =====================================

class GestionEntrepot:

    def __init__(self):
        self.sas = []

    def ajouter_sas(self, sas):
        self.sas.append(sas)

    def affecter_sas(self, vehicule):

        compatibles = [
            s
            for s in self.sas
            if s.is_compatible(vehicule)
        ]

        if not compatibles:
            raise ValueError(
                f"Aucun sas disponible pour "
                f"{vehicule.immatriculation}"
            )

        compatibles.sort(
            key=lambda s: s.taille
        )

        sas = compatibles[0]

        sas.ajouter_vehicule(vehicule)

        print(
            f"Véhicule "
            f"{vehicule.immatriculation} "
            f"({vehicule.type_vehicule}) "
            f"affecté au sas {sas.nom}"
        )

        return sas

    def liberer_sas(
        self,
        nom_sas,
        immatriculation
    ):

        for sas in self.sas:

            if sas.nom == nom_sas:

                return sas.retirer_vehicule(
                    immatriculation
                )

        return False

    def afficher_etat_sas(self):

        print("\n=== ÉTAT DES SAS ===")

        for sas in self.sas:

            print(sas)

            if sas.vehicules:

                print(
                    "  Véhicules présents :"
                )

                for vehicule in sas.vehicules:

                    print(
                        f"   - "
                        f"{vehicule.immatriculation}"
                        f" ({vehicule.type_vehicule})"
                    )

            else:

                print(
                    "  Aucun véhicule"
                )


# =====================================
# Démonstration
# =====================================

gestion = GestionEntrepot()

gestion.ajouter_sas(
    Sas(
        "S1",
        Taille.PETIT,
        ["NORD", "SUD"],
        capacite_max=2
    )
)

gestion.ajouter_sas(
    Sas(
        "S2",
        Taille.MOYEN,
        ["NORD"],
        capacite_max=3
    )
)

gestion.ajouter_sas(
    Sas(
        "S3",
        Taille.GRAND,
        ["NORD", "SUD"],
        capacite_max=5
    )
)

vehicules = [

    Utilitaire(
        "AA-1245-BB",
        "SUD",
        "ENTREE"
    ),

    Camionnette(
        "AA-1245-CC",
        "NORD",
        "ENTREE"
    ),

    SemiRemorque(
        "AA-1245-DD",
        "SUD",
        "SORTIE"
    ),

    Utilitaire(
        "AA-9999-ZZ",
        "NORD",
        "ENTREE"
    )
]

for vehicule in vehicules:
    gestion.affecter_sas(vehicule)

gestion.afficher_etat_sas()

print("\n--- Libération ---")

gestion.liberer_sas(
    "S1",
    "AA-1245-BB"
)

gestion.afficher_etat_sas()
```

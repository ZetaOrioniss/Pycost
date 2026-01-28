
# Pycost 💸

Pycost est un petit outil en ligne de commande pour gérer simplement les dépenses d’un business ou d’un projet personnel.

Les dépenses sont saisies en **une seule commande**, stockées dans un **fichier JSON**, et versionnées avec **Git** pour garder un historique fiable.

---

## Fonctionnalités

- Ajouter une dépense depuis le terminal
  - montant
  - article
  - date (format `jj/mm/aaaa`)
- Stockage des données dans un fichier `costs.json`
- Historique des modifications grâce à Git
- Afficher les dépenses :
  - entre deux dates
  - tri croissant ou décroissant

---

## Prérequis

- Python 3.8 ou plus
- Git installé sur la machine

Vérification :
```bash
python --version
git --version
````

---

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/TON_UTILISATEUR/pycost.git
cd pycost
```

---

## Utilisation (concept)

### Ajouter une dépense

Une dépense se saisit en **une seule commande** :

```bash
pycost 32 "café client" 01/02/2024
```

### Afficher les dépenses entre deux dates

```bash
pycost list 01/01/2024 31/01/2024 --asc
```

ou

```bash
pycost list 01/01/2024 31/01/2024 --desc
```

---

## Format des données

Les dépenses sont stockées dans `costs.json` sous la forme :

```json
{
  "costs": [
    {
      "price": 7.50,
      "date": "01/02/2024",
      "article": "café"
    }
  ]
}
```

---

## Versionnement avec Git

Chaque modification peut être sauvegardée :

```bash
git add costs.json
git commit -m "Ajout dépense : café client"
```

Git permet ainsi :

* de garder un historique complet
* d’annuler une erreur
* d’auditer les dépenses dans le temps

---

## Roadmap (idées futures)

* Catégories de dépenses
* Export CSV
* Total par période
* Recherche par mot-clé
* Validation stricte des entrées utilisateur

---

## Licence

Projet personnel / open-source.
Libre d’utilisation et de modification.


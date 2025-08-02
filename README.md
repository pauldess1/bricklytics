# 🧱 Bricklytics

**Bricklytics** est un outil d’aide à l’investissement locatif qui simule la capacité d’emprunt, évalue la rentabilité d’un bien immobilier, et collecte automatiquement des annonces via du scraping.  
Son objectif : permettre à un investisseur de détecter rapidement des opportunités viables, en fonction de son profil financier et du marché.

---

## 🚀 Fonctionnalités

- 🧮 **Calcul de capacité d’emprunt** basé sur le revenu, l’âge, l’apport, le taux et la durée.
- 📉 **Simulation de prêt** avec mensualités, intérêts et résumé complet.
- 📊 **Évaluation de rentabilité** (brute, nette, TRI) d’un bien locatif.
- 🏘️ **Scraping d’annonces** (à venir) pour détecter des opportunités en ligne automatiquement.
- 💡 **Pipeline complet** du profil emprunteur à la simulation financière.

---

## 📁 Structure du projet
```
bricklytics/
│
├── borrower_profile.py
├── loan_calculator.py 
├── rentability_evaluator.py
├── scraper/
├── tests/
├── main.py 
└── README.md
```
---

## 🔧 Exécution de l'outil

### 1. Installation
```bash
git clone https://github.com/pauldess1/bricklytics.git
cd bricklytics
python -m venv venv
venv/bin/activate
pip install -r requirements.txt
```


# 🗺️ Roadmap
## ✅ Phase 1 – Core financier
 Création du profil utilisateur

 Calcul du montant d'emprunt maximal

 Simulation du prêt et mensualités

## ✅ Phase 2 – Évaluation financière
 Calcul du cashflow

 Rentabilité brute et nette

 Calcul du TRI

## 🔄 Phase 3 – Scraping & données marché
 Développement du module de scraping d'annonces

 Intégration automatique dans le pipeline

 Filtrage intelligent des biens viables

## 🔜 Phase 4 – Interface & automatisation
 Lancement en ligne (API ou interface web)

 Génération de rapports PDF
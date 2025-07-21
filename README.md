# Copilote SEO : Votre Assistant de Rédaction IA pour un Contenu Performant

Fatigué de jongler entre 10 onglets pour analyser vos concurrents, trouver les bons mots-clés et structurer vos articles ? **Copilote SEO** est une application web conçue pour centraliser et simplifier l'intégralité du processus de création de contenu optimisé pour les moteurs de recherche.

De l'analyse de la SERP à la rédaction assistée par l'IA, cet outil a pour but de transformer une tâche complexe et chronophage en un processus fluide, guidé et efficace.

## 🚀 Fonctionnalités Clés

Ce projet intègre une suite d'outils puissants pour vous accompagner de l'idée à la publication :

*   **Analyse de la Concurrence :** En se basant sur un mot-clé, l'outil analyse les 5 premiers résultats de Google pour extraire leurs données clés (nombre de mots, structure des titres Hn).
*   **Briefing SEO en Temps Réel :** Un tableau de bord dynamique vous guide pendant la rédaction avec :
    *   Un **Score SEO** qui évolue en direct.
    *   Une **checklist de mots-clés sémantiques** qui se cochent automatiquement.
    *   Une **checklist de la structure de l'article** (H2, H3) à suivre.
*   **Plan d'Article Généré par IA :** En se basant sur l'analyse des concurrents, l'IA (Google Gemini) propose un plan d'article optimisé et unique, conçu pour être plus complet que celui de la concurrence.
*   **Copilote de Rédaction :** Un chatbot contextuel vous assiste pendant l'écriture. Demandez-lui de reformuler une phrase, de rédiger un paragraphe ou de trouver des idées, le tout avec le choix de plusieurs modèles d'IA.
*   **Interface Moderne et Intuitive :**
    *   Une vue "Studio" à trois volets pour avoir toutes les informations sous les yeux.
    *   Un **Thème Sombre & Clair** pour le confort visuel.

## 🛠️ Stack Technique

Ce projet est une application full-stack utilisant des technologies modernes et performantes.

#### **Backend (Python)**
*   **Framework :** Flask
*   **Gestion des API :** Flask-CORS pour la communication cross-origin.
*   **Variables d'environnement :** `python-dotenv`
*   **APIs Externes :**
    *   **ValueSERP :** Pour l'analyse des résultats de recherche Google.
    *   **Google Gemini :** Pour la génération de plans et l'assistance par IA.

#### **Frontend (JavaScript)**
*   **Framework :** Vue.js 3 (avec l'API de Composition)
*   **Build Tool :** Vite
*   **Composants UI :** PrimeVue pour une interface riche et réactive.
*   **Mise en page :** PrimeFlex pour le système de grille.

## ⚙️ Installation et Lancement

Suivez ces étapes pour lancer le projet sur votre machine locale.

#### **Prérequis**
*   Node.js (v18 ou supérieure)
*   Python (v3.10 ou supérieure)

#### **1. Cloner le Dépôt**
```bash
git clone https://github.com/VOTRE_NOM/VOTRE_REPO.git
cd COPILOT-SEO
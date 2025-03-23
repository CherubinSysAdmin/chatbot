```markdown
# Supervision Bot sur Ubuntu

Ce projet consiste en la création d'un bot Telegram pour la supervision des services et des ressources système sur un serveur Ubuntu. Grâce à ce bot, tu peux surveiller l'état des services, la mémoire, l'utilisation du CPU, et bien plus, directement depuis Telegram. Le bot est conçu pour être facile à utiliser et accessible à distance, ce qui simplifie l'administration des serveurs.

## Fonctionnalités

- **Vérification de l'état des services** : Vérifie si des services comme Apache, SSH, Samba, etc., sont actifs ou inactifs.
- **Redémarrer/Arrêter des services** : Redémarre ou arrête un service spécifié à la demande.
- **Surveillance de la mémoire et du CPU** : Affiche l'utilisation actuelle de la mémoire et du CPU.
- **Redémarrage du serveur** : Permet de redémarrer le serveur via une commande Telegram.

## Prérequis

Avant d'utiliser le bot, tu dois t'assurer que les éléments suivants sont installés sur ton serveur Ubuntu :

- Python 3.x
- pip (pour installer les bibliothèques Python)
- Un bot Telegram (créé via [BotFather](https://core.telegram.org/bots#botfather))

## Installation

### 1. Mise à jour du système et installation des prérequis
sudo apt update && sudo apt install python3 python3-pip -y

### 2. Installation des dépendances

Installe les bibliothèques Python nécessaires avec pip :
pip install chatterbot chatterbot_corpus python-telegram-bot

### 3. Configuration du bot Telegram

- Crée un bot via [BotFather](https://core.telegram.org/bots#botfather) sur Telegram et récupère ton token.
- Remplace le token dans le fichier bot.py par le token obtenu.

TOKEN = 'TON_BOT_TOKEN_ICI'

### 4. Exécution du bot

Lance le bot avec la commande suivante :
python3 bot.py

Une fois que le bot est lancé, tu peux interagir avec lui via Telegram en utilisant les commandes suivantes :

- /check_services : Vérifie l'état de tous les services.
- /check_service [nom_du_service] : Vérifie l'état d'un service spécifique.
- /restart [nom_du_service] : Redémarre un service.
- /stop_service [nom_du_service] : Arrête un service.
- /memory : Affiche l'utilisation de la mémoire.
- /cpu : Affiche l'utilisation du CPU.
- /restart_server : Redémarre le serveur.

## Auteurs
- **TSHIENDA Cherubin

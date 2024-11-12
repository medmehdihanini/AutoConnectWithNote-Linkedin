# LinkedIn Connection Automation Script

Ce script automatise l'envoi de demandes de connexion personnalisées sur LinkedIn. Il recherche des recruteurs dans les entreprises spécifiées et envoie une demande de connexion avec un message personnalisé.

## Prérequis

1. **Google Chrome** : Assurez-vous que Google Chrome est installé sur votre ordinateur.

2. **ChromeDriver** : Téléchargez ChromeDriver compatible avec votre version de Chrome :
   - Visitez la [page de téléchargement de ChromeDriver](https://sites.google.com/chromium.org/driver/).
   - Téléchargez la version correspondant à votre version de Chrome.
   - Extrayez le fichier et notez son chemin d'accès ; vous en aurez besoin plus tard.

3. **Python** : Assurez-vous que Python est installé. Vous pouvez le télécharger depuis [python.org](https://www.python.org/downloads/).

4. **Bibliothèque Selenium** : Installez Selenium via pip :
   ```bash
   pip install selenium


## Configuration

1. **Cloner ou Télécharger le Référentiel** :
   - Clonez ce référentiel GitHub ou téléchargez le code sur votre machine locale.

2. **Spécifiez le Chemin vers ChromeDriver** :
   - Mettez à jour le chemin `chrome_service` dans le code avec l'emplacement où vous avez enregistré `chromedriver.exe` :
     ```python
     chrome_service = Service('D:/software/chromedriver-win64/chromedriver.exe')
     ```

3. **Spécifiez le Chemin vers Chrome** :
   - Définissez le chemin de votre navigateur Chrome dans `chrome_options.binary_location` :
     ```python
     chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
     ```

4. **Spécifiez Votre Profil Chrome** :
   - Utilisez le chemin de votre profil utilisateur Chrome pour rester connecté à LinkedIn. Remplacez `"user-data-dir=C:/Users/mehdi/AppData/Local/Google/Chrome/User Data"` par le chemin de votre dossier de profil.

## Utilisation

1. **Modifier la Liste des Entreprises** :
   - Modifiez la liste `companies` avec les noms des entreprises auprès desquelles vous souhaitez envoyer des demandes de connexion :
     ```python
     companies = ["HP", "Apple", "samsung"]
     ```

2. **Modifier le Message de Connexion** :
   - Personnalisez le `connection_message` avec votre propre message à envoyer avec chaque demande :
     ```python
     connection_message = ("Bonjour ! En tant qu'étudiant en dernière année de génie logiciel ...")
     ```

3. **Exécuter le Script** :
   - Exécutez le script avec la commande suivante :
     ```bash
     python nom_du_script.py
     ```
   - **Note** : Assurez-vous que Chrome est fermé avant d'exécuter le script pour éviter les conflits de profil.

## Fonctionnement

1. Le script lance Chrome avec votre profil utilisateur, accédant à LinkedIn en mode connecté.
2. Il recherche des recruteurs LinkedIn dans chaque entreprise spécifiée.
3. Pour chaque recruteur, il :
   - Clique sur le bouton "Se connecter".
   - Ajoute un message personnalisé.
   - Envoie la demande de connexion.

4. **Gestion des Erreurs** :
   - Le script ignorera un recruteur si une erreur se produit et affichera un message d'erreur.

5. Après l'envoi de toutes les demandes de connexion, le script ferme automatiquement le navigateur.

## Dépannage

- **Incompatibilité de Version de ChromeDriver** : Assurez-vous que votre version de ChromeDriver correspond à la version de votre navigateur Chrome.
- **Captchas LinkedIn** : Une utilisation excessive de ce script peut déclencher des captchas. Utilisez-le de manière responsable pour éviter les restrictions de compte.

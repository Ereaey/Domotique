#Présentation des différents modules

##Serveur

###xpl_parser.py
Permet de récuperer les informations au sein d'une trame xpl

###xpl_sender.py
Permet d'envoyer une trame en udp

###xpl_treatment.py
Permet de traiter les trames xpl recu pour lancer des évenements en conséquence

###server_udp.py
Permet de centraliser les différentes classes pour la mise en place du serveur au complet

###xpl_logger.py
Permet d'enregister dans un fichier toute les trames xpl naviguant dans le réseau avec l'heure et l'addresse IP

###xpl.py
Permet de générer les trames xpl

##Modules

###xpl_clock.py
Permet d'envoyer la date à chaque minute au format xpl

###xpl_mail.py
Permet d'envoyer des mails via le protocole xpl

###xpl_ping.py
Permet de recevoir le ping("google.com") via xpl


Linux Priv Escalation

# Linux Priv Escalation

## Trouver les SUID Binaries : 

`find / -perm -u=s -type f 2>/dev/null`

find - Commande find

/ - chercher sur tout le system

-perm - chercher les fichier avec des permissions spécifiques

-u=s - Any of the permission bits mode are set for the file. Symbolic modes are accepted in this form

-type f - chercher uniquement des fichiers
2>/dev/null - supprimer les erreurs


* * *

## Understanding /etc/passwd format :

The /etc/passwd file contains one entry per line for each user (user account) of the system. All fields are separated by a colon : symbol. Total of seven fields as follows. Generally, /etc/passwd file entry looks as follows:

    test:x:0:0:root:/root:/bin/bash

[as divided by colon (:)]

Username: It is used when user logs in. It should be between 1 and 32 characters in length.


Password: An x character indicates that encrypted password is stored in /etc/shadow file. Please note that you need to use the passwd command to computes the hash of a password typed at the CLI or to store/update the hash of the password in /etc/shadow file, in this case, the password hash is stored as an "x".


User ID (UID): Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.


Group ID (GID): The primary group ID (stored in /etc/group file)
User ID Info: The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.


Home directory: The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /


Command/shell: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell.



















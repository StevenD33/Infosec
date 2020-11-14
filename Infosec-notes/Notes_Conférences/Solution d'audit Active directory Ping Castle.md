#  Sécurisation AD les basics par Vincent Le Toux 

Vincent Le Toux : 
Head of VINCI-CERT
Ancien Head of CERT-ENGIE
Contributeur sur mimikatz et auteur de PingCastle
@mysmartlogon

### Admin qui veut admin

Built-in Administrators 

Server Operators 

Print operators 

Account operators

Backup operators 

Dns Admin 


## Le B.A BA du hacker 


### Coté Attaque

Bloodhound 

Sharphound obfusqué

Outils bloodhoung permet de déterminer comment l'attaquant peut devenir admin du domain.

Mimikatz 

### Coté défense 

Carbon Black et DarkTrace "censé stoppé mimikatz"

Recommandation de l'ANSSI et points de controle Active Directory
Guide NIST et STIG

Mimikatz pas detecté si bien compilé

### Et sérieusement ? 

- Avoir une cartographie à jour 
- Avoir un controle régulier des domaines 
- Avoir une veille sur les vulnérabilités 
- Avoir une surveillance (SOC
Avoir des étapes d'organisation avant de vouloir détécter du mimikatz. 

Ping Castle pour auditer son AD

Superviser et faire de la détection sur l'AD : 
AZURE ATP 
Varonis
ALCID




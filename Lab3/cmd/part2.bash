hashcat --stdout -r rules.rule rockyou.txt | sed '/^[0-9]/d' > rockyou_mod.dic

#Para conocer la cantidad de contraseñas en cada archivo:
wc -l rockyou_mod.dic
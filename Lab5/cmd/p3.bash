#modificar archivo sshd_config
vim /etc/ssh/sshd_config

#agregar config
Ciphers aes128-ctr
HostKeyAlgorithms ecdsa-sha2-nistp256
KexAlgorithms ecdh-sha2-nistp256
MACs hmac-sha2-256

#reiniciar servicio
service ssh restart
#clonar el repositorio
git clone https://github.com/openssh/openssh-portable.git .

#acceder al archivo para realizar las modificaciones
vim version.h

#guardar los cambios
autoreconf
.\configure
make
make install
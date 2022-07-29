echo -e '\e[0;31m.'
cat ./banner/ban
echo -e '\e[0;31m [*]Iniciando instalacion de dependencia'
sleep 1
echo -e '\e[1;31m Instalando python \e'
pacman -Syu python3
pacman -Sy python
pacman -Sy python3-pip
pacman -Sy python-pip
echo -e '\e[0;31m Instalando librerias necesarias \e'
pip3 install colorama
pip3 install pprint
pip3 install subprocess
pip3 install readline
pip3 install time

pip install colorama
pip install pprint
pip install subprocess
pip install readline
pip install time
echo -e '\e[0;31m Instalacion Finalizada \e'
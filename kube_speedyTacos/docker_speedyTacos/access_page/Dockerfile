FROM php:8.0-apache
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
RUN apt-get update && apt-get upgrade -y

#Creazione cartella Immagini
RUN mkdir -p /var/www/html/Immagini

#Copia dei file del progetto nei container
COPY index.php /var/www/html
COPY ./immagini/logo.png /var/www/html/Immagini


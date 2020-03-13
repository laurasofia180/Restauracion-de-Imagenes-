# Restauracion de Imagenes
La restauración de imagenes es el proceso de mejorar la calidad de una imagen, esto permite eliminar el ruido, mejorar el brillo, el color y los detalles en una imagen. 
Las técnicas de restauración han evolucionado a lo largo del tiempo. 
Actualmente este proceso se  basa en métodos algebraicos y la manipulación de grandes sistemas de ecuaciones para recuperar la imagen.

### Prerequsitos 
*Python 3.8

### Instalación

`git -clone https://github.com/laurasofia180/Restauracion-de-Imagenes-.git`


## Metodos para la restauracion de imagenes 

### Interpolación de Laplace 

Este método de interpolación esta espacializado en restaurar datos de una matriz con datos perdidos.
la explicacion facil es que para cada valor perdido en el interior de la  matriz se toma un promedio sobre los 4 valores circundantes a este, para el caso de los borrdes aplican unas reglas diferentes.
Hay que tener encuenta que este metodo solo funciona bien para las funciones harmonicas y esta optimizado para imagenes de calor.

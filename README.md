# Capa8_Git_Challenge

Este reto está diseñado para que en una situación en la que podrias encontrarte en tu día a día en ingeniero, pongas en prueba lo que haz aprendido el día de hoy sobre git y github.

## Descripción: 
Este repositorio tiene un unico archivo que es una clase simple que busca representar el funcionamiento de una calculadora.

Además de este archivo, el repositorio cuenta con varias ramas a parte de la rama main, intenta explorarlas y entender que hace cada una. Luego vuelve y te diremos que debes hacer.


## Reto:

1. Primero debes de clonar este repositorio, recuerda el comando que te permite hacerlo. --> clonar <--

2. Ahora muevete a la siguiente rama -->

### Rama Feature/Multiply:

1. Esta rama agrega la funcionalidad de multiplicar a nuestra calculdora, pero revisa los commits en las misma, ves un error en el codigo?

2. Cuando descubras el error, verás que este fue agregado en el ultimo commit, debes *Revertir* ese commit, hay un comando que te lo permite hacer. Pista: Necesitas el hash del commit para hacerlo.

3. Ahora muevete a la siguiente rama -->


### Rama Feature/Divide:

1. Esta rama agrega la funcionalidad de dividir a nuestra calculador, pero, revisa bien y compara con el codigo de main, se ve diferente, no? Es así, esta rama quedó atrás a lo que main es ahora, necesitas hacer que esta rama vuelva a quedar en linea con el codigo de main, y manteniendo tu codigo nuevo de esta rama.

### Rama Hotfix/handle_divide_0:

1. Si eres atento notaste que la funcion de dividir tiene un error, no en su logica, esta funciona, pero que pasa en este momento si intentamos dividir por 0?, tendremos un error en tiempo de ejecución! Esto es particularmente peligroso en un codigo productivo, tenemos que corregirlo.

2. Esta rama la llamada hotfix entre sus commits tiene la que remedia la situación anterior, pero tambien otros commits no relacionados, necesitamos que lleves *UNICAMENTE* el commit de la correción a la rama Feature/Divide. :cherries: :cherries:

### Agrega tu propio codigo:

1. Ve a la rama main de nuevo.

2. Agrega el metodo que deseas a la clase, lo que quieras no hay restricciones. *NO HAGAS COMMIT DE ESTE CAMBIO* :bomb:

3. Espera, no es correcto ni una buena practica hacer cambios en main sin contexto, lo mejor que puedes hacer es crear una rama para esta feature.

4. Guarda estos cambios sin hacer commit, sí, es posible, te mencionamos un comando usalo.

5. Crea una nueva rama Feature/tunombre_tudiadenacimiento_own_method. Y trae los cambios que habias hecho a esta nueva rama.

6. Ahora publica esta rama en el repo, recuerda que este moment github no sabe de esta rama, solo está en el local, el comando para publicar debe tener unas flags extra.


### Reto final:

1. Crea una nueva rama basada en main con el siguiente nombre Epic/tunombre_tudiadenacimiento_git_capa8.

2. Mergea en esta rama las ramas de los features, y tu propia rama que creaste.

3. Publica esta rama en github y crea un pull request hacia main, para que hayas creado tu primera contribución en un repositorio!!! :octocat: :octocat:

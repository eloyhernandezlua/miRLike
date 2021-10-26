# miRLike
Proyecto materia compiladores


### Avance 1

En este avance se presenta el léxico y las reglas gramaticales que va a seguir el lenguaje, cuenta con un archivo de prueba que valida su funcionamiento, para correrlo únicamente es necesario correr: 

```shell
$ python3 ./lex.py
```

y se ejecutará el código prueba `pass.txt`. Pendiente o aún por definir está el agregar las funciones especiales de estadística pero ya se tiene estipulado en dónde irán y su interacción con los otros componentes. El repositorio está fuertemente documentado de para que es cada cosa (más que nada porque luego a mi se me olvida).


### Avance 2

En este avance se hizo lo básico de semantica, comenzar a cachar errores y detener el programa si se los encuentra, ver si la hija baila con el señor, que los tipos coincidan que en las asignaciones sean correctas y que valide las operaciones con los tipos de datos regresando el tipo de dato que se obtiene.

Hubo cambios ligeros en las reglas de gramatica por potenciales problemas en el futuro

Primeros avances para la generación de cuadruplos

Lista de dudas para resolver en asesoría o clase para la proxima semana

### Avance 3

Ya se puede hacer la parte de manejo de expreciones con los datos reales desde el parsers, creación de la primer draft de la tabla de direcciones virtuales, asignación exitosa, probando con pass3.txt. Manejo de posibles nuevos errores. Mi compu murió esta seamana y perdí avances de la generación de cuadruplos, pero ya es cosa de reescibirlo, también se agregó la sección de project en GITHUB para tener un mejor control de lo que me falta y que hacer en cada avance

### Avance 4

* Se quitaron muchos prints de pruebas que ya no se necesitaban
* Se modifico el acomodo de la memoria virtual
* Definición del objeto cuadruplo para manejar solo 4 ints
* Funciones para obtener las direcciones virutales según sea el caso
* Moficaciones que ya permiten agregar correctamente cosas a la tabla de variables locales y globales
* Se generan los cuadruplos de asignación
* Lógica integrada para los cuadruplos arietméticos _no jalando al 100_

En general está rezagado el avance a lo que debería de ser pero me pondré al corriente esta semana i, espero un avance 4.5 a mitad de la semana 

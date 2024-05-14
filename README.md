# **Data Challenge 3**
Este repositorio busca profundizar en los conceptos principales de Git a través de la colaboración en un proyecto de software existente que simula eventos astronómicos utilizando programación orientada a objetos. Este challenge está diseñado para que los estudiantes de astrofísica con mención en ciencia de datos apliquen y evalúen sus habilidades en control de versiones en un contexto de desarrollo colaborativo.

## **Documentación de Clases y funciones**:

### **Clases**:
1. **Estrella**:
    Clase que representa una estrella. Sus atributos principales son:

    * *Atributos*:
        - nombre: El nombre de la estrella. (público)
        - masa: La masa de la estrella. (protegido)
        - radio: El radio de la estrella. (protegido)
        - temperaturasuperficial: La temperatura superficial de la estrella. (protegido)
        - distancia: La distancia de la estrella. (protegido)
        - movimientopropio: El movimiento propio de la estrella. (protegido)

    * *Funciones de la clase*:
        - **luminosidad_total**: Calcula la luminosidad total de la estrella.
        - **luminosidad_secuencia_principal**: Calcula la luminosidad de la estrella en la secuencia principal.
            Parámetros:
            - l_sol: La luminosidad del Sol.
            - m_sol: La masa del Sol.
        - **(NUEVA)** **radio_schwarzschild**: Calcula el radio de Schwarzschild de la estrella.    
            Parámetros:
            - g: La constante de gravitación universal.
            - c: La velocidad de la luz.

2. **Planeta**:
    Clase que representa un planeta que orbita alrededor de una estrella. Un planeta es un cuerpo con masa menor que 13 Mjup (masas de Júpiter) que orbita una estrella. 
    Los atributos principales de un planeta son:
    
    * *Atributos*:
        - nombre: El nombre del planeta.
        - estrella_protegida: La estrella alrededor de la cual orbita el planeta.
        - masaplanetaria: La masa del planeta en masas de Júpiter.
        - radio: El radio del planeta.
        - a: El semieje mayor de la órbita del planeta.
        - i: La inclinación de la órbita del planeta.
        - e: La excentricidad de la órbita del planeta.
        - periastron: El argumento del periastron del planeta.
    
    * *Funciones de la clase*:
        - **periodo_rotacion_kepleriana**:Calcula y devuelve el periodo de rotación kepleriano del planeta.
            Parámetros:
            - g: La constante gravitacional.
        - **(NUEVA)** **velocidad_escape**(self,g): Calcula y devuelve la velocidad de escape del planeta.
            Parámetros:
            - g: La constante gravitacional.

3. **PlanetaExoplanetario(Planeta)**
    Clase que representa un planeta exoplanetario, es decir, un planeta con una estrella anfitriona que no es el Sol.
    Hereda de la clase Planeta.

    * *Atributos*:
        - *"Los mismos de planeta"*

    * *Funciones de la clase*:
        - **metodo_descubrimiento**: Determina el método de primer descubrimiento del planeta exoplanetario, si por ”imagen directa”, ”velocidad radial” o ”transito”.
        
        - **tatooine**: Determina si el planeta es similar a Tatooine, es decir, si orbita alrededor de una estrella binaria.

4. **SistemaJerarquico**:
    Clase que representa un sistema jerárquico, que es un sistema estelar múltiple compuesto por N ≥ 2 estrellas.
    Los atributos principales de un sistema jerárquico son:
    
    * *Atributos*:
        - estrellas: Una lista de estrellas que contiene (tipo lista).

    * *Funciones de la clase*:
        - **agregar_estrella**: Agrega una estrella al sistema jerárquico.      
        Parámetros:
            - estrella: La estrella a agregar al sistema jerárquico.
        
        * **devolver_por_masa**: Devuelve la lista de estrellas ordenada por masa estelar.
        
        * **devolver_por_nombres**: Imprime los nombres de las estrellas seguidos de la lista ordenada de letras del alfabeto. 

5. **SistemaPlanetario**:
    Clase que representa un sistema planetario, que es el conjunto de planetas que orbitan una estrella dada.
    
    * *Atributos*:
        - estrella: El nombre de la estrella alrededor de la cual orbitan los planetas.
        - planetas: Una lista de objetos de la clase Planeta que representan los planetas en el sistema.

    * *Funciones de la clase*:
        - **numero_planetas**: Devuelve el número de planetas en el sistema (Entero).

        - **planetas_ordenados**: Devuelve la lista de planetas ordenada según su radio semimayor de la órbita. Si un planeta no tiene un radio semimayor definido, se indica en la cadena correspondiente
        
### **Funciones**:

* **def crear_estrella(data, nombre_estrella)**:
    Crea una instancia de la clase Estrella a partir de los datos de una estrella y su nombre.

    * Argumentos:
        - data (DataFrame): DataFrame de pandas con los datos de una estrella.
        - nombre (str): El nombre de la estrella.

    * Return:
        Información de la estrella y si sus datos se encuentran en la base de datos o no.

* **def crear_sistema(data, estrella)**:
    Crea un sistema planetario a partir del DataFrame con los datos de planetas exoplanetarios y el nombre de la estrella a la que orbita.

    * Argumentos:
        - data (DataFrame): DataFrame de pandas con los datos del planeta.
        - estrella (Class): un objeto de la clase Estrella.

    * Return:
        Información del sistema planetario, con respectivos métodos de clases, y si los datos se encuentran en la base de datos o no.

## Dependencias:
* numpy==1.26.4
* pandas==2.2.2

<!-- Títulos -->
# Títulos H
* # H1
* ## H2
* ### H3
* #### H4
* ##### H5
* ###### H6

<!-- Tipografía -->
# Tipografía
Italica con *asteriscos* o _guiones bajos_

Negrita con **dobles asteriscos** o __dobles guiones bajos__

Combined emphasis with ***asterisks* and _underscores_**

Tachado con ~~dobles virgulillas~~ pulsando **AltGr+4**

<!-- Listas -->
# Listas
## Listas ordenadas OL
1. Primer nodo
    1. Primer sub-nodo
       1. Primer sub-sub nodo
    2. Segundo sub-nodo
2. Segundo nodo

## Listas desdordenadas UL
* Primer nodo
    * Primer sub-nodo
      * Primer sub-sub nodo
    * Segundo sub-nodo
* Segundo nodo

### Listas desordenadas se pueden poner con:
* \*
- \-
+ \+

<!-- Enlaces -->
# Enlaces
+ https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet
+ <https://www.youtube.com/watch?v=y6XdzBNC0_0&ab_channel=JavierCristobalGutierrez>

+ [Wiki Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)

+ [Wiki Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet "Tooltip")
## Imágenes
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Tooltip")

<!-- Código -->
# Código
## Codigo en linea
Se usan las comas de parrafo `string saludo = "Hola mundo"`
## Codigo en parrafo
~~~
String saludo = "Hola mundo";
syso(saludo);
~~~
## Sintaxis para lenguajes
+ HTML:
    ```html
    <p class="bony fabada">Hola mundo</p>
    ```
+ CSS:
    ```css
    .fabada{
        background: rgba(243, 103, 199, 1.0);
    }
    ```
+ JS:
    ```javascript
    console.log('Hola mundo')
    ```
+ Python:
    ```python
    print('Hola mundo')
    ```
+ Java:
    ```java
    public void imprimir(String texto){
        System.out.println("Hola " + texto);
    }
    ```
+ C++:
    ```cpp
    printf("Hola mundo");
    ```
+ Go:
    ```go
    fmt.Printf("Hola mundo");
    ```
+ Rust:
    ```rust
    println!("Hola mundo");
    ```

<!-- Tablas -->
# Tablas
| Tables        |      Are      |         Cool |
| ------------- | :-----------: | -----------: |
| col 3 is      | right-aligned | left-aligned |
| col 2 is      |   centered    |          $12 |
| zebra stripes |   are neat    |           $1 |
| nueva columna |      soy      |     tu padre |
<!-- Citas -->
# Citas
> **Markdown** para ficheros **readme.md**

<!-- Separadores -->
# Separadores \<br\>
Con ___ tres guiones bajos
___

<!-- También renderiza HTML -->
# También renderiza HTML
<marquee>
    <dl>
        <dt>Coffee</dt>
            <dd>Disponible: frio y caliente</dd>
        <dt>Milk</dt>
            <dd>Disponible: entera, desnatada, sin lactosa</dd>
    </dl>
    <details>
        <summary>Acordeón desplegable</summary>
        ¿Dónde caemos gente?
    </details>
</marquee>

<!-- Expresiones matemáticas -->
# Expresiones matemáticas
Usando $ para encerrar la expresión

$-b \pm \sqrt{b^2 - 4ac} \over 2a$
$x = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + a_4}}}$
$\forall x \in X, \quad \exists y \leq \epsilon$


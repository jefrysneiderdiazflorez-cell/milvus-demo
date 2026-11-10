# Ejemplo de Milvus: recomendador de películas

Ejemplo sencillo de búsqueda por similitud usando Milvus, una base de datos vectorial de código abierto.

## Qué es Milvus

Milvus es una base de datos vectorial. En lugar de guardar solo texto o números sueltos, guarda cada elemento como un vector (una lista de números) y permite encontrar rápidamente los elementos más parecidos a una consulta. Se usa en recomendadores, búsqueda de imágenes, búsqueda semántica de texto y aplicaciones de inteligencia artificial como RAG.

## Para qué sirve este ejemplo

El ejemplo muestra una búsqueda por similitud con un recomendador de películas.

Cada película se representa con 3 números que indican cuánto tiene de cada género, de 0 a 1:

| Posición | Significado |
|----------|-------------|
| 1        | Acción      |
| 2        | Romance     |
| 3        | Comedia     |

Por ejemplo, Mad Max es `[0.9, 0.1, 0.2]`: mucha acción, poco romance y algo de comedia.

La consulta del ejemplo es `[0.9, 0.1, 0.6]`, que significa "quiero mucha acción y algo de comedia". Milvus compara ese vector con todas las películas y devuelve las 3 más cercanas usando la métrica COSINE (mientras más cerca de 1, más parecidas son).

## Versión usada

Milvus Lite, la versión gratuita y de código abierto de Milvus. Corre de forma local y guarda los datos en un archivo, por lo que no necesita servidor ni cuenta.

## Estructura del repositorio

```
milvus-demo/
├── README.md
├── demo.py
└── requirements.txt
```

## Cómo ejecutarlo

Milvus Lite funciona en Linux y macOS. No corre de forma nativa en Windows, así que la forma más simple de ejecutarlo es con GitHub Codespaces, que abre un entorno Linux en el navegador sin instalar nada.

### Opción 1: GitHub Codespaces

1. En la página principal del repositorio, haz clic en **Code**.
2. Abre la pestaña **Codespaces** y haz clic en **Create codespace on main**.
3. Cuando cargue el entorno, abre la terminal y ejecuta:

```bash
pip install -r requirements.txt
python demo.py
```

### Opción 2: Linux, macOS o WSL

1. Clona el repositorio:

```bash
git clone https://github.com/jefrysneiderdiazflorez-cell/milvus-demo.git
cd milvus-demo
```

2. Crea un entorno virtual e instala las dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Ejecuta el ejemplo:

```bash
python demo.py
```

## Qué hace el código

1. Crea una base de datos local (`peliculas.db`) y una colección de vectores de 3 dimensiones.
2. Inserta 6 películas con su vector de géneros.
3. Busca las 3 películas más parecidas a la consulta `[0.9, 0.1, 0.6]`.
4. Imprime los resultados con su porcentaje de similitud.

## Resultado esperado

Los valores pueden variar ligeramente:

```
Colección creada
Se insertaron 6 películas

Te recomiendo:
  Deadpool  (similitud: 0.97)
  John Wick  (similitud: 0.95)
  Mad Max  (similitud: 0.90)
```

## Idea clave

Milvus no compara palabras: compara números. Cada elemento es un punto en un espacio y la búsqueda devuelve los puntos más cercanos a la consulta. En aplicaciones reales, los vectores los genera un modelo de inteligencia artificial (embeddings) a partir de texto, imágenes o audio, y pueden tener cientos de dimensiones.

## Seguridad

Este repositorio no contiene contraseñas, claves de acceso ni tokens. El ejemplo se ejecuta de forma local y no se conecta a ningún servicio externo.

## Autor

Jefry Sneider Díaz Flórez
Ingeniería Multimedia

## Referencias

- Repositorio oficial de Milvus: https://github.com/milvus-io/milvus
- Documentación: https://milvus.io/docs
- Cliente de Python (pymilvus): https://github.com/milvus-io/pymilvus

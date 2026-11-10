from pymilvus import MilvusClient

# 1. Conectar (crea un archivo local, no necesita servidor)
client = MilvusClient("peliculas.db")

# Borrar la colección si ya existía (para poder repetir el ejemplo)
if client.has_collection("peliculas"):
    client.drop_collection("peliculas")

# 2. Crear la colección: vectores de 3 dimensiones
#    COSINE mide qué tan parecida es la "dirección" de dos vectores
client.create_collection(
    collection_name="peliculas",
    dimension=3,
    metric_type="COSINE",
)
print("✔ Colección creada")

# 3. Insertar datos: cada película tiene su vector [acción, romance, comedia]
peliculas = [
    {"id": 1, "vector": [0.9, 0.1, 0.2], "titulo": "Mad Max"},
    {"id": 2, "vector": [0.8, 0.2, 0.3], "titulo": "John Wick"},
    {"id": 3, "vector": [0.1, 0.9, 0.2], "titulo": "Titanic"},
    {"id": 4, "vector": [0.2, 0.8, 0.6], "titulo": "Mi gran boda griega"},
    {"id": 5, "vector": [0.1, 0.2, 0.9], "titulo": "Superbad"},
    {"id": 6, "vector": [0.7, 0.1, 0.8], "titulo": "Deadpool"},
]
client.insert(collection_name="peliculas", data=peliculas)
print("✔ Se insertaron", len(peliculas), "películas")

# 4. Buscar: "quiero mucha acción y algo de comedia"
consulta = [0.9, 0.1, 0.6]

resultados = client.search(
    collection_name="peliculas",
    data=[consulta],
    limit=3,                      # las 3 más parecidas
    output_fields=["titulo"],     # qué dato queremos recuperar
)

# 5. Mostrar los resultados
print("\nTe recomiendo:")
for r in resultados[0]:
    print(f"  {r['entity']['titulo']}  (similitud: {r['distance']:.2f})")

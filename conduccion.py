from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["yovoybd"]
conduccion = db["conduccion"]

def agregar_conduccion(conduccion):
    conduccion.insert_one(conduccion)
    print("la conducción fue agregada.")

def leer_conduccion(id_conduccion):
    return conduccion.find_one({"id_conduccion": id_conduccion})

def actualizar_conduccion(id_conduccion, actualizacion):
    conduccion.update_one({"id_conduccion": id_conduccion}, {"$set": actualizacion})
    print("la conducción fue actualizada.")

def eliminar_conduccion(id_conduccion):
    conduccion.delete_one({"id_conduccion": id_conduccion})
    print("la conducción fue eliminada.")

if __name__ == "__main__":
    conduccion = {
        "id_conduccion": "C001",
        "id_vehiculo": "V001",
        "nivel_agresividad": 2,
        "frecuencia_frenadas": 3,
        "fecha_registro": "2025-02-28",
        "patrones_conduccion": "Aceleración suave, frenado brusco"
    }
    agregar_conduccion(conduccion)

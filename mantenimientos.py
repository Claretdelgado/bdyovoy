from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["yovoybd"]
mantenimientos = db["mantenimientos"]

def agregar_mantenimiento(mantenimiento):
    mantenimientos.insert_one(mantenimiento)
    print("El mantenimiento fue agregado.")

def leer_mantenimiento(id_mantenimiento):
    return mantenimientos.find_one({"id_mantenimiento": id_mantenimiento})

def actualizar_mantenimiento(id_mantenimiento, actualizacion):
    mantenimientos.update_one({"id_mantenimiento": id_mantenimiento}, {"$set": actualizacion})
    print("El mantenimiento fue actualizado.")

def eliminar_mantenimiento(id_mantenimiento):
    mantenimientos.delete_one({"id_mantenimiento": id_mantenimiento})
    print("El mantenimiento fue eliminado.")

if __name__ == "__main__":
    mantenimiento= {
        "id_mantenimiento": "M001",
        "id_vehiculo": "V001",
        "tipo_mantenimiento": "Preventivo",
        "piezas_cambiadas": ["Filtro de aceite", "Llantas"],
        "tiempo_estimado_reparacion": 4,
        "fecha_programada": "2025-04-015",
        "fecha_realizado": "2025-05-28",
        "alertas_fallas": ["Sensor de oxígeno"],
        "vida_util_piezas": 5000
    }
    agregar_mantenimiento(mantenimiento)

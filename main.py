import vehiculos
import sensores
import conduccion
import mantenimiento

if __name__ == "__main__":
    vehiculo = {
        "id_vehiculo": "V001",
        "modelo": "mercedes",
        "marca": "Mercedes",
        "año": 2018,
        "kilometraje": 120000,
        "estado_actual": "Bueno",
        "fecha_ultimo_mantenimiento": "2025-02-20",
        "ubicacion_actual": "Aguascalientes",
        "nivel_combustible": 65,
        "estado_motor": "Óptimo",
        "horas_operacion": 3500
    }
    vehiculos.crear_vehiculo(vehiculo)

    sensor= {
        "id_sensor": "S001",
        "id_vehiculo": "V001",
        "aceleracion": 1.2,
        "frenado": 0.3,
        "velocidad_actual": 80,
        "vibraciones": 0.02,
        "temperatura_motor": 90,
        "ubicacion_gps": "19.432608,-99.133209",
        "fecha_registro": "2025-02-28T21:00:00",
        "horas_motor": 100
    }
    sensores.crear_sensor(sensor)

    conduccion= {
        "id_conduccion": "C001",
        "id_vehiculo": "V001",
        "nivel_agresividad": 2,
        "frecuencia_frenadas": 3,
        "fecha_registro": "2025-02-28",
        "patrones_conduccion": "Aceleración suave, frenado brusco"
    }
    conduccion.crear_conduccion(conduccion)

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
    mantenimiento.crear_mantenimiento(mantenimiento)

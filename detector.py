import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict

def detectar_fuerza_bruta(archivo_csv, umbral=5, ventana_minutos=10):
    """
    Detecta posibles ataques de fuerza bruta:
    +5 intentos fallidos desde la misma IP en 10 minutos
    """
    try:
        df = pd.read_csv(archivo_csv)
        df['login_date'] = pd.to_datetime(df['login_date'])

        # Filtrar solo intentos fallidos
        fallidos = df[df['login_success'] == 0]

        print(f"Analizando {len(df)} intentos de login...")
        print(f"Encontrados {len(fallidos)} intentos fallidos\n")

        sospechosos = []
        reporte = []

        # Agrupar por IP
        for ip in fallidos['login'].unique():
            intentos_ip = fallidos[fallidos['login'] == ip].sort_values('login_date')

            # Ventana deslizante de 10 minutos
            for i in range(len(intentos_ip)):
                ventana_inicio = intentos_ip.iloc[i]['login_date']
                ventana_fin = ventana_inicio + timedelta(minutes=ventana_minutos)

                intentos_ventana = intentos_ip[
                    (intentos_ip['login_date'] >= ventana_inicio) &
                    (intentos_ip['login_date'] <= ventana_fin)
                ]

                if len(intentos_ventana) >= umbral:
                    sospechosos.append({
                        'IP': ip,
                        'intentos': len(intentos_ventana),
                        'inicio': ventana_inicio,
                        'fin': ventana_fin,
                        'usuarios_atacados': intentos_ventana['username'].nunique()
                    })
                    break # Evitar duplicados

        # Generar reporte
        with open('reporte_sospechosos.txt', 'w') as f:
            f.write("=== REPORTE DE DETECCION DE FUERZA BRUTA ===\n")
            f.write(f"Fecha analisis: {datetime.now()}\n")
            f.write(f"Umbral: {umbral} intentos en {ventana_minutos} minutos\n")

            if sospechosos:
                f.write(f"ALERTA: Se detectaron {len(sospechosos)} IPs sospechosas:\n\n")
                for s in sospechosos:
                    linea = f"IP: {s['IP']} | Intentos: {s['intentos']} | "
                    linea += f"Ventana: {s['inicio']} a {s['fin']} | "
                    linea += f"Usuarios atacados: {s['usuarios_atacados']}\n"
                    f.write(linea)
                    reporte.append(linea)
            else:
                f.write("No se detectaron patrones de fuerza bruta.\n")

        print("REPORTE GENERADO: reporte_sospechosos.txt")
        for r in reporte:
            print(r)

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo {archivo_csv}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    detectar_fuerza_bruta("log_in_attempts.csv")
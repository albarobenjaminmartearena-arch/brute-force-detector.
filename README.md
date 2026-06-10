# Brute Force Detector

Script en Python que analiza logs de login y detecta ataques de fuerza bruta.

## Qué hace
Busca +5 intentos fallidos desde la misma IP en 10 minutos usando Pandas.

## Cómo usarlo
```bash
python detector.py
## Evidencias

### Captura 1: Ejecución del script en terminal
![Captura de terminal ejecutando detector.py](captura1.png)

### Captura 2: Contenido del reporte generado  
![Reporte de IPs sospechosas](captura2.png)

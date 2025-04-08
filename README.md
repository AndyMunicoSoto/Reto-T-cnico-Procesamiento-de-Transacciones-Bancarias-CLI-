# Reto-T-cnico-Procesamiento-de-Transacciones-Bancarias-CLI-

## Introducción:

Este proyecto tiene como objetivo desarrollar una aplicación de línea de comandos (CLI) que procesa un archivo CSV con transacciones bancarias. El programa genera un reporte que incluye lo siguiente:

Balance Final: Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".

Transacción de Mayor Monto: Identificar el ID y el monto de la transacción con el valor más alto.

Conteo de Transacciones: Número total de transacciones para cada tipo ("Crédito" y "Débito").

## Instrucciones de Ejecución:

Requisitos: Tener **Python** 3 

Dependencias: Libreria **Pandas** para la manipulación del archivo **CSV**

EJECUCIÓN: 

1. Clona el repositorio.

2. Verificar que el archivo CSV  este en el mismo directorio que el script o especific a la ruta.

3. Ejecuta el script con el siguiente comando: python script.py data.csv

## Enfoque y Solución:
Explica de forma concisa la lógica implementada y las decisiones de diseño que tomaste.

La lógica de la aplicación:

1. Lectura del archivo CSV: Utilicé pandas para leer el archivo CSV con las transacciones bancarias.

2. Cálculo del Balance Final: Se calculan las sumas de los montos de las transacciones de tipo "Crédito" y "Débito" por separado, y luego se obtiene la diferencia para el balance final.

3. Transacción de Mayor Monto: Se identifica la transacción con el valor máximo en la columna 'monto', y se obtiene la fila correspondiente con el ID y monto.

4. Conteo de Transacciones: Usamos el metodo shape de pandas para obtener el número de transacciones de tipo "Crédito" y "Débito".


## Estructura del Proyecto:
/Proyecto

│

├── script.py                # Archivo principal que contiene la lógica 

├── data.csv                 # Archivo CSV con las transacciones bancarias

└── README.md                # Documentación

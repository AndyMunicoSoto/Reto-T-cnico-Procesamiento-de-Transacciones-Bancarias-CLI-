import pandas as pd

def procesar_transacciones(csv_file):
   """
    Esta función procesa un archivo CSV de transacciones bancarias y genera un reporte con:
    - El balance final (diferencia entre los montos de 'Crédito' y 'Débito').
    - La transacción de mayor monto.
    - El conteo de transacciones por tipo ('Crédito' y 'Débito').

    Parámetros:
    csv_file (str): La ruta al archivo CSV que contiene las transacciones bancarias. 
                    El archivo debe tener las columnas 'id', 'tipo' y 'monto'.
    """

    # Cargamos los datos del archivo CSV
    df = pd.read_csv(csv_file)

    # Calculamos la suma de los montos de las transacciones de tipo 'Crédito' y 'Débito'
    monto_credito = df[df['tipo'] == 'Crédito']['monto'].sum()
    monto_debito = df[df['tipo'] == 'Débito']['monto'].sum()

    # Calculamos el balance final
    balance_final = monto_credito - monto_debito

    # Obtenemos el registro con el monto máximo
    registro_max = df.loc[df['monto'].idxmax()]

    # Contamos el número de transacciones de tipo 'Crédito' y 'Débito'
    conteo_credito = df[df['tipo'] == 'Crédito'].shape[0]
    conteo_debito = df[df['tipo'] == 'Débito'].shape[0]

    # Mostramos el reporte de transacciones
    print("Reporte de Transacciones")
    print("----------------------------------")
    print(f"Balance Final: {balance_final}")
    print(f"Transacción de Mayor Monto: ID {registro_max['id']} - {registro_max['monto']}")
    print(f"Conteo de Transacciones : Crédito: {conteo_credito} Débito: {conteo_debito}")

# Llamamos a la función pasando el archivo CSV
procesar_transacciones('data.csv')

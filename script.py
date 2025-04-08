import pandas as pd

def procesar_transacciones(csv_file):
   
    df = pd.read_csv(csv_file)

    
    monto_credito = df[df['tipo'] == 'Crédito']['monto'].sum()
    monto_debito = df[df['tipo'] == 'Débito']['monto'].sum()
    balance_final = monto_credito - monto_debito

    
    registro_max = df.loc[df['monto'].idxmax()]


    conteo_credito = df[df['tipo'] == 'Crédito'].shape[0]
    conteo_debito = df[df['tipo'] == 'Débito'].shape[0]

    
    print("Reporte de Transacciones")
    print("----------------------------------")
    print(f"Balance Final: {balance_final}")
    print(f"Transacción de Mayor Monto: ID {registro_max['id']} - {registro_max['monto']:}")
    print(f"Conteo de Transacciones : Crédito: {conteo_credito} Dédito: {conteo_debito}")

procesar_transacciones('data.csv')

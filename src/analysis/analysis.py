import pandas as pd  
import os
from ..decorators.decorators import timeit, logit  

@logit  
@timeit  
def load_data(data_path):
    
    if data_path.endswith('.csv'):
        df = pd.read_csv(data_path)  
    else:
        raise ValueError("Unsupported file format")  
    print("Data loaded successfully")  
    return df  

@logit  
@timeit  
def analyze_data(df):
    print("Basic Data Analysis:")  
    print(df.describe())  
    # print("\nProducts with highest prices:")  
    # print(pd.to_numeric(df.nlargest(5, 'Price')))  


if __name__ == "__main__":
    data_path = "data/products.csv"  
    output_path = "data/processed/cleaned_products.csv"  
    
    df = load_data(data_path)  # Carga los datos 
    analyze_data(df)  # Analiza los datos
    # os.makedirs("/data/processed", exist_ok=True)  # Crea el directorio de salida si no existe
  
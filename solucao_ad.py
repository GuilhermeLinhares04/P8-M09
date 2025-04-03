import polars as pl
import time

def convert_csv_to_parquet(csv_file: str, parquet_file: str, sep: str = ";"):
    df = pl.read_csv(csv_file, separator=sep, new_columns=["station", "temperature"])
    df.write_parquet(parquet_file)
    print(f"Arquivo convertido para Parquet: {parquet_file}")

def aggregate_temperatures_to_csv(parquet_file: str, output_csv: str):
    start_time = time.time()

    df_lazy = pl.scan_parquet(parquet_file)
    result = (
        df_lazy
        .groupby("station")
        .agg([
            pl.col("temperature").max().alias("max_temperature"),
            pl.col("temperature").min().alias("min_temperature"),
            pl.col("temperature").mean().alias("mean_temperature"),
        ])
        .collect()
    )
    
    result.write_csv(output_csv)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("Tabela agregada (máximo, mínimo e média) salva como CSV:")
    print(result)
    print(f"Tempo de execução: {elapsed_time:.4f} segundos")

if __name__ == "__main__":
    csv_file = "measurements.txt"
    parquet_file = "measurements.parquet"
    output_csv = "aggregated_temperatures.csv"

    # Converter o CSV para Parquet (opcional, mas recomendado para otimização)
    convert_csv_to_parquet(csv_file, parquet_file)

    # Agregar os dados e salvar em um arquivo CSV
    aggregate_temperatures_to_csv(parquet_file, output_csv)

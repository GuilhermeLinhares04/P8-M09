import csv
import time
from collections import defaultdict

def process_temperatures(file_name, output_file):
    start_time = time.time()
    station_data = defaultdict(list)

    # Lê o arquivo e organiza os dados por estação
    with open(file_name, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            try:
                station = row[0]
                temperature = float(row[1])
                station_data[station].append(temperature)
            except (ValueError, IndexError):
                continue

    # Calcula os resultados por estação
    results = []
    for station, temperatures in station_data.items():
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        avg_temp = sum(temperatures) / len(temperatures)
        results.append([station, max_temp, min_temp, avg_temp])

    # Salva os resultados em um arquivo CSV
    with open(output_file, mode='w', encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Estação", "Máximo", "Mínimo", "Média"])
        writer.writerows(results)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Arquivo de saída '{output_file}' gerado com sucesso.")
    print(f"Tempo de processamento: {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    process_temperatures("measurements.txt", "output.csv")

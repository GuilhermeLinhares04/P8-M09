# Desafio: Processamento de 1 Bilhão de Linhas

Este repositório apresenta soluções para o desafio de processar um arquivo de **1 bilhão de linhas** contendo medições de temperatura.
Foram desenvolvidas duas abordagens:

1. **Solução Simples:** Utilizando leitura sequencial com o módulo `csv` do Python.
2. **Solução Otimizada:** Utilizando a biblioteca `Polars` e conversão para Parquet para melhorar a eficiência.

---

# 🎥 Vídeo Explicativo
![Vídeo Explicativo](https://youtu.be/LhdQwwtz99s)

---

## 📊 1. Gerando o Arquivo de 1 Bilhão de Linhas

O arquivo `createMeasurements.py` gera o dataset `measurements.txt`, onde cada linha tem o seguinte formato:

```
StationA;23.5
StationB;18.2
StationC;30.1
```

🔹 **Formato:** `nome_da_estacao;temperatura`
🔹 **Tamanho esperado:** ~12GB para 1 bilhão de linhas
🔹 **Gerado usando escrita sequencial em modo `append`**

Para executar:
```bash
python createMeasurements.py
```

---

## 🛠 2. Solução Simples (CSV)

O arquivo `solucao_bs.py` faz a leitura linha por linha e soma as temperaturas utilizando a biblioteca `csv`.

### 🚨 Problemas da Solução Simples
❌ Lenta para arquivos massivos (leitura sequencial)
❌ Alto consumo de CPU sem aproveitamento de paralelismo

---

## 🚀 3. Solução Otimizada (Polars + Parquet)

O arquivo `solucao_ad.py` converte os dados para o formato **Parquet**, que é mais eficiente para leitura e agregações.

### **Etapas:**
1️⃣ **Converte o CSV para Parquet** (compressão reduz o tamanho em até 90%)
2️⃣ **Usa Lazy Evaluation** para processar apenas o necessário
3️⃣ **Utiliza paralelismo** para acelerar os cálculos

### 🎯 **Benefícios da Otimização**
✅ **Processamento paralelo** utilizando todos os núcleos do CPU
✅ **Lazy Evaluation** (evita carregamento desnecessário de dados)
✅ **Redução de tamanho** (CSV ~13.5GB → Parquet ~3GB)
✅ **Leitura otimizada** (apenas colunas necessárias são carregadas)

---

## 🔥 4. Comparativo de Desempenho

| Solução | Tempo de Execução | Uso de Memória | Paralelismo |
|-----------|----------------|--------------|-------------|
| CSV Simples | Alto (~horas) | Alto         | Não        |
| Polars + Parquet | Baixo (~minutos) | Baixo        | Sim        |

---

## 🔧 5. Possíveis Melhorias

🔹 **Particionamento no Parquet** (dividir por estação meteorológica)
🔹 **Uso de DuckDB ou Spark** para processamento distribuído
🔹 **Armazenamento em SSD NVMe** para reduzir latência de I/O
🔹 **Multithreading na leitura do CSV**

---
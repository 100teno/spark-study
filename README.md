
## 🚀 Tecnologias Utilizadas

- 💻 **Databricks (runtime baseado em Apache Spark)**
- 🐍 **PySpark (API de DataFrames)**
- 🐘 **Delta Lake (armazenamento transacional)**
- 🧪 Notebooks interativos com comandos `display()`, `printSchema()` e `count()`

## 📌 Principais Conceitos Abordados

### ✅ Lazy Evaluation
Demonstração prática de como transformações em Spark (ex: `.filter()`, `.select()`) não são executadas até uma *ação* ser chamada (ex: `.show()`, `.count()`, `.write()`).

### 🔁 Deduplicação de Dados
- Identificação de duplicatas com `.groupBy().count()`
- Uso da função `dropDuplicates()` para eliminar entradas repetidas
- Aplicação de `Window Functions` com `row_number()` para manter o registro mais recente por chave de negócio

### 📊 Análise Exploratória
- Contagem total e por categoria (`lead_status`)
- Contagem de valores únicos por coluna com `approx_count_distinct`

## 🧪 Simulação com Dummy Data

Todos os dados utilizados neste projeto foram **anonimizados** ou gerados sinteticamente para fins educacionais.

### Exemplo de Schema Simulado

| Coluna               | Tipo       | Descrição                        |
|----------------------|------------|----------------------------------|
| lead_opportunity_id  | string     | Identificador da oportunidade    |
| lead_status          | string     | Status do lead (ex: CONTACTED)   |
| lead_open_dt         | timestamp  | Data de abertura                 |
| etl_timestamp        | timestamp  | Timestamp de ingestão            |
| etl_med_timestamp    | timestamp  | Timestamp intermediário          |

## 📂 Como Rodar Localmente

> ⚠️ Requer ambiente com **PySpark** configurado ou uso do **Databricks Community Edition**.

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/eda-databricks-bronze.git
cd eda-databricks-bronze

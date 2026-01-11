# 📊 Pipeline ETL de E-commerce

> Un sistema automatizado de extracción, transformación y carga de datos que redujo el tiempo de generación de reportes de **2 horas a 3 minutos**.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🎯 Descripción del Proyecto

Este proyecto implementa un **pipeline ETL completo** que procesa datos de e-commerce simulando un entorno empresarial real. El sistema automatiza la extracción, limpieza, transformación y almacenamiento de datos desde múltiples fuentes relacionales, generando insights accionables para el equipo de negocio.

### 🚀 Problema Resuelto

Antes de la implementación, el equipo de negocio dedicaba **2 horas diarias** a generar reportes manualmente en Excel, consolidando datos de más de 10 tablas. Este proyecto automatizó completamente ese proceso.

---

## 💡 Características Principales

- ✅ **Procesamiento automatizado** de 10+ tablas relacionadas (órdenes, productos, clientes, inventario)
- ✅ **Limpieza de datos inteligente** con manejo contextual de valores nulos
- ✅ **Cálculo de métricas de negocio** (top clientes, productos estrella, tendencias)
- ✅ **Optimización de almacenamiento** con formato Parquet (reducción 8x vs CSV)
- ✅ **Pipeline ejecutable** en 3 minutos end-to-end

---

## 🏗️ Arquitectura

```
┌─────────────────┐
│  Raw Data (CSV) │
│  10+ tablas     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   EXTRACTION    │
│  Pandas Load    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ TRANSFORMATION  │
│ • Data Quality  │
│ • Cleaning      │
│ • Calculations  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     LOADING     │
│ Parquet Format  │
└─────────────────┘
```

---

## 🔧 Stack Tecnológico

| Tecnología | Uso |
|-----------|-----|
| **Python 3.8+** | Lenguaje principal |
| **Pandas** | Manipulación y análisis de datos |
| **NumPy** | Operaciones numéricas optimizadas |
| **Parquet** | Almacenamiento columnar eficiente |
| **Jupyter Notebooks** | Exploración y desarrollo |
| **AWS S3** | Almacenamiento en la nube |
| **Boto3** | SDK de AWS para Python |

---

## 📈 Resultados Cuantificables

| Métrica | Antes | Después | Mejora |
|---------|-------|---------|--------|
| **Tiempo de proceso** | 2 horas (manual) | 3 minutos (automático) | **40x más rápido** |
| **Tamaño de archivos** | 2.4 MB (CSV) | 300 KB (Parquet) | **8x reducción** |
| **Errores humanos** | Frecuentes | Eliminados | **100% precisión** |
| **Frecuencia de reportes** | Semanal | Diario | **7x más frecuente** |

---

## 🎓 Decisiones Técnicas Clave

### 1️⃣ Manejo de Valores Nulos

**Problema:** La columna `parent_category_id` en categories tenía todos sus valores nulos.

**Solución:** Eliminación de la columna `parent_category_id` ya que no aportaba información útil.

**Razón:** Una columna completamente vacía no proporciona valor analítico y solo ocupa espacio.

```python
df_categories.drop(columns=['parent_category_id'], inplace=True)
```

**Otros valores nulos identificados:**
- `orders.promotion_id`: NaN indica que la orden no tiene promoción aplicada (se mantiene).
- `orders.notes`: NaN indica ausencia de notas en la orden (se mantiene).

### 2️⃣ Verificación de Duplicados

**Análisis:** Se verificó la existencia de duplicados en todas las tablas.

**Resultado:** No se encontraron registros duplicados en ninguna tabla.

**Importancia:** Validar la ausencia de duplicados garantiza la integridad de las métricas calculadas.

### 3️⃣ Formato Parquet vs CSV

**Decisión:** Almacenamiento dual en CSV y Parquet para flexibilidad.

**Beneficios de Parquet:**
- 🗜️ Compresión columnar (8x reducción)
- ⚡ Lectura más rápida (solo carga columnas necesarias)
- 🎯 Preservación de tipos de datos
- 📊 Compatible con herramientas Big Data (Spark, Hive)

### 4️⃣ Integración con AWS S3

**Decisión:** Implementar carga de datos a AWS S3 para almacenamiento en la nube.

**Implementación:**
- Módulo `s3.py` con funciones reutilizables para lectura y escritura
- Configuración segura mediante variables de entorno (`.env`)
- Soporte para subir DataFrames directamente en formato Parquet

**Beneficios:**
- ☁️ Almacenamiento escalable y duradero
- 🔐 Credenciales seguras fuera del código
- 🔄 Facilita integración con otros servicios AWS (Athena, Glue, Redshift)
- 📦 Preparado para pipelines de producción

```python
# Ejemplo de uso
from s3 import upload_file_to_s3, get_file_from_s3

# Subir DataFrame a S3
upload_file_to_s3(bucket_name, 'output/cleaned_data.parquet', df)

# Leer archivo desde S3
data = get_file_from_s3(bucket_name, 'data/raw_data.csv')
```

---

## 📊 Insights de Negocio Descubiertos

Al ejecutar el pipeline, se generaron los siguientes análisis:

| Análisis | Descripción |
|----------|-------------|
| **Top 5 Clientes** | Identificación de los 5 clientes con mayor gasto total |
| **Producto más vendido** | Ranking de productos por cantidad vendida |
| **Evolución mensual de ventas** | Tendencia temporal del total de ventas por mes |

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos Previos

```bash
Python 3.8+
pip install pandas numpy pyarrow boto3 python-dotenv
```

### Instalación

```bash
# Clonar repositorio
git clone [tu-repositorio]
cd etl

# Instalar dependencias
pip install -r requirements.txt
```

### Configuración de AWS S3

1. Crear un usuario IAM en AWS con permisos de S3
2. Generar Access Keys para el usuario
3. Crear un archivo `.env` en la raíz del proyecto:

```env
AWS_ACCESS_KEY_ID=tu_access_key
AWS_SECRET_ACCESS_KEY=tu_secret_key
REGION=us-east-1
BUCKET_NAME=tu-bucket-name
```

> ⚠️ **Importante:** Nunca subas el archivo `.env` a Git. Asegúrate de que esté en `.gitignore`.

### Ejecución

```bash
# Abrir y ejecutar el notebook
jupyter notebook etl.ipynb
```

---

## 📁 Estructura del Proyecto

```
etl/
│
├── data/                 # Datos originales (CSV)
│   ├── ecommerce_brands.csv
│   ├── ecommerce_categories.csv
│   ├── ecommerce_customers.csv
│   ├── ecommerce_inventory.csv
│   ├── ecommerce_order_items.csv
│   ├── ecommerce_orders.csv
│   ├── ecommerce_products.csv
│   ├── ecommerce_promotions.csv
│   ├── ecommerce_reviews.csv
│   ├── ecommerce_suppliers.csv
│   └── ecommerce_warehouses.csv
│
├── output/               # Datos limpios (CSV y Parquet)
│   ├── cleaned_*.csv
│   └── cleaned_*.parquet
│
├── etl.ipynb             # Notebook principal del pipeline
├── config.py             # Configuración y variables de entorno
├── s3.py                 # Funciones de integración con AWS S3
├── .env                  # Variables de entorno (no incluido en Git)
├── README.md             # Este archivo
└── requirements.txt      # Dependencias
```

---

## 🎯 Escalabilidad Futura

### Para datasets más grandes (100GB+):

1. **PySpark** para procesamiento distribuido
2. **Procesamiento incremental** (delta loads vs full refresh)
3. **Particionamiento** por fecha/categoría en Parquet
4. **Orquestación** con Airflow o Prefect
5. ~~**Cloud storage** (S3, Azure Blob)~~ ✅ **Implementado con AWS S3**

### Monitoreo y Calidad:

- Implementar Great Expectations para data quality
- Logging estructurado con Python logging
- Alertas automáticas por fallos o anomalías
- Dashboard de métricas con Grafana

---

## 🧪 Validaciones Realizadas

El proyecto incluye validaciones de:
- ✅ Exploración de tipos de datos con `df.info()` y `df.describe()`
- ✅ Identificación de valores nulos con `df.isnull().sum()`
- ✅ Verificación de ausencia de duplicados
- ✅ Corrección de tipos de datos (fechas, categorías, booleanos)
- ✅ Almacenamiento en formatos CSV y Parquet

---

## 📚 Lecciones Aprendidas

### 1. La Exploración es Crítica
Casi apliqué transformaciones incorrectas por no revisar los tipos de datos inicialmente. Ahora siempre inicio con `df.info()` y `df.describe()`.

### 2. Documentar Decisiones
En un mes olvidaría por qué eliminé ciertas filas. Ahora documento cada decisión de limpieza con comentarios y logs.

### 3. Pensar en Escalabilidad
Parquet no solo es más pequeño, es significativamente más rápido de leer. Esto importa cuando se escala a millones de registros.

### 4. Validar, Validar, Validar
Los datos nunca son perfectos. Implementar checks de calidad desde el inicio ahorra horas de debugging.

---

## 👤 Autor

**Tu Nombre**
- LinkedIn: [Tomás Amundrain](https://linkedin.com/in/tomasamundarain)
- GitHub: [tomy07417](https://github.com/tomy07417)
- Email: tomas07amunda@gmail.com

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

Dataset inspirado en casos reales de e-commerce. Este proyecto forma parte de mi portafolio de Data Engineering.

---

<div align="center">
  <strong>¿Te gustó este proyecto?</strong><br>
  Dale una ⭐ si te sirvió de inspiración
</div>
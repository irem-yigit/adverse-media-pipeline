# Adverse Media Pipeline
<a name="readme-top"></a>
Adverse Media Pipeline, yurt içi ve yurt dışı haber kaynaklarından adverse media (olumsuz haber) içeriklerini otomatik olarak toplayan, depolayan ve çok katmanlı bir AI pipeline ile analiz eden uçtan uca bir veri işleme sistemidir.

Bu proje; web crawling, web scraping, veri depolama (PostgreSQL) ve AI tabanlı içerik analizi bileşenlerini ayrıştırılmış, ölçeklenebilir bir mimariyle ele alır.

## Projenin Amacı

* Finans, uyum (compliance), AML/KYC ve risk analiz süreçlerinde kritik öneme sahip olan adverse media haberlerinin:
* Günlük olarak otomatik toplanması
* İçeriklerinin analiz edilmesi
* Olumsuz/olumlu haber ayrımının yapılması
* Haber metinlerinden kişi, kurum ve organizasyonların çıkarılması amaçlanmaktadır.

## Tech Stack

- Python 3.14.2 version
- beautifulsoup4 (bs4)
- AI / NLP Modelleri (Sentiment & Entity Extraction)
- PostgreSQL 16 version

## Getting Started

### Requirements

To run the project, you must have the following software installed on your system:

- Python 3.10+
- urllib3
- beautifulsoup4 (bs4)
- lxml (opsiyonel)
- openai veya httpx
- PostgreSQL or another compatible SQL database

### Installation

1. **Clone the project:**

   ```bash
   git clone https://github.com/irem-yigit/adverse-media-pipeline.git
   ```

2. **Import library**

    - python -m venv venv
    - venv\Scripts\activate
    - pip install requests beautifulsoup4 urllib3 lxml python-dotenv

    
3. **Build the project:**


4. **Run the project:**

   Once the application is launched, you can start using the APIs.

5. **Running with Docker (optional):**

   To run the application with Docker, you can use the `docker-compose.yml` file located in the root directory of the project:

   ```bash
   docker-compose up --build
   ```
<p align="right"><a href="#readme-top">Back to the Top ↑ </a></p>

## API Test

   **Swagger URL:**

   ```bash
   http://localhost:8080/swagger-ui/index.html#/v3/api-docs
   ```
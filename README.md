# Adverse Media Pipeline
<a name="readme-top"></a>
Adverse Media Pipeline is an end-to-end data processing system that automatically collects, stores, and analyzes adverse media (negative news) content from domestic and international news sources using a multi-layered AI pipeline. This project adopts a decoupled, scalable architecture that integrates web crawling, web scraping, data storage, and AI-based content analysis components.

## Project Objective

The goal of this project is to support critical processes in finance, compliance, AML/KYC, and risk analysis by:

* Automatically collecting adverse media news on a daily basis
* Analyzing the content of collected news articles
* Classifying news as positive or negative
* Extracting people, companies, and organizations from news texts

## Tech Stack

- Python 3.14.2 version
- AI / NLP Models (Sentiment & Entity Extraction)
- PostgreSQL 16 version

## Getting Started

### Requirements

To run the project, you must have the following software installed on your system:

- Python 3.10+
- urllib3 2.6+
- beautifulsoup4 (bs4) 4.14+
- lxml (opsiyonel) 6.0+
- openai veya httpx
- PostgreSQL or another compatible SQL database
- Docker

### Installation

1. **Clone the project:**

   ```bash
   git clone https://github.com/irem-yigit/adverse-media-pipeline.git
   ```

2. **Create and active a virtual environment**

    ```bash
    python -m venv venv
    ```

    ```bash
    venv\Scripts\activate
    ```
    

3. **Import and check the library**

    ```bash
    pip install requests beautifulsoup4 urllib3 lxml python-dotenv
    ```

    ```bash
    pip list
    ```


4. **Run the project:**

    ```bash
   python main.py
    ```

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

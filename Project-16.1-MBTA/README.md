🚍 MBTA Route 1 Transit Data Engineering Pipeline

This project builds a complete real-time transit data pipeline that ingests live MBTA Route 1 bus data, stores it in MySQL, streams database changes into MongoDB using Debezium CDC, and visualizes bus activity using a Flask web dashboard.
A Jupyter Notebook provides analysis of route timings, speeds (via Haversine distance), and GPS movement.

📂 Repository Structure
Project-16.1-MBTA/
│
├── DebeziumCDC/              # Debezium + Spring Boot CDC listener
│   ├── Dockerfile
│   ├── pom.xml
│   └── src/main/...
│
├── flask_app/                # Flask dashboard + API client + MySQL loader
│   ├── MBTAApiClient.py
│   ├── mysqldb.py
│   ├── requirements.txt
│   └── server.py
│
├── mysqlDocker/              # MySQL schema + Docker build
│   └── MBTA.sql
│
├── notebook/                 # Notebook analysis + sample CSV
│   ├── mbta.csv
│   └── Project16-Analysis.ipynb
│
├── docs/                     # (Optional) screenshots or diagrams
│
├── .gitignore
└── README.md

🛠 Technologies Used
Languages
  - Python
  - SQL
  - Java

Frameworks & Libraries
- Flask
- Spring Boot
- pandas
- MySQL Connector
- requests

Databases
- MySQL (Docker)
- MongoDB (Docker)

CDC (Change Data Capture)
- Debezium for MySQL binlog streaming → MongoDB sink

Tools & Infrastructure
- Docker
- Docker networks
- Maven
- Jupyter Notebook
- PowerShell automation
- Haversine geospatial distance calculations

1️⃣ Create the Shared Docker Network
docker network create MBTANetwork

2️⃣ Build & Run the MySQL Container
cd mysqlDocker
docker build -t mysqlmbtamasterimg .
docker run -d --name mysqlserver --network MBTANetwork -p 3307:3306 mysqlmbtamasterimg

# MySQL now runs at: localhost:3307

# It contains:
- Database: MBTA
- Table: mbta_buses

3️⃣ Run MongoDB Container
docker run -d --name some-mongo --network MBTANetwork -p 27017:27017 mongo

# MongoDB runs at: localhost:27017

4️⃣ Build & Run Debezium CDC Listener
# Build Debezium:

cd ../DebeziumCDC
docker build -t debeziummodule16 .

# Run container:
docker run -it --name debezium16 --network MBTANetwork debeziummodule16

# Inside the container, start the Spring Boot CDC listener:
mvn spring-boot:run

# Debezium now:
- Watches MySQL binlogs
- Detects inserts/updates
- Sends CDC events to MongoDB automatically

5️⃣ Start the Flask Web Dashboard
cd ../flask_app
pip install -r requirements.txt
python server.py

# Open the dashboard:
👉 http://localhost:3000

# What you will see:
- Map-based bus visualization
- Live MBTA API calls
- MySQL insert activity
- Auto-refresh markers

6️⃣ Run Analysis Notebook
cd ../notebook
jupyter notebook Project16-Analysis.ipynb

Notebook features include:
⏱ Average time for a bus to complete MBTA Route 1
🛰 GPS distance using Haversine formula
📈 Speed estimation (km/h)
🗺 Visualization of route movement
🧼 Cleaning inconsistent MBTA API values

📈 Learning Outcomes
- Through this project you demonstrate professional-level skills in:

🔹 Data Engineering & ETL
- Ingesting live API data
- Designing relational schemas
- Writing ingestion + transformation logic

🔹 Real-Time Systems
- Debezium CDC
- Binlog-based change tracking
- Event streaming into MongoDB

🔹 Backend Engineering
- Flask server development
- JSON parsing
- Database insert performance

🔹 Cloud & Containers
- Docker networking
- Multi-container orchestration
- Building custom images (MySQL, Debezium, Flask)

🔹 Analytics & Visualization
- Haversine distance calculations
- Trip duration analysis
- Geospatial mapping

🔹 Professional Project Structure
- Clear modular folder layout
- Reproducible environment
- Scalable microservice-style pipeline

# 🚍 MBTA Route 1 Transit Data Engineering Pipeline

This project builds a complete **real-time transit data pipeline** that ingests live MBTA Route 1 bus data, stores it in **MySQL**, streams database changes into **MongoDB** using **Debezium CDC**, and visualizes bus activity with a **Flask dashboard**.
A **Jupyter Notebook** provides route timing analysis, Haversine-based speed estimation, and GPS movement visualization.

## 📂 Repository Structure
```plaintext
Project-16.1-MBTA/
│
├── DebeziumCDC/                # Debezium + Spring Boot CDC listener
│   ├── Dockerfile
│   ├── pom.xml
│   └── src/main/...
│
├── flask_app/                  # Flask dashboard + API client + MySQL loader
│   ├── MBTAApiClient.py
│   ├── mysqldb.py
│   ├── requirements.txt
│   └── server.py
│
├── mysqlDocker/                # MySQL schema + Dockerfile
│   └── MBTA.sql
│
├── notebook/                   # Notebook analysis + sample CSV
│   ├── mbta.csv
│   └── Project16-Analysis.ipynb
│
├── docs/                       # (Optional) screenshots or diagrams
│
├── .gitignore
└── README.md
```

## 🛠 Technologies Used

### Languages
- Python
- SQL
- Java

### Frameworks & Libraries
- Flask
- Spring Boot
- pandas
- MySQL Connector
- requests

### Databases
- MySQL (Docker container)
- MongoDB (Docker container)

### CDC (Change Data Capture)
- Debezium (MySQL binlog → MongoDB)

### Tools & Infrastructure
- Docker
- Docker networks
- Maven
- Jupyter Notebook
- PowerShell automation
- Haversine geospatial distance calculations

---

# 🚀 How to Run the Pipeline (Step-by-Step)

## 1️⃣ Create the Shared Docker Network
```bash
docker network create MBTANetwork
```

## 2️⃣ Build & Run the MySQL Container
```bash
cd mysqlDocker
docker build -t mysqlmbtamasterimg .
docker run -d --name mysqlserver --network MBTANetwork -p 3307:3306 mysqlmbtamasterimg
```

MySQL now runs at:
```
localhost:3307
```

## 3️⃣ Run MongoDB Container
```bash
docker run -d --name some-mongo --network MBTANetwork -p 27017:27017 mongo
```

## 4️⃣ Build & Run Debezium CDC Listener
```bash
cd ../DebeziumCDC
docker build -t debeziummodule16 .
docker run -it --name debezium16 --network MBTANetwork debeziummodule16
```

Inside container:
```bash
mvn spring-boot:run
```

## 5️⃣ Start the Flask Dashboard
```bash
cd ../flask_app
pip install -r requirements.txt
python server.py
```

Open dashboard:  
👉 http://localhost:3000

## 6️⃣ Run Jupyter Notebook Analysis
```bash
cd ../notebook
jupyter notebook Project16-Analysis.ipynb
```

---

# 📈 Learning Outcomes

- Built a complete ETL + CDC pipeline using Docker
- Ingested streaming API data into MySQL
- Used Debezium for MySQL binlog CDC
- Replicated database changes into MongoDB
- Built a real-time Flask dashboard
- Performed geospatial & time-based analysis in Python
- Structured a scalable microservice-style project

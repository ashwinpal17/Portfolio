🚍 MBTA Route 1 Transit Data Engineering Pipeline

This project builds a complete real-time data pipeline that ingests MBTA Route 1 bus information, stores it in MySQL, streams changes into MongoDB via Debezium CDC, and provides a Flask-based visualization dashboard.
It also includes a Jupyter Notebook for performance analysis and speed estimation.

📂 Repository Structure
Project-16.1-MBTA/
├── DebeziumCDC/        # Debezium + Spring Boot CDC listener
├── flask_app/          # Flask web server + MBTA API client
├── mysqlDocker/        # MySQL schema + Dockerfile
├── notebook/           # Analysis notebook + samples
├── docs/               # Screenshots (optional)
├── .gitignore
└── README.md

🛠 Technologies Used
Languages

Python

SQL

Java

Frameworks / Libraries

Flask

Spring Boot

pandas

MySQL Connector

Requests

Databases

MySQL (Docker container)

MongoDB (Docker container)

CDC (Change Data Capture)

Debezium (MySQL binlog streaming)

Tools & Infrastructure

Docker

Maven

Jupyter Notebook

PowerShell automation

Haversine distance analysis for speed estimation

🚀 How to Run the Pipeline (Step-by-Step)

Prerequisites:
Docker, Python 3.10+, Java 17, Maven, pip

1️⃣ Create Docker network
docker network create MBTANetwork

2️⃣ Build and run MySQL container
cd mysqlDocker
docker build -t mysqlmbtamasterimg .
docker run -d --name mysqlserver --network MBTANetwork -p 3307:3306 mysqlmbtamasterimg


MySQL now runs at:

localhost:3307

3️⃣ Build and run MongoDB
docker run -d --name some-mongo --network MBTANetwork -p 27017:27017 mongo

4️⃣ Build & start Debezium CDC listener
cd ../DebeziumCDC
docker build -t debeziummodule16 .
docker run -it --name debezium16 --network MBTANetwork debeziummodule16


Inside the container run:

mvn spring-boot:run


Debezium now watches MySQL and streams changes into MongoDB.

5️⃣ Run Flask app
cd ../flask_app
pip install -r requirements.txt
python server.py


Open dashboard:

http://localhost:3000


This page displays real-time bus positions.

6️⃣ Run Notebook Analysis
cd ../notebook
jupyter notebook Project16-Analysis.ipynb


Notebook includes:

Average bus completion time

Visualization of movement

Speed estimation via Haversine

📈 Learning Outcomes

This project demonstrates your ability to:

Build a full ETL + CDC pipeline using Docker and microservices

Ingest streaming API data into MySQL

Use Debezium for binlog-based CDC

Replicate database changes into MongoDB

Build a real-time Flask visualization tool

Perform geospatial + time-based analysis in Python

Organize a maintainable, production-style data engineering project

👤 Author

Ashwin Pal
Data Engineering • Analytics • Machine Learning
🇨🇦 Canada
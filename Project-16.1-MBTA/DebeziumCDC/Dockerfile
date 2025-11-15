FROM eclipse-temurin:17-jdk
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y maven && rm -rf /var/lib/apt/lists/*
RUN mvn -q -ntp clean package -f /app/pom.xml
CMD ["mvn","spring-boot:run","-f","/app/pom.xml"]

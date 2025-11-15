package mit.edu.tv.listener;

import io.debezium.engine.ChangeEvent;
import io.debezium.engine.DebeziumEngine;
import io.debezium.engine.format.Json;

import java.util.Properties;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Application {

    public static void main(String[] args) throws Exception {

        Properties p = new Properties();

        // --------------------------------------------------------------------
        // REQUIRED: Offset storage (fixed for Debezium 2.3.0.Final)
        // --------------------------------------------------------------------
        p.setProperty("offset.storage", "org.apache.kafka.connect.storage.FileOffsetBackingStore");
        p.setProperty("offset.storage.file.filename", "./debezium-offsets.dat");
        p.setProperty("offset.flush.interval.ms", "60000");

        // --------------------------------------------------------------------
        // NEW REQUIRED FIX: Use FILE-BASED Schema History
        // (Prevents Debezium trying KafkaSchemaHistory and crashing)
        // --------------------------------------------------------------------
        p.setProperty("schema.history.internal", "io.debezium.storage.file.history.FileSchemaHistory");
        p.setProperty("schema.history.internal.file.filename", "./schema-history.dat");

        // --------------------------------------------------------------------
        // Basic connector config for MySQL
        // --------------------------------------------------------------------
        p.setProperty("name", "mysql-connector");
        p.setProperty("connector.class", "io.debezium.connector.mysql.MySqlConnector");

        // Matches your docker MySQL container
        p.setProperty("database.hostname", "mysqlserver");
        p.setProperty("database.port", "3306");
        p.setProperty("database.user", "user");
        p.setProperty("database.password", "user");

        // --------------------------------------------------------------------
        // What database/table to capture
        // --------------------------------------------------------------------
        p.setProperty("topic.prefix", "cdc_demo");
        p.setProperty("database.include.list", "employeedb");
        p.setProperty("table.include.list", "employeedb.employee");

        // No schema change events, only data
        p.setProperty("include.schema.changes", "false");

        // Snapshot on first startup
        p.setProperty("snapshot.mode", "initial");

        // Unique ID for binlog reader
        p.setProperty("database.server.id", "184054");

        // --------------------------------------------------------------------
        // Debezium Engine Creation
        // --------------------------------------------------------------------
        DebeziumEngine<ChangeEvent<String, String>> engine =
                DebeziumEngine.create(Json.class)
                        .using(p)
                        .notifying(record -> {
                            System.out.println(record.value());
                        })
                        .build();

        ExecutorService executor = Executors.newSingleThreadExecutor();
        executor.execute(engine);

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            try { engine.close(); } catch (Exception ignored) {}
            executor.shutdown();
        }));

        Thread.currentThread().join();
    }
}

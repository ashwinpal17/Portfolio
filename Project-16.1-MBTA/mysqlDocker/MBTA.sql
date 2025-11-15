CREATE DATABASE IF NOT EXISTS MBTA;
USE MBTA;

DROP TABLE IF EXISTS mbta_buses;
CREATE TABLE mbta_buses (
  id                      VARCHAR(64) PRIMARY KEY,
  label                   VARCHAR(64),
  latitude                DOUBLE,
  longitude               DOUBLE,
  updated_at              DATETIME,
  current_stop_sequence   INT,
  speed                   DOUBLE,
  occupancy_status        VARCHAR(64),
  direction_id            INT,
  route_id                VARCHAR(32),
  trip_id                 VARCHAR(64),
  bearing                 DOUBLE,
  stop_id                 VARCHAR(64),
  vehicle_status          VARCHAR(64),
  last_modified           TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

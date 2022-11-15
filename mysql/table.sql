USE db;

CREATE TABLE stream_table(
	event_timestamp timestamp,
	sensor_name VARCHAR(20),
	sensor_value double,
	is_anomaly VARCHAR(20)
);
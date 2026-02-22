/* @bruin
name: staging.trips
type: duckdb.sql

depends:
  - ingestion.trips

materialization:
  type: table
@bruin */

SELECT * FROM ingestion.trips;
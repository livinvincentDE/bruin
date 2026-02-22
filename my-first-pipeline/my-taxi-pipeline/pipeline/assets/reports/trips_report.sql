/* @bruin
name: reports.trips_report
type: duckdb.sql

depends:
  - ingestion.trips
  - ingestion.payment_lookup

materialization:
  type: table

@bruin */

SELECT 
    CAST(t.pickup_datetime AS DATE) AS trip_date,
    t.payment_type,
    COUNT(*) AS trip_count,
    SUM(t.total_amount) AS total_revenue
FROM ingestion.trips t
GROUP BY 1, 2;
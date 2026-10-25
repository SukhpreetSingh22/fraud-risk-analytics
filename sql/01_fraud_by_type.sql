-- Fraud count and fraud rate by transaction type
SELECT   type,
         COUNT(*)                     AS total_txns,
         SUM(isFraud)                 AS fraud_txns,
         ROUND(100.0 * SUM(isFraud) / COUNT(*), 3) AS fraud_rate_pct
FROM     transactions
GROUP BY type
ORDER BY fraud_rate_pct DESC;

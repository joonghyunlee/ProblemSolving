SELECT a.Id AS Id
FROM Weather a, Weather b
WHERE DATE_SUB(a.RecordDate, INTERVAL 1 DAY) = b.RecordDate AND a.Temperature > b.Temperature

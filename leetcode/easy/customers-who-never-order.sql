SELECT Name AS Customers
FROM Customers c
LEFT JOIN (
    SELECT *
    FROM Orders
) o
ON c.Id = o.CustomerId
WHERE o.Id IS NULL

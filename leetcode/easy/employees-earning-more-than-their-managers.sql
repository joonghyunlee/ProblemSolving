SELECT e.Name AS Employee
FROM Employee e
RIGHT JOIN (
    SELECT Id, Salary
    FROM Employee
) m
ON e.ManagerId = m.Id
WHERE e.Salary > m.Salary

# Write your MySQL query statement below

SELECT employees.name AS Employee
    FROM Employee AS employees
    JOIN Employee AS managers
    ON employees.managerId = managers.id
    WHERE employees.salary > managers.salary
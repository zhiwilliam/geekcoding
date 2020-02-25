CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    WITH r AS (
        SELECT SALARY,
               dense_rank () over ( order by salary desc ) rn 
        FROM EMPLOYEE
      )
    SELECT unique salary
    INTO result 
    FROM r
    where rn = N 
    ;
    
    RETURN result;
END;


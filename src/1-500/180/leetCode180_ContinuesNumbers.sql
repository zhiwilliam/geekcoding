
with s as (
    select num, 
           sum(num) over( order by id rows between 2 preceding and current row  ) s,
           min(num) over( order by id rows between 2 preceding and current row  ) m 
    from logs 
)select distinct num "ConsecutiveNums"
from s 
where num*3 = s and num = m 
;


select * from grandfather;

select * from father;

select name, gender, spouse_name, wealth
from grandfather_siblings;

-- grandparents brother list
select name as relative_name, wealth
from grandfather_siblings
where gender = "Male";

-- gifts more than 30000
select gift_description, estimated_value, year 
from father_gifts
where estimated_value > 30000;

-- who is alive
select name, birth_date
from grandfather_siblings
where alive = true;

-- Who is richer
select name, wealth
from grandfather_siblings
order by wealth desc;		-- [order by means 'Average']


-- average wealth by gender where it's less than 1000
select gender, avg(wealth) as avg_wealth
from grandfather_siblings
group by gender
having avg_wealth < 5700000;

-- total brother
select count(*) as total_brother
from grandfather_siblings
where gender = "Male";


-- list all sisters who are married
select name
from grandfather_siblings
where gender = "Female" and spouse_name is not null;



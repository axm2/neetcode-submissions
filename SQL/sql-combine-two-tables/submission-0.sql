-- Write your query below
select person.first_name, person.last_name, address.city, address.state from address right join person on person.person_id = address.person_id
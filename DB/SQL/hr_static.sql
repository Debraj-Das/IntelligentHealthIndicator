create table hr_static (
   id serial primary key,
   userid integer not null,
   name text not null,
   dob date,
   gender text,
   phone text,
   email text,
   joining_date date,
   leaving_date date
);

insert into hr_static (userid, name, dob, gender, phone, email, joining_date, leaving_date) values
(1240, 'John Doe', '1980-01-01', 'male', '1234567890', 'john@gmail.com', '2010-01-01', null),
(1245, 'Debraj Das', '1985-01-10', 'male', '1234567891', 'debraj@gmai.com',
   '2010-01-01', '2015-01-01');
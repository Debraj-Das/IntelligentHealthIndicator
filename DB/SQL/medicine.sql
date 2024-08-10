create table medicine(
   id serial primary key,
   userid int not null,
   date date,
   doctor text,
   medicine text
);

insert into medicine(userid, date, doctor, medicine) values(1234, '2019-01-01', 'Dr. A', 'Medicine A'), (1234, '2019-01-02', 'Dr. B', 'Medicine B');
create table opd (
   id serial primary key,
   userid integer not null,
   date date,
   doctor text,
   status int
);

insert into opd (userid, date, doctor, status) values (1234, '2017-01-01', 'Dr. Abc', 0),
(1234, '2024-05-07', 'Dr. Abs', 1);
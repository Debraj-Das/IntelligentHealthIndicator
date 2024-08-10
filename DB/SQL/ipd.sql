create table ipd (
   id serial primary key,
   userid integer not null,
   admit_no integer,
   admit_date date,
   discharge_date date,
   doctor text,
   prescription text,
   status int
);

insert into ipd (userid, admit_no, admit_date, discharge_date, doctor, prescription, status) values (1, 1, '2019-01-01', '2019-01-10', 'Dr. A', 'Medicine A', 1), (2, 2, '2019-01-02', '2019-01-11', 'Dr. B', 'Medicine B', 1), (3, 3, '2019-01-03', '2019-01-12', 'Dr. C', 'Medicine C', 1), (4, 4, '2019-01-04', '2019-01-13', 'Dr. D', 'Medicine D', 1), (5, 5, '2019-01-05', '2019-01-14', 'Dr. E', 'Medicine E', 1);
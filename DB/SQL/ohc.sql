create table ohc(
   id serial primary key,
   userid integer not null,
   date date,
   doctor text,
   prescription text
);


insert into ohc(userid, date, doctor, prescription)
values (1234, '2024-07-01', 'B.C.Roy', 'fever 100 degF'),
(1234, '2024-07-10', 'B.C.Roy', 'fever 101 degF');
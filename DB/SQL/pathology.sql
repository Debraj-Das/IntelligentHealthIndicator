create table pathology (
   id serial primary key,
   userid integer not null,
   date date,
   test text,
   result text
);

insert into pathology (userid, date, test, result) values (1234, '2016-01-01', 'CBC', 'Normal'), (1234, '2016-01-01', 'CBC', 'Normal'), (1234, '2016-01-01', 'CBC', 'Normal');
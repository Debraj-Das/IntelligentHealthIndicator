create table hr_dynamic (
   id serial primary key,
   userid integer not null,
   shopid integer not null,
   shift text,
   grade text,
   joining_shop date
);

insert into hr_dynamic (userid, shopid, shift, grade, joining_shop) values
(1240, 234, 'morning: 10am-6pm', 'A', '2010-01-01'),
(1245, 236, 'night: 6pm - 12am', 'B', '2010-01-01');
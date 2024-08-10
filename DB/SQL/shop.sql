create table shop(
   id serial primary key,
   shopid integer not null unique,
   location text,
);

insert into shop(shopid, location) 
values (2356, 'contai, purba Medinipur'),
(4534, 'digha, purba Medinipur'),
(2345, 'kharagpur, paschim Medinipur'),
(2345, 'kolkata, kolkata');
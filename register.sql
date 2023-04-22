show databases;
create database log_;
use log_;
create table log_in(name varchar(100),password varchar(100),gender varchar(100));
show tables;
insert into log_in values('vinayak','8108');
select username,password from log_in;
select * from log_in;
delete from log_in where password='';

 
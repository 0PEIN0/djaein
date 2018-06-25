ALTER ROLE djaein SET client_encoding TO 'utf8';
ALTER ROLE djaein SET default_transaction_isolation TO 'read committed';
ALTER ROLE djaein SET timezone TO 'UTC';
drop database if exists djaein ;
create database djaein ;
grant all privileges on database djaein to djaein ;
alter role djaein superuser;
ALTER USER djaein CREATEDB;
drop database if exists test_djaein ;
create database test_djaein ;
grant all privileges on database test_djaein to djaein ;
grant all privileges on database test_djaein to postgres ;

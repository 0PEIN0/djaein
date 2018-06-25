ALTER USER postgres PASSWORD 'postgres' ;
drop database if exists djaein ;
CREATE DATABASE djaein ;
DO
$body$
BEGIN
   IF NOT EXISTS (
      SELECT *
      FROM   pg_catalog.pg_user
      WHERE  usename = 'djaein') THEN

      CREATE ROLE djaein LOGIN PASSWORD 'djaein';
      CREATE USER djaein WITH PASSWORD 'djaein' ;
   END IF;
END
$body$;
ALTER ROLE djaein SET client_encoding TO 'utf8' ;
ALTER ROLE djaein SET default_transaction_isolation TO 'read committed' ;
ALTER ROLE djaein SET timezone TO 'UTC' ;
GRANT ALL PRIVILEGES ON DATABASE djaein TO djaein ;
alter role djaein superuser;
ALTER USER djaein CREATEDB;
drop database if exists test_djaein ;
create database test_djaein ;
grant all privileges on database test_djaein to djaein ;

## PART 1
```
sudo apt-get install mysql-server -y

SHOW DATABASES;
CREATE DATABASE devops;
USE devops;
CREATE TABLE students( id INT AUTO_INCREMENT PRIMARY KEY, surname VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL );
CREATE TABLE tasks( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, students_id INT NOT NULL, FOREIGN KEY (students_id) references students(id) );
CREATE TABLE english( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(2) NOT NULL, english_id INT NOT NULL, FOREIGN KEY (english_id) references students(id) );

INSERT INTO students (name,surname) values ('Petro','Zalivnuy'),('Oleg','Pechniy'),('Sergiy','Oltichniy'),('Olga','Cvetnaya');

mysql> SELECT * FROM students;
+----+--------+-----------+
| id | name   | surname   |
+----+--------+-----------+
|  1 | Petro  | Zalivnuy  |
|  2 | Oleg   | Pechniy   |
|  3 | Sergiy | Oltichniy |
|  4 | Olga   | Cvetnaya  |
+----+--------+-----------+
4 rows in set (0.01 sec)

mysql> INSERT INTO tasks (name,students_id) values ('task3',1),('task4',2),('task4',3),('task5',4);
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM tasks;
+----+-------+-------------+
| id | name  | students_id |
+----+-------+-------------+
|  1 | task3 |           1 |
|  2 | task4 |           2 |
|  3 | task4 |           3 |
|  4 | task5 |           4 |
+----+-------+-------------+
4 rows in set (0.00 sec)

mysql> INSERT INTO english (name,english_id) values ('A1',3),('A2',2),('B2',1),('C2',4);
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM english;
+----+------+------------+
| id | name | english_id |
+----+------+------------+
|  1 | A1   |          3 |
|  2 | A2   |          2 |
|  3 | B2   |          1 |
|  4 | C2   |          4 |
+----+------+------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM students WHERE id = 1;
+----+-------+----------+
| id | name  | surname  |
+----+-------+----------+
|  1 | Petro | Zalivnuy |
+----+-------+----------+
1 row in set (0.00 sec)

mysql> SELECT * FROM students WHERE id > 2;
+----+--------+-----------+
| id | name   | surname   |
+----+--------+-----------+
|  3 | Sergiy | Oltichniy |
|  4 | Olga   | Cvetnaya  |
+----+--------+-----------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM students WHERE name = 'Oleg';
+----+------+---------+
| id | name | surname |
+----+------+---------+
|  2 | Oleg | Pechniy |
+----+------+---------+
1 row in set (0.00 sec)

mysql> SELECT * FROM students WHERE NOT surname LIKE '%uy';
+----+--------+-----------+
| id | name   | surname   |
+----+--------+-----------+
|  2 | Oleg   | Pechniy   |
|  3 | Sergiy | Oltichniy |
|  4 | Olga   | Cvetnaya  |
+----+--------+-----------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM students WHERE surname LIKE '%uy';
+----+-------+----------+
| id | name  | surname  |
+----+-------+----------+
|  1 | Petro | Zalivnuy |
+----+-------+----------+
1 row in set (0.00 sec)

mysql> SELECT * FROM tasks WHERE id > 3 AND students_id < 5;
+----+-------+-------------+
| id | name  | students_id |
+----+-------+-------------+
|  4 | task5 |           4 |
+----+-------+-------------+
1 row in set (0.00 sec)

mysql> SELECT * FROM students WHERE id BETWEEN 2 and 3;
+----+--------+-----------+
| id | name   | surname   |
+----+--------+-----------+
|  2 | Oleg   | Pechniy   |
|  3 | Sergiy | Oltichniy |
+----+--------+-----------+
2 rows in set (0.00 sec)


mysql> SELECT id AS "Индентификатор", name AS "Имя", surname AS "Фамилия" FROM students;
+------------------------------+--------+----------------+
| Индентификатор               | Имя    | Фамилия        |
+------------------------------+--------+----------------+
|                            1 | Petro  | Zalivnuy       |
|                            2 | Oleg   | Pechniy        |
|                            3 | Sergiy | Oltichniy      |
|                            4 | Olga   | Cvetnaya       |
+------------------------------+--------+----------------+
4 rows in set (0.00 sec)


mysql> SELECT * FROM students ORDER BY name;
+----+--------+-----------+
| id | name   | surname   |
+----+--------+-----------+
|  2 | Oleg   | Pechniy   |
|  4 | Olga   | Cvetnaya  |
|  1 | Petro  | Zalivnuy  |
|  3 | Sergiy | Oltichniy |
+----+--------+-----------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM students ORDER BY surname;
+----+--------+-----------+
| id | name   | surname   |
+----+--------+-----------+
|  4 | Olga   | Cvetnaya  |
|  3 | Sergiy | Oltichniy |
|  2 | Oleg   | Pechniy   |
|  1 | Petro  | Zalivnuy  |
+----+--------+-----------+
4 rows in set (0.00 sec)


mysql> SELECT * FROM english ORDER BY name;
+----+------+------------+
| id | name | english_id |
+----+------+------------+
|  1 | A1   |          3 |
|  2 | A2   |          2 |
|  3 | B2   |          1 |
|  4 | C2   |          4 |
+----+------+------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM english ORDER BY name DESC;
+----+------+------------+
| id | name | english_id |
+----+------+------------+
|  4 | C2   |          4 |
|  3 | B2   |          1 |
|  2 | A2   |          2 |
|  1 | A1   |          3 |
+----+------+------------+
4 rows in set (0.00 sec)

mysql> SHOW COLUMNS FROM tasks;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int          | NO   | PRI | NULL    | auto_increment |
| name        | varchar(255) | NO   |     | NULL    |                |
| students_id | int          | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
3 rows in set (0.01 sec)

mysql> ALTER TABLE tasks ADD mark INT AFTER name;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SHOW COLUMNS FROM tasks;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int          | NO   | PRI | NULL    | auto_increment |
| name        | varchar(255) | NO   |     | NULL    |                |
| mark        | int          | YES  |     | NULL    |                |
| students_id | int          | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> UPDATE tasks SET mark = 10 where id = 1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE tasks SET mark = 9 where id = 2;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE tasks SET mark = 10 where id = 3;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE tasks SET mark = 8 where id = 4;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * from tasks;
+----+-------+------+-------------+
| id | name  | mark | students_id |
+----+-------+------+-------------+
|  1 | task3 |   10 |           1 |
|  2 | task4 |    9 |           2 |
|  3 | task4 |   10 |           3 |
|  4 | task5 |    8 |           4 |
+----+-------+------+-------------+
4 rows in set (0.00 sec)

mysql> SELECT mark from tasks GROUP BY mark;
+------+
| mark |
+------+
|   10 |
|    9 |
|    8 |
+------+
3 rows in set (0.00 sec)

mysql> SELECT mark, COUNT(mark) FROM tasks GROUP BY mark;
+------+-------------+
| mark | COUNT(mark) |
+------+-------------+
|   10 |           2 |
|    9 |           1 |
|    8 |           1 |
+------+-------------+
3 rows in set (0.01 sec)

DDL – Data Definition Language

CREATE – используется для создания объектов базы данных;
ALTER – используется для изменения объектов базы данных;
DROP – используется для удаления объектов базы данных.

DML – Data Manipulation Language

SELECT – осуществляет выборку данных;
INSERT – добавляет новые данные;
UPDATE – изменяет существующие данные;
DELETE – удаляет данные.

DCL – Data Control Language

GRANT – предоставляет пользователю или группе разрешения на определённые операции с объектом;
REVOKE – отзывает выданные разрешения;
DENY– задаёт запрет, имеющий приоритет над разрешением.

CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

ALL PRIVILEGES — как мы уже увидели ранее, данный набор прав предоставляет пользователю MySQL полный доступ к определенной базе данных (если не выбрана ни одна база данных, предоставляется глобальный доступ к системе)
CREATE — позволяет пользователю создавать новые таблицы или базы данных
DROP — позволяет пользователю удалять таблицы или базы данных
DELETE — позволяет пользователю удалять строки из таблиц
INSERT — позволяет пользователю вставлять строки в таблицы
SELECT — позволяет пользователю выполнять команду SELECT для чтения данных из базы
UPDATE — позволяет пользователю обновлять строки таблицы
GRANT OPTION — позволяет пользователю предоставлять или отзывать права других пользователей

mysql> CREATE USER 'student_moderator'@'localhost' IDENTIFIED BY 'Mypass2020#';
Query OK, 0 rows affected (0.01 sec)


mysql> GRANT INSERT,DELETE,SELECT,UPDATE ON devops.students TO 'student_moderator'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW GRANTS FOR 'student_moderator'@'localhost';
+------------------------------------------------------------------------------------------------+
| Grants for student_moderator@localhost                                                         |
+------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `student_moderator`@`localhost`                                          |
| GRANT SELECT, INSERT, UPDATE, DELETE ON `devops`.`students` TO `student_moderator`@`localhost` |
+------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> CREATE USER 'task_moderator'@'localhost' IDENTIFIED BY 'Mypass2020#';
Query OK, 0 rows affected (0.00 sec)

mysql> GRANT INSERT,SELECT,UPDATE ON devops.tasks TO 'task_moderator'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW GRANTS FOR 'task_moderator'@'localhost';
+----------------------------------------------------------------------------------+
| Grants for task_moderator@localhost                                              |
+----------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `task_moderator`@`localhost`                               |
| GRANT SELECT, INSERT, UPDATE ON `devops`.`tasks` TO `task_moderator`@`localhost` |
+----------------------------------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)

mysql -u student_moderator -p

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| devops             |
| information_schema |
+--------------------+
2 rows in set (0.00 sec)

mysql> USE devops;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+------------------+
| Tables_in_devops |
+------------------+
| students         |
+------------------+
1 row in set (0.01 sec)

mysql> INSERT INTO students (name,surname) values ('Vasiliy','Zabolotniy'),('Ostap','Stahiv');
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM students;
+----+---------+------------+
| id | name    | surname    |
+----+---------+------------+
|  1 | Petro   | Zalivnuy   |
|  2 | Oleg    | Pechniy    |
|  3 | Sergiy  | Oltichniy  |
|  4 | Olga    | Cvetnaya   |
|  5 | Vasiliy | Zabolotniy |
|  6 | Ostap   | Stahiv     |
+----+---------+------------+
6 rows in set (0.00 sec)

mysql -u task_moderator -p

mysql> USE devops;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+------------------+
| Tables_in_devops |
+------------------+
| tasks            |
+------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO tasks (name,students_id,mark) values ('task5',5,7),('task4',6,10);
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM tasks;
+----+-------+------+-------------+
| id | name  | mark | students_id |
+----+-------+------+-------------+
|  1 | task3 |   10 |           1 |
|  2 | task4 |    9 |           2 |
|  3 | task4 |   10 |           3 |
|  4 | task5 |    8 |           4 |
|  9 | task5 |    7 |           5 |
| 10 | task4 |   10 |           6 |
+----+-------+------+-------------+
6 rows in set (0.01 sec)

mysql> DELETE FROM tasks WHERE id = 1;
ERROR 1142 (42000): DELETE command denied to user 'task_moderator'@'localhost' for table 'tasks'
mysql>

mysql> use mysql
Database changed
mysql> SHOW TABLES;
+------------------------------------------------------+
| Tables_in_mysql                                      |
+------------------------------------------------------+
| columns_priv                                         |
| component                                            |
| db                                                   |
| default_roles                                        |
| engine_cost                                          |
| func                                                 |
| general_log                                          |
| global_grants                                        |
| gtid_executed                                        |
| help_category                                        |
| help_keyword                                         |
| help_relation                                        |
| help_topic                                           |
| innodb_index_stats                                   |
| innodb_table_stats                                   |
| password_history                                     |
| plugin                                               |
| procs_priv                                           |
| proxies_priv                                         |
| replication_asynchronous_connection_failover         |
| replication_asynchronous_connection_failover_managed |
| replication_group_configuration_version              |
| replication_group_member_actions                     |
| role_edges                                           |
| server_cost                                          |
| servers                                              |
| slave_master_info                                    |
| slave_relay_log_info                                 |
| slave_worker_info                                    |
| slow_log                                             |
| tables_priv                                          |
| time_zone                                            |
| time_zone_leap_second                                |
| time_zone_name                                       |
| time_zone_transition                                 |
| time_zone_transition_type                            |
| user                                                 |
+------------------------------------------------------+
37 rows in set (0.00 sec)

mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
+-------------------+------------------------------------------------------------------------+-----------------------+-----------+
| user              | authentication_string                                                  | plugin                | host      |
+-------------------+------------------------------------------------------------------------+-----------------------+-----------+
| debian-sys-maint  | $A$005$N.L!jWrgnW=bJcLPYFoQWdIoYdrwXzys1rifgzLOQ6qhNva5X9mB6qZ2f0      | caching_sha2_password | localhost |
| mysql.infoschema  | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| mysql.session     | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| mysql.sys         | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED | caching_sha2_password | localhost |
| root              | $A$005$di16;z;^o P5A=ZYAMzaHRlC1H92StjE/NYghM05jxCfFGUqyI4b9gIq8       | caching_sha2_password | localhost |
| student_moderator | $A$005$evMhs{#K8dGo?ETjKpQaWjrmj9zWcUy/5XAmOXmj1ORC2EXB6rg9hkuctz4     | caching_sha2_password | localhost |
| task_moderator    | $A$005$~zg|'L0#J(@8{Jfpg&RukGCQurrDJZwiLRAmVPP87TlRw1bRVrtaM4hd5n0o6   | caching_sha2_password | localhost |
+-------------------+------------------------------------------------------------------------+-----------------------+-----------+
7 rows in set (0.00 sec)

mysql> SELECT * FROM db;
+-----------+--------------------+---------------+-------------+-------------+-------------+-------------+-------------+-----------+------------+-----------------+------------+------------+-----------------------+------------------+------------------+----------------+---------------------+--------------------+--------------+------------+--------------+
| Host      | Db                 | User          | Select_priv | Insert_priv | Update_priv | Delete_priv | Create_priv | Drop_priv | Grant_priv | References_priv | Index_priv | Alter_priv | Create_tmp_table_priv | Lock_tables_priv | Create_view_priv | Show_view_priv | Create_routine_priv | Alter_routine_priv | Execute_priv | Event_priv | Trigger_priv |
+-----------+--------------------+---------------+-------------+-------------+-------------+-------------+-------------+-----------+------------+-----------------+------------+------------+-----------------------+------------------+------------------+----------------+---------------------+--------------------+--------------+------------+--------------+
| localhost | performance_schema | mysql.session | Y           | N           | N           | N           | N           | N         | N          | N               | N          | N          | N                     | N                | N                | N              | N                   | N                  | N            | N          | N            |
| localhost | sys                | mysql.sys     | N           | N           | N           | N           | N           | N         | N          | N               | N          | N          | N                     | N                | N                | N              | N                   | N                  | N            | N          | Y            |
+-----------+--------------------+---------------+-------------+-------------+-------------+-------------+-------------+-----------+------------+-----------------+------------+------------+-----------------------+------------------+------------------+----------------+---------------------+--------------------+--------------+------------+--------------+
2 rows in set (0.00 sec)
```
## PART 2
```
dmalyshok@server:~$ mysqldump -u root -p devops > /home/dmalyshok/devops.sql
Enter password:
dmalyshok@server:~$ ls /home/dmalyshok/
DevOps_online_Kiev_2021Q4  devops.sql

dmalyshok@server:~$ mysql -u root -p
Enter password:
mysql> USE devops
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+------------------+
| Tables_in_devops |
+------------------+
| english          |
| students         |
| tasks            |
+------------------+
3 rows in set (0.00 sec)

mysql> DROP TABLE tasks;
Query OK, 0 rows affected (0.02 sec)

mysql> SHOW TABLES;
+------------------+
| Tables_in_devops |
+------------------+
| english          |
| students         |
+------------------+
2 rows in set (0.01 sec)

mysql> source /home/dmalyshok/devops.sql

mysql> SELECT * FROM tasks;
+----+-------+------+-------------+
| id | name  | mark | students_id |
+----+-------+------+-------------+
|  1 | task3 |   10 |           1 |
|  2 | task4 |    9 |           2 |
|  3 | task4 |   10 |           3 |
|  4 | task5 |    8 |           4 |
|  9 | task5 |    7 |           5 |
| 10 | task4 |   10 |           6 |
+----+-------+------+-------------+
6 rows in set (0.00 sec)


mysql> DROP DATABASE devops;
Query OK, 3 rows affected (0.02 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> CREATE DATABASE devops;
Query OK, 1 row affected (0.00 sec)

mysql> SHOW TABLES;
ERROR 1046 (3D000): No database selected
mysql> USE devops;
Database changed
mysql> SHOW TABLES;
Empty set (0.00 sec)

dmalyshok@server:~$ mysql -u root -p devops < devops.sql
Enter password:
dmalyshok@server:~$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 39
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| devops             |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)


mysql> USE devops;
Database changed
mysql> SHOW TABLES;
+------------------+
| Tables_in_devops |
+------------------+
| english          |
| students         |
| tasks            |
+------------------+
3 rows in set (0.00 sec)

mysql> SHOW TABLES;
+------------------+
| Tables_in_devops |
+------------------+
| english          |
| students         |
| tasks            |
+------------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM students;
+----+---------+------------+
| id | name    | surname    |
+----+---------+------------+
|  1 | Petro   | Zalivnuy   |
|  2 | Oleg    | Pechniy    |
|  3 | Sergiy  | Oltichniy  |
|  4 | Olga    | Cvetnaya   |
|  5 | Vasiliy | Zabolotniy |
|  6 | Ostap   | Stahiv     |
+----+---------+------------+
6 rows in set (0.01 sec)

mysql> SELECT * FROM english;
+----+------+------------+
| id | name | english_id |
+----+------+------------+
|  1 | A1   |          3 |
|  2 | A2   |          2 |
|  3 | B2   |          1 |
|  4 | C2   |          4 |
+----+------+------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM tasks;
+----+-------+------+-------------+
| id | name  | mark | students_id |
+----+-------+------+-------------+
|  1 | task3 |   10 |           1 |
|  2 | task4 |    9 |           2 |
|  3 | task4 |   10 |           3 |
|  4 | task5 |    8 |           4 |
|  9 | task5 |    7 |           5 |
| 10 | task4 |   10 |           6 |
+----+-------+------+-------------+
6 rows in set (0.00 sec)
```
![Screen2](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m4/task4.1/Screen4.1.2.JPG)
```
dmalyshok@server:~$ mysql -h devops.cgryvglaxh4x.eu-central-1.rds.amazonaws.com -P 3306 -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 24
Server version: 8.0.23 Source distribution

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.04 sec)

mysql> CREATE DATABASE devops;
Query OK, 1 row affected (0.04 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| devops             |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.03 sec)

dmalyshok@server:~$ mysql -u root -p -h devops.cgryvglaxh4x.eu-central-1.rds.amazonaws.com -D devops < devops.sql
Enter password:

mysql> SHOW TABLES;
+------------------+
| Tables_in_devops |
+------------------+
| english          |
| students         |
| tasks            |
+------------------+
3 rows in set (0.04 sec)

mysql> SELECT * FROM english;
+----+------+------------+
| id | name | english_id |
+----+------+------------+
|  1 | A1   |          3 |
|  2 | A2   |          2 |
|  3 | B2   |          1 |
|  4 | C2   |          4 |
+----+------+------------+
4 rows in set (0.04 sec)

mysql> SELECT * FROM students;
+----+---------+------------+
| id | name    | surname    |
+----+---------+------------+
|  1 | Petro   | Zalivnuy   |
|  2 | Oleg    | Pechniy    |
|  3 | Sergiy  | Oltichniy  |
|  4 | Olga    | Cvetnaya   |
|  5 | Vasiliy | Zabolotniy |
|  6 | Ostap   | Stahiv     |
+----+---------+------------+
6 rows in set (0.03 sec)

mysql> SELECT * FROM tasks;
+----+-------+------+-------------+
| id | name  | mark | students_id |
+----+-------+------+-------------+
|  1 | task3 |   10 |           1 |
|  2 | task4 |    9 |           2 |
|  3 | task4 |   10 |           3 |
|  4 | task5 |    8 |           4 |
|  9 | task5 |    7 |           5 |
| 10 | task4 |   10 |           6 |
+----+-------+------+-------------+
6 rows in set (0.04 sec)

mysql> INSERT INTO english (name,english_id) values ('B1',5),('A2',6);
Query OK, 2 rows affected (0.35 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM english;
+----+------+------------+
| id | name | english_id |
+----+------+------------+
|  1 | A1   |          3 |
|  2 | A2   |          2 |
|  3 | B2   |          1 |
|  4 | C2   |          4 |
|  5 | B1   |          5 |
|  6 | A2   |          6 |
+----+------+------------+
6 rows in set (0.04 sec)

dmalyshok@server:~$ mysqldump -h devops.cgryvglaxh4x.eu-central-1.rds.amazonaws.com -u root -p  devops  > rds-dump.sql
Enter password:
Warning: A partial dump from a server that has GTIDs will by default include the GTIDs of all transactions, even those that changed suppressed parts of the database. If you don't want to restore GTIDs, pass --set-gtid-purged=OFF. To make a complete dump, pass --all-databases --triggers --routines --events.
dmalyshok@server:~$ vi rds-dump.sql

-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `mark` int DEFAULT NULL,
  `students_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `students_id` (`students_id`),
  CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`students_id`) REFERENCES `students` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'task3',10,1),(2,'task4',9,2),(3,'task4',10,3),(4,'task5',8,4),(9,'task5',7,5),(10,'task4',10,6);
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;


```
## PART 3.
```
![Screen2](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m4/task4.1/Screen4.1.2.JPG?raw=true)
```
dmalyshok@server:~$ wget https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/sampledata.zip
--2021-11-28 13:06:57--  https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/sampledata.zip
Resolving docs.aws.amazon.com (docs.aws.amazon.com)... 54.239.24.117
Connecting to docs.aws.amazon.com (docs.aws.amazon.com)|54.239.24.117|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1997 (2.0K) [application/zip]
Saving to: ‘sampledata.zip’

sampledata.zip                       100%[===================================================================>]   1.95K  --.-KB/s    in 0s

2021-11-28 13:06:57 (230 MB/s) - ‘sampledata.zip’ saved [1997/1997]

dmalyshok@server:~$ unzip sampledata.zip
Archive:  sampledata.zip
  inflating: Forum.json
  inflating: ProductCatalog.json
  inflating: Reply.json
  inflating: Thread.json


dmalyshok@server:~$ aws dynamodb batch-write-item --request-items file://ProductCatalog.json
{
    "UnprocessedItems": {}
}
dmalyshok@server:~$ aws dynamodb batch-write-item --request-items file://Forum.json
{
    "UnprocessedItems": {}
}
dmalyshok@server:~$ aws dynamodb batch-write-item --request-items file://Thread.json
{
    "UnprocessedItems": {}
}
dmalyshok@server:~$ aws dynamodb batch-write-item --request-items file://Reply.json
{
    "UnprocessedItems": {}
}
```
![Screen3](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m4/task4.1/Screen4.1.3.JPG?raw=true)
![Screen4](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m4/task4.1/Screen4.1.4.JPG?raw=true)
## Task1.Part1

    1) Log in to the system as root.
```
dmalyshok@server:~$ sudo -i
[sudo] password for dmalyshok:
root@server:~# id
uid=0(root) gid=0(root) groups=0(root)
root@server:~#
```
    2) Use the passwd command to change the password. Examine the basic parameters of the command. What system file does it change *?
```
root@server:~# passwd
New password:
Retype new password:
passwd: password updated successfully

       /etc/passwd
           содержит информацию о пользователях

       /etc/shadow
           содержит защищаемую информацию о пользователях

       /etc/pam.d/passwd
           настройки PAM для passwd

Чтение файла «/etc/passwd»

root:x:0:0:root:/root:/bin/bash

Поля информации разделяются двоеточием (:). Каждая строка типичного Linux-файла «/etc/passwd» содержит 7 полей:

Root: имя пользователя;
х: место для информации о паролях; пароль можно найти в файле «/etc/shadow».
0: ID пользователя. Каждый пользователь имеет уникальный идентификатор, благодаря которому система распознает его. ID root-пользователя всегда 0;
0: ID группы. Каждая группа имеет уникальный идентификатор. По умолчанию у каждого пользователя есть главная группа. Опять же, ID root-группы всегда 0;
root: поле для примечаний. Данное поле можно использовать для описания пользователя или его функций. Оно может содержать что угодно, начиная от контактной информации пользователя и заканчивая описанием сервисов, для которых была создана учетная запись;
/root: домашний каталог. Для обычных пользователей домашним каталогом является «/home/username», для root-пользователя это «/root»;
/bin/bash: оболочка пользователя. Данное поле содержит оболочку, которая будет создана, или команды, которые будут выполняться при входе пользователя в систему.

Что такое «/etc/shadow»?

Файл «/etc/shadow» содержит следующие поля:

daemon: имя пользователя;
*: хешированный пароль; данное поле можно просмотреть, войдя как root. Как указано выше, звездочка значит, что данная учетная запись не может быть использована для входа в систему.
15455: последнее изменение пароля. Данное значение ограничивается датой начала «Unix-эпохи» (1 января 1970).
0: допустимое количество дней для смены пароля. 0 в данном поле значит, что таких ограничений нет.
99999: количество дней до необходимости смены пароля. Значение 99999 указывает на то, что ограничения на продолжительность использования одного пароля не установлены.
7: количество дней до предупреждения об истечении срока использования пароля. Если требуется сменить пароль, пользователь будет извещен о данной необходимости за указанное количество дней.
[blank]: последние три поля нужны для того, чтобы указать количество дней до деактивации учетной записи. Последнее поле не используется.
```

    3) Determine the users registered in the system, as well as what commands they execute. What additional information can be gleaned from the command execution?
```
root@server:~# w
 12:27:01 up  3:02,  2 users,  load average: 0.19, 0.23, 0.15
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
dmalysho pts/0    192.168.233.1    10:44    0.00s  0.03s  0.03s sshd: dmalyshok [priv]
devops   pts/1    192.168.233.1    12:25    4.00s  0.02s  0.00s mc

Name of the user
User’s machine number or tty number
Remote machine address
User’s Login time
Idle time (not usable time)
Time used by all processes attached to the tty (JCPU time)
Time used by the current process (PCPU time)
Command currently getting executed by the users

root@server:~# last
devops   pts/1        192.168.233.1    Mon Nov 29 12:25   still logged in
dmalysho pts/0        192.168.233.1    Mon Nov 29 10:44   still logged in
dmalysho pts/0        192.168.233.1    Mon Nov 29 09:32 - 10:44  (01:11)
dmlshk   pts/0        192.168.233.1    Mon Nov 29 09:31 - 09:32  (00:00)
reboot   system boot  5.4.0-90-generic Mon Nov 29 09:24   still running

root@server:~# who
dmalyshok pts/0        2021-11-29 10:44 (192.168.233.1)
devops   pts/1        2021-11-29 12:25 (192.168.233.1)

root@server:~# users
devops dmalyshok
```
    4) Change personal information about yourself.
```
root@server:~# chfn devops
Changing the user information for devops
Enter the new value, or press ENTER for the default
        Full Name []: Devops Course 2021
        Room Number [111-1111]:
        Work Phone [111-1111]:
        Home Phone [111-1111]:
        Other []: Winter Learning

root@server:~# getent passwd devops
devops:x:1002:1002:Devops Course 2021,111-1111,111-1111,111-1111,Winter Learning:/home/devops:/bin/bash

root@server:~# getent passwd root
root:x:0:0:Super User,Main Room,111-11111,111-1111:/root:/bin/bash
```
    5) Become familiar with the Linux help system and the man and info commands. Get help on the previously discussed commands, define and describe any two keys for these commands. Give examples.
```
root@server:~# man chfn

OPTIONS
       The options which apply to the chfn command are:

       -f, --full-name FULL_NAME
           Change the user's full name.

root@server:~# chfn -f Malyshok
root@server:~# getent passwd root
root:x:0:0:Malyshok,Main Room,111-11111,111-1111:/root:/bin/bash

root@server:~# man w

 -s, --short
              Use the short format.  Don't print the login time, JCPU or PCPU times.

root@server:~# w -s
 20:00:09 up  1:13,  2 users,  load average: 0.24, 0.22, 0.13
USER     TTY      FROM              IDLE WHAT
dmalysho tty1     -                 1:12m -bash
dmalysho pts/0    192.168.233.1     0.00s sshd: dmalyshok [priv]
```
    6) Explore the more and less commands using the help system. View the contents of files .bash* using commands.
```
dmalyshok@server:~$ less .bash_history

git clone https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4.git
dir
cd DevOps_online_Kiev_2021Q4/
ls
mkdir m1/task1.1

dmalyshok@server:~$ more .bashrc

# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
```
    7) * Describe in plans that you are working on laboratory work 1. Tip: You should read the documentation for the finger command.
```
sudo apt install finger

finger [-lmsp] [user ...] [user@host ...]

dmalyshok@server:~$ finger devops
Login: devops                           Name: Devops Course 2021
Directory: /home/devops                 Shell: /bin/bash
Office: 111-1111, 111-1111              Home Phone: 111-1111
On since Thu Dec  2 08:27 (UTC) on pts/1 from 192.168.233.1
   5 minutes 37 seconds idle
No mail.
No Plan.

dmalyshok@server:~$ finger -l
Login: dmalyshok                        Name:
Directory: /home/dmalyshok              Shell: /bin/bash
On since Thu Dec  2 08:07 (UTC) on pts/0 from 192.168.233.1 (messages off)
No mail.
No Plan.

Login: devops                           Name: Devops Course 2021
Directory: /home/devops                 Shell: /bin/bash
Office: 111-1111, 111-1111              Home Phone: 111-1111
On since Thu Dec  2 08:27 (UTC) on pts/1 from 192.168.233.1
   5 seconds idle
No mail.
No Plan.
```
    8) * List the contents of the home directory using the ls command, define its files and directories. Hint: Use the help system to familiarize yourself with the ls command.
```
dmalyshok@server:~$ ls -lh
total 48K
drwxrwxr-x 6 dmalyshok dmalyshok 4.0K Nov  5 09:15 DevOps_online_Kiev_2021Q4
-rw-rw-r-- 1 dmalyshok dmalyshok 3.8K Nov 28 10:14 devops.sql
-rw-rw-r-- 1 dmalyshok dmalyshok 3.8K Nov 28 10:34 devops.sql_bk
-rw-r--r-- 1 dmalyshok dmalyshok  586 Dec  1  2015 Forum.json
-rw-r--r-- 1 dmalyshok dmalyshok 8.9K Jan 14  2016 ProductCatalog.json
-rw-rw-r-- 1 dmalyshok dmalyshok 4.1K Nov 28 12:11 rds-dump.sql
-rw-r--r-- 1 dmalyshok dmalyshok 2.2K Dec  1  2015 Reply.json
-rw-rw-r-- 1 dmalyshok dmalyshok 2.0K Nov 25 15:32 sampledata.zip
-rw-r--r-- 1 dmalyshok dmalyshok 3.9K Dec  1  2015 Thread.json

dmalyshok@server:~$ ls -lF
total 48
drwxrwxr-x 6 dmalyshok dmalyshok 4096 Nov  5 09:15 DevOps_online_Kiev_2021Q4/
-rw-rw-r-- 1 dmalyshok dmalyshok 3884 Nov 28 10:14 devops.sql
-rw-rw-r-- 1 dmalyshok dmalyshok 3884 Nov 28 10:34 devops.sql_bk
-rw-r--r-- 1 dmalyshok dmalyshok  586 Dec  1  2015 Forum.json
-rw-r--r-- 1 dmalyshok dmalyshok 9073 Jan 14  2016 ProductCatalog.json
-rw-rw-r-- 1 dmalyshok dmalyshok 4164 Nov 28 12:11 rds-dump.sql
-rw-r--r-- 1 dmalyshok dmalyshok 2235 Dec  1  2015 Reply.json
-rw-rw-r-- 1 dmalyshok dmalyshok 1997 Nov 25 15:32 sampledata.zip
-rw-r--r-- 1 dmalyshok dmalyshok 3965 Dec  1  2015 Thread.json

dmalyshok@server:~$ ls -R
.:
DevOps_online_Kiev_2021Q4  devops.sql  devops.sql_bk  Forum.json  ProductCatalog.json  rds-dump.sql  Reply.json  sampledata.zip  Thread.json

./DevOps_online_Kiev_2021Q4:
m1  m2  m3

./DevOps_online_Kiev_2021Q4/m1:
task1.1

./DevOps_online_Kiev_2021Q4/m1/task1.1:
readme.txt

./DevOps_online_Kiev_2021Q4/m2:
task2.1  task2.2

./DevOps_online_Kiev_2021Q4/m2/task2.1:

./DevOps_online_Kiev_2021Q4/m2/task2.2:

./DevOps_online_Kiev_2021Q4/m3:
task3.1  task3.2

./DevOps_online_Kiev_2021Q4/m3/task3.1:

./DevOps_online_Kiev_2021Q4/m3/task3.2:

dmalyshok@server:~$ ls *.json
Forum.json  ProductCatalog.json  Reply.json  Thread.json

dmalyshok@server:~$ ls -d */
DevOps_online_Kiev_2021Q4/

dmalyshok@server:~$ ls -d .*/ */
../  ./  .aws/  .cache/  .config/  DevOps_online_Kiev_2021Q4/  .local/

dmalyshok@server:~$ ls -l --group-directories-first
total 52
drwxrwxr-x 6 dmalyshok dmalyshok 4096 Nov  5 09:15 DevOps_online_Kiev_2021Q4
drwxrwxr-x 2 dmalyshok dmalyshok 4096 Dec  2 09:09 W_directory_test
-rw-rw-r-- 1 dmalyshok dmalyshok 3884 Nov 28 10:14 devops.sql
-rw-rw-r-- 1 dmalyshok dmalyshok 3884 Nov 28 10:34 devops.sql_bk
-rw-r--r-- 1 dmalyshok dmalyshok  586 Dec  1  2015 Forum.json
-rw-r--r-- 1 dmalyshok dmalyshok 9073 Jan 14  2016 ProductCatalog.json
-rw-rw-r-- 1 dmalyshok dmalyshok 4164 Nov 28 12:11 rds-dump.sql
-rw-r--r-- 1 dmalyshok dmalyshok 2235 Dec  1  2015 Reply.json
-rw-rw-r-- 1 dmalyshok dmalyshok 1997 Nov 25 15:32 sampledata.zip
-rw-r--r-- 1 dmalyshok dmalyshok 3965 Dec  1  2015 Thread.json
```
## Task1.Part2
    1) Examine the tree command. Master the technique of applying a template, for example, display all files that contain a character c, or files that contain a specific sequence of characters. List subdirectories of the root directory up to and including the second nesting level.
```
dmalyshok@server:~$ tree
.
├── DevOps_online_Kiev_2021Q4
│   ├── m1
│   │   └── task1.1
│   │       └── readme.txt
│   ├── m2
│   │   ├── task2.1
│   │   └── task2.2
│   └── m3
│       ├── task3.1
│       └── task3.2
├── devops.sql
├── devops.sql_bk
├── Forum.json
├── ProductCatalog.json
├── rds-dump.sql
├── Reply.json
├── sampledata.zip
├── Thread.json
└── W_directory_test

10 directories, 9 files

dmalyshok@server:~$ tree -d
.
├── DevOps_online_Kiev_2021Q4
│   ├── m1
│   │   └── task1.1
│   ├── m2
│   │   ├── task2.1
│   │   └── task2.2
│   └── m3
│       ├── task3.1
│       └── task3.2
└── W_directory_test

10 directories

dmalyshok@server:~$ tree -P '*c*' -L 2
.
├── DevOps_online_Kiev_2021Q4
│   ├── m1
│   ├── m2
│   └── m3
├── ProductCatalog.json
└── W_directory_test

5 directories, 1 file

dmalyshok@server:~$ tree -P '*devops*' -L 2
.
├── DevOps_online_Kiev_2021Q4
│   ├── m1
│   ├── m2
│   └── m3
├── devops.sql
├── devops.sql_bk
└── W_directory_test

5 directories, 2 files
```
    2) What command can be used to determine the type of file (for example, text or binary)? Give an example.
```
dmalyshok@server:~$ file Thread.json  devops.sql key.pem cert.pem
Thread.json: JSON data
devops.sql:  ASCII text
key.pem:     ASCII text
cert.pem:    PEM certificate
```
    3) Master the skills of navigating the file system using relative and absolute paths. How can you go back to your home directory from anywhere in the filesystem?
```
Some examples of absolute path:
dmalyshok@server:/$ less /home/dmalyshok/key.pem
dmalyshok@server:/$ cd /home/dmalyshok/

Some examples of relative path:
dmalyshok@server:~/W_directory_test$ cd ../DevOps_online_Kiev_2021Q4/
dmalyshok@server:~/DevOps_online_Kiev_2021Q4$ cd ~/DevOps_online_Kiev_2021Q4/
dmalyshok@server:~/DevOps_online_Kiev_2021Q4$ cd m3/
```
    4) Become familiar with the various options for the ls command. Give examples of listing directories using different keys. Explain the information displayed on the terminal using the -l and -a switches.
```
List files in long format
Type the ls -l command to list the contents of the directory in a table format with columns including:

content permissions
number of links to the content
owner of the content
group owner of the content
size of the content in bytes
last modified date / time of the content
file or directory name

dmalyshok@server:~$ ls -l
total 60
-rw-rw-r-- 1 dmalyshok dmalyshok 1939 Dec  2 09:28 cert.pem
drwxrwxr-x 6 dmalyshok dmalyshok 4096 Nov  5 09:15 DevOps_online_Kiev_2021Q4
-rw-rw-r-- 1 dmalyshok dmalyshok 3884 Nov 28 10:14 devops.sql
-rw-rw-r-- 1 dmalyshok dmalyshok 3884 Nov 28 10:34 devops.sql_bk
-rw-r--r-- 1 dmalyshok dmalyshok  586 Dec  1  2015 Forum.json
-rw------- 1 dmalyshok dmalyshok 3414 Dec  2 09:28 key.pem
-rw-r--r-- 1 dmalyshok dmalyshok 9073 Jan 14  2016 ProductCatalog.json
-rw-rw-r-- 1 dmalyshok dmalyshok 4164 Nov 28 12:11 rds-dump.sql
-rw-r--r-- 1 dmalyshok dmalyshok 2235 Dec  1  2015 Reply.json
-rw-rw-r-- 1 dmalyshok dmalyshok 1997 Nov 25 15:32 sampledata.zip
-rw-r--r-- 1 dmalyshok dmalyshok 3965 Dec  1  2015 Thread.json
drwxrwxr-x 2 dmalyshok dmalyshok 4096 Dec  2 09:09 W_directory_test

List files including hidden files
Type the ls -a command to list files or directories including hidden files or directories. In Linux, anything that begins with a . is considered a hidden file:

dmalyshok@server:~$ ls -a
.                          devops.sql           rds-dump.sql
..                         devops.sql_bk        Reply.json
.aws                       Forum.json           sampledata.zip
.bash_history              .gitconfig           .ssh
.bash_logout               key.pem              .sudo_as_admin_successful
.bashrc                    .lesshst             Thread.json
.cache                     .local               .viminfo
cert.pem                   .mysql_history       W_directory_test
.config                    ProductCatalog.json
DevOps_online_Kiev_2021Q4  .profile
```
    5) Perform the following sequence of operations: - create a subdirectory in the home directory; - in this subdirectory create a file containing information about directories located in the root directory (using I/O redirection operations);
```
dmalyshok@server:~$ mkdir test; ls / -d /* > ~/test/info_dir.txt

- view the created file;

dmalyshok@server:~$ cat ~/test/info_dir.txt
/
/bin
/boot
/cdrom
/dev
/etc
/home
/lib
...

- copy the created file to your home directory using relative and absolute addressing.
dmalyshok@server:~$ cp /home/dmalyshok/test/info_dir.txt /home/dmalyshok/
dmalyshok@server:~$ ls
DevOps_online_Kiev_2021Q4  git  info_dir.txt  test

dmalyshok@server:~$ cp /home/dmalyshok/test/info_dir.txt ~/info_dir.txt
dmalyshok@server:~$ ls
DevOps_online_Kiev_2021Q4  git  info_dir.txt  test

dmalyshok@server:~$ cp ~/test/info_dir.txt ~/info_dir.txt
dmalyshok@server:~$ ls
DevOps_online_Kiev_2021Q4  git  info_dir.txt  test

dmalyshok@server:~$ cp test/info_dir.txt ~/info_dir.txt
dmalyshok@server:~$ ls
DevOps_online_Kiev_2021Q4  git  info_dir.txt  test

- delete the previously created subdirectory with the file requesting removal;

dmalyshok@server:~$ rm -r test/
dmalyshok@server:~$ ls
cert.pem                   info_dir.txt         sampledata.zip
DevOps_online_Kiev_2021Q4  key.pem              Thread.json
devops.sql                 ProductCatalog.json  W_directory_test
devops.sql_bk              rds-dump.sql
Forum.json                 Reply.json

- delete the file copied to the home directory.

dmalyshok@server:~$ ls
cert.pem                   devops.sql_bk  ProductCatalog.json  sampledata.zip
DevOps_online_Kiev_2021Q4  Forum.json     rds-dump.sql         Thread.json
devops.sql                 key.pem        Reply.json           W_directory_test
dmalyshok@server:~$
```

    6) Perform the following sequence of operations:
```
- create a subdirectory test in the home directory;
dmalyshok@server:~$ mkdir test
- copy the .bash_history file to this directory while changing its name to labwork2;
dmalyshok@server:~$ cp .bash_history test/labwork2
- create a hard and soft link to the labwork2 file in the test subdirectory;
dmalyshok@server:~/test$ ln -s labwork2 sym_link_to_labwork2
dmalyshok@server:~/test$ ln -s /home/dmalyshok/test/labwork2 sym_link_absolut_to_labwork2
dmalyshok@server:~/test$ ls -li
total 8
1078271 -rw------- 1 dmalyshok dmalyshok 7534 Dec  2 11:13 labwork2
1078273 lrwxrwxrwx 1 dmalyshok dmalyshok   29 Dec  2 11:34 sym_link_absolut_to_labwork2 -> /home/dmalyshok/test/labwork2
1078272 lrwxrwxrwx 1 dmalyshok dmalyshok    8 Dec  2 11:30 sym_link_to_labwork2 -> labwork2

dmalyshok@server:~/test$ ln labwork2 hard_link_to_labwork2
dmalyshok@server:~/test$ ls -li
total 16
1078271 -rw------- 2 dmalyshok dmalyshok 7534 Dec  2 11:13 hard_link_to_labwork2
1078271 -rw------- 2 dmalyshok dmalyshok 7534 Dec  2 11:13 labwork2
1078273 lrwxrwxrwx 1 dmalyshok dmalyshok   29 Dec  2 11:34 sym_link_absolut_to_labwork2 -> /home/dmalyshok/test/labwork2
1078272 lrwxrwxrwx 1 dmalyshok dmalyshok    8 Dec  2 11:30 sym_link_to_labwork2 -> labwork2

- how to define soft and hard link, what do these concepts;

Hard link

1078271 -rw------- 2 dmalyshok dmalyshok 7534 Dec  2 11:13 hard_link_to_labwork2
1078271 -rw------- 2 dmalyshok dmalyshok 7534 Dec  2 11:13 labwork2

File have the same the inodes number (1078271) and file permissions (-rw-------).
Hence, it is proved that hard link file shares the same inodes number and permissions of original file.

Soft Link

1078273 lrwxrwxrwx 1 dmalyshok dmalyshok   29 Dec  2 11:34 sym_link_absolut_to_labwork2 -> /home/dmalyshok/test/labwork2
1078272 lrwxrwxrwx 1 dmalyshok dmalyshok    8 Dec  2 11:30 sym_link_to_labwork2 -> labwork2

- change the data by opening a symbolic link. What changes will happen and why
dmalyshok@server:~/test$ vi sym_link_to_labwork2
add CHANGE DATA first string

dmalyshok@server:~/test$ head labwork2
CHANGE DATA
git clone https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4.git
dir
cd DevOps_online_Kiev_2021Q4/
ls
mkdir m1/task1.1
mkdir -p m1/task1.1
mkdir -p m2/task2.1
mkdir -p m2/task2.2
mkdir -p m3/task3.1

- rename the hard link file to hard_lnk_labwork2;
dmalyshok@server:~/test$ mv hard_link_to_labwork2 hard_lnk_labwork2
- rename the soft link file to symb_lnk_labwork2 file;
dmalyshok@server:~/test$ mv sym_link_to_labwork2 symb_lnk_labwork2
- then delete the labwork2. What changes have occurred and why?
dmalyshok@server:~/test$ rm labwork2

dmalyshok@server:~/test$ head hard_lnk_labwork2
CHANGE DATA
git clone https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4.git
dir
cd DevOps_online_Kiev_2021Q4/
ls
mkdir m1/task1.1
mkdir -p m1/task1.1
mkdir -p m2/task2.1
mkdir -p m2/task2.2
mkdir -p m3/task3.1

dmalyshok@server:~/test$ head symb_lnk_labwork2
head: cannot open 'symb_lnk_labwork2' for reading: No such file or directory
```
    7) Using the locate utility, find all files that contain the squid and traceroute sequence.
```
dmalyshok@server:~/test$ sudo apt-get install locate
dmalyshok@server:~$ sudo updatedb
dmalyshok@server:~$ locate -S
Database /var/cache/locate/locatedb is in the GNU LOCATE02 format.
Database was last modified at 2021:12:02 13:05:22.191768586 +0000
Locate database size: 2289241 bytes
All Filenames: 207171
File names have a cumulative length of 11950209 bytes.
Of those file names,

        11 contain whitespace,
        0 contain newline characters,
        and 10 contain characters with the high bit set.
Compression ratio 80.84% (higher is better)

dmalyshok@server:~$ locate -A squid
/usr/lib/python3/dist-packages/sos/report/plugins/__pycache__/squid.cpython-38.pyc
/usr/lib/python3/dist-packages/sos/report/plugins/squid.py
/usr/share/vim/vim81/syntax/squid.vim

dmalyshok@server:~$ locate -A traceroute
/etc/alternatives/traceroute6
/etc/alternatives/traceroute6.8.gz
/usr/bin/traceroute6
/usr/bin/traceroute6.iputils
/usr/lib/modules/5.4.0-89-generic/kernel/drivers/tty/n_tracerouter.ko
/usr/lib/modules/5.4.0-90-generic/kernel/drivers/tty/n_tracerouter.ko
/usr/share/man/man8/traceroute6.8.gz
/usr/share/man/man8/traceroute6.iputils.8.gz
/var/lib/dpkg/alternatives/traceroute6
```
    8) Determine which partitions are mounted in the system, as well as the types of these partitions.
```
root@server:~# df -h
Filesystem                         Size  Used Avail Use% Mounted on
udev                               936M     0  936M   0% /dev
tmpfs                              196M  1.3M  195M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   19G  6.5G   12G  37% /
tmpfs                              980M     0  980M   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
tmpfs                              980M     0  980M   0% /sys/fs/cgroup
/dev/loop0                          62M   62M     0 100% /snap/core20/1169
/dev/loop1                          62M   62M     0 100% /snap/core20/1242
/dev/loop2                          56M   56M     0 100% /snap/core18/2253
/dev/loop3                          71M   71M     0 100% /snap/lxd/21029
/dev/loop4                          68M   68M     0 100% /snap/lxd/21835
/dev/loop5                          56M   56M     0 100% /snap/core18/2246
/dev/loop6                          43M   43M     0 100% /snap/snapd/14066
/dev/loop7                          33M   33M     0 100% /snap/snapd/13640
/dev/sda2                          976M  203M  707M  23% /boot
tmpfs                              196M     0  196M   0% /run/user/1001

root@server:~# lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0                       7:0    0 61.9M  1 loop /snap/core20/1169
loop1                       7:1    0 61.9M  1 loop /snap/core20/1242
loop2                       7:2    0 55.5M  1 loop /snap/core18/2253
loop3                       7:3    0 70.3M  1 loop /snap/lxd/21029
loop4                       7:4    0 67.2M  1 loop /snap/lxd/21835
loop5                       7:5    0 55.5M  1 loop /snap/core18/2246
loop6                       7:6    0 42.2M  1 loop /snap/snapd/14066
loop7                       7:7    0 32.5M  1 loop /snap/snapd/13640
sda                         8:0    0   20G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0    1G  0 part /boot
└─sda3                      8:3    0   19G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0   19G  0 lvm  /
sr0                        11:0    1 1024M  0 rom

dmalyshok@server:~$ df -T
Filesystem                        Type     1K-blocks    Used Available Use% Mounted on
udev                              devtmpfs    957996       0    957996   0% /dev
tmpfs                             tmpfs       200636    1284    199352   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv ext4      19475088 6775672  11687092  37% /
tmpfs                             tmpfs      1003164       0   1003164   0% /dev/shm
tmpfs                             tmpfs         5120       0      5120   0% /run/lock
tmpfs                             tmpfs      1003164       0   1003164   0% /sys/fs/cgroup
/dev/loop2                        squashfs     72064   72064         0 100% /snap/lxd/21029
/dev/loop3                        squashfs     63360   63360         0 100% /snap/core20/1169
/dev/loop4                        squashfs     56832   56832         0 100% /snap/core18/2253
/dev/loop1                        squashfs     68864   68864         0 100% /snap/lxd/21835
/dev/loop0                        squashfs     63360   63360         0 100% /snap/core20/1242
/dev/loop5                        squashfs     56832   56832         0 100% /snap/core18/2246
/dev/sda2                         ext4        999320  207412    723096  23% /boot
/dev/loop6                        squashfs     43264   43264         0 100% /snap/snapd/14066
/dev/loop7                        squashfs     33280   33280         0 100% /snap/snapd/13640
tmpfs                             tmpfs       200632       0    200632   0% /run/user/1001
```
    9) Count the number of lines containing a given sequence of characters in a given file.
```
dmalyshok@server:~$ wc labwork2
 362 1025 7534 labwork2


362 is the number of lines.
1025 is the number of words.
7534 is the number of bytes.

dmalyshok@server:~$ wc -l labwork2
362 labwork2
dmalyshok@server:~$ wc -w labwork2
1025 labwork2
dmalyshok@server:~$ wc -c labwork2
7534 labwork2
dmalyshok@server:~$ wc -m labwork2
7523 labwork2

-l, --lines - Print the number of lines.
-w, --words - Print the number of words.
-m, --chars - Print the number of characters.
-c, --bytes - Print the number of bytes.
-L, --max-line-length - Print the length of the longest line.
```
    10) Using the find command, find all files in the /etc directory containing the host character sequence.
```
dmalyshok@server:~$ sudo find /etc -type f -name "*host*"
[sudo] password for dmalyshok:
/etc/hosts.deny
/etc/X11/Xsession.d/60x11-common_localhost
/etc/X11/Xsession.d/35x11-common_xhost-local
/etc/hosts
/etc/cloud/templates/hosts.alpine.tmpl
/etc/cloud/templates/hosts.debian.tmpl
/etc/cloud/templates/hosts.redhat.tmpl
/etc/cloud/templates/hosts.suse.tmpl
/etc/cloud/templates/hosts.freebsd.tmpl
/etc/ImageMagick-6/type-ghostscript.xml
/etc/host.conf
/etc/ssh/ssh_host_rsa_key.pub
/etc/ssh/ssh_host_ed25519_key
/etc/ssh/ssh_host_ed25519_key.pub
/etc/ssh/ssh_host_rsa_key
/etc/ssh/ssh_host_ecdsa_key
/etc/ssh/ssh_host_dsa_key
/etc/ssh/ssh_host_dsa_key.pub
/etc/ssh/ssh_host_ecdsa_key.pub
/etc/hostname
/etc/apache2/mods-available/vhost_alias.load
/etc/apache2/mods-available/authz_host.load
/etc/apache2/conf-available/other-vhosts-access-log.conf
/etc/hosts.allow
```
    11) List all objects in /etc that contain the ss character sequence. How can I duplicate a similar command using a bunch of grep?
```
dmalyshok@server:~$ sudo find /etc -maxdepth 1 -name "*ss*"
/etc/ssl
/etc/ssh
/etc/issue
/etc/gss
/etc/nsswitch.conf
/etc/issue.net
/etc/passwd-
/etc/passwd

dmalyshok@server:~$ ls /etc -la | grep "ss"
drwxr-xr-x   3 root root       4096 Aug 24 08:45 gss
-rw-r--r--   1 root root         26 Aug  4 14:53 issue
-rw-r--r--   1 root root         19 Aug  4 14:53 issue.net
-rw-r--r--   1 root root        510 Aug 24 08:43 nsswitch.conf
-rw-r--r--   1 root root       2177 Nov 29 19:57 passwd
-rw-r--r--   1 root root       2177 Nov 29 19:57 passwd-
drwxr-xr-x   4 root root       4096 Nov  4 20:06 ssh
drwxr-xr-x   4 root root       4096 Nov  4 20:00 ssl
```
    12) Organize a screen-by-screen print of the contents of the /etc directory. Hint: You must use stream redirection operations.
```
dmalyshok@server:~$ ls /etc | less
```
    13) What are the types of devices and how to determine the type of device? Give examples.
```
dmalyshok@server:~$ ls -l /dev
total 0
crw------- 1 root root     10, 175 Dec  3 09:57 agpgart
crw-r--r-- 1 root root     10, 235 Dec  3 09:57 autofs
drwxr-xr-x 2 root root         340 Dec  3 09:58 block
drwxr-xr-x 2 root root          80 Dec  3 09:57 bsg
crw-rw---- 1 root disk     10, 234 Dec  3 09:57 btrfs-control
drwxr-xr-x 3 root root          60 Dec  3 09:57 bus
lrwxrwxrwx 1 root root           3 Dec  3 09:57 cdrom -> sr0
lrwxrwxrwx 1 root root           3 Dec  3 09:57 cdrw -> sr0
drwxr-xr-x 2 root root        3720 Dec  3 09:58 char
crw--w---- 1 root tty       5,   1 Dec  3 09:58 console
lrwxrwxrwx 1 root root          11 Dec  3 09:57 core -> /proc/kcore
drwxr-xr-x 3 root root          60 Dec  3 09:57 cpu
crw------- 1 root root     10,  59 Dec  3 09:57 cpu_dma_latency

The columns are as follows from left to right:

Permissions
Owner
Group
Major Device Number
Minor Device Number
Timestamp
Device Name
Remember in the ls command you can see the type of file with the first bit on each line. Device files are denoted as the following:

c - character
b - block
p - pipe
s - socket
Character Device

These devices transfer data, but one a character at a time. You'll see a lot of pseudo devices (/dev/null) as character devices, these devices aren't really physically connected to the machine, but they allow the operating system greater functionality.

Block Device

These devices transfer data, but in large fixed-sized blocks. You'll most commonly see devices that utilize data blocks as block devices, such as harddrives, filesystems, etc.

Pipe Device

Named pipes allow two or more processes to communicate with each other, these are similar to character devices, but instead of having output sent to a device, it's sent to another process.

Socket Device

Socket devices facilitate communication between processes, similar to pipe devices but they can communicate with many processes at once.

Device Characterization

Devices are characterized using two numbers, major device number and minor device number. You can see these numbers in the above ls example, they are separated by a comma. For example, let's say a device had the device numbers: 8, 0:

The major device number represents the device driver that is used, in this case 8, which is often the major number for sd block devices. The minor number tells the kernel which unique device it is in this driver class, in this case 0 is used to represent the first device (a).
```
    14) How to determine the type of file in the system, what types of files are there?
```
As per my knowledge, totally 7 types of files are available in Linux with 3 Major categories. The details are below.

Regular File
Directory File
Special Files (There are five types of files in the special category)
Link File
Character Device File
Socket File
Named Pipe File
Block File
Refer the below table for a better understanding of file types and their symbols in Linux.

+--------------+------------------------+
|    Symbol    |      File Types        |
+--------------+------------------------+
|      -       | Regular File           |
|      d       | Directory              | 
|      l       | Link File              |
|      c       | Character Device File  |
|      s       | Local Socket File      |
|      p       | Named Pipe File        |
|      b       | Block Device File      |
+--------------+------------------------+0

ls -la | grep ^-

dmalyshok@server:~$ ls -la | grep ^-
-rw-------  1 dmalyshok dmalyshok 10016 Dec  2 16:09 .bash_history

ls -la | grep ^d
dmalyshok@server:~$ ls -la | grep ^d
drwxrwxr-x  6 dmalyshok dmalyshok  4096 Nov  5 09:15 DevOps_online_Kiev_2021Q4

ls -la | grep ^l
dmalyshok@server:~/test$ ls -la | grep ^l
lrwxrwxrwx  1 dmalyshok dmalyshok    8 Dec  2 11:30 symb_lnk_labwork2 -> labwork2

ls -la | grep ^c
dmalyshok@server:~/test$ ls -la /dev | grep ^c
crw-------  1 root root     10, 175 Dec  3 09:57 agpgart

ls -la | grep ^b
dmalyshok@server:~/test$ ls -la /dev | grep ^b
brw-rw----  1 root disk    253,   0 Dec  3 09:57 dm-0

ls -la | grep ^s

ls -la | grep ^p

OR file OR stat

symb_lnk_labwork2: broken symbolic link to labwork2
dmalyshok@server:~/test$ file symb_lnk_labwork2

dmalyshok@server:~/test$ stat symb_lnk_labwork2
  File: symb_lnk_labwork2 -> labwork2
  Size: 8               Blocks: 0          IO Block: 4096   symbolic link
Device: fd00h/64768d    Inode: 1078272     Links: 1
Access: (0777/lrwxrwxrwx)  Uid: ( 1001/dmalyshok)   Gid: ( 1001/dmalyshok)
Access: 2021-12-03 15:37:13.581667149 +0000
Modify: 2021-12-02 11:30:22.203806807 +0000
Change: 2021-12-02 12:56:48.623772029 +0000
 Birth: -
```
    15) * List the first 5 directory files that were recently accessed in the /etc directory.
```
dmalyshok@server:~/test$ ls -1t /etc | head -5
alternatives
cron.daily
passwd
passwd-
shadow

dmalyshok@server:~/test$ ls -1tr /etc | tail -5
shadow
passwd-
passwd
cron.daily
alternatives
```
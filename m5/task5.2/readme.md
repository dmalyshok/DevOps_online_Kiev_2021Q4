## Task2

    1) Analyze the structure of the /etc/passwd and /etc/group file, what fields are present in it, what users exist on the system? Specify several pseudo-users, how to define them?
```
dmalyshok@server:~$ head -3 /etc/passwd
root:x:0:0:Malyshok,Main Room,111-11111,111-1111:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin

/etc/passwd Format

Username: It is used when user logs in. It should be between 1 and 32 characters in length.

Password: An x character indicates that encrypted password is stored in /etc/shadow file. Please note that you need to use the passwd command to computes the hash of a password typed at the CLI or to store/update the hash of the password in /etc/shadow file.

User ID (UID): Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.

Group ID (GID): The primary group ID (stored in /etc/group file)
User ID Info (GECOS): The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.

Home directory: The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /

Command/shell: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell. For example, sysadmin can use the nologin shell, which acts as a replacement shell for the user accounts. If shell set to /sbin/nologin and the user tries to log in to the Linux system directly, the /sbin/nologin shell closes the connection.

dmalyshok@server:~$ head -3 /etc/group
root:x:0:
daemon:x:1:
bin:x:2:

Group Name: It is the name of group. If you run ls -l command, you will see this name printed in the group field.

Password: Generally password is not used, hence it is empty/blank. It can store encrypted password. This is useful to implement privileged groups.

Group ID (GID): Each user must be assigned a group ID. You can see this number in your /etc/passwd file.

Group List: It is a list of user names of users who are members of the group. The user names, must be separated by commas.

There are three types of Linux users:
Superuser (root uid = 0)
General user (UID 500-60000)
Pseudo user (UID 1-499)
Note: root is not necessarily a superuser, but the user with uid = 0 must be a superuser.

Pseudo user

Pseudo users are related to system and program services
Any Linux system has these pseudo users by default
Mail news games, Apache FTP, MySQL and sshd are related to the process of Linux system
Pseudo users usually do not need or cannot log in to the system
There can be no host directory
```
    2) What are the uid ranges? What is UID? How to define it?
```
UID : User Identifier
UID (User identifier)is a number that assigned by Linux to every user of the system. UIDs are stored in the /etc/passwd
Value of UID
0 to 99 value = System
100 to 499 = Reserved for dynamic allocation
500 / 1000 = Reserved for new users

dmalyshok@server:~$ cat /etc/login.defs | grep UID
UID_MIN                  1000
UID_MAX                 60000
#SYS_UID_MIN              100
#SYS_UID_MAX              999
dmalyshok@server:~$

dmalyshok@server:~$ id
uid=1001(dmalyshok) gid=1001(dmalyshok) groups=1001(dmalyshok),27(sudo)
dmalyshok@server:~$ id devops
uid=1002(devops) gid=1002(devops) groups=1002(devops)
```
    3) What is GID? How to define it?
```
GID (Group Identifier)
A group is a collection of users having similar permissions. Like a user who is identified by the UID, a group is identified by the GID in a system. GID 0 is reserved for the root group.

GID
Groups in Linux are defined by GIDs (group IDs).
GID 0 (zero) is reserved for the root group.
GID 1–99 are reserved for the system and application use.
GID 100+ allocated for the user’s group.

dmalyshok@server:~$ id -G dmalyshok
1001 27
dmalyshok@server:~$ id -u dmalyshok
1001
dmalyshok@server:~$ id -g dmalyshok
1001
dmalyshok@server:~$ id -G dmalyshok
1001 27
dmalyshok@server:~$ id
uid=1001(dmalyshok) gid=1001(dmalyshok) groups=1001(dmalyshok),27(sudo)
```
    4) How to determine belonging of user to the specific group?
```
dmalyshok@server:~$ id -g dmalyshok
1001
dmalyshok@server:~$ id -G dmalyshok
1001 27
dmalyshok@server:~$ groups dmalyshok
dmalyshok : dmalyshok sudo
```
    5) What are the commands for adding a user to the system? What are the basic parameters required to create a user?
```
Syntax:
useradd [options] name_of_the_user

Working with useradd Command
1. To add a simple user
sudo useraddtest_user

2. To give a home directory path for new user
sudo useradd -d /home/test_user test_user

3. To create a user with specific user id
sudo useradd -u 1234 test_user

4. To create a user with specific group id
sudo useradd -g 1000 test_user

5. To create a user without home directory
sudo useradd -M test_user

6. To create a user with expiry date
sudo useradd -e 2021-12-12 test_user

7. To create a user with a comment
sudo useradd -c "This is a test user" test_user

8. To create a user with changed login shell
sudo useradd -s /bin/bash test_user

9 To set an unencrypted password for the user
sudo useradd -p test_password test_user

10. To display help
sudo useradd --help
```
    6) How do I change the name (account name) of an existing user?
```
sudo usermod -l newUsername oldUsername
sudo usermod -d /home/newHomeDir -m newUsername

dmalyshok@server:~$ sudo usermod -l malyshok metest
malyshok:x:1003:1003::/home/metest:/bin/bash

dmalyshok@server:~$ sudo usermod -d /home/malyshok -m malyshok

dmalyshok@server:~$ grep -w '^malyshok' /etc/passwd
malyshok:x:1003:1003::/home/malyshok:/bin/bash
```
    7) What is skell_dir? What is its structure?
```
The skel directory
Directory /etc/skel/ (skel is derived from the “skeleton”) is used to initiate home directory when a user is first created. A sample layout of “skeleton” user files is as shown below:

dmalyshok@server:~$ ls -lart /etc/skel
total 20
-rw-r--r--   1 root root  807 Feb 25  2020 .profile
-rw-r--r--   1 root root 3771 Feb 25  2020 .bashrc
-rw-r--r--   1 root root  220 Feb 25  2020 .bash_logout
drwxr-xr-x   2 root root 4096 Aug 24 08:45 .
drwxr-xr-x 112 root root 4096 Dec  4 09:56 ..

Below is a sample /etc/defualt/useradd file which defines the skel directory. You can change the default location /etc/skel to any other location.

dmalyshok@server:~$ cat /etc/default/useradd | grep SKEL
# The SKEL variable specifies the directory containing "skeletal" user
# SKEL=/etc/skel
```
    8) How to remove a user from the system (including his mailbox)?
```
userdel Command Syntax
The syntax for the userdel command is as follows:
userdel [OPTIONS] USERNAME

How to Delete User in Linux
To delete a user account named username using the userdel command you would run:
userdel username

Use the -r (--remove) option to force userdel to remove the user’s home directory and mail spool:

userdel -r username

Another option is to use the -f (--force) option that tells userdel to forcefully remove the user account, even if the user is still logged in or if there are running processes that belong to the user.
userdel -f username

dmalyshok@server:~$ sudo userdel -r malyshok
userdel: user malyshok is currently used by process 7228
dmalyshok@server:~$ w
 10:13:38 up  3:21,  2 users,  load average: 0.20, 0.18, 0.12
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
dmalysho pts/0    192.168.233.1    06:52    0.00s  0.47s  0.00s w
malyshok pts/1    192.168.233.1    10:10    3:14   0.09s  0.09s -bash
dmalyshok@server:~$ sudo userdel -r -f malyshok
userdel: user malyshok is currently used by process 7228
userdel: malyshok mail spool (/var/mail/malyshok) not found
dmalyshok@server:~$ w
 10:13:59 up  3:22,  2 users,  load average: 0.13, 0.16, 0.11
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
dmalysho pts/0    192.168.233.1    06:52    3.00s  0.48s  0.00s w
dmalyshok@server:~$ ls /home
devops  dmalyshok  dmlshk
dmalyshok@server:~$ grep -w 'malyshok' /etc/passwd
```
    9) What commands and keys should be used to lock and unlock a user account?
```
Lock:
dmalyshok@server:~$ sudo passwd -l devops
passwd: password expiry information changed.
dmalyshok@server:~$ sudo usermod -L devops

dmalyshok@server:~$ sudo grep -w 'devops' /etc/shadow
devops:!$6$3S.G/UM4j379S/a4$3Gqzo5BqRDEHs1PYUX06UtoU4Zud4I3yrI0s0QvyKRantYNzHSQLuFQw3L4HPYKpIiryugqczKYYd1yRVx5ui.:18960:0:99999:7:::

Unlock:

dmalyshok@server:~$ sudo usermod -U devops
dmalyshok@server:~$ sudo passwd -u devops
passwd: password expiry information changed.
dmalyshok@server:~$ sudo grep -w 'devops' /etc/shadow
devops:$6$3S.G/UM4j379S/a4$3Gqzo5BqRDEHs1PYUX06UtoU4Zud4I3yrI0s0QvyKRantYNzHSQLuFQw3L4HPYKpIiryugqczKYYd1yRVx5ui.:18960:0:99999:7:::
```
    10) How to remove a user's password and provide him with a password-free login for subsequent password change?
```
dmalyshok@server:~$ sudo chage -l devops
Last password change                                    : Nov 29, 2021
Password expires                                        : never
Password inactive                                       : never
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 99999
Number of days of warning before password expires       : 7

dmalyshok@server:~$ sudo chage --lastday 0 devops
dmalyshok@server:~$ sudo chage -l devops
Last password change                                    : password must be changed
Password expires                                        : password must be changed
Password inactive                                       : password must be changed
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 99999
Number of days of warning before password expires       : 7

OR
dmalyshok@server:~$ sudo passwd --expire devops

dmalyshok@server:~$ sudo passwd -d 'devops'
dmalyshok@server:~$ su devops
You are required to change your password immediately (administrator enforced)
New password:
```
    11) Display the extended format of information about the directory, tell about the information columns displayed on the terminal.
```
dmalyshok@server:~$ ls -lahinF
total 156K
1067971 drwxr-xr-x 10 1001 1001 4.0K Dec  2 12:53 ./
1048577 drwxr-xr-x  5    0    0 4.0K Dec  4 10:13 ../
1082344 drwxrwxr-x  2 1001 1001 4.0K Nov 28 13:16 .aws/
1068109 -rw-------  1 1001 1001 9.8K Dec  2 16:09 .bash_history
1067974 -rw-r--r--  1 1001 1001  220 Nov  5 07:32 .bash_logout
1067972 -rw-r--r--  1 1001 1001 3.7K Nov  5 07:32 .bashrc
1067975 drwx------  3 1001 1001 4.0K Nov  5 07:33 .cache/

Using -F option in the ls command will include the’/’ Character in the end of each directory.
-ln UID and GID of Files use –ln 
–a option lists all files including hidden starting with ‘.’
-h - human view
-i - print the index number of each file
```
    12) What access rights exist and for whom (i. e., describe the main roles)? Briefly describe the acronym for access rights.
```
dmalyshok@server:~$ ls -ln
total 72
-rw-rw-r-- 1 1001 1001 1939 Dec  2 09:28 cert.pem
drwxrwxr-x 6 1001 1001 4096 Nov  5 09:15 DevOps_online_Kiev_2021Q4

-rwxrwxrwx

File Types
The possible file types you may see are depicted by preceding the permissions by one of these:

- = Regular File
d = Directory
l = Symbolic Link
b = Block Special Device
c = Character Device
s = Unix Socket (local domain socket)
p = Named Pipe

- rwx   rwx  rwx
  user group other

Permission Types
Each file or directory has three basic permission types:

read – The Read permission refers to a user’s capability to read the contents of the file.
write – The Write permissions refer to a user’s capability to write or modify a file or directory.
execute – The Execute permission affects a user’s capability to execute a file or view the contents of a directory.

Permissions: Octal Representation
Sometimes, you'll see permissions referred to numerically in base 8 octal (i.e. using digits 0-7).

Permissions                 Symbolic	    Binary	  Octal
read, write, and execute	rwx	            111	        7
read and write	            rw-	            110	        6
read and execute	        r-x	            101	        5
read	                    r--	            100     	4
write and execute	        -wx	            011	        3
write	                    -w-	            010	        2
execute	                    --x	            001	        1
no permissions	            ---	            000	        0

Other Octal Permission Examples:

User / Group / Other rwx Mode Symbols	Octal Equivalent
-rwxr-xr-x	                                755
-rw-rw-r--	                                664
-rw-r--r--	                                644
-rw-------	                                600
```
    13) What is the sequence of defining the relationship between the file and the user?
```
dmalyshok@server:~$ touch file_permission.txt
dmalyshok@server:~$ ls -l file_permission.txt
-rw-rw-r-- 1 dmalyshok dmalyshok 0 Dec  4 11:21 file_permission.txt 

Where,

-rw-rw-r-- : file mode (-rw-rw-r-- its  - file rw- - for user; rw- - for group; r-- - read for others)
1 – number of links
dmalyshok – Owner name (if user name is not a known user, the numeric user id displayed)
dmalyshok – Group name (if group name is not a known group, the numeric group id displayed)
0 – number of bytes in the file (file size)
Dec  4 11:21 – abbreviated month, day-of-month file was
last modified, hour file last modified, minute file last modified
file_permission.txt  – File name / pathname

dmalyshok@server:~$ ls -ln file_permission.txt
-rw-rw-r-- 1 1001 1001 0 Dec  4 11:23 file_permission.txt
dmalyshok@server:~$ id
uid=1001(dmalyshok) gid=1001(dmalyshok) groups=1001(dmalyshok),27(sudo)

1001 1001 - owner file
```
    14) What commands are used to change the owner of a file (directory), as well as the mode of access to the file? Give examples, demonstrate on the terminal.
```
chown new-owner  filename

dmalyshok@server:~$ sudo chown devops file_permission.txt
[sudo] password for dmalyshok:
dmalyshok@server:~$ ls -ln file_permission.txt
-rwxr--r-- 1 1002 1001 0 Dec  4 11:23 file_permission.txt
dmalyshok@server:~$ ls -l file_permission.txt
-rwxr--r-- 1 devops dmalyshok 0 Dec  4 11:23 file_permission.txt

chgrp group filename

dmalyshok@server:~$ sudo chgrp root file_permission.txt
dmalyshok@server:~$ ls -l file_permission.txt
-rwxr--r-- 1 root root 0 Dec  4 11:23 file_permission.txt

Changing File Permissions - Chmod
The chmod command is used to change the various permission bits of a file or directory.

The command takes the general form:

chmod

The letters for user, group, and other are u, g, and o respectively. The letter a is used to mean all three of these categories.
The MODE above takes the form (as per manpage):

[ugoa...][[+-=][permissions...]...]
So, the operations available are:

+ (add the permissions to what currently exists).
- (remove the permissions from what currently exists).
= (set to this value only, replacing existing permissions).

When you combine the above with the permission letters r, w, and x you can run chmod commands like those shown below.
For example, to use chmod to set permissions of file "filename" to -rwxrwxrwx you could run:

chmod a=rwx filename

dmalyshok@server:~$ chmod a=rwx file_permission.txt
dmalyshok@server:~$ ls -ln file_permission.txt
-rwxrwxrwx 1 1001 1001 0 Dec  4 11:23 file_permission.txt
dmalyshok@server:~$ chmod o-wx file_permission.txt
dmalyshok@server:~$ ls -ln file_permission.txt
-rwxrwxr-- 1 1001 1001 0 Dec  4 11:23 file_permission.txt
dmalyshok@server:~$ chmod g-wx file_permission.txt
dmalyshok@server:~$ ls -ln file_permission.txt
-rwxr--r-- 1 1001 1001 0 Dec  4 11:23 file_permission.txt
```
    15) What is an example of octal representation of access rights? Describe the umask command.
```
Permissions                 Symbolic	    Binary	  Octal
read, write, and execute	rwx	            111	        7
read and write	            rw-	            110	        6
read and execute	        r-x	            101	        5
read	                    r--	            100     	4
write and execute	        -wx	            011	        3
write	                    -w-	            010	        2
execute	                    --x	            001	        1
no permissions	            ---	            000	        0

Read  	  Write  	  Execute	Total Value	   Symbolic Equivalent:
0	        0	        0	        0	
0	        0	        1	        1	        x
0	        2	        0	        2	        w
0	        2	        1	        3	        wx
4	        0	        0	        4	        r
4	        0	        1	        5	        rx
4	        2	        0	        6	        rw
4	        2	        1	        7	        rwx


Umask, or the user file-creation mode, is a Linux command that is used to assign the default file permission sets for newly created folders and files. The term mask references the grouping of the permission bits, each of which defines how its corresponding permission is set for newly created files. The bits in the mask may be changed by invoking the umask command.

(default users)umask 0002
(root) umask 0022

Numeric Headings
0 --- no permission
1 --x execute
2 -w- write
3 -wx write and execute
4 r-- read
5 r-x read and execute
6 rw- read and write
7 rwx read, write and execute

Below, we can see the translated values of the octal and how they are related.

Number	Permission
4	read
2	write
1	execute

dmalyshok@server:~$ umask
0002
dmalyshok@server:~$ umask -S
u=rwx,g=rwx,o=rx

To determine the umask value you want to set, subtract the value of the permissions you want from 666 (for a file) or 777 (for a directory). The remainder is the value to use with the umask command. For example, suppose you want to change the default mode for files to 644 (rw-r--r--). The difference between 666 and 644 is 022, which is the value you would use as an argument to the umask command.

dmalyshok@server:~$ touch umask.txt
dmalyshok@server:~$ stat umask.txt
  File: umask.txt
  Size: 0               Blocks: 0          IO Block: 4096   regular empty file
Device: fd00h/64768d    Inode: 1078275     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1001/dmalyshok)   Gid: ( 1001/dmalyshok)
Access: 2021-12-04 12:04:16.921683904 +0000
Modify: 2021-12-04 12:04:16.921683904 +0000
Change: 2021-12-04 12:04:16.921683904 +0000
 Birth: -
dmalyshok@server:~$ 666 - 002 = 664

dmalyshok@server:~$ mkdir umask_dir
dmalyshok@server:~$ stat umask_dir
  File: umask_dir
  Size: 4096            Blocks: 8          IO Block: 4096   directory
Device: fd00h/64768d    Inode: 1082310     Links: 2
Access: (0775/drwxrwxr-x)  Uid: ( 1001/dmalyshok)   Gid: ( 1001/dmalyshok)
Access: 2021-12-04 12:07:46.189738522 +0000
Modify: 2021-12-04 12:07:46.189738522 +0000
Change: 2021-12-04 12:07:46.189738522 +0000
 Birth: -
dmalyshok@server:~$ 777 - 002 = 775

dmalyshok@server:~$ umask 0777
dmalyshok@server:~$ umask -S
u=,g=,o=
dmalyshok@server:~$ touch ch_umask.txt
dmalyshok@server:~$ mkdir ch_umask
dmalyshok@server:~$ stat ch_umask.txt
  File: ch_umask.txt
  Size: 0               Blocks: 0          IO Block: 4096   regular empty file
Device: fd00h/64768d    Inode: 1078280     Links: 1
Access: (0000/----------)  Uid: ( 1001/dmalyshok)   Gid: ( 1001/dmalyshok)
Access: 2021-12-04 12:17:08.702841573 +0000
Modify: 2021-12-04 12:17:08.702841573 +0000
Change: 2021-12-04 12:17:08.702841573 +0000
 Birth: -
dmalyshok@server:~$ stat ch_umask
  File: ch_umask
  Size: 4096            Blocks: 8          IO Block: 4096   directory
Device: fd00h/64768d    Inode: 1082347     Links: 2
Access: (0000/d---------)  Uid: ( 1001/dmalyshok)   Gid: ( 1001/dmalyshok)
Access: 2021-12-04 12:17:20.886874607 +0000
Modify: 2021-12-04 12:17:20.886874607 +0000
Change: 2021-12-04 12:17:20.886874607 +0000
 Birth: -
dmalyshok@server:~$ ls -lF ch_umask.txt ch_umask
---------- 1 dmalyshok dmalyshok    0 Dec  4 12:17 ch_umask.txt

ls: cannot open directory 'ch_umask': Permission denied
dmalyshok@server:~$ cd ch_umask/
-bash: cd: ch_umask/: Permission denied
dmalyshok@server:~$ echo 1 > ch_umask.txt
-bash: ch_umask.txt: Permission denied
dmalyshok@server:~$ umask 0002
```
    16) Give definitions of sticky bits and mechanism of identifier substitution. Give an example of files and directories with these attributes.
```
Special Mode Bits
The setuid, setgid, and sticky bit can be set using chmod where

1 = sticky bit
2 = setgid
4 = setuid
For example to set the setuid bit along with permissions 766:

chmod 4766 filename
To set the setgid bit along with 776:

chmod 2776 filename
To set sticky bit along with 766:

chmod 1776 fileanme
To set both setuid(2) and setgid(4) along with 766, prepend with 6. i.e. 2+4:

chmod 6766 filename

SUID is a special permission assigned to a file. These permissions allow the file being executed to be executed with the privileges of the owner. For example, if a file was owned by the root user and has the setuid bit set, no matter who executed the file it would always run with root user privileges.

When the Set Group ID bit is set, the executable is run with the authority of the group. For example, if a file was owned by the users’ group, no matter who executed that file it would always run with the authority of the user’s group.

When the sticky bit is set on a directory, only the root user, the owner of the directory, and the owner of a file can remove files within said directory.

Practics SUID:

dmalyshok@server:~$ cat setgid.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[], char *envpp[]) {
    printf("Process id\t\t=%d\n", getpid());
    printf("Parent process id\t=%d\n", getppid());
    printf("Real user id\t\t=%d\n", getuid());
    printf("Effective user id\t=%d\n", geteuid());
    printf("Real group id\t\t=%d\n", getgid());
    printf("Effective group id\t=%d\n", getegid());
    exit(0);
}
dmalyshok@server:~$ gcc -o setgid setgid.c
dmalyshok@server:~$ chmod u+s,g-s setgid
dmalyshok@server:~$ ll setgid
-rwsrwxr-x 1 dmalyshok dmalyshok 17008 Dec  4 16:33 setgid*
dmalyshok@server:~$ ./setgid
Process id              =22747
Parent process id       =1338
Real user id            =1001
Effective user id       =1001
Real group id           =1001
Effective group id      =1001
dmalyshok@server:~$ id
uid=1001(dmalyshok) gid=1001(dmalyshok) groups=1001(dmalyshok),27(sudo)
dmalyshok@server:~$

Run script another user devops:

devops@server:/home/dmalyshok$ ./setgid
Process id              =22763
Parent process id       =15030
Real user id            =1002
Effective user id       =1001
Real group id           =1002
Effective group id      =1002

Practics SGID:

Add SGID bit:

dmalyshok@server:~$ chmod u-s,g+s setgid
dmalyshok@server:~$ ll setgid
-rwxrwsr-x 1 dmalyshok dmalyshok 17008 Dec  4 16:33 setgid*
dmalyshok@server:~$ ./setgid
Process id              =22798
Parent process id       =1338
Real user id            =1001
Effective user id       =1001
Real group id           =1001
Effective group id      =1001

Run script another user devops:

devops@server:/home/dmalyshok$ ./setgid
Process id              =22817
Parent process id       =15030
Real user id            =1002
Effective user id       =1002
Real group id           =1002
Effective group id      =1001

Practics Sticky Bit:
dmalyshok@server:~$ cd my_dir/
dmalyshok@server:~/my_dir$ chmod +t .
dmalyshok@server:~/my_dir$ ll
total 8
drwxrwxrwt  2 dmalyshok dmalyshok 4096 Dec  4 15:20 ./
drwxr-xr-x 13 dmalyshok dmalyshok 4096 Dec  4 15:19 ../
dmalyshok@server:~/my_dir$ touch delete.me
dmalyshok@server:~/my_dir$ chmod a=rwx delete.me
dmalyshok@server:~/my_dir$ ll
total 8
drwxrwxrwt  2 dmalyshok dmalyshok 4096 Dec  4 15:21 ./
drwxr-xr-x 13 dmalyshok dmalyshok 4096 Dec  4 15:19 ../
-rwxrwxrwx  1 dmalyshok dmalyshok    0 Dec  4 15:21 delete.me*

Anothe user when +t set :
devops@server:/home/dmalyshok/my_dir$ rm delete.me
rm: cannot remove 'delete.me': Operation not permitted

dmalyshok@server:~/my_dir$ rm delete.me
```
    17) What file attributes should be present in the command script?
```
Define each file attributes
The detailed meaning of these attributes according to the manual page is:

a - append only: this attribute allows a file to be added to, but not to be removed. It prevents accidental or malicious changes to files that record data, such as log files.
c - compressed: it causes the kernel to compress data written to the file automatically and uncompress it when it’s read back.
d - no dump: it makes sure the file is not backed up in backups where the dump utility is used
e - extent format: it indicates that the file is using extents for mapping the blocks on disk.
i - immutable: it makes a file immutable, which goes a step beyond simply disabling write access to the file. The file can’t be deleted, links to it can’t be created, and the file can’t be renamed.
j - data journaling: it ensures that on an Ext3 file system the file is first written to the journal and only after that to the data blocks on the hard disk.
s - secure deletion: it makes sure that recovery of a file is not possible after it has been deleted.
t - no tail-merging: Tail-merging is a process in which small data pieces at a file’s end that don’t fill a complete block are merged with similar pieces of data from other files.
u - undeletable: When a file is deleted, its contents are saved which allows a utility to be developed that works with that information to salvage deleted files.
A - no atime updates: Linux won’t update the access time stamp when you access a file.
D - synchronous directory updates: it makes sure that changes to files are written to disk immediately, and not to cache first.
S - synchronous updates: the changes on a file are written synchronously on the disk.
T - and top of directory hierarchy: A directory will be deemed to be the top of directory hierarchies for the purposes of the Orlov block allocator.

Command:
lsattr
chattr

dmalyshok@server:~$ lsattr
--------------e----- ./test.txt

dmalyshok@server:~$ lsattr  test.txt
------d-------e----- test.txt
dmalyshok@server:~$ chattr +sd test.txt
dmalyshok@server:~$ lsattr  test.txt
s-----d-------e----- test.txt

a - append only
c - compressed
d - no dump
e - extent format
i - immutable
j - data journaling
s - secure deletion
t - no tail-merging
u - undeletable
A - no atime updates
D - synchronous directory updates
S - synchronous updates
T - top of directory hierarchy
```
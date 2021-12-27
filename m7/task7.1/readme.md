## Task 7.1
# A. Create a script that uses the following keys:
```
#!/bin/bash
fun_ping()
{
  	ping -c 1 $1 > /dev/null
  	[ $? -eq 0 ] && echo Find live host IP: $i is up and hostname is $(host $i | awk '{print $5}')
}

fun_scan_port()
{
for PORT in {20..443}
do
	timeout 1 bash -c "</dev/tcp/$(($2))/$PORT &>/dev/null" 2>/dev/null
	[ $? -eq 0 ] && echo "port $PORT is open !"
done
}

if [ "$1" = --all ];
then
echo "You choose parameter to scan all IP, $1"
for i in 10.20.1.{1..254}
do
fun_ping $i & disown
done


elif [[ "$1" = --target && -z "$2" ]];
then
echo -n "Enter IP adress for scan:"
read IP
echo "You choose ip adress for scan $IP"
fun_scan_port

elif [[ "$1" = --target && -n "$2" ]];
then
echo "You choose parameter to scan target ports, $1 , $2"
fun_scan_port

elif [ -z "$1" ];
then
echo "Choose parameter --all or --target"
echo "--all key displays the IP addresses and symbolic names of all hosts in the current subnet"
echo "--target key displays a list of open system TCP ports"

else
echo "Bad parametrs or check/choose parametrs --all or --target"
fi
```
```
malyshok@vm1malyshok:~$ ./my_script
Choose parametrs --all or --target
malyshok@vm1malyshok:~$ ./my_script --test
Bad parametrs or check or Choose parametrs --all or --target
malyshok@vm1malyshok:~$ ./my_script --target
Enter IP adress for scan:10.20.1.1
You choose ip adress 10.20.1.1
port 22 is open !
port 53 is open !
port 179 is open !
malyshok@vm1malyshok:~$ ./my_script --all
You choose parametr to scan all IP, --all
Find live host IP: 10.20.1.6 is up and hostname is 3(NXDOMAIN)
Find live host IP: 10.20.1.1 is up and hostname is ns1.malyshok.local.
malyshok@vm1malyshok:~$ 
```
# B. Using Apache log example create a script to answer the following questions:

```
#!/bin/bash
[ -z "$1" ] && echo "We can not start the script...Choose you log file
Example: /parser_apachelog apache_logs.txt" && exit 1

echo -n "1. From which ip were the most requests?
2. What is the most requested page?
3. How many requests were there from each ip?
4. What non-existent pages were clients referred to?
5. What time did site get the most requests?
6. What search bots have accessed the site? (UA + IP)" 
read answer
case $answer in
1) echo "You chose  1 answer"
awk '{print $1}' $1  | sort -nr | uniq -c | sort -nr | head -1
;;
2) echo "You chose  2 answer"
awk '{print $7}' $1 | sort | uniq -c | sort -nr | head -1
;;
3) echo "You chose  3 answer"
echo All requests $(awk '{print $1}' $1 | sort | uniq -c | sort -nr | wc -l)
awk '{print $1}' $1 | sort | uniq -c | sort -nr 
;;
4) echo "You chose  4 answer"
echo All requests $(grep " 404 " $1 | awk '{print $7,$11}' | sort | uniq -c | sort -nr | wc -l)
grep " 404 " $1 | awk '{print $7,$11}' | sort | uniq -c | sort -nr
;;
5) echo "You chose 5 answer"
#hours
awk -F: '{print $2":00"}' $1  | sort -n | uniq -c | sort -nr | head -1
# minute
#awk -F: '{print $2":"$3}' $1 | sort -n | uniq -c | sort -nr | head -1
;;
6) echo "You chose 6 answer"
grep bot $1 | awk -F'"' '{print $6,$1}' | cut --complement -d"-" -f2-3 | sort | uniq -c | sort -nr
#grep bot $1 | awk -F' - |\"' '{print $7, $1}' | sort | uniq -c | sort -nr
#grep bot $1 | awk '{ print $1 }' | sort | uniq -c | sort -rn | head -n 25 | \awk '{ printf("%5d\t%-15s\t", $1, $2); system("geoiplookup " $2 " | cut -d \\: -f2 ") }'
;;
*) echo "Bad chose"
esac
```

```
malyshok@vm1malyshok:~$ ./parser_apachelog
We can not start the script...Choose you log file
Example: /parser_apachelog apache_logs.txt
```
```
malyshok@vm1malyshok:~$ ./parser_apachelog example_log.log 
1. From which ip were the most requests?
2. What is the most requested page?
3. How many requests were there from each ip?
4. What non-existent pages were clients referred to?
5. What time did site get the most requests?
6. What search bots have accessed the site? (UA + IP)
```
```
You chose  1 answer
     29 94.78.95.154
You chose  2 answer
    190 /wp-content/uploads/2014/11/favicon.ico
You chose  3 answer
All requests 394
     29 94.78.95.154
     21 95.31.14.165
     19 176.108.5.105
     16 31.7.230.210
     14 144.76.76.115
     12 217.69.133.239
You chose  4 answer
All requests 35
      5 /wp-content/themes/cassia/css/fonts/flexslider-icon.eot? "http://example.com/ukhod-za-soboj/pokhudenie/dieti/dieta-maggi-tvorozhnyjj-variant.html"
      2 /wp-content/themes/cassia/css/fonts/flexslider-icon.eot? "http://example.com/ukhod-za-soboj/bolezni-kozhi/sukhaya-mozol-na-palce-nogi.html"
      2 /.svn/wc.db "-"
      2 /.svn/format "-"
      2 /.hg/hgrc "-"
You chose 5 answer
    253 11:00
You chose 6 answer
     14 Mozilla/5.0 (compatible; MJ12bot/v1.4.7; http://mj12bot.com/) 144.76.76.115 
     12 Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/help/robots) 217.69.133.239 
     11 Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots) 5.255.251.28 
     11 Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/help/robots) 217.69.133.234 
```
```
malyshok@vm1malyshok:~$ ./parser_apachelog apache_logs.txt 
1. From which ip were the most requests?
2. What is the most requested page?
3. How many requests were there from each ip?
4. What non-existent pages were clients referred to?
5. What time did site get the most requests?
6. What search bots have accessed the site? (UA + IP)1
```
```
You chose  1 answer
     62 157.55.39.250
You chose  2 answer
      8 /sitemap1.xml.gz
You chose  3 answer
All requests 24
     62 157.55.39.250
     61 46.29.2.62
     34 207.46.13.48
     10 178.76.227.154
      7 176.59.119.104
You chose  4 answer
All requests 0
You chose 5 answer
    129 02:00
You chose 6 answer
     62 Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) 157.55.39.250 
     33 Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) 207.46.13.48 
      3 Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots) 37.140.141.30 
      3 Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) 157.55.39.174 
```
# C. Create a data backup script that takes the following data as parameters:

```
#!/bin/bash
# C. Create a data backup script that takes the following data as parameters:
# 1. Path to the syncing directory.
# 2. The path to the directory where the copies of the files will be stored.
# In case of adding new or deleting old files, the script must add a corresponding entry to the log file indicating the time,
# type of operation and file name. 
# [The command to run the script must be added to crontab with a run frequency of one minute]
#
# mkdir -p {A,b}/1/2/{3,4}
#

if [ -z "$1" ] || [ -z "$2" ]; then
	echo "You have failed chose two parameter."
	echo "USAGE: ./sync_dir_script ABS_PATH_DIRECTORY-TO-BACKUP/. ABS_BACKUP-DIRECTORY"
      echo "EXAMPLE: ./sync_dir_script /home/malyshok/src/. /home/malyshok/dst"
	echo "Reminder: 1 parameter: path to the syncing directory. 2 parameter: path to the directory where the copies of the files will be stored"
	exit 255;
fi

# Start log block
find $1 -type f | sed 's/\.\///g' > ch_new_files
find $1 -type d | sed 's/\.\///g'> ch_new_dir

CH_FILE=$(diff -u ch_old_files ch_new_files | grep -e +/ -e -/ | sed 's/-/Delete file: /g; s/+/Add new file: /g;') 
CH_DIR=$(diff -u ch_old_dir ch_new_dir | grep -e +/ -e -/ | sed 's/-/Delete dir: /g; s/+/Add new dir: /g;')

echo $TIMESTAMP

if [ -z "$CH_FILE" ]
then
      echo "CH_FILE is NULL"
else
      echo "$CH_FILE" | while IFS= read -r line; do printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$line"; done >> logfile
fi

if [ -z "$CH_DIR" ]
then
      echo "CH_DIR is NULL"
else 
      echo "$CH_DIR" | while IFS= read -r line; do printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$line"; done  >> logfile
fi

find $1 -type f | sed 's/\.\///g' > ch_old_files
find $1 -type d | sed 's/\.\///g' > ch_old_dir
# End log block

#echo "Chek new file or directory"
#RESULT=$(diff -rq $1 $2 | awk '{print$3,$4}' | sed 's/: /\//')
#if [ -z $RESULT ]; then
#  echo New file not detected
#else
#  echo Detect new file $(diff -rq $1 $2 | awk '{print$3,$4}' | sed 's/: /\//') >> logfile
#fi

cp -pur $1 $2
echo Copy file succesfully!
#echo $(diff -rq $1 $2 | awk '/Only in \/home\/malyshok\/dst/{print substr($3, 1, length($3)-1) "/" $4}')
rm -rf $(diff -rq $1 $2 | awk '{print$3,$4}' | sed 's/: /\//')

```

```
malyshok@vm1malyshok:~$ crontab -e
# m h  dom mon dow   command
*/1 * * * *  /home/malyshok/sync_dir_script /home/malyshok/src/. /home/malyshok/dst
```

```
create two directories
mkdir /home/malyshok/src/ /home/malyshok/dst/
generate many folders:
cd src/ ; mkdir -p {A,b}/1/2/{3,4}
malyshok@vm1malyshok:~$ tree src/
src/
├── A
│   └── 1
│       └── 2
│           ├── 3
│           └── 4
└── b
    └── 1
        └── 2
            ├── 3
            └── 4

after 1 minutes:
malyshok@vm1malyshok:~$ cat logfile 

[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/b
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/b/1
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/b/1/2
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/b/1/2/3
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/b/1/2/4
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/A
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/A/1
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/A/1/2
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/A/1/2/3
[2021-12-27 14:23:01] Add new dir: /home/malyshok/src/A/1/2/4

create 2 files and delete 2 directories
malyshok@vm1malyshok:~$ rm -rf /home/malyshok/src/A/1/2
malyshok@vm1malyshok:~$ rm -rf /home/malyshok/src/b/1/2/3
malyshok@vm1malyshok:~$ touch /home/malyshok/src/A/myfirstfile
malyshok@vm1malyshok:~$ touch /home/malyshok/src/A/1/secondfile

malyshok@vm1malyshok:~$ cat logfile 
[2021-12-27 14:26:01] Delete dir: /home/malyshok/src/A/1/2
[2021-12-27 14:26:01] Delete dir: /home/malyshok/src/A/1/2/3
[2021-12-27 14:26:01] Delete dir: /home/malyshok/src/A/1/2/4
[2021-12-27 14:27:01] Add new file: /home/malyshok/src/A/myfirstfile
[2021-12-27 14:27:01] Delete dir: /home/malyshok/src/b/1/2/3
[2021-12-27 14:28:01] Add new file: /home/malyshok/src/A/1/secondfile

check syn dir:

malyshok@vm1malyshok:~$ tree src/ dst/
src/
├── A
│   ├── 1
│   │   └── secondfile
│   └── myfirstfile
└── b
    └── 1
        └── 2
            └── 4
dst/
├── A
│   ├── 1
│   │   └── secondfile
│   └── myfirstfile
└── b
    └── 1
        └── 2
            └── 4

delete file myfirstfile from src/
malyshok@vm1malyshok:~$ rm src/A/1/secondfile 
after 1 minutes:
malyshok@vm1malyshok:~$ cat logfile | tail -n 1
[2021-12-27 14:31:01] Delete file: /home/malyshok/src/A/1/secondfile

malyshok@vm1malyshok:~$ tree src/ dst/
src/
├── A
│   ├── 1
│   └── myfirstfile
└── b
    └── 1
        └── 2
            └── 4
dst/
├── A
│   ├── 1
│   └── myfirstfile
└── b
    └── 1
        └── 2
            └── 4

12 directories, 2 files

```
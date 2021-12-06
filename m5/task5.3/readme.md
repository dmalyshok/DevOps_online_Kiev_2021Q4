## Part1

  1. How many states could has a process in Linux?
```
In Linux, a process is an instance of executing a program or command. While these processes exist, they’ll be in one of the five possible states:

Running or Runnable (R)
Uninterruptible Sleep (D)
Interruptable Sleep (S)
Stopped (T)
Zombie (Z)
```
  2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process.
``
In a Linux system, “pstree” helps visualize processes hierarchy which is a less complex way to display running processes.
The “pstree” command is one of the Linux commands that merge branches through square brackets and display the process as a tree. The root of the tree could be “init” or “pid”.

pstree COMMAND:
pstree command displays the process hierarchy in a tree structured format. It also shows the parent/child relationship between the processes.
SYNTAX :
pstree
OPTIONS:
-a	Show command line arguments.
-c	Disable compaction of identical subtrees.
-G	Use VT100 line drawing characters.
-h	Highlight the current process and its ancestors.
-l	Display long lines.
-n	Sort processes with the same ancestor by PID instead of by name. (Numeric sort.)
-u	Show uid transitions.
-V	Display version information.
-s	Show Security ID (SID) for each process.
-x	Show security context for each process.

dmalyshok@server:~$ pstree -h
systemd─┬─VGAuthService
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─agetty
        ├─apache2───2*[apache2───26*[{apache2}]]
        ├─atd
        ├─cron
        ├─dbus-daemon
        ├─multipathd───6*[{multipathd}]
        ├─mysqld───36*[{mysqld}]
        ├─networkd-dispat
        ├─polkitd───2*[{polkitd}]
        ├─rsyslogd───3*[{rsyslogd}]
        ├─snapd───8*[{snapd}]
        ├─sshd───sshd───sshd───bash───pstree

dmalyshok@server:~$ ps aux | grep apache2
root         935  0.0  0.2   6688  4728 ?        Ss   20:14   0:00 /usr/sbin/apache2 -k start
www-data     941  0.0  0.2 752816  4616 ?        Sl   20:14   0:00 /usr/sbin/apache2 -k start
www-data     942  0.0  0.2 752816  4616 ?        Sl   20:14   0:00 /usr/sbin/apache2 -k start
dmalysh+    3081  0.0  0.0   6432   672 pts/0    S+   21:07   0:00 grep --color=auto apache2
dmalyshok@server:~$ pstree -H 941
systemd─┬─VGAuthService
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─agetty
        ├─apache2───2*[apache2───26*[{apache2}]]
        ├─atd
        ├─cron
        ├─dbus-daemon

dmalyshok@server:~$ pstree dmalyshok
sshd───bash───pstree

systemd───(sd-pam)
```
  3. What is a proc file system? 
```
Proc file system (procfs) is virtual file system created on fly when system boots and is dissolved at time of system shut down.
It contains useful information about the processes that are currently running, it is regarded as control and information center for kernel.
The proc file system also provides communication medium between kernel space and user space.
Below is snapshot of /proc from my PC.

dmalyshok@server:~$ ls -l /proc
total 0
dr-xr-xr-x  9 root             root                           0 Dec  4 20:14 1
dr-xr-xr-x  9 root             root                           0 Dec  4 20:14 10
dr-xr-xr-x  9 root             root                           0 Dec  4 20:14 100
dr-xr-xr-x  9 root             root                           0 Dec  4 20:14 101

You will find that for each PID of a process there is dedicated directory.

In linux, /proc includes a directory for each running process, including kernel processes, in directories named /proc/PID, these are the directories present:

directory	description
/proc/PID/cmdline	Command line arguments.
/proc/PID/cpu	Current and last cpu in which it was executed.
/proc/PID/cwd	Link to the current working directory.
/proc/PID/environ	Values of environment variables.
/proc/PID/exe	Link to the executable of this process.
/proc/PID/fd	Directory, which contains all file descriptors.
/proc/PID/maps	Memory maps to executables and library files.
/proc/PID/mem	Memory held by this process.
/proc/PID/root	Link to the root directory of this process.
/proc/PID/stat	Process status.
/proc/PID/statm	Process memory status information.
/proc/PID/status	Process status in human readable form.
Some other files in /proc file system are:

file	description
/proc/crypto	list of available cryptographic modules
/proc/diskstats	information (including device numbers) for each of the logical disk devices
/proc/filesystems	list of the file systems supported by the kernel at the time of listing
/proc/kmsg	holding messages output by the kernel
/proc/meminfo	summary of how the kernel is managing its memory.
/proc/scsi	information about any devices connected via a SCSI or RAID controller
/proc/tty	information about the current terminals
/proc/version	containing the Linux kernel version, distribution number, gcc version number (used to build the kernel) and any other pertinent information relating to the version of the kernel currently running
```
  4. Print information about the processor (its type, supported technologies, etc.).
```
dmalyshok@server:~$ cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 142
model name      : Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz
stepping        : 12
microcode       : 0xea
cpu MHz         : 2112.004
cache size      : 6144 KB
physical id     : 0
siblings        : 1
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 22
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon nopl xtopology tsc_reliable nonstop_tsc cpuid pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid rdseed adx smap clflushopt xsaveopt xsavec xsaves arat md_clear flush_l1d arch_capabilities
bugs            : spectre_v1 spectre_v2 spec_store_bypass swapgs itlb_multihit srbds
bogomips        : 4224.00
clflush size    : 64
cache_alignment : 64
address sizes   : 43 bits physical, 48 bits virtual
power management:

dmalyshok@server:~$ lscpu
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   43 bits physical, 48 bits virtual
CPU(s):                          1
On-line CPU(s) list:             0
Thread(s) per core:              1
Core(s) per socket:              1
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           142
Model name:                      Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz
Stepping:                        12
CPU MHz:                         2112.004
BogoMIPS:                        4224.00
Hypervisor vendor:               VMware
Virtualization type:             full
L1d cache:                       32 KiB
L1i cache:                       32 KiB
L2 cache:                        256 KiB
L3 cache:                        6 MiB
NUMA node0 CPU(s):               0
Vulnerability Itlb multihit:     KVM: Vulnerable
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Enhanced IBRS, IBPB conditional, RSB filling
Vulnerability Srbds:             Mitigation; TSX disabled
Vulnerability Tsx async abort:   Not affected
Flags:                           fpu vme de pse tsc msr 
```
  5. Use the ps command to get information about the process. The information should be as follows: the owner of the process, the arguments with which the process was launched for execution, the group owner of this process, etc. 
```
ps command is used to report the process status. ps is the short name for Process Status.

dmalyshok@server:~$ ps o user:12,pid,gid,%cpu,%mem,vsz,rss,tty,stat,start,time,comm,args 941
USER             PID   GID %CPU %MEM    VSZ   RSS TT       STAT  STARTED     TIME COMMAND         COMMAND
www-data         941    33  0.0  0.2 752816  4616 ?        Sl   20:14:51 00:00:00 apache2         /usr/sbin/apache2 -k start

dmalyshok@server:~$ ps -Ao user:12,pid,gid,%cpu,%mem,vsz,rss,tty,stat,start,time,comm,args
USER             PID   GID %CPU %MEM    VSZ   RSS TT       STAT  STARTED     TIME COMMAND         COMMAND
root               1     0  0.1  0.5 102028 11152 ?        Ss   20:14:21 00:00:07 systemd         /sbin/init maybe-ubiquity
root               2     0  0.0  0.0      0     0 ?        S    20:14:21 00:00:00 kthreadd        [kthreadd]
root               3     0  0.0  0.0      0     0 ?        I<   20:14:21 00:00:00 rcu_gp          [rcu_gp]
```
  6. How to define kernel processes and user processes?
```
Every process has a unique identifier which it is represented by, called as the process ID(pid). The first process that the kernel runs is called the idle process and has the pid 0. The first process that runs after booting is called the init process and has the pid 1.

User-space processes have its own virtual address space.

Kernel processes or threads do not have their own address space, they operate within kernel address space only. And they may be started before the kernel has started any user process (e.g. init).

Kernel processes (or "kernel threads") are children of PID 2 (kthreadd), so this might be more accurate:

dmalyshok@server:~$ sudo ps --ppid=2 --pid=2
    PID TTY          TIME CMD
      2 ?        00:00:00 kthreadd
      3 ?        00:00:00 rcu_gp
      4 ?        00:00:00 rcu_par_gp
      6 ?        00:00:00 kworker/0:0H-kblockd
      9 ?        00:00:00 mm_percpu_wq
     10 ?        00:00:00 ksoftirqd/0
     11 ?        00:00:03 rcu_sched
     12 ?        00:00:00 migration/0
     13 ?        00:00:00 idle_inject/0
OR

dmalyshok@server:~$ sudo pstree 2
kthreadd─┬─acpi_thermal_pm
         ├─ata_sff
         ├─blkcg_punt_bio
         ├─charger_manager
         ├─cpuhp/0

Users processes:
dmalyshok@server:~$ sudo ps -N --ppid=2 --pid=2
    PID TTY          TIME CMD
      1 ?        00:00:07 systemd
    483 ?        00:00:04 systemd-journal
    513 ?        00:00:00 systemd-udevd
    681 ?        00:00:06 multipathd
    722 ?        00:00:00 systemd-timesyn
    733 ?        00:00:00 VGAuthService
    734 ?        00:00:15 vmtoolsd
```
  7. Print the list of processes to the terminal. Briefly describe the statuses of the processes. What condition are they in, or can they be arriving in?
```
PROCESS STATE CODES
       Here are the different values that the s, stat and state output specifiers (header "STAT" or "S") will display to describe the state of a process:
       D    uninterruptible sleep (usually IO)
       R    running or runnable (on run queue)
       S    interruptible sleep (waiting for an event to complete)
       T    stopped, either by a job control signal or because it is being traced.
       W    paging (not valid since the 2.6.xx kernel)
       X    dead (should never be seen)
       Z    defunct ("zombie") process, terminated but not reaped by its parent.

       For BSD formats and when the stat keyword is used, additional characters may be displayed:
       <    high-priority (not nice to other users)
       N    low-priority (nice to other users)
       L    has pages locked into memory (for real-time and custom IO)
       s    is a session leader
       l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
       +    is in the foreground process group.

       dmalyshok@server:~$ ps o user:12,pid,gid,%cpu,%mem,vsz,rss,tty,stat,start,time,comm,args 941
USER             PID   GID %CPU %MEM    VSZ   RSS TT       STAT  STARTED     TIME COMMAND         COMMAND
www-data         941    33  0.0  0.2 752816  4616 ?        Sl   20:14:51 00:00:00 apache2         /usr/sbin/apache2 -k start

Sl - interruptible sleep (waiting for an event to complete), is a session leader
```
  8. Display only the processes of a specific user. 
```
dmalyshok@server:~$ ps -u dmalyshok
    PID TTY          TIME CMD
   1819 ?        00:00:00 systemd
   1823 ?        00:00:00 (sd-pam)
   1946 ?        00:00:02 sshd
   1947 pts/0    00:00:00 bash
   5622 pts/0    00:00:00 top
   5625 pts/0    00:00:00 ps
dmalyshok@server:~$ ps -u devops
    PID TTY          TIME CMD
   5395 ?        00:00:00 systemd
   5397 ?        00:00:00 (sd-pam)
   5521 ?        00:00:00 sshd
   5522 pts/1    00:00:00 bash
dmalyshok@server:~$ top -U dmalyshok
top - 22:38:56 up  2:24,  2 users,  load average: 0.30, 0.22, 0.11
Tasks: 205 total,   2 running, 202 sleeping,   1 stopped,   0 zombie
%Cpu(s):  0.3 us,  1.0 sy,  0.0 ni, 98.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1959.3 total,    749.7 free,    591.7 used,    617.9 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   1204.5 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   5666 dmalysh+  20   0    9272   3804   3232 R   1.0   0.2   0:00.05 top
   1946 dmalysh+  20   0   14056   6000   4520 S   0.3   0.3   0:02.16 sshd
   1819 dmalysh+  20   0   18400   9588   8020 S   0.0   0.5   0:00.20 systemd
   1823 dmalysh+  20   0  103260   3328     12 S   0.0   0.2   0:00.00 (sd-pam)
   1947 dmalysh+  20   0    8408   5476   3656 S   0.0   0.3   0:00.42 bash
   5622 dmalysh+  20   0    9272   3924   3352 T   0.0   0.2   0:00.08 top

dmalyshok@server:~$ pstree dmalyshok
sshd───bash─┬─pstree
            └─top

systemd───(sd-pam)
```
  9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?
```
pstree, ps, top see task 8.

dmalyshok@server:~$ pgrep -l apach
935 apache2
941 apache2
942 apache2

htop, atop
```
  10. What information does top command display?
```
The top command displays the list of running processes in the order of decreasing CPU usage. This means that the most resource-heavy processes appear at the top of the list:

dmalyshok@server:~$ top -U dmalyshok
top - 22:38:56 up  2:24,  2 users,  load average: 0.30, 0.22, 0.11
Tasks: 205 total,   2 running, 202 sleeping,   1 stopped,   0 zombie
%Cpu(s):  0.3 us,  1.0 sy,  0.0 ni, 98.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1959.3 total,    749.7 free,    591.7 used,    617.9 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   1204.5 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   5666 dmalysh+  20   0    9272   3804   3232 R   1.0   0.2   0:00.05 top
   1946 dmalysh+  20   0   14056   6000   4520 S   0.3   0.3   0:02.16 sshd
   1819 dmalysh+  20   0   18400   9588   8020 S   0.0   0.5   0:00.20 systemd

The output of the top command updates in real time, with the three-second default refresh rate. The top command output contains the following categories:

PID: Process identification number.
USER: The name of the user running the process.
PR: The scheduling priority for the process.
NI: The nice value of the process, with negative numbers indicating higher priority.
VIRT: The virtual memory amount used by the process.
RES: The resident (physical) memory amount used by the process.
SHR: The total shared memory used by the process.
S: The status of the process - R (running) or S (sleeping).
%CPU: The percentage of CPU usage.
%MEM: The memory usage percentage.
TIME+: Total CPU usage amount.
COMMAND: The name of the command that started the process.

The top command is running, use the following options to interact with it or change the output format:

c: Display the absolute process path.
d: Change the output refresh rate to a user-defined value (in seconds).
h: Display the help window.
k: Kill a process by providing the PID.
M: Sort the list by memory usage.
N: Sort the list by PID.
r: Change the nice value (priority) of a process by providing the PID.
z: Change the output color to highlight running processes.
q: Quit the command interface.
```
  11. Display the processes of the specific user using the top command.
```
dmalyshok@server:~$ top -U dmalyshok
top - 22:38:56 up  2:24,  2 users,  load average: 0.30, 0.22, 0.11
Tasks: 205 total,   2 running, 202 sleeping,   1 stopped,   0 zombie
%Cpu(s):  0.3 us,  1.0 sy,  0.0 ni, 98.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1959.3 total,    749.7 free,    591.7 used,    617.9 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   1204.5 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   5666 dmalysh+  20   0    9272   3804   3232 R   1.0   0.2   0:00.05 top

```
  12. What interactive commands can be used to control the top command? Give a couple of examples.
```
Once in top...

P <- Sort by CPU usage
M <- Sort by MEM usage
z <- Add cool visual colors
x <- Highlight column you are currently sorting by

The top command is running, use the following options to interact with it or change the output format

c: Display the absolute process path.
d: Change the output refresh rate to a user-defined value (in seconds).
h: Display the help window.
k: Kill a process by providing the PID.
M: Sort the list by memory usage.
N: Sort the list by PID.
r: Change the nice value (priority) of a process by providing the PID.
z: Change the output color to highlight running processes.
q: Quit the command interface.
```
  13. Sort the contents of the processes window using various parameters (for example, the amount of processor time taken up, etc.)
```
top -o +%CPU
top -o +%MEM
top -o +TIME

ps aux --sort -pmem | head -5
ps aux --sort -pid | head -5
ps aux --sort -pcpu | head -5
ps -eo comm,pcpu --sort -pcpu | head -5

in top interactive commands:
You can change the sort field in the interactive top window with the < and > keys
P <- Sort by CPU usage
M <- Sort by MEM usage
Or F and choose CPU or MEM
```
  14. Concept of priority, what commands are used to set priority?
```
Linux Kernel schedules the process and allocates CPU time accordingly for each of them. But, when one of your process requires higher priority to get more CPU time, you can use nice and renice command 
The process scheduling priority range is from -20 to 19. We call this as nice value.

A nice value of -20 represents highest priority, and a nice value of 19 represent least priority for a process.

By default when a process starts, it gets the default priority of 0.

dmalyshok@server:~$ yes > /dev/null &
dmalyshok@server:~$ ps aux --sort -pcpu | head -5
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
dmalysh+   20171 98.6  0.0   5476   592 pts/0    R    07:04   3:56 yes
mysql        998  0.3 19.0 1292296 382964 ?      Ssl  03:20   0:42 /usr/sbin/mysqld

dmalyshok@server:~$ ps -l
F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1001    7721    7720  0  80   0 -  2069 do_wai pts/0    00:00:00 bash
0 R  1001   20171    7721 98  80   0 -  1369 -      pts/0    00:08:04 yes
0 R  1001   20409    7721  0  80   0 -  2203 -      pts/0    00:00:00 ps

dmalyshok@server:~$ renice -n 15 -p 20171
20171 (process ID) old priority 0, new priority 15
dmalyshok@server:~$ ps -l
F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1001    7721    7720  0  80   0 -  2069 do_wai pts/0    00:00:00 bash
0 R  1001   20171    7721 99  95  15 -  1369 -      pts/0    00:11:16 yes
0 R  1001   20488    7721  0  80   0 -  2203 -      pts/0    00:00:00 ps

dmalyshok@server:~$ nice -10 yes > /dev/null &
[2] 20673
[1]   Terminated              yes > /dev/null
dmalyshok@server:~$ ps -l
F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1001    7721    7720  0  80   0 -  2136 do_wai pts/0    00:00:00 bash
0 R  1001   20673    7721 99  90  10 -  1369 -      pts/0    00:00:05 yes
0 R  1001   20678    7721  0  80   0 -  2203 -      pts/0    00:00:00 ps

dmalyshok@server:~$ sudo renice -n -19 -p 20673
20673 (process ID) old priority 10, new priority -19
dmalyshok@server:~$ ps -fl
F S UID          PID    PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
0 S dmalysh+    7721    7720  0  80   0 -  2136 do_wai 06:21 pts/0    00:00:00 -bash
0 R dmalysh+   20673    7721 99  61 -19 -  1369 -      07:21 pts/0    00:03:14 yes
0 R dmalysh+   20762    7721  0  80   0 -  2223 -      07:25 pts/0    00:00:00 ps -fl

dmalyshok@server:~$ renice -n 5 -u dmalyshok
1001 (user ID) old priority -19, new priority 5
dmalyshok@server:~$ ps -fl
F S UID          PID    PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
0 S dmalysh+    7721    7720  0  85   5 -  2136 do_wai 06:21 pts/0    00:00:00 -bash
0 R dmalysh+   20673    7721 99  85   5 -  1369 -      07:21 pts/0    00:04:18 yes
0 R dmalysh+   20791    7721  0  85   5 -  2223 -      07:26 pts/0    00:00:00 ps -fl
```
  15. Can I change the priority of a process using the top command? If so, how? 
```
Renice by pressing r. You will be prompted for the Process ID (PID) of the process you wish to renice. The default PID is the first process (one consuming the most resources).

top - 07:47:22 up  4:26,  2 users,  load average: 1.08, 1.01, 0.90
Tasks: 211 total,   2 running, 209 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us, 74.5 sy, 25.5 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1959.3 total,    231.8 free,    667.0 used,   1060.5 buff/cache
MiB Swap:   2048.0 total,   2046.0 free,      2.0 used.   1110.0 avail Mem
Renice PID 21335 to value 18
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
  21335 dmalysh+  36  16    5476    592    528 R  98.0   0.0   8:47.76 yes
  21614 dmalysh+  20   0    9356   4004   3232 R   1.0   0.2   0:00.17 top
      1 root      20   0  106972  13576   7592 S   0.0   0.7   0:11.09 systemd
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.03 kthreadd

Add two process "yes" and balance:

top - 07:54:05 up  4:33,  2 users,  load average: 2.01, 1.59, 1.19
Tasks: 213 total,   3 running, 210 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us, 68.9 sy, 31.1 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1959.3 total,    231.1 free,    667.0 used,   1061.2 buff/cache
MiB Swap:   2048.0 total,   2046.0 free,      2.0 used.   1109.9 avail Mem

    PID    PPID   UID USER     RUSER    TTY          TIME+  %CPU  %MEM S COMMAND
  21335   21105  1001 dmalysh+ dmalysh+ pts/1     11:31.08  48.0   0.0 R yes
  21708   21603  1001 dmalysh+ dmalysh+ pts/0      3:55.03  48.0   0.0 R yes
  21814   21603  1001 dmalysh+ dmalysh+ pts/0      0:00.05   2.0   0.2 R top
  21104   21024  1001 dmalysh+ dmalysh+ ?          0:01.25   1.0   0.3 S sshd
```
  16. Examine the kill command. How to send with the kill command process control signal? Give an example of commonly used signals.
```
Kill command in Linux (located in /bin/kill), is a built-in command which is used to terminate processes manually. kill command sends a signal to a process which terminates the process. If the user doesn’t specify any signal which is to be sent along with kill command then default TERM signal is sent that terminates the process.

The most commonly used signals are:

1 (HUP) - Reload a process.
9 (KILL) - Kill a process.
15 (TERM) - Gracefully stop a process.

Signals can be specified in three different ways:

Using number (e.g., -1 or -s 1).
Using the “SIG” prefix (e.g., -SIGHUP or -s SIGHUP).
Without the “SIG” prefix (e.g., -HUP or -s HUP).
The following commands are equivalent to one another:

kill -1 PID_NUMBER
kill -SIGHUP PID_NUMBER
kill -HUP PID_NUMBER

dmalyshok@server:~$ kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX

SIGTERM - kill -15 pid or kill pid

dmalyshok@server:~$ yes > /dev/null &
[1] 22190
dmalyshok@server:~$ ps -fl
F S UID          PID    PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
0 S dmalysh+   21603   21602  0  80   0 -  2135 do_wai 07:46 pts/0    00:00:00 -bash
0 R dmalysh+   22190   21603 99  80   0 -  1369 -      08:08 pts/0    00:00:07 yes
0 R dmalysh+   22195   21603  0  80   0 -  2223 -      08:08 pts/0    00:00:00 ps -fl
dmalyshok@server:~$ kill 22190
dmalyshok@server:~$ ps -fl
F S UID          PID    PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
0 S dmalysh+   21603   21602  0  80   0 -  2135 do_wai 07:46 pts/0    00:00:00 -bash
0 R dmalysh+   22200   21603  0  80   0 -  2223 -      08:09 pts/0    00:00:00 ps -fl
[1]+  Terminated              yes > /dev/null

SIGTERM - kill -9 pid

dmalyshok@server:~$ yes > /dev/null &
[1] 22230
dmalyshok@server:~$ ps -fl
F S UID          PID    PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
0 S dmalysh+   21603   21602  0  80   0 -  2135 do_wai 07:46 pts/0    00:00:00 -bash
0 R dmalysh+   22230   21603 99  80   0 -  1369 -      08:10 pts/0    00:00:01 yes
0 R dmalysh+   22231   21603  0  80   0 -  2223 -      08:10 pts/0    00:00:00 ps -fl
dmalyshok@server:~$ kill -9 22230
dmalyshok@server:~$ ps -fl
F S UID          PID    PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
0 S dmalysh+   21603   21602  0  80   0 -  2135 do_wai 07:46 pts/0    00:00:00 -bash
0 R dmalysh+   22238   21603  0  80   0 -  2223 -      08:10 pts/0    00:00:00 ps -fl
[1]+  Killed                  yes > /dev/null

dmalyshok@server:~$ pidof yes
22372
dmalyshok@server:~$ kill $(pidof yes)
dmalyshok@server:~$ pidof yes
[1]+  Terminated              yes > /dev/null

dmalyshok@server:~$ kill -STOP 22443
    PID    PPID   UID USER     RUSER    TTY          TIME+  %CPU  %MEM S COMMAND
  22783   21603  1001 dmalysh+ dmalysh+ pts/0      0:00.17   1.9   0.2 R top

dmalyshok@server:~$ kill -CONT 22443
   PID    PPID   UID USER     RUSER    TTY          TIME+  %CPU  %MEM S COMMAND
  22443   21603  1001 dmalysh+ dmalysh+ pts/0      7:20.08  98.1   0.0 R yes
```
  17. Commands jobs, fg, bg, nohup. What are they for? Use the sleep, yes command to demonstrate the process control mechanism with fg, bg.
```
Some times we require to control jobs/commands on how they are running ie either foreground or background on the screen. Commands which run longer duration and do not require any manual intervention are sent to background so that we can run other commands in foreground. In this post we will see how to manage process/commands to run in background or foreground by using some inbuilt commands like fg and bg

dmalyshok@server:~$ jobs
[1]-  Stopped                 vi
[2]+  Stopped                 top
[3]   Running                 yes > /dev/null &
[4]   Running                 sleep 100 &

dmalyshok@server:~$ fg 2

dmalyshok@server:~$ jobs -l
dmalyshok@server:~$ sleep 900
^Z
[1]+  Stopped                 sleep 900
dmalyshok@server:~$ jobs -l
[1]+ 24589 Stopped                 sleep 900
dmalyshok@server:~$ bg 1
[1]+ sleep 900 &
dmalyshok@server:~$ jobs -l
[1]+ 24589 Running                 sleep 900 &

The NOHUP command runs the command specified by the command parameter and any associated arg parameter, ignoring all the SIGHUP signals. Use the NOHUP command to run the program in the background after logging out. To run the NOHUP command in the background, add & (indicate the symbol of "and") to the tail of the command.

dmalyshok@server:~$ nohup ping 127.0.0.1 &
[1] 23996
Close terminal

dmalyshok@server:~$ ps aux | grep ping
dmalysh+   24177  0.0  0.0   7092   936 ?        S    09:13   0:00 ping 127.0.0.1
dmalysh+   24311  0.0  0.0   6300   672 pts/2    S+   09:14   0:00 grep --color=auto ping

Disown removes the job from the shell's job list, so all the subpoints above don't apply any more (including the process being sent a SIGHUP by the shell) SIGHUP = controlling terminal closed/dead

dmalyshok@server:~$ jobs
dmalyshok@server:~$ vi

[1]+  Stopped                 vi
dmalyshok@server:~$ disown
-bash: warning: deleting stopped job 1 with process group 25686
dmalyshok@server:~$ jobs
dmalyshok@server:~$ ps -u dmalyshok
    PID TTY          TIME CMD
   7594 ?        00:00:00 systemd
  25686 pts/0    00:00:00 vi

So to summarize:

& puts the job in the background, that is, makes it block on attempting to read input, and makes the shell not wait for its completion.

disown removes the process from the shell's job control, but it still leaves it connected to the terminal. One of the results is that the shell won't send it a SIGHUP. Obviously, it can only be applied to background jobs, because you cannot enter it when a foreground job is running.

nohup disconnects the process from the terminal, redirects its output to nohup.out and shields it from SIGHUP. One of the effects (the naming one) is that the process won't receive any sent SIGHUP. It is completely independent from job control and could in principle be used also for foreground jobs (although that's not very useful).
```
##Part2

  1. Check the implementability of the most frequently used OPENSSH commands in the MS Windows operating system. (Description of the expected result of the commands + screenshots: command – result should be presented)
```
The normal suite of of functions are included with the Windows 10 port,

ssh.exe, which is the SSH client used from the user's local system
sshd.exe, which is the SSH server that accept connections from other systems
ssh-keygen.exe generates, manages and converts authentication keys for SSH
ssh-agent.exe stores private keys used for public key authentication
ssh-add.exe adds private keys to the list allowed by the server
ssh-keyscan.exe aids in collecting the public SSH host keys from a number of- hosts
sftp.exe is the service that provides the Secure File Transfer Protocol, and- runs over SSH
scp.exe is a file copy utility that runs on SSH

ssh user@ip
ssh -i "key.pem"  host

copy a file from a local server to a remote server
scp -i "key.pem" file_transfer.txt user@host:/dir_to_copy

copy a file from a remote server to a local machine
scp -i "key.pem" ec2-user@1.2.3.4:~/source/of/remote/test.txt ./where/to/put

Run command

scp -i "key.pem" ec2-user@1.2.3.4 "run your command"


![Screen1](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m5/task5.3/Screen1.JPG?raw=true)
![Screen2](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m5/task5.3/Screen2.JPG?raw=true)
![Screen3](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m5/task5.3/Screen3.JPG?raw=true)
![Screen4](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m5/task5.3/Screen4.JPG?raw=true)
![Screen5](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m5/task5.3/Screen5.JPG?raw=true)
```
  2. Implement basic SSH settings to increase the security of the client-server connection (at least 
```
dmalyshok@server:~$ cat /etc/ssh/sshd_config

PermitEmptyPasswords no
PermitRootLogin no
Protocol 2
Port 2222
Banner /etc/banner
ClientAliveInterval 300
ClientAliveCountMax 2
AllowUsers dmalyshok devops
X11Forwarding no

dmalyshok@server:~$ sudo service sshd restart
```
  3. List the options for choosing keys for encryption in SSH. Implement 3 of them.
```
dmalyshok@server:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/dmalyshok/.ssh/id_rsa):
/home/dmalyshok/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/dmalyshok/.ssh/id_rsa
Your public key has been saved in /home/dmalyshok/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:FKGKQtjf8cDZSsAFCFJ5Un+aop6v5KNApiSGTHP4oUE dmalyshok@server
The key's randomart image is:
+---[RSA 3072]----+
|oE.=+o. o.       |
|+.= o+ + .       |
|.*.=  O +        |
|= *o.+ X         |
|+B..+ = S        |
|B. . .           |
|o o              |
|.+..             |
|..=+.            |
+----[SHA256]-----+

dmalyshok@server:~$ ssh-keygen -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/dmalyshok/.ssh/id_rsa):
/home/dmalyshok/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/dmalyshok/.ssh/id_rsa
Your public key has been saved in /home/dmalyshok/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:0SYDHcSeIiQKFqEdvfb0TngI9uSKAwwCLzMCsk0kDOA dmalyshok@server
The key's randomart image is:
+---[RSA 4096]----+
|B+=.  .+o.       |
|B=o.o  .o.       |
|BE.o . .+.o      |
|X o * + o=       |
|=+ o O =S        |
|..    * +        |
| . . . +         |
|  o .   .        |
|   .             |
+----[SHA256]-----+

dmalyshok@server:~$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/dmalyshok/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/dmalyshok/.ssh/id_ed25519
Your public key has been saved in /home/dmalyshok/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:kBI3vPVwkWQh5x/+hg7mt/zYOYQr8SmtxWPodVI/RrI dmalyshok@server
The key's randomart image is:
+--[ED25519 256]--+
|    ..o ..*+     |
|     o.oo=o      |
|    . oo +. .    |
|     ...  .o .   |
|        S   oo.. |
|          .o.+=. |
|          ++OE+o.|
|         +oB*Bo..|
|          +==o+. |
+----[SHA256]-----+
```
  4. Implement port forwarding for the SSH client from the host machine to the guest Linux virtual machine behind NAT.
```
Forward local port 22 to 2222 virtual machine

![Screen6](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m5/task5.3/Screen6.JPG?raw=true)

PS C:\Users\dmitry.malyshok\Desktop> ssh dmalyshok@127.0.0.1
This is Server for Study
dmalyshok@127.0.0.1's password:
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-90-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun 05 Dec 2021 12:02:13 PM UTC

  System load:  0.79               Processes:              219
  Usage of /:   38.2% of 18.57GB   Users logged in:        1
  Memory usage: 43%                IPv4 address for ens33: 192.168.233.128
```
  5*. Intercept (capture) traffic (tcpdump, wireshark) while authorizing the remote client on the server using ssh, telnet, rlogin. Analyze the result.
```
sudo tcpdump -w /var/tmp/capture1.pcap

![Screen7](https://github.com/dmalyshok/DevOps_online_Kiev_2021Q4/blob/main/m5/task5.3/Screen7.JPG?raw=true)

```
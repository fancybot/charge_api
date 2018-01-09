
# charge_api
the python server forsmart charge

server.py
需要安装相关的包

mkdir server
cd server
mkdir tmp

cd ..

pip install beautifulsoup4

python server.py

#后台运行
nohup python server.py&
python server.py &
关闭进程

ps aux |grep
kill -9 +[pid]

jobs
fg
bg
kill

fuser -k 8000/tcp  

[root@pvcent107 ~]# nohup ping www.ibm.com &
[1] 3059
nohup: appending output to `nohup.out'
[root@pvcent107 ~]# ps -ef |grep 3059
root      3059   984  0 21:06 pts/3    00:00:00 ping www.ibm.com
root      3067   984  0 21:06 pts/3    00:00:00 grep 3059
[root@pvcent107 ~]#

[root@pvcent107 ~]# setsid ping www.ibm.com
[root@pvcent107 ~]# ps -ef |grep www.ibm.com
root     31094     1  0 07:28 ?        00:00:00 ping www.ibm.com
root     31102 29217  0 07:29 pts/4    00:00:00 grep www.ibm.com
[root@pvcent107 ~]#
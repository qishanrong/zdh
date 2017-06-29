#!/bin/bash

full_backup(){
[ -d /home/backup ]||mkdir /home/backup -p
cd /home/backup
[ -f full.txt ]||touch full.txt
rm -rf inc_backup.txt
innobackupex --defaults-file=/etc/my.cnf --socket=/tmp/mysql.sock --user=root --password=rootroot /home/backup/
if (($?==0))
then
        echo "success"
        full=`ls -lt|head -2|tail -1|awk '{print $9}'`
        echo $full >full.txt
#	echo $full >>del_backup.txt
else
        echo "failure"
fi
echo 1 >degree.txt
}

full_backup

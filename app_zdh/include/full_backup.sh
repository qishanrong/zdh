#!/bin/bash

full_backup(){
[ -d /home/backup ]||mkdir /home/backup -p
cd /home/backup
innobackupex --defaults-file=/etc/my.cnf --socket=/tmp/mysql.sock --user=root --password=rootroot /home/backup/
if (($?==0))
then
        echo "success"
        full=`ls -lt|head -2|tail -1|awk '{print $9}'`
	binlog=`cat $full/xtrabackup_binlog_info |awk '{print $1}'`
	pos=`cat $full/xtrabackup_binlog_info |awk '{print $2}'`
	gtid=`cat $full/xtrabackup_binlog_info |awk '{print $3}'`
	echo $full $binlog $pos $gtid
	mysql -uroot -prootroot -e "insert into lepus.backup_record(ml,binlog,pos,gtid,status) values('$full','$binlog',$pos,'$gtid',1)"
else
        echo "failure"
fi
}

full_backup

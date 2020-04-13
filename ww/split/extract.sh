#!/bin/bash

# THIS PROGRAM MUST INSTALL IN SAME PATH OF MONGODB
# WHICH CAN CONNECT WITH HADOOP

###############################
# ENV SOURCE SETTING
# BASE_PATH= You need to edit this file
# DJ_PATH=${BASE_PATH}dj_migration/
# DBLIST_PATH=${BASE_PATH}dj_migration/dblist/
# TABLELIST_PATH=${BASE_PATH}dj_migration/tablelist/
# LOG_PATH=${BASE_PATH}dj_migration/log/
# TABLEDATA_PATH=${BASE_PATH}dj_migration/tabledata/
###############################
. usr/etc/dj_migration/.conf_env



###############################
# DB LIST TEXT SAVE & DELETE WARNING MSG
###############################
hive -e 'show databases;' > ${DBLIST_PATH}'databaselist.txt'
cat ${DBLIST_PATH}'databaselist.txt'
sed -i 'N;$!P;$!D;$d'  ${DBLIST_PATH}'databaselist.txt'
echo "revised txt contents"
cat  ${DBLIST_PATH}'databaselist.txt'




###############################
# READ DB & SAVE TABLE LIST
###############################
while read line
do
	echo $line
	hive -e "show tables in \`${line}\`;" > ${TABLELIST_PATH}"${line}^tables.txt"
	sed -i 'N;$!P;$!D;$d' ${TABLELIST_PATH}"${line}^tables.txt"
done < $DBLIST_PATH'databaselist.txt'



###############################
# SET GLOBAL VAL FOR WHILE
###############################
tmp_db_name=""



###############################
# READ TABLELIST FROM DATABASE
###############################
ls -1 ${TABLELIST_PATH} | while read line2
do
	echo $line2
	tmp_db_name=`echo $line2 | awk -F "^" '{print $1}'`
	echo "${tmp_db_name}"
	echo "${TABLELIST_PATH}${line2}"

	

###############################
# READ DATABASE LIST
###############################
# - if DATABASE HAS TABLE
	while read tmp_table_name;
	do
		if [ -n $tmp_table_name ];then
			#echo "데이터 베이스 이름과 테이블${tmp_db_name}  ${tmp_table_name}"


###############################
# HIVE SELECT & SAVE TO CSV 
###############################

			hive -e "set hive.cli.print.header=true; select * from ${tmp_db_name}.${tmp_table_name} limit 100;" | sed 's/[\t]/,/g' > ${TABLEDATA_PATH}"${tmp_db_name}^${tmp_table_name}^data.csv"

###############################
# SOME EDIT WITH CSV RESULT
###############################
# - EDIT COLUMN HEAD
			echo "$tmp_db_name"

			sed -i "1s/${tmp_table_name}\.//g" ${TABLEDATA_PATH}"${tmp_db_name}^${tmp_table_name}^data.csv"

# - DELETE HIVE WARNING IN LAST TWO LINE
			sed -i 'N;$!P;$!D;$d' ${TABLEDATA_PATH}"${tmp_db_name}^${tmp_table_name}^data.csv"
			scp ${TABLEDATA_PATH}"${tmp_db_name}^${tmp_table_name}^data.csv"  "${CP_USER}@${MONGODB_IP}:${MONGODB_SAVE_PATH}"
		else
			continue;
		fi

	done < <(cat "${TABLELIST_PATH}${tmp_db_name}^tables.txt" );
# END ONE DATABASE
done
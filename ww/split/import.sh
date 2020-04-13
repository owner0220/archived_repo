#!/bin/bash

export M_BASE_PATH=/usr/etc/
export MONGO_PATH=${M_BASE_PATH}"dj_mongo/MONGO_DATA/"

ls -1 ${MONGO_PATH} | while read impdata
do
	tb_name=`echo ${impdata} | awk -F "/" '{print $NF}' | awk -F "^" '{print $2}'`
	db_name=`echo ${impdata} | awk -F "/" '{print $NF}' | awk -F "^" '{print $1}'`
#		echo "데이터 베이스 : ${db_name} 테이블:  ${tb_name}"

	mongoimport --type csv -d "${db_name}" -c "${tb_name}" --headerline --drop  "${MONGO_PATH}${db_name}^${tb_name}^data.csv"
		#echo "${TABLEDATA_PATH}${db_name}^${tb_name}^data.csv"
done

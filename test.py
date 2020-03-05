hiveDbNm="a"
hiveTableNm="b"
cmd = "mongo --eval \"db.getSiblingDB(\'"+hiveDbNm+"\')."+hiveTableNm+".find().toArray();\" | sed -n  \"3,\$p\""
print(cmd)
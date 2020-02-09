from V3_0.Storer.MySQL.api import dropAllTable, createTable, testInsert

dropAllTable()
tableName = "0101-哲学"
createTable(tableName)
info = ""
testInsert(tableName, info)



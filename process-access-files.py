### EXTRACT DATA FROM ACCESS FILE ###
def process_access_files(pathTo,accessFiles,password):
    fileNameTables = {}
    for fileName in accessFiles:
        accessFilePath = pathTo+'\\'+fileName
        connection = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;PWD=%s' % (accessFilePath, password)
        connection = pyodbc.connect(connection)
        cursor = connection.cursor()
        tableNames = []
        for tableInfo in cursor.tables(tableType='TABLE'):
            tableNames.append(tableInfo.table_name)
        tableNameData = {}
        for tableName in tableNames:
            data = pd.read_sql('select * from ['+tableName+']',connection)
            tableNameData[tableName] = data
        fileNameTables[fileName] = tableNameData
        connection.close()
    return fileNameTables

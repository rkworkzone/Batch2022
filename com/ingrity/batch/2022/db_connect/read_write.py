import pyodbc
import pandas as pd
from sqlalchemy import sql, create_engine

def db_read(server, db, schema, table):
    print('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';UID=' + 'sa' + ';PWD=' + 'Ingrity@123')
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';UID=' + 'sa' + ';PWD=' + 'Ingrity@123')
    print(conn)
    engine = 'mssql+pyodbc:///?odbc_connect={}'.format(conn)
    engine = create_engine(engine)
    conn = engine.connect()
    tbl = conn.execute(sql.text("select * from dbo.business"))
    for t in tbl:
        print(t)
    print(engine)

def db_write(file, server, db, schema, table):
    df = pd.read_csv(file)
    print(len(df))
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+db+';UID='+'sa'+';PWD='+ 'Ingrity@123')
    cursor = conn.cursor()
    tbl = schema + "." + table
    print(tbl)
    insert_stmt = f"INSERT INTO {tbl} values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.fast_executemany = True
    cursor.executemany(insert_stmt, df.values.tolist() )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # db_write("D:\Support\snowflakedata\PersonDemographics\PersonDemographics2.csv"
    #          , "localhost" #127.0.0.1
    #          , "dg_target_db"
    #          ,"dbo"
    #          ,"business"
    #          )
    db_read("localhost", "dg_target_db"
             ,"dbo"
             ,"business")
    print("Done")

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


if __name__ == "__main__":
    spark = SparkSession.Builder().appName("Practice").master("local[4]").getOrCreate()

    df = spark.read.csv("D:\Support\snowflakedata\PersonDemographics\PersonDemographics2.csv", header=True)
    #df.groupby("Gender").agg("TotalChildren").show(100, False)
    df.createTempView("tbl")
    spark.sql("select sum(TotalChildren), gender from tbl group by gender ").show(100)

    df.groupby("Gender").count().show(100, False)
    df.filter(col("gender") == 'M').show()
    df_m = spark.sql("select BusinessEntityID, YearlyIncome, Education from tbl where gender = 'M'")

    df_m.write.parquet("D:\Support\snowflakedata\out3")

    #df_m.write.jdbc()



    #df.show(1000, False)
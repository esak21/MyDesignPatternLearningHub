
from appwriter.WriteProcessor import WriteProcessor
from appwriter.JsonWriter import JsonWriter
from appwriter.CsvWriter import CsvWriter
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.csv("Data/sample.csv")
df.printSchema()
df.show()
processor = WriteProcessor(CsvWriter())
processor.write(df, "Data/output/sample.csv")

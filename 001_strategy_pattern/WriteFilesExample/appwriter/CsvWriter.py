from .writerStrategy import WriterStrategy
from pyspark.sql import DataFrame

class CsvWriter(WriterStrategy):

    def write(self, df: DataFrame, file_output_path: str):
        df.write.format("csv").save(file_output_path)


from .writerStrategy import WriterStrategy
from pyspark.sql import DataFrame

class JsonWriter(WriterStrategy):


    def write(self, df: DataFrame, file_output_path: str):
        df.write.json(file_output_path)


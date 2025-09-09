from .writerStrategy import WriterStrategy

from pyspark.sql import DataFrame

class WriteProcessor():
    def __init__(self, strategy: WriterStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: WriterStrategy):
        self.strategy = strategy

    def write(self, df: DataFrame , file_path_name: str):
        self.strategy.write(df, file_path_name)
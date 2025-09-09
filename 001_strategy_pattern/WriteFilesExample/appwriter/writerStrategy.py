from abc import ABC, abstractmethod
from pyspark.sql import DataFrame

class WriterStrategy(ABC):
    """ we are defining the abstract methods for writing a file """
    @abstractmethod
    def write(self, df: DataFrame, file_output_path: str):
        pass


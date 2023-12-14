from abc import ABC, abstractmethod
#import sqlparse


class BaseDb(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def connect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def run_query(self, connection, sqlQuery)-> None:
        #toexecute = sqlparse.format(sqlQuery, strip_comments=True).strip()
        raise NotImplementedError
    
    @abstractmethod
    def run_query_to_df(self, connection, sqlQuery):
        raise NotImplementedError
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float 

class BaseTableClass:
    def __init__(self, table_name = "", columns = []):
        self.engine = create_engine("sqlite:///db/ideal_functions.db")
        self.meta_data = MetaData()
        self.connection = self.engine.connect()
        self.__tablename__ = table_name
        self.columns = columns
        self.__table__ = None

    def migrate_up(self):
        if self.__tablename__ == "":
            raise RuntimeError("Table name not provided")
        elif len(self.columns) == 0:
            raise RuntimeError("Columns not provided")
        else:
            table = Table(self.__tablename__, self.meta_data)
            table.append_column(Column("id"), Integer, primary_key = True, autoincrement = True, nullable = False)
            for c in self.column_names:
                table.append_column(Column(c["name"]), c["column_type"], nullable = c["nullable"])

            self.meta_data.create_all(self.engine)
            self.__table__ = Table(self.__tablename__, self.meta_data, autoload = True, autoload_with = self.engine)

    def migrate_down(self):
        self.__table__.drop(self.engine)


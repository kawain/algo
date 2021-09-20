from abc import ABC, abstractmethod


class MySQL1():
    pass


class MySQL2():
    pass


class MySQL3():
    pass


class Oracle1():
    pass


class Oracle2():
    pass


class Oracle3():
    pass


class IFactory(ABC):
    @abstractmethod
    def create_db1(self):
        pass

    @abstractmethod
    def create_db2(self):
        pass

    @abstractmethod
    def create_db3(self):
        pass


class MySQLFactory(IFactory):
    def create_db1(self):
        return MySQL1()

    def create_db2(self):
        return MySQL2()

    def create_db3(self):
        return MySQL3()


class OracleFactory(IFactory):
    def create_db1(self):
        return Oracle1()

    def create_db2(self):
        return Oracle2()

    def create_db3(self):
        return Oracle3()


class Factory:
    @staticmethod
    def get_factory(num) -> IFactory:
        if num == 1:
            return MySQLFactory()
        elif num == 2:
            return OracleFactory()

        return None


db_type = 2

factory = Factory.get_factory(db_type)
df1 = factory.create_db1()
df2 = factory.create_db2()
df3 = factory.create_db3()

print(df1)
print(df2)
print(df3)

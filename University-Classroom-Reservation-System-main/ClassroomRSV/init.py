# coding:utf-8
import click,py_compile,os
from configparser import ConfigParser
from util.configread import config_read
from util.sqlinit import Create
@click.group()
def sub():
    pass


@click.command()
def initdb(ini="config.ini"):
    dbtype, host, port, user, passwd, dbName, charset = config_read(ini)
    if dbtype == 'mysql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}`  /*!40100 DEFAULT CHARACTER SET utf8 */ ;".format(dbName))

        cm.conn_close()
    elif dbtype == 'mssql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;".format(dbName))

        cm.conn_close()
    else:
        print('please modify config.ini file')

@click.command()
def initsql(ini="config.ini"):
    dbtype, host, port, user, passwd, dbName, charset = config_read(ini)
    if dbtype == 'mysql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}`  /*!40100 DEFAULT CHARACTER SET utf8 */ ;".format(dbName))
        with open("./db/djangoz3gw0.sql", encoding="utf8") as f:
            createsql = f.read()
        createsql = "DROP TABLE" + createsql.split('DROP TABLE', 1)[-1]
        cm.create_tables(createsql.split(';')[:-1])
        cm.conn_close()
    elif dbtype == 'mssql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;".format(dbName))
        with open("./db/mssql.sql", encoding="utf8") as f:
            createsql = f.read()
        createsql = "DROP TABLE" + createsql.split('DROP TABLE', 1)[-1]
        cm.create_tables(createsql.split(';')[:-1])
        cm.conn_close()
    else:
        print('please modify config.ini file')

sub.add_command(initdb,"initdb")
sub.add_command(initsql,"initsql")
if __name__ == "__main__":
    sub()

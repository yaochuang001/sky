# 在mac系统上运行时候需要添加pymysql，pymysql.install_as_MySQLdb()，不然系统报错_mysql is not defined
import pymysql
pymysql.install_as_MySQLdb()
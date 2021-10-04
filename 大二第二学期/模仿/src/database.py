'''
这里是数据库操作的地方
'''

import uuid

from PyQt5 import QtSql, QtCore


def create():
    query = QtSql.QSqlQuery()
    query.exec_("create table if not exists flight("
                "id varchar(20) primary key,"
                "name varchar(20),"
                "start varchar(20),"
                "end varchar(20))")
    # 航班表，id是航班编号，name是航班名称，start是起始地，end是目的地。

    query.exec_("create table if not exists seat("
                "id varchar(20),"
                "grade varchar(20),"
                "count int,"
                "remain int,"
                "price float,"
                "primary key (id,grade))")
    # 座位表,id是航班编号，grade是舱位等级，count是舱位总数，remain是舱位剩余，price是价格

    query.exec_("create table if not exists client("
                "id varchar(20) primary key,"
                "name varchar(20),"
                "phone varchar(20))")
    # 客户表，id是身份证号，name是名字，phone是手机号

    query.exec_("create table if not exists record("
                "id varchar(32) primary key,"
                "clientname varchar(20),"
                "clientid varchar(20),"
                "flightid varchar(20),"
                "flightname varchar(20),"
                "start varchar(20),"
                "end varchar(20),"
                "grade varchar(20),"
                "price float"
                "ncov boolean"
                "firmtime datetime)")
    print('创建表成功')
    '''
    记录表,id是流水号，clientname是乘客名字，clientid是身份证号
    flightid是航班编号，flightname是航班名称，start是起始地
    end是目的地，grade是舱位等级，price是票价,ncov是新冠阳性
    firmtime是航班时间
    '''

def modify_price(flight_id, grade, price):
    query = QtSql.QSqlQuery()
    query.prepare('update seat set price = ? where id = ? and grade = ?')
    query.addBindValue(price)
    query.addBindValue(flight_id)
    query.addBindValue(grade)
    if not query.exec_():
        return query.lastError().text()
    else:
        return 'success'

def query_flight(flight_id, flight_name, start, end):
    condition = ""
    if flight_id:
        condition += "id = '" + flight_id + "' "
    if flight_name:
        condition += "name = '" + flight_name + "' "
    if start:
        condition += " start = '" + start + "' "
    if end:
        condition += " end = '" + end + "' "
    if condition:
        condition = 'where ' + condition
    # 实例化一个可编辑数据模型
    model = QtSql.QSqlQueryModel()
    model.setQuery('select f.id, name, start, end, grade, price, count, remain '
                   'from flight as f inner join seat as s on f.id = s.id '
                   + condition +
                   'order by f.id ')
    # 设置表格头
    model.setHeaderData(0, QtCore.Qt.Horizontal, '航班编号')
    model.setHeaderData(1, QtCore.Qt.Horizontal, '航班名称')
    model.setHeaderData(2, QtCore.Qt.Horizontal, '起始地')
    model.setHeaderData(3, QtCore.Qt.Horizontal, '目的地')
    model.setHeaderData(4, QtCore.Qt.Horizontal, '舱位等级')
    model.setHeaderData(5, QtCore.Qt.Horizontal, '价格')
    model.setHeaderData(6, QtCore.Qt.Horizontal, '舱位总数')
    model.setHeaderData(7, QtCore.Qt.Horizontal, '舱位剩余')


    return model

def query_seat(flight_id, grade):
    query = QtSql.QSqlQuery()
    query.prepare('select price, count from seat where id = ? and grade = ?')
    # 查询价格和舱位总数，id是航班编号,grade是舱位等级。
    query.addBindValue(flight_id)
    query.addBindValue(grade)
    if not query.exec_():
        return 'error', query.lastError().text(), None
    else:
        while query.next():
            price = query.value(0)
            count = query.value(1)
            return 'success', price, count
    return 'success', None, 0

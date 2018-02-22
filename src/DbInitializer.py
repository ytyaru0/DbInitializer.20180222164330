#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os.path

# 抽象クラス
class DbInitializer(metaclass=ABCMeta):
    def __init__(self):
#        self.__path_dir_root = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#        self.__setting = setting.Setting.Setting()
        self.__path_dir_this = os.path.abspath(os.path.dirname(__file__))
#        self.__path_dir_db = self.__setting.DbPath
        pass

    #@abstractmethod
    def CreateDb(self):
        dbname = self.__class__.__name__.replace(super().__thisclass__.__name__, '')
        print(dbname)
        self.__class__.dbname = dbname
        self.CreateDbFileName()
    #@abstractmethod
    def CreateTable(self):
        self.__GetCreateTableSqlFilePaths()
    #@abstractmethod
    def InsertInitData(self): pass

    def CreateDbFileName(self):
        return 'GitHub.' + self.__class__.dbname + '.sqlite3'
    @property
    def DbFileName(self):
        return 'GitHub.' + self.__class__.dbname + '.sqlite3'

    # パス取得（テーブル作成用SQLファイル）
    def __GetCreateTableSqlFilePaths(self):
        path = os.path.join(self.__path_dir_this, self.__class__.dbname, 'sql', 'create')
#        path = os.path.join(self.__path_dir_this, self.__class__.dbname, 'sql', 'create')
#        for path_sql in glob.glob(os.path.join(path + '*.sql')): yield path_sql
        print(path)

    """
    # パス取得（テーブル作成用SQLファイル）
    def __GetCreateTableSqlFilePaths(self, dbname):
        path = os.path.join(self.__path_dir_this, dbname, 'sql', 'create')
        for path_sql in glob.glob(os.path.join(path + '*.sql')): yield path_sql

    # パス取得（初期値挿入用TSVファイル）
    def __GetInsertTsvFilePaths(self, dbname):
        path = os.path.join(self.__path_dir_this, dbname, 'tsv')
        for path_tsv in glob.glob(os.path.join(path + '*.tsv')): yield path_tsv
        return self.__dbs[dbname]

    # SQLファイル発行
    def __ExecuteSqlFile(self, dbname, sql_path):
        with open(sql_path, 'r') as f:
            sql = f.read()
            self.__dbs[dbname].query(sql)
    """


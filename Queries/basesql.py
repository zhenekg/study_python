#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3


class SQLconnection():
    def __init__(self):
        self.status = "открыта"
        self.type = "ИТ"
        self.theme = "лень писать"
        self.description = "можно отдыхать и ничего не делать"
        self.user = "аноним"
        self.spec = "Горбатенко"
        self.screen = "none"


    def read_base(self):
        conn = sqlite3.connect('queries.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM queries;")
        result = cur.fetchall()
        conn.close()
        return result

    def write_base(self, status, type, theme, description, user, spec, screen):
        self.status = status
        self.type = type
        self.theme = theme
        self.description = description
        self.user = user
        self.spec = spec
        self.screen = screen
        conn = sqlite3.connect('queries.db')
        cur = conn.cursor()
        sql = "INSERT INTO queries(status, type, theme, description, user, spec) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (self.status, self.type, self.theme, self.description, self.user, self.spec, self.screen)
        cur.execute(sql, val)
        conn.commit()
        conn.close()

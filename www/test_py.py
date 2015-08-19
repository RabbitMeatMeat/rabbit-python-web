#!/usr/bin/env pyton
# -*- coding: utf-8 -*-

def work(a, b,c, **k):
    print k


def create_engine(user, password, database, host = '127.0.0.1', port = 3306, **kw):
    print kw
dic = {
    'a': 222,
    'b': 'b',
    'c': 'c',
}

work(**dic)

dicc = {
    'user': 'root',
    'password': 'admin',
    'database': 'awesome',
}
create_engine(**dicc)

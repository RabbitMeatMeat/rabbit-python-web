#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'RabbitMeatMeat'

from models import User, Blog, Comment

from transwarp import db

db.create_engine(user='root', password='admin', database='awesome')

u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')

u.insert()

print 'new user id:', u.id

u1 = User.find_first('where email=?', 'test@example.com')


u2 = User.find_first('where email=?', 'test@example.com')
if u2:
    print 'find user:', u2

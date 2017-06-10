# -*- coding: utf-8 -*-
import xmlrpclib

class Odoo():
    _url = None
    _db = None
    _user = None
    _password = None
    _sock_common = None
    _sock_object = None
    _uid = None
    _version = None
     
    def __init__(self, url, db, user, password):
        self._url = url
        self._db = db
        self._user = user
        self._password = password
        self._sock_common = xmlrpclib.ServerProxy ( url + '/xmlrpc/2/common')
        self._uid = self._sock_common.login(db, user, password)
        if not self._uid:
            raise Exception('Invalid username or password') 
        self._version = self._sock_common.version()
        self._sock_object = xmlrpclib.ServerProxy( url +  '/xmlrpc/2/object')

    def execute(self, *args):
        return self._sock_object.execute(self._db, self._uid, self._password, *args)



    

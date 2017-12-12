# config.py
import os
# Enable Flask's debugging features. Should be False in production
DEBUG = True

#Database connection
db = 	{
		'user': 'root',
		'pwd': '',
		'host': 'localhost',
		'baseteste': 'base_teste',
		'baseprod': 'base'
		}

#WTForms
WTF_CSRF_ENABLED = True
SECRET_KEY = 'admin'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/db'
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
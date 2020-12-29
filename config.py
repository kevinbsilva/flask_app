import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    MYSQL_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://{host}:{port}/{db_name}'.format(host='localhost', port='3306', db_name='flask')
    MYSQL_TRACK_MODIFICATIONS = False
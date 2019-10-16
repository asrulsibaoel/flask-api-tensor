import os
import connexion

# create an application instance

my_app = connexion.App(__name__, specification_dir='./swagger')
MYSQL_HOST = str(os.getenv('MYSQL_HOST','localhost'))
MYSQL_PORT = str(os.getenv('MYSQL_PORT','3306'))
MYSQL_DB_NAME = str(os.getenv('MYSQL_DB_NAME','flask_tensor'))
MYSQL_USERNAME = str(os.getenv('MYSQL_USERNAME','root'))
MYSQL_PASSWORD = str(os.getenv('MYSQL_PASSWORD',''))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+MYSQL_USERNAME+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST+':'+MYSQL_PORT+'/'+MYSQL_DB_NAME

my_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
my_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

my_app.add_api('swagger.yml')

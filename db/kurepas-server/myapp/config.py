class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Password12!@localhost/kurepas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

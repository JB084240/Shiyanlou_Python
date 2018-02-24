class BaseConfig(object):
    """Config Base Class"""
    SECRET_KEY = 'make sure to set a very sectet key'
    
class DevelopmentConfig(BaseConfig):
    """Config Development Env"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu2?charset=utf8'

class ProductionConfig(BaseConfig):
    """Config Production Env"""
    pass

class TestingConfig(BaseConfig):
    """Test"""
    pass

configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
}


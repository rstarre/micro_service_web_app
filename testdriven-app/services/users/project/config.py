# services/users/project/config.py


class BaseConfig:
    """Basic configuration"""
    TESTING = False


class DevelopmentConfig:
    """Development configuration"""
    pass


class TestingConfig:
    """Testing configuration"""
    TESTING = True


class ProductionConfig:
    """Production configuration"""
    pass

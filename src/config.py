import os

POSTGRES_URL = os.environ.get('POSTGRES_URL', 'localhost:5432')
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')


class Config(object):
    DEBUG = False
    TESTING = False
    uri_template = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
    SQLALCHEMY_DATABASE_URI = uri_template.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PASSWORD,
        url=POSTGRES_URL,
        db=POSTGRES_DB
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_PAGINATION_PER_PAGE = 10


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    pass


def get_config(env=None):
    if env == 'prod':
        return ProductionConfig()

    return DevelopmentConfig()


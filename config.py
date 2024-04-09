USERNAME="root"
PASSWORD="root"
SERVER='localhost'
DB = 'conta_flask'

SQL_ALCHEMY_DATABASE_URI = f"mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}"

SQLALCHEMY_TRACKING_MODIFICATIONS = True

SECRET_KEY="minha_chave_secreta"
# config.py
class Config:
    SECRET_KEY = 'asjdnahhbdskansdkuahsda1234'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:abhi-1708@database-1.c1isuua0qsuk.us-east-1.rds.amazonaws.com/abhinav'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable SQLAlchemy modification tracking (optional)
    # Other configuration options (if needed) go here

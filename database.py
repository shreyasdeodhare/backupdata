from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = "postgresql://postgres:aadhya17@localhost/students"

engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=True)
db = engine.connect()

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

session = Session()


def close_session():
    try:
        session.close()
        db.close()
        engine.dispose()
    except Exception as e:
        session.rollback()
        print("error in close database", str(e))

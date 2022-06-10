from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from InnexiaBot import DB_URI, LOGGER as log

if DB_URI and DB_URI.startswith("postgres://"):
    DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)

def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    log.info("[INFO] Process Started To Connect Database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
try:
    SESSION = start()
except Exception as e:
    log.exception(f'[ALERT] Database Failed to connect due to {e}')
    exit()
   
log.info("[CONGRATS] Database Connection successful, session started.")

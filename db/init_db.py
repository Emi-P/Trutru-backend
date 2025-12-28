from db.session import engine
from db.base import Base

# IMPORTANTE: importar modelos
import models.match
import models.user

def init_db():
    Base.metadata.create_all(bind=engine)

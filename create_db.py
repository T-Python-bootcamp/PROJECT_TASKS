from database import engine, Base
from models import Tasks
Base.metadata.create_all(engine)
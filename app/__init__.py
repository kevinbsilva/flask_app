from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# __name__ - Predefined variable - Name of the module in use
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# routes - Different URLs that the application implements - Handlers are written as Python functions, called view functions
from app import routes
from app import models


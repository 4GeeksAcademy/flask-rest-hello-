import os
from flask_admin import Admin
from models import db, User, Personajes,Planetas, Favoritos
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
   
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Personajes, db.session))
    admin.add_view(ModelView(Planetas, db.session))
    admin.add_view(ModelView(Favoritos, db.session))


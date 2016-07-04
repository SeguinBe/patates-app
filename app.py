from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from flask.ext.restful import Resource, fields, marshal, Api
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
api = Api(app)


class Price(db.Model):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String())
    size = db.Column(db.String())
    price = db.Column(db.Integer)
    available = db.Column(db.Boolean)

    def __init__(self, type, size, price):
        self.type = type
        self.size = size
        self.price = price
        self.available = True

    def __repr__(self):
        return '<id {}, {}: {} -> {} euros. Availability : {}>'.format(self.id,
                                                                       self.type,
                                                                       self.size,
                                                                       self.price,
                                                                       self.available)

db.create_all()


@app.route('/')
def home():
    return app.send_static_file("base.html")


def get_prices():
    result = Price("Agatha", "15kg", 35)
    db.session.add(result)
    db.session.commit()


class PricesRessource(Resource):
    entry_fields = {
        'type':     fields.String,
        'size':     fields.String,
        'price':     fields.Float,
        'available': fields.Boolean
    }

    def get(self):
        return [marshal(r, self.entry_fields) for r in Price.query.all()]


api.add_resource(PricesRessource, '/api/prices')
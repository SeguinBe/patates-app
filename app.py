from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from flask.ext.restful import Resource, fields, marshal, Api, reqparse, abort
import requests
import os
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['MAILGUN_DOMAIN'] = os.environ['MAILGUN_DOMAIN']
#app.config['MAILGUN_API_KEY'] = os.environ['MAILGUN_API_KEY']
#db = SQLAlchemy(app)
api = Api(app)


# class Price(db.Model):
#     __tablename__ = 'prices'
#
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String())
#     size = db.Column(db.String())
#     price = db.Column(db.Integer)
#     available = db.Column(db.Boolean)
#
#     def __init__(self, type, size, price):
#         self.type = type
#         self.size = size
#         self.price = price
#         self.available = True
#
#     def __repr__(self):
#         return '<id {}, {}: {} -> {} euros. Availability : {}>'.format(self.id,
#                                                                        self.type,
#                                                                        self.size,
#                                                                        self.price,
#                                                                        self.available)

#db.create_all()


@app.route('/')
def home():
    return app.send_static_file("base.html")


# def get_prices():
#     result = Price("Agatha", "15kg", 35)
#     db.session.add(result)
#     db.session.commit()
#
#
# class PricesRessource(Resource):
#     entry_fields = {
#         'type':     fields.String,
#         'size':     fields.String,
#         'price':     fields.Float,
#         'available': fields.Boolean
#     }
#
#     def get(self):
#         return [marshal(r, self.entry_fields) for r in Price.query.all()]
#
#
# class BuyRessource(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('email', type=str, help='Email of the buyer', required=True)
#     parser.add_argument('firstName', type=str, help='First name of the buyer')
#     parser.add_argument('lastName', type=str, help='Last name of the buyer')
#     parser.add_argument('phone', type=str, help='Phone of the buyer')
#     parser.add_argument('comments', type=str, help='')
#
#     def post(self):
#         args = self.parser.parse_args()
#         r = requests.post('https://api.mailgun.net/v3/{}/messages'.format(app.config['MAILGUN_DOMAIN']),
#                     auth=('api', app.config['MAILGUN_API_KEY']),
#                     data={'from': 'Patates Seguin <noreply@{}>'.format(app.config['MAILGUN_DOMAIN']),
#                     'to': args['email'],
#                     'subject': 'Bonjour {} {}'.format(args['firstName'], args['lastName']),
#                     'text': 'Ceci est un email de test'})
#         if r.status_code != 200:
#             abort(500, msg="Impossible to send email")
#
#
# api.add_resource(PricesRessource, '/api/prices')
# api.add_resource(BuyRessource, '/api/buy')

from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
import random
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='IMC App API',
    description='A simple IMC APP API',
)

ns = api.namespace('userinfo', description='userInfo operations')

userInfo = api.model('userInfo', {    
    'id': fields.Integer(readonly=True,required=True, description='The user unique identifier'),
    'name': fields.String(required=True, description='The user name'),
    'weight': fields.Integer(required=True, description='The user weight'),
    'height': fields.Integer(required=True, description='The user height'),

})



class userDAO(object):
    def __init__(self):
        self.counter = 0
        self.usersinfo = [
    {
        'id': random.randint(0,100) ,
        'name': 'Ricardo',
        'weight': 60,
        'height': 160,
        
        
    }
]

    def get(self, id):
        for user in self.usersinfo:
            if user['id'] == id:
                return user
        api.abort(404, "User {} doesn't exist".format(id))

    def create(self, data):
        user = data
      
        new_user = {
            'id': random.randint(0,100),
            'name': user['name'],
            'height': user['height'],
            'weight': user['weight'],
         
                
                
            }
        self.usersinfo.append(new_user)
        return user




DAO = userDAO()




@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all users'''
    @ns.doc('list user info')
    @ns.marshal_list_with(userInfo)
    def get(self):
        '''List user information'''
        return DAO.usersinfo

    @ns.doc('create_todo')
    @ns.expect(userInfo)
    @ns.marshal_with(userInfo, code=201)
    def post(self):
        '''Create user information'''
        return DAO.create(api.payload), 201






if __name__ == '__main__':
    app.run(debug=True)

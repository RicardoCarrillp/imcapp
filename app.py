from flask import Flask, jsonify, request
import random

app = Flask('__name__')

usersinfo = [
    {
        'id': random.randint(0,100) ,
        'name': 'Ricardo',
        'weight': 60,
        'height': 160,
        'imc': 23.5
        
        
    }
]


@app.route('/userinfo', methods=['POST'])
def create_userinfo():
    request_data = request.get_json()
    w=request_data['weight'] 
    h= request_data['height']
    h2=h*h
    imc=w/h2
    print(imc)

    new_user = {

        'id': random.randint(0,100),
        'name': request_data['name'],
        'height': request_data['height'],
        'weight': request_data['weight'],
        'imc':imc
        
        
    }
 
    usersinfo.append(new_user)
    return jsonify(new_user)


@app.route('/userinfo/<int:id>', methods=['GET'])
def get_userinfo(id):
    for user in usersinfo:
        if user['id'] == id:  
            
            return jsonify(user)
    return jsonify({'message': 'user not found'})


@app.route('/userinfo')
def get_usersinfo():
    return jsonify({'Users': usersinfo})



if __name__ == '__main__':
    app.run()
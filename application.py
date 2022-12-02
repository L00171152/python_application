from flask import Flask  
from flask import jsonify
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/fact', methods=['GET']) #decorator drfines the   
def home():  
    # return jsonify("heymmm")
    return {
    "fact": "Baking chocolate is the most dangerous chocolate to your cat.",
    "length": 61
}
  
if __name__ =='__main__':
    app.run(host='0.0.0.0')
    app.run(debug = True)


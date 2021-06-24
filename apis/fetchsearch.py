from flask import Flask
from flask import jsonify
from flask import request
import sys
sys.path.append('/var/www/html/ubm/informa/contentgeneration/gpt_2/src')

from resourceaccessor import interact_model
app = Flask(__name__)

@app.route('/generate/content',methods=['POST'])
def generateGPT2Content():
    initText = request.form['initText']
    output = interact_model(initText,'124M',None,1,1,None,1,0,1,'gpt_2/models')
    return jsonify({'initText':initText, "output": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8555, debug=True)
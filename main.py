from flask import Flask
from flask import render_template
openai.api_key=key

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generateimages/<prompt>')
def generate(prompt):
    print("prompt:",prompt)
    response=openai.Image.create(prompt=prompt,n=3,size="104*104")
    image_url=response['data'][0]['url']
    #return render_template('index.html')
    print(response)
    return jsonify(response)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

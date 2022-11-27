from re import DEBUG, sub
from flask import Flask, render_template, request,jsonify
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)
uploads_dir = os.path.join(app.instance_path, 'instance')
os.makedirs(uploads_dir, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['POST','GET'])
def detect():
    if not request.method == "POST":
        f=open('ans.txt','r')
        c=f.readlines()
        return jsonify({"Number of Tablets":str(c)})
    image = request.files['image']
    image.save(os.path.join(uploads_dir, secure_filename(image.filename)))
    print(image)
    subprocess.run("ls",shell=True)
    
    subprocess.run(['python3', 'detect.py', '--source',os.path.join(uploads_dir, secure_filename(image.filename))],shell=True)
    
    # return os.path.join(uploads_dir, secure_filename(video.filename))
    obj = secure_filename(image.filename)
    return obj


if __name__=="__main__":
    app.run()

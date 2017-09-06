from flask import Flask, request, redirect, url_for, render_template,jsonify
import os
import json
import glob
from uuid import uuid4
import model_final as ml

app = Flask(__name__)


@app.route("/")
def index():
    return "Server is on"


@app.route("/healthcare/mri/analysis", methods=["POST"])
def upload():
    """Handle the upload of a file."""
    form = request.form

    # Create a unique "session ID" for this particular batch of uploads.
    upload_key = str(uuid4())

    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True

    # Target folder for these uploads.
    target = "static/uploads/{}".format(upload_key)
    print(target);
    try:
        os.makedirs(target)
    except:
        if is_ajax:
            return ajax_response(False, "Couldn't create upload directory: {}".format(target))
        else:
            return "Couldn't create upload directory: {}".format(target)

    print ("=== Form Data ===")
    for key, value in form.items():
        print (key, "=>", value)

    for upload in request.files.getlist("file"):
        filename = upload.filename.rsplit("/")[0]
        print(filename);
        destination = "/".join([target, filename])
        print(target);
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    if is_ajax:
        loadedData = loadmodel(target)
        print(loadedData)
        return jsonify(loadedData)
        # return redirect(url_for('do_foo'))
        # return redirect(url_for("upload_complete", uuid=upload_key))

    else:
        loadedData = loadmodel(target)
        print(loadedData)
        return jsonify(loadedData)
        # return redirect(url_for('do_foo'))
        # return redirect(url_for("upload_complete", uuid=upload_key))
# 
    # if is_ajax:
    #     return ajax_response(True, upload_key)
    # else:
    #     return redirect(url_for("upload_complete", uuid=upload_key))        


@app.route('/foo')
def do_foo():
    data = request.args['jsonD']  # counterpart for url_for()
    print(data)
    return render_template("data.html", data=data)

@app.route("/files/<uuid>")
def upload_complete(uuid):
    """The location we send them to at the end of the upload."""

    # Get their files.
    root = "uploadr/static/uploads/{}".format(uuid)
    print(root)
    if not os.path.isdir(root):
        return "Error: UUID not found!"

    files = []
    for file in glob.glob("{}/*.*".format(root)):
        fname = file.split(os.sep)[-1]
        files.append(fname)

    loadedData = loadmodel(root)
    print(loadedData)
    # return jsonify(loadedData)    

    return render_template("files.html",
        uuid=uuid,
        files=files,
        data=loadedData
    )

def loadmodel(target):
    print(target);
    data = ml.runProgram(target) 
    return data;   

def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))


app.run(debug = False,host='0.0.0.0',port=2006)
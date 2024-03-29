from flask import Flask,request,jsonify
import util
app=Flask(__name__)
@app.route("/classify_image",methods=["GET","POST", "PUT", "DELETE"])

def classify_image():
    print("hiiiii")
    img_data=request.form["image_data"]
    
    response=jsonify(util.classify_image(img_data))
    print(util.classify_image(img_data))
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

if __name__=="__main__":
    util.load_saved_artifacts()
    app.run()
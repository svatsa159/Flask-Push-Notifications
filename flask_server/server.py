import pickle
import logging
import json, os
from flask_redis import FlaskRedis
from flask import request, Response, render_template, jsonify, Flask
from pywebpush import webpush, WebPushException
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
redis_client = FlaskRedis(app)
DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(),"private_key.txt")
DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(),"public_key.txt")
# redis_client.flushdb()
VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")
dummydb = {"subscription" : None }
VAPID_CLAIMS = {
"sub": "mailto:develop@raturi.in"
}




def saveToDatabase(uid,subscription):
    # dummydb["subscription"]=subscription
    # x = (redis_client.dbsize())
    # lis = redis_client.get("subscriptions")
    # print(lis)
    # lis.append(subscription)
    sub_p=pickle.dumps(subscription)
    redis_client.set(uid,sub_p)
    # print(type(subscription))




def send_web_push(subscription_information, message_body):
    # print(subscription_information["subscription_token"])
    return webpush(
        subscription_info=subscription_information["subscription_token"],
        data=message_body,
        vapid_private_key=VAPID_PRIVATE_KEY,
        vapid_claims=VAPID_CLAIMS
    )



@app.route("/save-subscription", methods=["POST"])
@cross_origin()
def subscription():
    """
        POST creates a subscription
        GET returns vapid public key which clients uses to send around push notification
    """
    subscription_token = request.get_json("subscription_token")
    # print(subscription_token)
    # print('....')
    uid = request.get_json("subscription_token")["user"]
    # print(uid)
    saveToDatabase(uid,subscription_token)
    return Response(status=201, mimetype="application/json")

@app.route("/push/",methods=['POST'])
@cross_origin()
def push():
    # subscription = dummydb["subscription"]
    message = (request.args["message"])
    user = request.args["user"]
    # print(user)
    if user=="admin":
        subscription=redis_client.get("admin")
        sub_p = pickle.loads(subscription)
        try:
            send_web_push(sub_p,message)
        except Exception as e:
            print(e)
            pass
    elif int(user)==9999:
        for key in redis_client.scan_iter("*"):
            if key=="admin":
                continue
            subscription=redis_client.get(key)
            sub_p = pickle.loads(subscription)
            
            try:
                send_web_push(sub_p,message)
            except Exception as e:
                print(e)
                pass
    else:
        subscription=redis_client.get(user)
        # print("user")
        sub_p = pickle.loads(subscription)
        try:
            send_web_push(sub_p,message)
        except Exception as e:
            print(e)
            pass
    # message = request.get_json("message")
    # x = (redis_client.dbsize())
    
            # print("error",e)
    # for i in range(0,x):
    #     subscription=redis_client.get("subscriptions"+str(i))
        
    #     sub_p = pickle.loads(subscription)
    #     # print(type(sub_p))
    #     try:

    #         send_web_push(sub_p,message)
    #     except Exception as e:
    #         pass
    #         # print("error",e)
    return jsonify({'success':1})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
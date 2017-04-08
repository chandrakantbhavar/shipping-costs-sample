#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "recommender.actions":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    exp = parameters.get("Experience")
    exp=''.join(exp)
    skillset=parameters.get("Skillset")
    skillset=''.join(skillset)
    practice=parameters.get("Practice")
    practice=''.join(practice)

    data=[]
    data.append({'practice':'IBM','experience':'Fresher','skillset':'Java'})
    data.append({'practice': 'CIS', 'experience': '2-5 years', 'skillset': 'python'})
    data.append({'practice': 'Convergens', 'experience': '2-5 years', 'skillset': '.net'})
    data.append({'practice': 'IBM', 'experience': '0-1 years', 'skillset': 'java'})
    data.append({'practice': 'CIS', 'experience': '7-9 years', 'skillset': 'java'})
    data.append({'practice': 'SMAC', 'experience': '5-7 years', 'skillset': 'python'})
    data.append({'practice': 'Kpoint', 'experience': '2-5 years', 'skillset': 'java'})
    data.append({'practice': 'SMAC', 'experience': '0-1 years', 'skillset': 'java'})
    str="We have no such oppurtunities right now. But we will get back to you when we have such openings"
    for x in data:
        if (x['practice']==practice):
            if (x['experience']==exp ) or ( x['experience']==exp + ' years'):
                if x['skillset']==skillset:
                    str="We have oppurtunities in " + practice + " practice with " + exp  + ' experience and skill required is ' + skillset
                else:
                    str="We have no such oppurtunities right now. But we will get back to you when we have such openings"

    #return jsonify({'result':str})

    #speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."

    print("Response:")
    print(str)

    return {
        "speech": str,
        "displayText": str,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')

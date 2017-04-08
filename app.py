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
    exp=exp.strip()
    if (exp == '2+ years' or exp == '3+ years' or exp == '4+ years' or exp == '1+ years' or exp == 'SE' or exp=='0-1 years'
        or exp=='0-2 years' or exp=='1-2 years' or exp=='2-3 years' or exp=='3-4 years'):
        exp = "SE"
    if (exp == '5+ years' or exp == '6+ years' or exp == '7+ years' or exp == 'SSE'
        or exp == '5-6 years' or exp == '6-7 years' or exp == '5-7 years' or exp == '7 years'):
        exp = 'SSE'
    if (exp == '8+ years' or exp == '9+ years' or exp == 'LSE'
        or exp == '8-9 years' or exp == '9-10 years' ):
        exp = 'LSE'
    if (exp == '11+ years' or exp == '10+ years' or exp == 'ATM'
        or exp == '10-11 years'):
        exp = 'ATM'
    if (exp == '11+ years' or exp == '12+ years' or exp == 'Manager'
        or exp == '11-12 years'):
        exp = 'Manager'

    data=[]
    data.append({'practice': 'IBM', 'experience': 'SE', 'skillset': 'Java', 'Position': '02'})
    data.append({'practice': 'CIS', 'experience': 'SSE', 'skillset': 'python', 'Position': '01'})
    data.append({'practice': 'Convergens', 'experience': 'LSE', 'skillset': '.net', 'Position': '04'})
    data.append({'practice': 'IBM', 'experience': 'ATM', 'skillset': 'java', 'Position': '04'})
    data.append({'practice': 'CIS', 'experience': 'Manager', 'skillset': 'java', 'Position': '06'})
    data.append({'practice': 'SMAC', 'experience': 'SE', 'skillset': 'python', 'Position': '02'})
    data.append({'practice': 'Kpoint', 'experience': 'LSE', 'skillset': 'java', 'Position': '03'})
    data.append({'practice': 'SMAC', 'experience': 'ATM', 'skillset': 'java', 'Position': '08'})
    str = "We have no such oppurtunities right now. But we will get back to you when we have such openings"
    for x in data:
        if (x['practice'] == practice):
            if (x['experience'] == exp):
                if x['skillset'] == skillset:
                    str = "We have oppurtunities in " + practice + " and the position offered will be of " + exp + ' and skill required is ' + skillset + ' and the No.Of Positions available are ' + \
                          x['Position']
                else:
                    str = "We have no such oppurtunities right now. But we will get back to you when we have such openings"

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

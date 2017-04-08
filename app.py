#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask, jsonify
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/getData', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    data=[]
    if req.get("result").get("action") != "recommender.actions":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")

    exp = parameters.get("Experience")
    exp=''.join(exp)

    practice = parameters.get("Practice")
    practice = ''.join(practice)
    skillset = parameters.get("Skillset")
    skillset = ''.join(skillset)
    if(exp=='2+ years' or exp=='3+ years' or exp=='4+ years' or exp=='1+ years' or exp=='SE'):
        exp="SE"
    if (exp == '5+ years' or exp == '6+ years' or exp == '7+ years' or exp == 'SSE'):
        exp='SSE'
    if (exp == '8+ years' or exp == '9+ years' or exp == 'LSE'):
        exp='LSE'
    if (exp == '11+ years' or exp == '10+ years' or exp == 'ATM'):
        exp='ATM'
    if (exp == '11+ years' or exp == '12+ years' or  exp == 'Manager'):
        exp='Manager'
    print exp
    print practice
    print skillset
    data.append({'practice':'IBM','experience':'SE','skillset':'Java','Position':'02'})
    data.append({'practice': 'CIS', 'experience': 'SSE', 'skillset': 'python','Position':'01'})
    data.append({'practice': 'Convergens', 'experience': 'LSE', 'skillset': '.net','Position':'04'})
    data.append({'practice': 'IBM', 'experience': 'ATM', 'skillset': 'java','Position':'04'})
    data.append({'practice': 'CIS', 'experience': 'Manager', 'skillset': 'java','Position':'06'})
    data.append({'practice': 'SMAC', 'experience': 'SE', 'skillset': 'python','Position':'02'})
    data.append({'practice': 'Kpoint', 'experience': 'LSE', 'skillset': 'java','Position':'03'})
    data.append({'practice': 'SMAC', 'experience': 'ATM', 'skillset': 'java','Position':'08'})
    str="We have no such oppurtunities right now. But we will get back to you when we have such openings"
    for x in data:
        if (x['practice']==practice):
            if (x['experience']==exp ):
                if x['skillset']==skillset:
                    str="We have oppurtunities in " + practice + " and the position offered will be of " + exp  + 'and skill required is ' + skillset +' No.Of Position '+x['Position']
                else:
                    str="We have no such oppurtunities right now. But we will get back to you when we have such openings"

    #return jsonify({'result':str})

return {
        "speech": str,
        "displayText": str,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }

if _name_ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')

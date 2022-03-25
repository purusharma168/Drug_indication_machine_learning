import numpy as np
import logging
from flask import Flask, request, jsonify, render_template
import pickle
import model

app = Flask(__name__)


# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    global prediction
    if request.method == 'POST':
        src_nm = (request.form["src_nm"])
        src_id = (request.form["src_id"])
        cas_cas_no = (request.form["cas_cas_no"])
        cas_pt = (request.form["cas_pt"])
        cas_source = (request.form["cas_source"])
        cas_match = (request.form["cas_match"])
        umls_pt = (request.form["umls_pt"])
        umls_cui = (request.form["umls_cui"])
        ind_raw_value = (request.form["ind_raw_value"])
        ind_raw_target = (request.form["ind_raw_target"])
        ind_raw_match = (request.form["ind_raw_match"])
        ind_umls_entry_term_match = (request.form["ind_umls_entry_term_match"])

        arr = np.array([[src_nm, src_id, cas_cas_no, cas_pt, cas_source, cas_match, umls_pt, umls_cui, ind_raw_value,
                         ind_raw_target, ind_raw_match, ind_umls_entry_term_match]])
        prediction = model.log_reg.predict(arr)

        print('Drugs name is', prediction)
        return render_template('after.html', prediction=prediction[0])

    # return render_template('index.html',

    # features = [int(x) for x in request.form.values()]
    # final_features = [np.array(features)]
    # prediction = model.clf.predict(final_features)
    #
    # output = round(prediction)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    # app.run(debug=True)  # running the app

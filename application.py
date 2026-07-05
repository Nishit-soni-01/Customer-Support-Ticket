from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import NLPData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/triage', methods=['POST'])
def triage_ticket():
    ticket_text = request.form.get('issue_description')
    
    data = NLPData(ticket_description=ticket_text)
    pred_df = data.get_data_as_data_frame()['Ticket Description']
    
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    
    return render_template('home.html', results=results[0], original_text=ticket_text)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
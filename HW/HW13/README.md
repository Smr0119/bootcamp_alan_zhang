# Model API Project

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Run Flask API: `python -c "from stage13_productization_homework_starter import *; run_flask()"`
3. Run Streamlit: `streamlit run app_streamlit.py`

## API Endpoints
- POST /predict: Send JSON with features
- GET /predict/<input1>: Single feature prediction
- GET /predict/<input1>/<input2>: Two feature prediction
- GET /plot: View model plot

## Model
Simple linear regression model trained on synthetic data.
Takes 2 features and predicts continuous output.

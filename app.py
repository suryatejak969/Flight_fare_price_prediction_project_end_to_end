from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('flight_price81.pkl')
le_totalStops = joblib.load('le_totalStops.pkl')

output = model.predict([[1, 13, 10, 20, 10,
       23, 30, 3, 20,
       1, 0, 0, 0, 0,
       0, 0, 0,
       0, 0, 0, 0, 1,
       0, 1, 0, 0, 0, 0,
       0]])

print(output[0])

@app.route('/')
def first():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
    date_dep = request.form["Dep_Time"]
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

    Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
    Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

    date_arr = request.form["Arr_Time"]
    Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
    Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)

    Total_stops = le_totalStops.transform([request.form["Stopage"]])

    airline=request.form['Airline']
    if airline == 'Air India':
        Air_India = 1
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'GoAir':
        Air_India = 0
        GoAir = 1
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'IndiGo':
        Air_India = 0
        GoAir = 0
        IndiGo = 1
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'Jet Airways':
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 1
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'Jet Airways Business':
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 1
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'Multiple carriers':
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 1
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'Multiple carriers Premium economy':
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 1
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'SpiceJet':
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 1
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'Trujet':
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 1
        Vistara = 0
        Vistara_Premium_economy = 0
    elif airline == 'Vistara':
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 1
        Vistara_Premium_economy = 0
    elif airline == 'Vistara Premium economy':
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 1
    else:
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_carriers = 0
        Multiple_carriers_Premium_economy = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0
    
    Source = request.form["Source"]
    if Source == 'Delhi':
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0
    elif Source == 'Kolkata':
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0
    elif Source == 'Mumbai':
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0
    elif Source == 'Chennai':
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1
    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    Destination = request.form["Destination"]
    if Destination == 'Cochin':
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
    elif Source == 'Delhi':
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
    elif Source == 'New Delhi':
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0
    elif Source == 'Hyderabad':
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0
    elif Source == 'Kolkata':
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1
    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
    
    print(Total_stops, Journey_day, Journey_month, Dep_hour, Dep_min,
       Arrival_hour, Arrival_min, dur_hour, dur_min,
       Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
       Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet,
       Trujet, Vistara, Vistara_Premium_economy, s_Chennai, s_Delhi,
       s_Kolkata, s_Mumbai, d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata,
       d_New_Delhi)

    prediction = model.predict([[Total_stops, Journey_day, Journey_month, Dep_hour, Dep_min,
       Arrival_hour, Arrival_min, dur_hour, dur_min,
       Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
       Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet,
       Trujet, Vistara, Vistara_Premium_economy, s_Chennai, s_Delhi,
       s_Kolkata, s_Mumbai, d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata,
       d_New_Delhi]])
    
    output=round(prediction[0],2)

    return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))

if __name__ == '__main__':
    app.run(debug = True)

#'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
    #    'Jet Airways Business', 'Multiple carriers',
    #    'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara',
    #    'Vistara Premium economy'
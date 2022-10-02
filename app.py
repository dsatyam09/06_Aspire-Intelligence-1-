from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__, template_folder='templates')
model = pickle.load(open('DecisionTreeClassifier.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Gender = (request.form['Gender'])
        if Gender== 'Female':
            Gender = 0
        elif Gender== 'Male':
            Gender = 1
        elif Gender== 'Non Binary':
            Gender = 2
        elif Gender== 'Prefer Not to answer':
            Gender = 3
        ######################################################################################
        Age =(request.form['Age']) 
        if Age == '26 to 35 years old':
            Age = 0
        elif Age== '16 to 25 years old':
            Age = 1
        elif Age== '36 to 45 years old':
            Age = 2
        elif Age== 'Over 45 years old':
            Age = 3
            ##################################################################################
        Geography=(request.form['Geography']) 
        if Geography == 'City center or metropolitan area':
            Geography = 0
        elif Geography== 'Suburban/Peri-urban':
            Geography = 1
        elif Geography== 'Rural':
            Geography = 2
        ###########################################################################################
        
        Education=(request.form['Education']) 

        if Education == 'University or college degree completed':
            Education = 0
        elif Education == 'Secondary school/ high school completed':
            Education = 1
        elif Education == 'Technical school diploma or degree completed':
            Education = 2
        elif Education == 'Some university or college':
            Education = 3
        elif Education == 'Some technical education (e.g polytechnic school)':
            Education = 4
        elif Education == 'Some secondary school / high school':
            Education = 5
        elif Education == 'Post-graduate education':
            Education = 6
        elif Education == 'Primary school completed':
            Education = 7
        elif Education== 'Prefer not to answer':
            Education = 8
        elif Education == 'Some primary education':
            Education = 9
        elif Education == 'No formal education':
            Education = 10

    ##############################################################################################
        Employment_Status=request.form['Employment_Status'] 
        if Employment_Status == 'I work part-time, either as an employee or self-employed':
            Employment_Status = 0
        elif Employment_Status == 'I work full-time, either as an employee or self-employed':
            Employment_Status = 1
        elif Employment_Status == 'I am unemployed':
            Employment_Status = 2
        elif Employment_Status == 'I am a student':
            Employment_Status = 3
        elif Employment_Status == 'I am a student and I work part-time':
            Employment_Status = 4
        elif Employment_Status == 'I do housework, fulfilling domestic tasks, looking after children':
            Employment_Status = 5
        elif Employment_Status == 'None of the above':
            Employment_Status = 6
        elif Employment_Status == 'I am retired':
            Employment_Status = 7
        elif Employment_Status== 'I am unable to work due to long-term illness or disability':
            Employment_Status = 8
        elif Employment_Status == 'I am doing community or military service':
            Employment_Status = 9
        

        
        
        prediction=model.predict([[Gender,  Age,Geography,Education,Employment_Status]])
        output=round(prediction[0],2)
        if output == 0:
            return render_template('index.html',prediction_texts="I can afford food, but nothing else")
        elif output == 1:
            return render_template('index.html',prediction_text="I cannot afford enough food for my family")
        elif output == 2:
            return render_template('index.html',prediction_text="I can afford food and regular expenses, but nothing else")
        elif output == 3:
            return render_template('index.html',prediction_text="I can afford food, regular expenses, and clothes, but nothing else")
        elif output == 4:
            return render_template('index.html',prediction_text="Prefer not to answer")
        elif output == 5:
            return render_template('index.html',prediction_text="I can comfortably afford food, clothes, and furniture, and I have savings")
        elif output == 6:
            return render_template('index.html',prediction_text="I can comfortably afford food, clothes, and furniture, but I don’t have savings")
        else:
            return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


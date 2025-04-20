from django.shortcuts import render
import joblib
import numpy as np
import os
from django.conf import settings
from django import forms

# Define the prediction form
class PredictionForm(forms.Form):
    age = forms.FloatField(min_value=0, max_value=120)
    sex = forms.FloatField(min_value=0, max_value=1)
    cp = forms.FloatField(min_value=0, max_value=3)
    trestbps = forms.FloatField(min_value=80, max_value=200)
    chol = forms.FloatField(min_value=100, max_value=600)
    fbs = forms.FloatField(min_value=0, max_value=1)
    restecg = forms.FloatField(min_value=0, max_value=2)
    thalach = forms.FloatField(min_value=60, max_value=220)
    exang = forms.FloatField(min_value=0, max_value=1)
    oldpeak = forms.FloatField(min_value=0, max_value=10)
    slope = forms.FloatField(min_value=0, max_value=2)
    ca = forms.FloatField(min_value=0, max_value=4)
    thal = forms.FloatField(min_value=0, max_value=3)

# Load model
def load_model():
    try:
        model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
        return joblib.load(model_path)
    except Exception as e:
        raise Exception(f"Failed to load model: {str(e)}")

def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            try:
                model = load_model()
                input_data = np.array([[
                    form.cleaned_data['age'],
                    form.cleaned_data['sex'],
                    form.cleaned_data['cp'],
                    form.cleaned_data['trestbps'],
                    form.cleaned_data['chol'],
                    form.cleaned_data['fbs'],
                    form.cleaned_data['restecg'],
                    form.cleaned_data['thalach'],
                    form.cleaned_data['exang'],
                    form.cleaned_data['oldpeak'],
                    form.cleaned_data['slope'],
                    form.cleaned_data['ca'],
                    form.cleaned_data['thal'],
                ]])
                prediction = model.predict(input_data)[0]
                result = 'The person has heart disease.' if prediction == 1 else 'The person does not have heart disease.'
                return render(request, 'result.html', {'result': result})
            except Exception as e:
                return render(request, 'result.html', {'result': f'Error: {str(e)}'})
        else:
            return render(request, 'result.html', {'result': 'Error: Invalid input data'})
    return render(request, 'home.html')
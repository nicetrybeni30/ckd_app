from django.shortcuts import render
from .forms import CKDForm
from .models import CKDRecord
import numpy as np
import tensorflow as tf
import joblib
import os

# Load model and fake scaler
MODEL_PATH = "/home/beni/ckd_project/model/model.h5"
SCALER_PATH = "/home/beni/ckd_project/model/fake_scaler.pkl"

model = tf.keras.models.load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

CONFIDENCE_THRESHOLD = 0.9

def index(request):
    if request.method == 'POST':
        form = CKDForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Use only the selected 12 features in this specific order
            features = [
                data['age'],
                data['bp'],
                data['sg'],
                data['al'],
                data['su'],
                data['bgr'],
                data['bu'],
                data['sc'],
                data['hemo'],
                data['pcv'],
                1 if data['htn'] == 'yes' else 0,
                1 if data['dm'] == 'yes' else 0,
            ]

            # Scale input
            input_data = scaler.transform([features])

            # Predict
            prediction = model.predict(input_data)[0]
            no_ckd_conf = prediction[0]
            ckd_conf = prediction[1]

            if max(no_ckd_conf, ckd_conf) < CONFIDENCE_THRESHOLD:
                result = f"❓ Uncertain result — Confidence too low"
            else:
                result = (
                    f"✅ No CKD Detected — Confidence: {no_ckd_conf:.2%}"
                    if np.argmax(prediction) == 0
                    else f"⚠️ CKD Detected — Confidence: {ckd_conf:.2%}"
                )

            CKDRecord.objects.create(**data, result=result)

            return render(request, 'ckd_app/result.html', {'result': result})

    else:
        form = CKDForm()

    return render(request, 'ckd_app/index.html', {'form': form})

# CKD Early Warning System (Django + Deep Learning)

This project is a Django-based web app for predicting Chronic Kidney Disease (CKD) progression using a trained deep learning model. It uses data from the [Kaggle CKD dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease) and is built to provide early warnings based on user medical input.

---

## ⚙️ Installation Steps

Step 1: Clone the Repository
```bash
git clone https://github.com/nicetrybeni30/ckd_app.git
cd ckd_app
```

Step 2: Create a Virtual Environment
```bash
Windows:
python -m venv venv
venv\Scripts\activate

Linux/macOS:
python3 -m venv venv
source venv/bin/activate
```

Step 3: Install Project Dependencies
```bash
pip install -r requirements.txt
```

Step 4: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

Step 5: Load the Model
```bash
Copy and paste the model files (model.h5, scaler.pkl, fake_scaler.pkl) into the "model/" folder
```

Step 6: Run the Development Server
```bash
python manage.py runserver
```

Step 7: Open in Browser
```bash
Visit http://127.0.0.1:8000 in your browser
```

Author:
```bash
 - Beni
```


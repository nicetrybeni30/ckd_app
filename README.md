# CKD Early Warning System (Django + Deep Learning)

This project is a Django-based web app for predicting Chronic Kidney Disease (CKD) progression using a trained deep learning model. It uses data from the [Kaggle CKD dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease) and is built to provide early warnings based on user medical input.

---

## ⚙️ Installation Steps

```bash
Step 1: Clone the Repository
git clone https://github.com/nicetrybeni30/ckd_app.git
cd ckd_app
```

```bash
Step 2: Create a Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate

Linux/macOS:
python3 -m venv venv
source venv/bin/activate
```

```bash
Step 3: Install Project Dependencies
pip install -r requirements.txt
```

```bash
Step 4: Apply Migrations
python manage.py makemigrations
python manage.py migrate
```

```bash
Step 5: Load the Model (if required)
Copy and paste the model files (model.h5, scaler.pkl, fake_scaler.pkl) into the "model/" folder
```

```bash
Step 6: Run the Development Server
python manage.py runserver
```

```bash
Step 7: Open in Browser
Visit http://127.0.0.1:8000 in your browser
```

```bash
Author: Beni
```


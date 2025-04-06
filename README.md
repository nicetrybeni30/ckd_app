# CKD Early Warning System (Django + Deep Learning)

This project is a Django-based web app for predicting Chronic Kidney Disease (CKD) progression using a trained deep learning model. It uses data from the [Kaggle CKD dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease) and is built to provide early warnings based on user medical input.

---

## ⚙️ Installation Steps

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/nicetrybeni30/ckd_app.git
cd ckd_app

Step 2: Create a Virtual Environment

Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

Step 3: Install Project Dependencies
pip install -r requirements.txt

Step 4: Apply Migrations
python manage.py makemigrations
python manage.py migrate

Step 5: Load the Model (if required)
Copy and Paste the model(model.h5, scaler.pkl and fake_scaler.pkl) to model folder

Step 6: Run the Development Server
python manage.py runserver

Visit http://127.0.0.1:8000 in your browser.

Author
Beni – working on AI solutions for healthcare diagnostics.

Let me know if you'd like to include screenshots or model training instructions too!






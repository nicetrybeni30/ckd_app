from django import forms

class CKDForm(forms.Form):
    age = forms.FloatField()
    bp = forms.FloatField(label="Blood Pressure")
    sg = forms.FloatField(label="Specific Gravity")
    al = forms.FloatField(label="Albumin")
    su = forms.FloatField(label="Sugar")
    rbc = forms.FloatField(label="Red Blood Cells")
    pc = forms.FloatField(label="Pus Cell")
    pcc = forms.FloatField(label="Pus Cell Clumps")
    ba = forms.FloatField(label="Bacteria")
    bgr = forms.FloatField(label="Blood Glucose Random")
    bu = forms.FloatField(label="Blood Urea")
    sc = forms.FloatField(label="Serum Creatinine")
    sod = forms.FloatField(label="Sodium")
    pot = forms.FloatField(label="Potassium")
    hemo = forms.FloatField(label="Hemoglobin")
    pcv = forms.FloatField(label="Packed Cell Volume")
    wc = forms.IntegerField(label="White Blood Cell Count")
    rc = forms.FloatField(label="Red Blood Cell Count")
    htn = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Hypertension")
    dm = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Diabetes Mellitus")
    cad = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Coronary Artery Disease")
    appet = forms.ChoiceField(choices=[('good', 'Good'), ('poor', 'Poor')])
    pe = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Pedal Edema")
    ane = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Anemia")
    sex = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])

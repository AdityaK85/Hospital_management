from django.db import models
import datetime

today = datetime.date.today()

# user : hospital
# pass : 123

# Create your models here.

class Doctor(models.Model):
    dr_name = models.CharField(max_length=50)
    dr_email = models.CharField(max_length=50)
    dr_addr = models.CharField(max_length=50)
    dr_mobile = models.CharField(max_length=50)
    dr_gender = models.CharField(max_length=50)
    dr_age = models.CharField(max_length=50)
    dr_exprience = models.CharField(max_length=50)
    dr_depart = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.dr_name

class Departments(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.department


class Hopsital_department(models.Model):
    department_name = models.CharField(max_length=50)
    discriptions = models.CharField( max_length=50)
    status = models.CharField( max_length=50)

    def __str__(self) -> str:
        return self.department_name
    
class Add_patient(models.Model):
    fk_dr = models.ForeignKey( Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField( max_length=50)
    patient_email = models.CharField( max_length=50)
    patient_phone = models.CharField( max_length=50)
    patient_age = models.CharField( max_length=50)
    patient_gender = models.CharField( max_length=50)
    patient_blood = models.CharField( max_length=50)
    patient_addr = models.CharField( max_length=50)
    patient_start_dt = models.DateField(default=today)
    patient_update_dt = models.DateField(default=today)
    
    def __str__(self) -> str:
        return self.patient_name
    
class Appointment(models.Model):
    patient_name = models.CharField( max_length=50)
    fk_department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    fk_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    problem = models.TextField()

    def __str__(self) -> str:
        return self.patient_name


class Schedule(models.Model):
    fk_department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    fk_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    available_days = models.CharField( max_length=50)
    available_time = models.CharField( max_length=50)
    end_time = models.CharField( max_length=50)
    per_patient_time = models.CharField( max_length=50)
    status = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.fk_doctor.dr_name
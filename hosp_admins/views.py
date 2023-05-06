from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def login_(request):
    return render(request, 'login.html')

@login_required(login_url='/login')
def dashboard(request):
    obj = Add_patient.objects.all()
    obj1 = Appointment.objects.all()
    obj2 = Schedule.objects.all()
    return render(request, 'dashboard.html', {'obj':obj, 'obj1':obj1, 'obj2':obj2})

@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def department(request):
    obj = Departments.objects.all()
    return render(request, 'department.html',{'obj':obj})

@login_required(login_url='/login')
def doctor(request):
    obj = Departments.objects.all()
    return render(request, 'doctor.html',{'obj':obj})

@login_required(login_url='/login')
def patient(request):
    obj = Doctor.objects.all()
    return render(request, 'patient.html',{'obj':obj})

@login_required(login_url='/login')
def appointment(request):
    obj = Doctor.objects.all()
    obj1 = Departments.objects.all()
    return render(request, 'appointment.html',{'obj':obj,'obj1':obj1})

@login_required(login_url='/login')
def schedule(request):
    obj = Departments.objects.all()
    obj1 = Doctor.objects.all()
    return render(request, 'schedule.html',{'obj':obj,'obj1':obj1})

@login_required(login_url='/login')
def manage_department(request):
    obj1 = Departments.objects.all()
    obj = Hopsital_department.objects.all()
    return render(request, 'manage_department.html',{'obj':obj,'obj1':obj1})

@login_required(login_url='/login')
def manage_doctor(request):
    obj1 = Departments.objects.all()
    obj = Doctor.objects.all()
    return render(request, 'manage_doctor.html',{'obj':obj, 'obj1':obj1})

@login_required(login_url='/login')
def manage_patients(request):
    obj = Add_patient.objects.all()
    obj1 = Doctor.objects.all()
    return render(request, 'manage_patients.html',{'obj':obj, 'obj1':obj1})

@login_required(login_url='/login')
def display_appointment(request):
    obj = Appointment.objects.all()
    obj1 = Departments.objects.all()
    obj2 = Doctor.objects.all()
    return render(request, 'display_appointment.html',{'obj':obj, 'obj1':obj1, 'obj2':obj2})

@login_required(login_url='/login')
def display_schedule(request):
    obj = Schedule.objects.all()
    obj1 = Departments.objects.all()
    obj2 = Doctor.objects.all()
    return render(request, 'display_schedule.html',{'obj':obj, 'obj1':obj1, 'obj2':obj2})

@login_required(login_url='/login')
@csrf_exempt
def save_department(request):
    if request.POST:
        department= request.POST.get("department")
        discription= request.POST.get("discription")
        status= request.POST.get("status")
        
        Hopsital_department.objects.create(department_name=department, discriptions=discription, status=status)
        return HttpResponse("success")

@login_required(login_url='/login')
@csrf_exempt
def save_doctor(request):
    if request.POST:
        dr_name= request.POST.get("dr_name")
        dr_email= request.POST.get("dr_email")
        dr_addr= request.POST.get("dr_addr")
        dr_mobile= request.POST.get("dr_mobile")
        dr_gender= request.POST.get("dr_gender")
        dr_age= request.POST.get("dr_age")
        dr_exprience= request.POST.get("dr_exprience")
        dr_depart= request.POST.get("dr_depart")
        Doctor.objects.create(dr_name=dr_name, dr_email=dr_email, dr_addr=dr_addr, dr_mobile=dr_mobile, dr_gender=dr_gender, dr_age=dr_age, dr_exprience=dr_exprience, dr_depart=dr_depart)
        return HttpResponse("success")

@login_required(login_url='/login')
@csrf_exempt
def save_patient(request):
    if request.POST:
        fk_dr= request.POST.get("fk_dr")
        patient_name= request.POST.get("patient_name")
        patient_email= request.POST.get("patient_email")
        patient_phone= request.POST.get("patient_phone")
        patient_age= request.POST.get("patient_age")
        patient_gender= request.POST.get("patient_gender")
        patient_blood= request.POST.get("patient_blood")
        patient_addr= request.POST.get("patient_addr")
        Add_patient.objects.create(fk_dr_id=fk_dr, patient_name=patient_name, patient_email=patient_email, patient_phone=patient_phone, patient_age=patient_age, patient_gender=patient_gender, patient_blood=patient_blood, patient_addr=patient_addr)
        return HttpResponse("success")

@login_required(login_url='/login')
@csrf_exempt
def save_appointment(request):
    if request.POST:
        patient_name= request.POST.get("patient_name")
        fk_department= request.POST.get("fk_department")
        fk_doctor= request.POST.get("fk_doctor")
        appointment_date= request.POST.get("appointment_date")
        problem= request.POST.get("problem")
        Appointment.objects.create(patient_name=patient_name, fk_department_id=fk_department, fk_doctor_id=fk_doctor, appointment_date=appointment_date, problem=problem)
        return HttpResponse("success")

@login_required(login_url='/login')
@csrf_exempt
def save_schedule(request):
    if request.POST:
        fk_department= request.POST.get("fk_department")
        fk_doctor= request.POST.get("fk_doctor")
        available_days= request.POST.get("available_days")
        available_time= request.POST.get("available_time")
        end_time= request.POST.get("end_time")
        per_patient_time= request.POST.get("per_patient_time")
        status= request.POST.get("status")
        Schedule.objects.create(fk_department_id=fk_department, fk_doctor_id=fk_doctor, available_days=available_days, available_time=available_time, end_time=end_time, per_patient_time=per_patient_time, status=status)
        return HttpResponse("success")

@login_required(login_url='/login')  
@csrf_exempt
def delete_department(request):
    id= request.POST.get('id')
    Hopsital_department.objects.get(id=id).delete()
    return HttpResponse("success")
    
@login_required(login_url='/login')
@csrf_exempt
def delete_doctor(request):
    id= request.POST.get('id')
    Doctor.objects.get(id=id).delete()
    return HttpResponse("success")

@login_required(login_url='/login')   
@csrf_exempt
def delete_patient(request):
    id= request.POST.get('id')
    Add_patient.objects.get(id=id).delete()
    return HttpResponse("success")

@login_required(login_url='/login')   
@csrf_exempt
def delete_appointment(request):
    id= request.POST.get('id')
    Appointment.objects.get(id=id).delete()
    return HttpResponse("success")

@login_required(login_url='/login')    
@csrf_exempt
def delete_schedule(request):
    id= request.POST.get('id')
    Schedule.objects.get(id=id).delete()
    return HttpResponse("success")

@login_required(login_url='/login')
@csrf_exempt
def edit_department(request, id):
        obj1 = Departments.objects.all()
        id= Hopsital_department.objects.get(id=id)
        return render(request,'edit_department.html',{'id':id, 'obj1':obj1})
    

@login_required(login_url='/login')
@csrf_exempt
def edit_doctor(request, id):
        obj = Departments.objects.all()
        id = Doctor.objects.get(id= id)
        return render(request,'edit_doctor.html',{'id':id, 'obj':obj})
    

@login_required(login_url='/login')
@csrf_exempt
def edit_patient(request, id):
        id= Add_patient.objects.get(id= id)
        return render(request,'edit_patient.html',{'id':id})
    

@login_required(login_url='/login')
@csrf_exempt
def edit_appointment(request, id):
        id= Appointment.objects.get(id= id)
        obj = Doctor.objects.all()
        obj1 = Departments.objects.all()
        return render(request,'edit_appointment.html',{'id':id, 'obj':obj, 'obj1':obj1})
    

@login_required(login_url='/login')
@csrf_exempt
def edit_schedule(request, id):
        id= Schedule.objects.get(id= id)
        obj = Doctor.objects.all()
        obj1 = Departments.objects.all()
        return render(request,'edit_schedule.html',{'obj':obj, 'id':id, 'obj1':obj1})
    


@login_required(login_url='/login')
@csrf_exempt 
def update_department(request):
    id = request.POST.get('id')
    obj = Hopsital_department.objects.get(id=id)
    obj.department_name = request.POST.get('department')
    obj.discriptions = request.POST.get('discription')
    obj.status = request.POST.get('status')
    obj.save()

    return HttpResponse('success')
   

@login_required(login_url='/login')
@csrf_exempt 
def update_doctor(request):
    id = request.POST.get('id')
    dr_name = request.POST.get('dr_name')
    dr_email = request.POST.get('dr_email')
    dr_addr = request.POST.get('dr_addr')
    dr_mobile = request.POST.get('dr_mobile')
    dr_gender = request.POST.get('dr_gender')
    dr_age = request.POST.get('dr_age')
    dr_exprience = request.POST.get('dr_exprience')
    dr_depart = request.POST.get('dr_depart')

    if Doctor.objects.filter(id=id):
        obj = Doctor.objects.get(id=id)
        obj.dr_name = dr_name
        obj.dr_email = dr_email
        obj.dr_addr = dr_addr
        obj.dr_mobile = dr_mobile
        obj.dr_gender = dr_gender
        obj.dr_age = dr_age
        obj.dr_exprience = dr_exprience
        obj.dr_depart = dr_depart
        obj.save()
        return HttpResponse('success')
    else:
        return HttpResponse('error')

@login_required(login_url='/login')
@csrf_exempt 
def update_patient(request):
    id = request.POST.get('id')
    fk_dr = request.POST.get('fk_dr')
    patient_name = request.POST.get('patient_name')
    patient_email = request.POST.get('patient_email')
    patient_phone = request.POST.get('patient_phone')
    patient_age = request.POST.get('patient_age')
    patient_gender = request.POST.get('patient_gender')
    patient_blood = request.POST.get('patient_blood')
    patient_addr = request.POST.get('patient_addr')

    if Add_patient.objects.filter(id=id):
        obj = Add_patient.objects.get(id=id)
        obj.fk_dr_id = fk_dr
        obj.patient_name = patient_name
        obj.patient_email = patient_email
        obj.patient_phone = patient_phone
        obj.patient_age = patient_age
        obj.patient_gender = patient_gender
        obj.patient_blood = patient_blood
        obj.patient_addr = patient_addr
        obj.patient_addr = patient_addr
        obj.patient_update_dt = datetime.date.today()
        obj.save()

        return HttpResponse('success')
    else:
        return HttpResponse('error')

@login_required(login_url='/login')
@csrf_exempt 
def update_appointment(request):
    id = request.POST.get('id')
    patient_name = request.POST.get('patient_name')
    fk_department = request.POST.get('fk_department')
    fk_doctor = request.POST.get('fk_doctor')
    appointment_date = request.POST.get('appointment_date')
    problem = request.POST.get('problem')

    if Appointment.objects.filter(id=id):
        obj = Appointment.objects.get(id=id)
        obj.patient_name = patient_name
        obj.fk_department_id = fk_department
        obj.fk_doctor_id = fk_doctor
        obj.appointment_date = appointment_date
        obj.problem = problem
        obj.save()

        return HttpResponse('success')
    else:
        return HttpResponse('error')

@login_required(login_url='/login')
@csrf_exempt 
def update_schedule(request):
    id = request.POST.get('id')
    available_days = request.POST.get('available_days')
    fk_department = request.POST.get('fk_department')
    fk_doctor = request.POST.get('fk_doctor')
    available_time = request.POST.get('available_time')
    end_time = request.POST.get('end_time')
    per_patient_time = request.POST.get('per_patient_time')
    status = request.POST.get('status')

    if Schedule.objects.filter(id=id):
        obj = Schedule.objects.get(id=id)
        obj.available_days = available_days
        obj.fk_department_id = fk_department
        obj.fk_doctor_id = fk_doctor
        obj.available_time = available_time
        obj.end_time = end_time
        obj.per_patient_time = per_patient_time
        obj.status = status
        obj.save()

        return HttpResponse('success')
    else:
        return HttpResponse('error')
   
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            return HttpResponse('error1')
        
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            login(request, user_obj)
            return HttpResponse('success')
    else:
        HttpResponse('erro')
   
@csrf_exempt
def signup_handle(request):
    if request.method == "POST":
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        userpassword = request.POST.get('userpassword')


        if User.objects.filter(email=useremail).exists():
            return HttpResponse('error1')
        elif User.objects.filter(username = username).exists():
            return HttpResponse('error2')
        else:
            user_obj = User(username=username, email=useremail , password=userpassword)
            user_obj.set_password(userpassword)
            user_obj.save()
            print("account created")
            print(f'{username}, useremail : {useremail}, userpassword : {userpassword}')
            return HttpResponse('success')
    else:
        return HttpResponse('error')

def logout_page(request):
    logout(request)
    return redirect('/login')
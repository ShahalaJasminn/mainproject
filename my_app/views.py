import csv

from astropy.wcs.docstrings import row
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from my_app.GPred import growthpredict
from my_app.models import *
from my_app.predictioncnn import predict
import pandas as pd
import os

from django.conf import settings

def index(request):
    return render(request,"home.html")



def login(request):
    return render(request,"login.html")

def login_post(request):
    username=request.POST['username']
    password=request.POST['pass']
    a=Login.objects.get(username=username,password=password)
    request.session['lid']=a.id

    if a.type=='admin':
        return HttpResponse('''<script>alert('Admin logined...');window.location='/admin_dash'</script>''')
    elif a.type=='user':
        return HttpResponse('''<script>alert('User logined...');window.location='/user_dash'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid...');window.location='/'</script>''')

def logout(request):
    request.session['lid']=''
    return redirect('/')


def admin_dash(request):
    if request.session['lid']=='':
        return redirect('/')
    return render(request,"Admin/Admin_dashboard.html")

def user_dash(request):
    if request.session['lid'] =='':
        return redirect('/')
    return render(request,"User/User_dashboard.html")

def registration(request):
    return render(request,"registration.html")



def registration_POST(request):
    name=request.POST['textfield4']
    email=request.POST['textfield3']
    phone=request.POST['textfield1']
    place=request.POST['textfield2']
    password=request.POST['pass1']
    confirmpassword=request.POST['pass2']
    if password == confirmpassword:
        lobj=Login()
        lobj.username=email
        lobj.password=password
        lobj.type="user"
        lobj.save()
        uobj=User()
        uobj.login_id=lobj
        uobj.name=name
        uobj.email = email
        uobj.place = place
        uobj.phone=phone
        uobj.save()
        return HttpResponse('''<script>alert('Account  successfully created...');window.location='/login'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid...');window.location='/registration'</script>''')
def view_feedback(request):
    if request.session['lid'] =='':
        return redirect('/')
    a=Feedback.objects.all()
    return render(request,"Admin/admin_view_feedback.html",{'data':a})

def view_user(request):
    if request.session['lid'] =='':
        return redirect('/')
    b=User.objects.all()
    return render(request,"Admin/admin_view_users.html",{'data':b})


def send_feedback(request):
    if request.session['lid'] =='':
        return redirect('/')

    return render(request,"User/send_feedback.html")


def send_feedback_post(request):
    feedback=request.POST['name']
    a=Feedback()
    a.user_id=User.objects.get(login_id_id=request.session['lid'])
    a.feedback=feedback
    a.save()
    return redirect('/user_dash')


def uploadimageee(request):
    return render(request,"User/uploadimg.html")




# def upload_image(request):
#     file1=request.FILES['file2']
#     fnn=FileSystemStorage()
#     fn=fnn.save(file1.name,file1)
#     print(fn,"hhhhhhhhhhhhhhhh")
#
#     res=predict(r"C:\Users\shaha\PycharmProjects\FarmMoni\media"+"/"+fn)
#     print(res,"ppppppppppppppppppp")
#
#     file2=request.FILES['file1']
#     fnn=FileSystemStorage()
#     fn=fnn.save(file2.name,file2)
#     print(fn)
#
#     ress=growthpredict(r"C:\Users\shaha\PycharmProjects\FarmMoni\media"+"/"+fn)
#     print(ress)
#     return render(request,"User/uploadimg.html",{"val":res,"val2":ress})





# def upload_growth_image(request):
#     if request.method == 'POST':
#         file1 = request.FILES.get('file1')
#         if file1:
#             fnn = FileSystemStorage()
#             fn = fnn.save(file1.name, file1)
#             print(fn, "Growth Image Uploaded")
#
#             file_path = r"C:\Users\shaha\PycharmProjects\FarmMoni\media" + "/" + fn
#             ress = growthpredict(file_path)
#             print(ress, "Growth Prediction Result")
#
#
#
#
#             return render(request, "User/uploadimg.html", {"val2": ress})
#     return render(request, "User/uploadimg.html")


# def upload_disease_image(request):
#     if request.method == 'POST':
#         file2 = request.FILES.get('file2')
#         if file2:
#             fnn = FileSystemStorage()
#             fn = fnn.save(file2.name, file2)
#             print(fn, "Disease Image Uploaded")
#
#             file_path = r"C:\Users\shaha\PycharmProjects\FarmMoni\media" + "/" + fn
#             res = predict(file_path)
#             print(res, "Disease Prediction Result")
#
#             return render(request, "User/uploadimg.html", {"val": res})
#     return render(request, "User/uploadimg.html")




# def upload_image(request):
#     if request.method == 'POST':
#         if 'file1' in request.FILES:
#             file1 = request.FILES.get('file1')
#
#             fnn = FileSystemStorage()
#             fn = fnn.save(file1.name, file1)
#             print(fn, "Growth Image Uploaded")
#
#             file_path = r"C:\Users\shaha\PycharmProjects\FarmMoni\media" + "/" + fn
#             ress = growthpredict(file_path)
#             print(ress, "Growth Prediction Result")
#
#             return render(request, "User/uploadimg.html", {"val2": ress})
#         if 'file2' in request.FILES:
#             file2 = request.FILES.get('file2')
#             fnn2 = FileSystemStorage()
#             fn2 = fnn2.save(file2.name, file2)
#             print(fn2, "Disease Image Uploaded")
#
#             file_path = r"C:\Users\shaha\PycharmProjects\FarmMoni\media" + "/" + fn2
#             res = predict(file_path)
#             print(res, "Disease Prediction Result")
#
#             return render(request, "User/uploadimg.html", {"val": res})
#
#     return render(request, "User/uploadimg.html")



#  fertilzer recommendation

CSV_FILE_PATH = os.path.join(settings.MEDIA_ROOT, 'fertilizers.csv')


def recommend_fertilizer(stage):
    try:
        df = pd.read_csv(CSV_FILE_PATH)

        recommendation = df[df['Growth Stage'].str.lower() == stage.lower()]

        if recommendation.empty:
            return None

        fertilizer_info = {
            "Fertilizer_Name": recommendation.iloc[0]['Fertilizer Name'],
            "Quantity_Acre_Cent": recommendation.iloc[0]['Quantity (Acre and Cent)'],
            "Usage_Manner": recommendation.iloc[0]['Usage Manner'],
            "Weekly_Watering_Schedule":recommendation.iloc[0]['Weekly Watering Schedule']
        }

        return fertilizer_info

    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None



# View function to handle form submission
def upload_growth_image(request):
    if request.method == 'POST':
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        category=request.POST["category"]

        print(category,"===========================================")

        if file1:
            fnn = FileSystemStorage()
            fn = fnn.save(file1.name, file1)
            print(fn, "Growth Image Uploaded")

            # Perform growth prediction
            file_path = os.path.join(settings.MEDIA_ROOT, fn)
            growth_stage = growthpredict(file_path)  # Assume this function returns stage name
            print(growth_stage, "Growth Prediction Result")

            # Get fertilizer recommendation
            fertilizer = recommend_fertilizer(growth_stage)

            return render(request, "User/uploadimg.html", {
                "val2": growth_stage,  # Growth stage result
                "fertilizer": fertilizer  # Fertilizer details
            })
        elif file2:

            fnn2 = FileSystemStorage()
            fn2 = fnn2.save(file2.name, file2)
            print(fn2, "Disease Image Uploaded")

            file_path = r"C:\Users\shaha\PycharmProjects\FarmMoni\media" + "/" + fn2
            res = predict(file_path)
            print(res, "Disease Prediction Result")

            csv_file = r"C:\Users\shaha\PycharmProjects\FarmMoni\media\chemicals.csv"
            df = pd.read_csv(csv_file)

            a = res

            recommended_chemical = df.loc[df["Plant - Disease"] == a, ["Recommended Chemical", "Application Method"]]

            # Display the result
            print(recommended_chemical.values[0][0])
            print(recommended_chemical.values[0][1])
            return render(request,"User/uploadimg.html",{"diseases":a,"RecommendedChemical":recommended_chemical.values[0][0],"ApplicationMethod":recommended_chemical.values[0][1]})

    # fertilizers = {
    #     "Fertilizer_Name": row["Fertilizer Name"],
    #     "Quantity_Acre_Cent": row["Quantity(Acre and Cent)"],
    #     "Usage_Manner": row["Usage Manner"],
    #     "Weekly_Watering_Schedule":row["Weekly Watering Schedule"]
    # }
    #
    # return render(request, 'uploadimg.html', {"fertilizer": fertilizers})


#leaf disease pred and chemical recommendation













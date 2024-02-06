from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

data_list = [
    {"person_id": 1, "first_name": "John", "last_name": "Doe", "age": 25, "gender": "Male", "email": "john.doe@email.com", "zip_code": 12345},
    {"person_id": 2, "first_name": "Jane", "last_name": "Smith", "age": 30, "gender": "Female", "email": "jane.smith@email.com", "zip_code": 56789},
    {"person_id": 3, "first_name": "Michael", "last_name": "Johnson", "age": 22, "gender": "Male", "email": "michael.johnson@email.com", "zip_code": 98765},
    {"person_id": 4, "first_name": "Emily", "last_name": "Williams", "age": 28, "gender": "Female", "email": "emily.williams@email.com", "zip_code": 43210},
    {"person_id": 5, "first_name": "David", "last_name": "Brown", "age": 35, "gender": "Male", "email": "david.brown@email.com", "zip_code": 67890},
    {"person_id": 6, "first_name": "Sophia", "last_name": "Miller", "age": 26, "gender": "Female", "email": "sophia.miller@email.com", "zip_code": 54321},
    {"person_id": 7, "first_name": "Matthew", "last_name": "Davis", "age": 32, "gender": "Male", "email": "matthew.davis@email.com", "zip_code": 13579},
    {"person_id": 8, "first_name": "Olivia", "last_name": "Martinez", "age": 29, "gender": "Female", "email": "olivia.martinez@email.com", "zip_code": 24680},
    {"person_id": 9, "first_name": "Christopher", "last_name": "Taylor", "age": 24, "gender": "Male", "email": "christopher.taylor@email.com", "zip_code": 97531},
    {"person_id": 10, "first_name": "Ava", "last_name": "Moore", "age": 31, "gender": "Female", "email": "ava.moore@email.com", "zip_code": 86420},
    {"person_id": 11, "first_name": "Daniel", "last_name": "Jackson", "age": 27, "gender": "Male", "email": "daniel.jackson@email.com", "zip_code": 15843},
    {"person_id": 12, "first_name": "Mia", "last_name": "Anderson", "age": 33, "gender": "Female", "email": "mia.anderson@email.com", "zip_code": 74269},
    {"person_id": 13, "first_name": "Ethan", "last_name": "White", "age": 23, "gender": "Male", "email": "ethan.white@email.com", "zip_code": 36912},
    {"person_id": 14, "first_name": "Isabella", "last_name": "Harris", "age": 28, "gender": "Female", "email": "isabella.harris@email.com", "zip_code": 95123},
    {"person_id": 15, "first_name": "Andrew", "last_name": "Turner", "age": 30, "gender": "Male", "email": "andrew.turner@email.com", "zip_code": 58246},
    {"person_id": 16, "first_name": "Chloe", "last_name": "Clark", "age": 25, "gender": "Female", "email": "chloe.clark@email.com", "zip_code": 14785},
    {"person_id": 17, "first_name": "William", "last_name": "Ward", "age": 34, "gender": "Male", "email": "william.ward@email.com", "zip_code": 63974},
    {"person_id": 18, "first_name": "Grace", "last_name": "Fisher", "age": 29, "gender": "Female", "email": "grace.fisher@email.com", "zip_code": 82536},
    {"person_id": 19, "first_name": "Liam", "last_name": "Baker", "age": 26, "gender": "Male", "email": "liam.baker@email.com", "zip_code": 46812},
    {"person_id": 20, "first_name": "Emma", "last_name": "Lopez", "age": 32, "gender": "Female", "email": "emma.lopez@email.com", "zip_code": 35791}
]

def Name(request,name):
    for i in range(len(data_list)):
        if data_list[i]["first_name"]==name:
            return HttpResponse(f"<h1>{name}-bunday ism mavjud</h1>")
    return HttpResponse("""
                        <div>
                            <h1 style="text-color:red;">Error</h1>
                        </div>
                        """)
def Id(request,id):
    for i in range(len(data_list)):
        if data_list[i]["person_id"]==id:

             return HttpResponse(f"<h1>{id} mavjud</h1><h2>{id}.dagi shaxsning ismi {data_list[i]["first_name"]}</h2>")
                        
                    
    return HttpResponse("""
                        <div>
                            <h1 style="text-color:red;">Error</h1>
                        </div>
                        """)

def Gender(request,gender):
    for i in range(len(data_list)):
        if data_list[i]["gender"]==gender:
            return HttpResponse(f"<h1>{gender}-bu shaxsning ismi {data_list[i]["first_name"]} familyasi {data_list[i]["last_name"]} </h1>")
    return HttpResponse("""
                        <div>
                            <h1 style="text-color:red;">Error</h1>
                        </div>
                        """)
def Zip_code(request,zip_code):
    for i in range(len(data_list)):
        if data_list[i]["zip_code"]==zip_code:
            return HttpResponse(f"<h1>{zip_code}-bu shaxsning ismi {data_list[i]["first_name"]} familyasi {data_list[i]["last_name"]} </h1>")
    return HttpResponse("""
                        <div>
                            <h1 style="text-color:red;">Error</h1>
                        </div>
                        """)
def Email(request,email):
    for i in range(len(data_list)):
        if data_list[i]["email"]==email:
            return HttpResponse(f"<h1>{email}-bu shaxsning ismi {data_list[i]["first_name"]} familyasi {data_list[i]["last_name"]} </h1>")
    return HttpResponse("""
                        <div>
                            <h1 style="text-color:red;">Error</h1>
                        </div>
                        """)


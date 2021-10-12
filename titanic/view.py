from django.shortcuts import render
from django.http import HttpResponse
import pickle


def home(request):

    return render(request, "index.html")


def predict(request):

    Pclass = request.POST.get('P_class')
    Age = request.POST.get("Age")
    Sex = request.POST.get("Sex")

    data = [Age, Sex, Pclass]
    print(data)

    with open("model_pickle", 'rb') as f:
        My_model = pickle.load(f)

    prediction = My_model.predict([data])
    print(prediction)

    survived = ""

    if prediction == [0]:
        survived = "Not Survived"
        params = {
            "result": survived
        }
        return render(request, "result1.html", params)

    elif prediction == [1]:
        survived = "Survived"
        params = {
            "result": survived
        }
        return render(request, "result.html", params)


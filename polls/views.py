import os

from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")


def testHtml(request):

	return render(request, "test.html")


def visu(request):
	os.remove('polls/static/monate.png')
	monate = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun']
	temperaturen = [5, 7, 12, 18, 22, 25]

	if request.method == 'POST':
		temperatur = request.POST['temp']
		monate.append("Jul")
		temperaturen.append(int(temperatur))

	plt.plot(monate, temperaturen)
	plt.xlabel('Monat')
	plt.ylabel('Temperatur (°C)')
	plt.title('Monatliche Temperaturen')
	plt.savefig('polls/static/monate.png')

	return render(request, 'test.html')

from django.shortcuts import  render, redirect
import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
import json
import pandas as pd
import numpy as np
from sklearn import decomposition
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import StudentRegistrationForm , Test
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from app.dicto import ro
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def index(request):
		return render(request, 'index.html', {})     

def profile(request):
		username = request.user
		return render(request, 'profile.html', {'username':username})  

def test(request):
	form = Test()
	x={}
	if request.method == 'POST':
		form = Test(request.POST)
		x['academic_percentage_in_operating_system']= request.POST.get('academic_percentage_in_operating_system')
		x['percentage_in_algorithm']=request.POST.get('percentage_in_algorithm')		
		x['percentage_in_programming_concepts']=request.POST.get('percentage_in_programming_concepts')		
		x['percentage_in_software_engineering']=request.POST.get('percentage_in_software_engineering')		
		x['percentage_in_computer_networks']=request.POST.get('percentage_in_computer_networks')		
		x['percentage_in_electronics_subjects']=request.POST.get('percentage_in_electronics_subjects')		
		x['percentage_in_computer_architecture']=request.POST.get('percentage_in_computer_architecture')		
		x['percentage_in_mathematics']=request.POST.get('percentage_in_mathematics')		
		x['percentage_in_communication_skills']=request.POST.get('percentage_in_communication_skills')		
		x['how_many_hours_in_a_day_you_can_work']=request.POST.get('how_many_hours_in_a_day_you_can_work')		
		x['Rate_your_logical_quotient']=request.POST.get('Rate_your_logical_quotient')		
		x['How_may_hackathon_have_you_participated']=request.POST.get('How_may_hackathon_have_you_participated')		
		x['Rate_your_coding_skills']=request.POST.get('Rate_your_coding_skills')		
		x['Rate_your_public_speaking']=request.POST.get('Rate_your_public_speaking')		
		x['can_work_long_time_before_system']=request.POST.get('can_work_long_time_before_system')
		x['self_learning_capability']=request.POST.get('self_learning_capability')
		x['which_certifications_do_you_prefer']=request.POST.get('which_certifications_do_you_prefer')
		x['any_talenttests_taken']=request.POST.get('any_talenttests_taken')
		x['scale_your_reading_and_writing_skills']= request.POST.get('scale_your_reading_and_writing_skills')
		x['scale_your_memory_capability_score'] = request.POST.get('scale_your_memory_capability_score')
		x['Interested_subjects'] = request.POST.get('Interested_subjects')
		x['interested_career_area'] = request.POST.get('interested_career_area')
		x['what_do_you_prefer_job_or_higher_studies'] = request.POST.get('what_do_you_prefer_job_or_higher_studies')
		x['type_of_company_you_prefer'] = request.POST.get('type_of_company_you_prefer')
		x['intereaction_with_seniors'] = request.POST.get('intereaction_with_seniors')
		x['do_you_love_games'] = request.POST.get('do_you_love_games')
		x['type_of_books_you_prefer'] = request.POST.get('type_of_books_you_prefer')
		x['most_likely_behaviour'] = request.POST.get('most_likely_behaviour')
		x['what_you_prefer_managemet_or_technical'] = request.POST.get('what_you_prefer_managemet_or_technical')
		
		x['have_you_ever_worked_with_teams'] = request.POST.get('have_you_ever_worked_with_teams')
		x['Are_you_an_Introvert']= request.POST.get('Are_you_an_Introvert') 
		
		print(x)
		career = fun(x)
		context= {'career':career}
		return render(request,'generated_career.html',context)
	context = {'form':form}
	return render(request,'test.html',context)

def fun(dict1):
	dataset = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\smackathon\\project\\app\\roo_data.csv')
	data = dataset.iloc[:,:-1].values
	label = dataset.iloc[:,-1].values
	labelencoder = LabelEncoder()
	data_t=np.zeros(shape=(20000,31))
	for i in range(14,31):
		data_t[:,i] = labelencoder.fit_transform(data[:,i])  
	data1=data[:,:14]
	# normalized_data = Normalizer().fit_transform(data1)
	# print(normalized_data.shape)
	# da=0.8383
	# normalized_data
	data2=data_t[:,14:]
	# data2.shape
	df1 = np.append(data1,data2,axis=1)
	X1 = pd.DataFrame(df1,columns=['Acedamic percentage in Operating Systems', 'percentage in Algorithms',
       'Percentage in Programming Concepts',
       'Percentage in Software Engineering', 'Percentage in Computer Networks',
       'Percentage in Electronics Subjects',
       'Percentage in Computer Architecture', 'Percentage in Mathematics',
       'Percentage in Communication skills', 'Hours working per day',
       'Logical quotient rating', 'hackathons', 'coding skills rating',
       'public speaking points', 'can work long time before system?',
       'self-learning capability?', 'certifications',
       'talenttests taken?',
       'reading and writing skills', 'memory capability score',
       'Interested subjects', 'interested career area ', 'Job/Higher Studies?',
       'Type of company want to settle in?',
       'Taken inputs from seniors or elders', 'interested in games',
       'Interested Type of Books', 
       'Gentle or Tuff behaviour?',
       'Management or Technical',
       'worked in teams ever?', 'Introvert'])
	label = labelencoder.fit_transform(label)
	y=pd.DataFrame(label,columns=["Suggested Job Role"])
	l2=labelencoder.inverse_transform(label)
	dict={}
	for i in label:
		dict[i]=l2[i]
	X_train, X_test, y_train, y_test = train_test_split(X1, np.ravel(y), test_size=0.4, random_state=1)
  
	gnb = GaussianNB()
	gnb.fit(X_train, y_train)
	
	# making predictions on the testing set
	y_pred = gnb.predict(X_test)
    
	a1=[]

	for i in dict1:
		a1.append(dict1[i])
	x=np.array(a1)

	tst_data=np.zeros(31)
	tst_data1=np.zeros(14)
	for i in range(14,31):
		labelencoder.fit(data[:,i])
		tst_data[i] = labelencoder.transform([(x[i])])  
		
	for i in range(0,14):
		tst_data1[i]=x[i]

	tst_data2=tst_data[14:]
	df2 = np.append(np.array([tst_data1]),np.array([tst_data2]),axis=1)
	a=gnb.predict(np.array(df2))
	print(dict[a[0]])
	return dict[a[0]]

def login(request):
 return render(request, 'login.html')

class CustomerRegistrationView(View):
	def get(self,request):
		print("get")
		form = StudentRegistrationForm()
		context = {'form':form}
		return render(request,'register.html',context)
	def post(self,request):
		print("post")
		form = StudentRegistrationForm(request.POST)
		if form.is_valid():
			messages.success(request,"Congratulations!! Register Successfully")
			form.save()
			print("post")
		context = {'form':form}
		return render(request,'register.html',context)

def roadmap(request,career):
	print(career)
	temp = ro.get(career)
	ans = list(temp.values())
	return render(request,'roadmap.html',{'ans':ans})
		

BASE_URL = 'https://udemy.com/courses/search/?q={}'
def courses(request,career):
	
	final_url = BASE_URL.format(quote_plus(career))
	response = requests.get(final_url)
	data = response.text
	soup = BeautifulSoup(data , features='html.parser')
	print(final_url)
	main = soup.find('div',{'class':'main-content'})
	print("MAIN--------------------------")
	print(main)
	DIV1= soup.find('div',{'class':'ud-app-loader ud-component--search--search ud-app-loaded'})
	print("DIV-----------------------------")
	print(DIV1)
	course_listing = soup.findAll('div',{'class':'course-card--main-content--2XqiY'})
	# class="udlite-heading-md course-card--course-title--vVEjC"
	# course-card--main-content--2XqiY course-card--has-price-text--1c0ze
	context = {}
	print(course_listing)
	for course in course_listing:
		link = course.find('a').get('href')
		heading = course.find('a').text
		context[heading]=link
	print(context)
	return render(request,'courses.html')



def about(request):
	return render(request,'about.html')
	
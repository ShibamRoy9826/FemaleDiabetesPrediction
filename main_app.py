from joblib import load
from numpy import array as ar
from colored import fg,bg,attr,stylize

model=load('FemaleDiabetesPrediction.joblib')



def ReturnInputArray():
	question=fg(48)
	Pregnancy=int(input(stylize('How many times did you get pregnant?(if not enter 0)--> ',question)))
	
	
	Weight=float(input(stylize('What about your weight?(in kg)--> ',question)))
	Height=float(input(stylize('And your height?(in m)--> ',question)))
	# The body mass index
	Height_square=Height*Height
	BMI=float(Weight/Height_square)

	NoOfDiabetesInFamily=int(input(stylize('Okay, How many people has diabetes in your family?--> ',question)))
	DiabetesPedigreeFunc=float(NoOfDiabetesInFamily/10)

	insulin=int(input(stylize('And How much insulin do you consume(if you dont, write 0)?(in U/ml)--> ',question)))

	age=int(input(stylize('So, whats your age?(in years)--> ',question)))

	Glucose=int(input(stylize('Any idea about your Glucose concentration(an approx. rate would work)?--> ',question)))

	BloodPressure=int(input(stylize('What about your Blood Pressure(an approx. rate would work)?(mm Hg) ',question)))

	SkinThickness=int(input(stylize('whats your skin thickness?(try checking the fold size of your triceps)(in mm)--> ',question)))

	return ar([[Pregnancy,Glucose,BloodPressure,SkinThickness,insulin,BMI,DiabetesPedigreeFunc,age]])



heading=fg(14)+attr(1)+attr(4)
print(stylize("Welcome to the Female Diabetes Prediction",heading))
print("\n")
IMPORTANT=fg(196)+attr(1)
FINE=fg(10)+attr(1)
while True:
	try:
		GivenData=ReturnInputArray()
		prediction=model.predict(GivenData)
		print("\n")
		if prediction[0]==1:
			print(stylize("You may have diabetes, its preferable to show a doctor!",IMPORTANT))
		else:
			print(stylize("You may not have diabetes, but always be careful!",FINE))
		print("\n\n\n")
	except Exception as e:
		print(e)
	
from .models import Employee
from django import forms
class EmForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields= ["eid","ename","esal","edesg"]
		widgets={
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Id"
			}),
		"ename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Name"
			}),
		"esal":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Salary",
			"man":50000,
			"min":10000,
			}),
		"edesg":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Designation"
			})
		
		}

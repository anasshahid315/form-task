# from django import forms
# from .models import Employee, City, State

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ('name', 'birthdate', 'country', 'city')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['state'].queryset = State.objects.none()

#         if 'country' in self.data:
#             try:
#                 country_id = int(self.data.get('country'))
#                 self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty state queryset
#         elif self.instance.pk:
#             self.fields['state'].queryset = self.instance.country.state_set.order_by('name')


#     from django import forms
# from .models import Person, City

# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ('name', 'birthdate', 'country', 'city')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['city'].queryset = City.objects.none()

#         if 'state' in self.data:
#             try:
#                 state_id = int(self.data.get('state'))
#                 self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['city'].queryset = self.instance.state.city_set.order_by('name')
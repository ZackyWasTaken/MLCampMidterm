student = {
'age': 'very_young',
'sex': 1,
'hs_type': 'private',
'scholarship_type': 0,
'extra_work': 0,
'activities': 1,
'partner': 0,
'salary': 'very_low',
'transportation': 'bus',
'accommodation': 'dorm',
'mom_education': 'primary',
'dad_education': 'secondary',
'siblings': 'three',
'parental_status': 'married',
'mom_occupation': 'housewife',
'dad_occupation': 'retired',
'study_per_week': 'five',
'non_science_reading': 'sometimes',
'science_reading': 'often',
'conf_attendance': 0,
'activity_impact': 'positive',
'class_attendance': 'always',
'midterm_prep_company': 'friends',
'midterm_prep_timing': 'late',
'note_taking': 'always',
'listening_in_class': 'sometimes',
'discussion_effect_on_interest': 'always',
'flip_classroom': 'not useful'
}

import requests

url = 'http://4.175.161.104/predict' 

response = requests.post(url, json=student) 

result = response.json() 

print(result)
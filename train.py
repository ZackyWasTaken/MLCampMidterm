import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
import pickle
rnd_seed = 5

full_df = pd.read_csv('StudentsPerformance.csv')
full_df= full_df[full_df['COURSE ID']!=1]

del full_df['COURSE ID']
del full_df['GRADE']
del full_df['Expected Cumulative grade point average in the graduation (/4.00)']


renamedict = {
    'STUDENT ID':'student_id',
    'Student Age': 'age' ,
    'Sex': 'sex' ,
    'Graduated high-school type': 'hs_type' ,
    'Scholarship type': 'scholarship_type' ,
    'Additional work': 'extra_work' ,
    'Regular artistic or sports activity': 'activities' ,
    'Do you have a partner': 'partner' ,
    'Total salary if available': 'salary' ,
    'Transportation to the university': 'transportation' ,
    'Accommodation type in Cyprus': 'accommodation' ,
    'Mother’s education': 'mom_education' ,
    'Father’s education': 'dad_education' ,
    'Number of sisters/brothers': 'siblings' ,
    'Parental status': 'parental_status' ,
    'Mother’s occupation': 'mom_occupation' ,
    'Father’s occupation': 'dad_occupation' ,
    'Weekly study hours': 'study_per_week' ,
    'Reading frequency': 'non_science_reading' ,
    'Reading frequency.1': 'science_reading' ,
    'Attendance to the seminars/conferences related to the department': 'conf_attendance' ,
    'Impact of your projects/activities on your success': 'activity_impact' ,
    'Attendance to classes': 'class_attendance' ,
    'Preparation to midterm exams 1': 'midterm_prep_company' ,
    'Preparation to midterm exams 2': 'midterm_prep_timing' ,
    'Taking notes in classes': 'note_taking' ,
    'Listening in classes': 'listening_in_class' ,
    'Discussion improves my interest and success in the course': 'discussion_effect_on_interest' ,
    'Flip-classroom': 'flip_classroom' ,
    'Course ID':'course_id',
    'Cumulative grade point average in the last semester (/4.00)': 'last_sem_grade'
}

full_df.rename(columns=renamedict, inplace = True)
full_df.set_index('student_id', inplace = True)

full_df.last_sem_grade = full_df.last_sem_grade.map(lambda x: (int)(x>3))


target_mapping={
    1: 0,
    2: 25,
    3: 50,
    4: 75,
    5: 100
}

full_df['scholarship_type'] = full_df['scholarship_type'].map(lambda x: target_mapping[x])

target_mapping={
    1:1,
    2:0
}
full_df.sex = full_df.sex.map(target_mapping)
full_df['extra_work'] = full_df['extra_work'].map(target_mapping)
full_df['activities'] = full_df['activities'].map(target_mapping)
full_df['partner'] = full_df['partner'].map(target_mapping)
full_df['conf_attendance'] = full_df['conf_attendance'].map(target_mapping)



target_mapping={
    1:'private',
    2:'state',
    3:'other'
}
full_df.hs_type = full_df.hs_type.map(target_mapping)

target_mapping={
    1:'not useful',
    2:'useful',
    3:'not applicable'
}
full_df.flip_classroom = full_df.flip_classroom.map(target_mapping)

target_mapping={
    1:'never',
    2:'sometimes',
    3:'always'
}
full_df.discussion_effect_on_interest = full_df.discussion_effect_on_interest.map(target_mapping)
full_df.listening_in_class = full_df.listening_in_class.map(target_mapping)
full_df.note_taking = full_df.note_taking.map(target_mapping)

target_mapping={
    1:'always',
    2:'sometimes',
    3:'never'
}
full_df.class_attendance = full_df.class_attendance.map(target_mapping)

target_mapping={
    1:'bus',
    2:'car',
    3:'bicycle',
    4:'other'
}
full_df.transportation = full_df.transportation.map(target_mapping)

target_mapping={
    1:'none',
    2:'sometimes',
    3:'often'
}
full_df.non_science_reading = full_df.non_science_reading.map(target_mapping)
full_df.science_reading = full_df.science_reading.map(target_mapping)


target_mapping={
    1: 'primary',
    2: 'secondary',
    3: 'high',
    4: 'uni',
    5: 'MSc',
    6: 'PhD'
}
full_df.mom_education = full_df.mom_education.map(target_mapping)
full_df.dad_education = full_df.dad_education.map(target_mapping)

target_mapping={
    1:'rental',
    2:'dorm',
    3:'family',
    4:'other'
}
full_df.accommodation = full_df.accommodation.map(target_mapping)

target_mapping={
    1:'very_young',
    2:'young',
    3:'old'
}
full_df.age = full_df.age.map(target_mapping)

target_mapping={
    1:'alone',
    2:'friends',
    3:'NA'
}
full_df.midterm_prep_company = full_df.midterm_prep_company.map(target_mapping)

target_mapping={
    1:'late',
    2:'regularly',
    3:'never'
}
full_df.midterm_prep_timing = full_df.midterm_prep_timing.map(target_mapping)

target_mapping={
    1:'none',
    2:'five', #or less
    3:'ten',  #or less
    4:'twenty', #or less
    5:'more' #more than twenty
}
full_df.study_per_week = full_df.study_per_week.map(target_mapping)

target_mapping={
    1:'married',
    2:'divorced',
    3:'died'
}
full_df.parental_status = full_df.parental_status.map(target_mapping)

target_mapping={
    1:'positive',
    2:'negative',
    3:'neutral'
}
full_df.activity_impact = full_df.activity_impact.map(target_mapping)

target_mapping={
    1: 'retired',
    2: 'housewife',
    3: 'government_officer',
    4: 'private_sector',
    5: 'self-employment',
    6: 'other'
}
full_df.mom_occupation = full_df.mom_occupation.map(target_mapping)

target_mapping={
    1: 'retired',
    2: 'government_officer',
    3: 'private_sector',
    4: 'self-employment',
    5: 'other'
}
full_df.dad_occupation = full_df.dad_occupation.map(target_mapping)

target_mapping={
    1: 'very_low', # 135-200 USD
    2: 'low', # 201-270 USD
    3: 'medium', # 271-340 USD
    4: 'high', # 341-410 USD
    5: 'higher' # >410 USD
}
full_df.salary = full_df.salary.map(target_mapping)


target_mapping={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'more_than_four'
}
full_df.siblings = full_df.siblings.map(target_mapping)


df_full_train, df_test = train_test_split(full_df, test_size=0.2, random_state=rnd_seed)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.last_sem_grade.values
y_test = df_test.last_sem_grade.values


del df_full_train['last_sem_grade']
del df_test['last_sem_grade']

dv = DictVectorizer(sparse=False)

train_dict = df_full_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)
dt = DecisionTreeClassifier(max_depth=5, min_samples_leaf=16, random_state=rnd_seed)
dt.fit(X_train, y_full_train)

output_file = 'tree.bin'

with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, dt), f_out)
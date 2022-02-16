import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("output/input.csv")

data['cancer_date'] = pd.to_datetime(data['cancer_date'])

def time(x):
    if (x < pd.to_datetime('2020-03-23')):
        return 0
    else:
        return 1

def age_group(x):
    if (x < 20):
        return "0-19"
    elif (x >= 20) & (x < 30):
        return "20-29"
    elif (x >= 30) & (x < 40):
        return "30-39"
    elif (x >= 40) & (x < 50):
        return "40-49"
    elif (x >= 50) & (x < 60):
        return "50-59"
    elif (x >= 60) & (x < 70):
        return "60-69"
    elif (x >= 70) & (x < 80):
        return "70-79"
    elif (x >= 80) & (x < 90):
        return "80-89"
    elif (x >= 90):
        return "90+"

data['time'] = data['cancer_date'].apply(time)

data['age_group'] = data['age'].apply(age_group)

data_pre_covid = data[data['time'] == 0]
data_post_covid = data[data['time'] == 1]

pre_covid_freq = data_pre_covid['age_group'].value_counts().to_dict()
post_covid_freq = data_post_covid['age_group'].value_counts().to_dict()

pre_covid_keys = pre_covid_freq.keys()
pre_covid_values = pre_covid_freq.values()

post_covid_keys = post_covid_freq.keys()
post_covid_values = post_covid_freq.values()

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.bar(pre_covid_keys, pre_covid_values)
ax2.bar(post_covid_keys, post_covid_values)

ax.set_xlabel('Ages')
ax.set_ylabel('Frequency')

ax1.set_title('Pre Covid')
ax2.set_title('Post Covid')

plt.savefig('output/cancer_by_age.jpg')
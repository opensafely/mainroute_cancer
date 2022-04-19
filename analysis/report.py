import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("output/input_referral.csv")

data2 = pd.read_csv("output/input_symptom.csv")

data['colorectal_referral_date'] = pd.to_datetime(data['colorectal_referral_date'])

data2['colorectal_symptom_date'] = pd.to_datetime(data2['colorectal_symptom_date'])

def time(x):
    return x - pd.to_datetime('2020-03-23')

data['colorectal_referral_time'] = data['colorectal_referral_date'].apply(time)

data2['colorectal_symptom_time'] = data2['colorectal_symptom_date'].apply(time)

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.hist(data['colorectal_referral_time'].astype('timedelta64[D]').to_numpy(), bins = 24)
ax2.hist(data2['colorectal_symptom_time'].astype('timedelta64[D]').to_numpy(), bins = 24)

ax.set_xlabel('Time')
ax.set_ylabel('Frequency')

ax1.set_title('Referrals')
ax2.set_title('Symptom presentations')

plt.savefig('output/colorectal_cancer.jpg')
import pandas as pd

institutes = pd.read_csv('institutes.csv')
users = pd.read_csv('user.csv')
notifications = pd.read_csv('notifications.csv')

dict_users = users.set_index('user_id')['user_email'].to_dict()
dict_institutes = institutes.set_index('institute_id')['institute_abbreviation'].to_dict()
users_3 = []
institutes_3 = []

for index, row in notifications.iterrows():
    users_1 = (str(row[1]))
    users_1 = users_1.split(',')
    for item in users_1:
        user_2 = dict_users.get(item)
        users_3.append(user_2)
    users_3 = str(users_3)
    users_3 = users_3.replace("[", "").replace("]", "").replace("[]", "").replace("'", "")
    notifications.at[index, 'users_email'] = str(users_3)
    users_3 = []
    institutes_1 = (str(row[3]))
    institutes_1 = institutes_1.split(',')
    for item in institutes_1:
        institutes_2 = dict_institutes.get(item)
        institutes_3.append(institutes_2)
    institutes_3 = str(institutes_3)
    institutes_3 = institutes_3.replace("[", "").replace("]", "").replace("[]", "").replace("'", "")
    notifications.at[index, 'institutes'] = str(institutes_3)
    institutes_3 = []
notifications.to_csv('notifications_result.csv', index=False)

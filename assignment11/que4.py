import pandas as pd
import random
party = pd.DataFrame({'days':range(1,11),
                      'John':[random.choice(["Yes","No"]) for _ in range(1,11)],
                      'Judy':[random.choice(["Yes","No"]) for _ in range(1,11)]})
can_party = [i for i in range(10) if party['John'][i]=='Yes' and party['Judy'][i]=='Yes']
print(can_party)
days=[]
for i in range(10):
    for j in can_party:
        if j>=i:
            days.append(j-i)
            break
    else:
        days.append(None)
party['days_till_party'] = days
print(party)
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

big_total = []
builds = [10, 15, 30, 50, 75, 100]

for build in builds:
    with open('number_of_builds_{0}.json'.format(build)) as json_data:
        d = json.load(json_data)
        big_total.append({"execution": str(build), "duration": float(d['total average duration']),
                          "errors": int(d['total number of errors'])})

# df = pd.DataFrame(big_total)
# print (df)

fig, ax1 = plt.subplots()
y1 = [y["duration"] for y in big_total]
y2 = [int(y["errors"]) for y in big_total]

ax2 = ax1.twinx()
ax1.plot(builds, y1, 'g-')
ax2.plot(builds, y2, 'b-')

ax1.set_xlabel('Number of Iterations')
ax1.set_ylabel('Average duration', color='g')
ax2.set_ylabel('Total Errors', color='b')


# df.plot(x='execution', y='data')
plt.ylim (ymin=0)
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

col_count = 3
bar_width = 0.2

indian_score = (554, 536, 538)
canada_score = (518, 523, 525)
china_score = (613, 570, 580)
ireland_score = (495, 505, 499)

index = np.arange(col_count)


def create_label(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 4, height+1, "%d" % int(height))
    return


i1 = plt.bar(index, indian_score, bar_width, alpha=.4, label="India")
c1 = plt.bar(index + 0.2, canada_score, bar_width, alpha=.4, label="Canada")
ch1 = plt.bar(index + 0.4, china_score, bar_width, alpha=.4, label="China")
ir1 = plt.bar(index + 0.6, ireland_score, bar_width,alpha=.4, label="Ireland")

plt.legend(frameon=False, bbox_to_anchor=(1, 1), loc=2)    # to display labels as Card Board

create_label(i1)
create_label(c1)
create_label(ch1)
create_label(ir1)

plt.xticks(index + .6 / 2, ("Mathematics", "Reading", "Science"))  # to move x-axis value
                            #to middle of bars and tubles is labels in x-axis

plt.ylabel("Mean Score of PISA in 2012")
plt.xlabel("Subjects")
plt.title("Test Scores by country")
plt.grid(True)

plt.show()

'''
+++ This is to show pie chart using pandas +++
raw_data = {"Names": ["Harshith", "Steve Jobs", "Elon Musk", "Arya bhatta"],
            "jan_ir": [134, 120, 184, 167],
            "feb_ir": [122, 150, 146, 138],
            "mar_ir": [140, 168, 175, 124]}

df = pd.DataFrame(raw_data, columns=["Names", "jan_ir", "feb_ir", "mar_ir"])

df["total"] = df["jan_ir"] + df["feb_ir"] + df["mar_ir"]

color = [(1, 0.4, 0.4), (0.4, 1, 0.4), (0.4, 0.4, 1), (0.7, 0.7, 0.7), (0.3, 0.1, 0.2)]
plt.pie(df["total"],    # data to pie
        labels=df["Names"],     # Names of pie Values
        colors=color,           # Color of  pie Values
        autopct="%1.1f%%")      # to display percentages

plt.axis("equal")   # to maintain correct aspect ratio in piechart

plt.show()

print(df)
'''

'''
++ This is for Pie Chart using matplotLib +++ 
lanInTech = ['python', 'c++', 'Ruby', 'java', 'Php', 'perl']
sizeOfTechies = [33, 52, 12, 17, 62, 48]
separated = (0.4, 0, 0, 0, 0, 0)
plt.pie(sizeOfTechies, labels=lanInTech, autopct="%1.1f%%", explode=separated)
plt.show()
'''
'''
+++ This is for Graph with multiple lines +++
import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7,
          2.9, 3.0, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3]

#plt.plot(years, deaths,":" , color=(0.6, 0.6, 1))
#plt.plot(years, pops, color=(255/255, 100/255, 100/255))

plt.grid(True)
lines = plt.plot(years, pops, years, deaths)
plt.setp(lines, color=(0.6, 0.6, 1), marker="+")

plt.ylabel("Population in Billions")
plt.xlabel("Population growth in Years")
plt.title("Population Growth")

plt.show()'''
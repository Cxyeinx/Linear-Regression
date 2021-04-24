import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use("ggplot")


def mean(lst):
    return sum(lst) / len(lst)


def slope(xs, ys):
    m = ( (mean(xs) * mean(ys)) - (mean(xs * ys)) ) / ( (mean(xs) ** 2) - (mean(xs ** 2)) )
    b = mean(ys) - (m * mean(xs))
    return m, b


df = pd.read_csv("salary_data.xls")


df.head()


plt.scatter(df["YearsExperience"], df["Salary"])
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Years of Experience")


xs = np.array(df["YearsExperience"])
ys = np.array(df["Salary"])


m, b = slope(xs, ys)


regression_line = [(m*x)+b for x in xs]


plt.scatter(df["YearsExperience"], df["Salary"])
plt.plot(df["YearsExperience"], regression_line, color="b")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Years of Experience")




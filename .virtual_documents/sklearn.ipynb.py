from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")


df = pd.read_csv("salary_data.xls")


df.head()


plt.scatter(df["YearsExperience"], df["Salary"])


xs = np.array(df["YearsExperience"])
xs = np.expand_dims(xs, axis=-1)
ys = np.array(df["Salary"])
ys = np.expand_dims(ys, axis=-1)


reg = LinearRegression()
reg.fit(xs, ys)
regression_line = reg.predict(xs)


plt.scatter(df["YearsExperience"], df["Salary"])
plt.plot(df["YearsExperience"], regression_line, color="b")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Years of Experience")




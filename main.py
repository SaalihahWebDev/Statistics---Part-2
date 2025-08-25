import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data={
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Temperature":[5,6,9,12,16,19,22,21,18,14,9,6],
    "Rainfall":[55,40,45,43,50,55,60,65,55,70,65,60]
}

df=pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.barplot(x="Month",y="Temperature",data=df,color="pink",label="Temperature(C)")
plt.ylabel("Average Temperature")
plt.title("Average Monthly temperature in London")
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
plt.bar(df["Month"],df["Rainfall"],color="lightgreen",label="Rainfall(mm)")
plt.ylabel("Average Rainfall")
plt.title("Average Monthly rainfall in london")
plt.legend()
plt.show
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Height = [150, 155, 160, 165, 170, 175, 180, 185]
Weight = [50, 53, 56, 60, 65, 68, 72, 78]
df = pd.DataFrame({
    "Height": Height,
    "Weight": Weight
})
print (df)

x_mean =  df["Height"].mean()
y_mean =  df["Weight"].mean()
print("X mean =", x_mean)
print("Y mean =", y_mean)

numerator = ( (df["Height"]-x_mean)*
              (df["Weight"]-y_mean)).sum()
denominator = ((df["Height"]-x_mean)**2).sum()
b1 = numerator /denominator 

#intercept
b0 = y_mean - b1 * x_mean

print("Slope =", b1)
print("Intercept =", b0)

#Prediction
df["Predicted"] = b0 + b1 * df["Height"]

print(df)
sns.scatterplot(data=df, x="Height", y="Weight")
sns.lineplot(
    data=df,
    x="Height",
    y="Predicted"
)

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Linear Regression")
plt.show()

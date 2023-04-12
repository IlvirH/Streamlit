import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'

tips = pd.read_csv(path)
tips.drop(columns=['Unnamed: 0'], inplace=True)

st.write("""
### Данный график показывает *размер дневной выручки ресторана* 
""")

fig, ax = plt.subplots()
sns.histplot(data=tips, x='total_bill')
st.pyplot(fig)

st.write("""
### График показывает **стоимость заказа** по шкале *Х*
### и **размер чаевых** по шкале *у*
""")

fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip')
st.pyplot(fig)

st.write("""
### Cвязь между днем недели и размером счета
""")

fig, ax = plt.subplots()
sns.barplot(data=tips, x='day', y='total_bill', estimator=np.sum)   
st.pyplot(fig)


st.write("""
### На графике указан размер чаевых 
### по дням недели среди мужщин и женщин
""")

fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='tip', y='day', hue='sex', size= 'sex', sizes=[50,100])
st.pyplot(fig)

fig, ax = plt.subplots()
sns.boxplot(data=tips, x="total_bill", y="day", hue='time')
st.pyplot(fig)

st.write("""
### Сумма чаевых за обед и за ужин
""")

sc = sns.FacetGrid(tips, col="time")
sc.map_dataframe(sns.histplot, 'tip')
st.pyplot(sc)

st.write("""
### Сумма чаевых за обед и за ужин
""")


sc = sns.FacetGrid(tips, col="sex", hue="smoker")
sc.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
st.pyplot(sc)

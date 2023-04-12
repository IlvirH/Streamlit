import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'

tips = pd.read_csv(path)
# tips.drop(columns=['Unnamed: 0'], inplace=True)

st.title("""
                      
**В данном проекте отображены дневные доходы и размер чаевых для разных категорий посетителей кафе 'PlutO'** 

""")

# st.write("""
# **размер дневной выручки ресторана** 
# """)
fig, ax = plt.subplots()
sns.histplot(data=tips, x='total_bill')
ax.set_xlabel('Доход')
ax.set_ylabel('Количество в тыс. руб.')
ax.set_title('размер дневной выручки ресторана')
ax.grid(axis='y')
st.pyplot(fig)



st.write("""

Визуализация суммы заказа и размер оставленных чаевых от каждого столика

""")

fig, ax = plt.subplots(figsize=(10,8))
sns.scatterplot(data=tips, x='total_bill', y='tip', size='size', sizes=list(np.arange(10,61,10)))
ax.set_title('Визуализация суммы заказа и размер чаевых \
             в зависимости от количества человек ')
ax.set_xlabel('Доход')
ax.set_ylabel('Количество в тыс. руб.')
ax.legend(markerfirst=False, fontsize='x-small')
st.pyplot(fig)


st.write("""
Общая сумма заказов по дням недели рабочего графика кафе
""")

fig, ax = plt.subplots()
sns.barplot(data=tips, x='day', y='total_bill', estimator=np.sum)   
st.pyplot(fig)


st.write("""
Размер чаевых по дням недели работы заведения, оставленных посетителями разделенных по полу.
""")

fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='tip', y='day', hue='sex', size= 'sex', sizes=[50,100])
st.pyplot(fig)

st.write("""
Ящик с усами отобращающий сумму всех счетов за обед и ланч по дням недели рабочего графика кафе 
""")

fig, ax = plt.subplots()
sns.boxplot(data=tips, x="total_bill", y="day", hue='time')
st.pyplot(fig)

st.write("""
Сумма чаевых за обед и за ужин по рабочим дням кафе. Слева чаевые за обед, справа чаевые за ланч
""")

sc = sns.FacetGrid(tips, col="time")
sc.map_dataframe(sns.histplot, 'tip')
st.pyplot(sc)

st.write("""
Диаграммы рассеивания показывающие связь размера счета и чаевых 
среди мужщин и женщин, разделенных также на курящих и не курящих.
Слева для показаны статистика для женщин, справа для мужщин
""")


sc = sns.FacetGrid(tips, col="sex", hue="smoker")
sc.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
st.pyplot(sc)

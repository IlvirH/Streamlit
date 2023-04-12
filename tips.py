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
# **** 
# """)


fig, ax = plt.subplots(figsize=(10,8))
sns.histplot(data=tips, x='total_bill')
ax.set_xlabel('Стоимость заказа (счета) ($)')
ax.set_ylabel('Количество заказов (счётов)')
ax.set_title('Количество заказов определенного диапазона их стоимости')
ax.grid(axis='y')
st.pyplot(fig)



# st.write("""
# Визуализация суммы заказа и размер оставленных чаевых от каждого столика
# """)


fig, ax = plt.subplots(figsize=(10,8))
sns.scatterplot(data=tips, x='total_bill', y='tip')
ax.set_title('Отношение размера чаевых к сумме счёта')
ax.set_xlabel('Стоимость счета ($)')
ax.set_ylabel('Размер чаевых ($)')
st.pyplot(fig)


# st.write("""
# Общая сумма заказов по дням недели
# """)


fig, ax = plt.subplots(figsize=(10,8))
sns.barplot(data=tips, x='day', y='total_bill', estimator=np.sum)
ax.set_xlabel('Дни недели')
ax.set_ylabel('Сумма ($)')
ax.set_title('Общая сумма счётов за день')
ax.grid(axis='y') 
st.pyplot(fig)


# st.write("""
# Размер чаевых по дням недели работы заведения, оставленных посетителями разделенных по полу
# """)


fig, ax = plt.subplots(figsize=(10,8))
sns.scatterplot(data=tips, x='tip', y='day', hue='sex', size= 'sex', sizes=[50,100])
ax.set_xlabel('Размер чаевых ($)')
ax.set_ylabel('День недели')
ax.set_title('Распределение чаевых по дням оплаченные мужчинами и женщинами')
ax.legend(markerfirst=False, fontsize='x-small')
ax.grid(axis='x')
st.pyplot(fig)


# st.write("""
# Визуализация распределения счётов
# """)


fig, ax = plt.subplots(figsize=(10,8))
sns.boxplot(data=tips, x="total_bill", y="day", hue='time')
ax.set_xlabel('Стоимость ($)')
ax.set_ylabel('День недели')
ax.set_title('Распределение счётов по стоимости за день')
ax.legend(markerfirst=False, fontsize='x-small')
ax.grid(axis='x')
st.pyplot(fig)


st.write("""
Сумма чаевых за обед и за ужин по рабочим дням кафе. Слева чаевые за обед, справа чаевые за ланч
""")

sc = sns.FacetGrid(tips, col="time")
sc.map_dataframe(sns.histplot, 'tip')
sc.set_xlabels('Размер ($)')
sc.set_ylabels('Количество чаевых')
st.pyplot(sc)


st.write("""
Диаграммы рассеяния показывающие связь размера счета и чаевых 
среди мужщин и женщин, разделенных также на курящих и не курящих.
Слева график со статистикой для женщин, справа для мужщин
""")


sc = sns.FacetGrid(tips, col="sex", hue="smoker")
sc.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
sc.set_xlabels('Сумма счёта ($)')
sc.set_ylabels('Чаевые ($)')
sc.add_legend()
st.pyplot(sc)

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
                      
**В данном проекте отображены суммы счётов и размер чаевых разных категорий посетителей** 

""")

st.write("""
Гистограмма отображает количество счетов в определенном интервале стоимости. 
Минимальное и максимальное значения около 4$ и 50$ соответственно, 
наиболее частая (более половины) стоимость счёта в интервале 10-23 $.
Количество счётов от 4$ до 10$ значительно меньше, чем количество от 23$ до 50$.
Среднее значение стоимости счёта находится в интервале 10-23$ ближе к максимальному, 
медианное значение ниже среднего.
""")


fig, ax = plt.subplots(figsize=(10,8))
sns.histplot(data=tips, x='total_bill')
ax.set_xlabel('Стоимость заказа (счета) ($)')
ax.set_ylabel('Количество заказов (счётов)')
ax.set_title('Количество заказов определенного интервала их стоимости')
ax.grid(axis='y')
st.pyplot(fig)



st.write("""
Диаграмма рассеяния показывает имеющуюся прямую зависимость размера чаевых
от стоимости счёта, на отрезке 10-25$ за счёт
""")


fig, ax = plt.subplots(figsize=(10,8))
sns.scatterplot(data=tips, x='total_bill', y='tip')
ax.set_title('Отношение размера чаевых к сумме счёта')
ax.set_xlabel('Стоимость счета ($)')
ax.set_ylabel('Размер чаевых ($)')
st.pyplot(fig)


st.write("""
На данной гистограмме увидим, что суммы счётов за субботу и воскресенье, каждые,
почти в 1,5 раза превышают уровень четверга и в 6-7 раз превосходят уровень пятницы.
""")


fig, ax = plt.subplots(figsize=(10,8))
sns.barplot(data=tips, x='day', y='total_bill', estimator=np.sum)
ax.set_xlabel('Дни недели')
ax.set_ylabel('Сумма ($)')
ax.set_title('Общая сумма счётов за день')
ax.grid(axis='y') 
st.pyplot(fig)


st.write("""
На данном графике видно, что в четверг количество чаевых от женщин
намного больше чем от мужчин, в воскрсенье ситуация обратная. 
Максимальные размеры чаевых за день всегда оплачиваются мужщинами.
Значительное преобладание размера чаевых в диапазоне 1-4$
""")


fig, ax = plt.subplots(figsize=(10,8))
sns.scatterplot(data=tips, x='tip', y='day', hue='sex', size= 'sex', sizes=[50,100])
ax.set_xlabel('Размер чаевых ($)')
ax.set_ylabel('День недели')
ax.set_title('Распределение чаевых по дням оплаченные мужчинами и женщинами')
ax.legend(markerfirst=False, fontsize='x-small')
ax.grid(axis='x')
st.pyplot(fig)


st.write("""
Ящик с усами. По данной диаграмме можно видеть, что средние значения 
практически всех дней в диапазоне 16-20$. Имеются выбросы максимальных значений
в четверг, субботу и воскресенье
""")


fig, ax = plt.subplots(figsize=(10,8))
sns.boxplot(data=tips, x="total_bill", y="day", hue='time')
ax.set_xlabel('Стоимость ($)')
ax.set_ylabel('День недели')
ax.set_title('Распределение счётов по стоимости за день')
ax.legend(markerfirst=False, fontsize='x-small')
ax.grid(axis='x')
st.pyplot(fig)


st.write("""

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

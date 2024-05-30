import pandas as pd
import matplotlib.pyplot as plt


# 1. Загрузите базу данных из файла Titanic.csv.
df = pd.read_csv("Titanic.csv")


# 2. Загрузите базу данных так из файла еще раз, но так, чтобы столбец PassengerId был
# идентификатором, то есть номером строки (index).
df = pd.read_csv("Titanic.csv", index_col=0)


# 3. Удалите из базы строки с пропущенными значениями и сохраните изменения в самой базе.
df = df.dropna()


# 3 Выведите сводную информацию по базе данных: какие переменные в ней есть,
# какого они типа + сколько заполненных наблюдений в каждой столбце.
df.info()


# 4 Выведите сводную статистическую информацию по каждому количественному показателю в базе
# (описательные статистики).
print(df.describe())


# 5. Постройте гистограмму для переменной Возраст (Age), сделайте ее красного цвета, подпишите оси
# и добавьте заголовок графика
df["Age"].plot.hist(color="red")
plt.title("Гистограмма для переменной Возраст")
plt.xlabel("Возраст")
plt.ylabel("Количество человек")
plt.show()


# 6. Выведите описательные статистики для столбца Стоимость билета (Fare).
print(df["Fare"].describe())


# 7. Выведите названия столбцов в базе данных в виде списка (объект типа list).
list_columns = list(df.columns)
print(list_columns)


# 8. Переименуйте столбец с классом пассажира из Pclass в Class.
cols = list(df.columns)
cols[2] = "Class"
df.columns = cols


# 9. Выберите из базы данных все строки, которые соответствуют пассажирам женского пола, и
# сохраните их в новую базу female
female = df[df["Sex"] == "female"]
female.to_csv("female.csv")


# 10. Выберите из базы данных все строки, которые соответствуют выжившим пассажирам мужского пола
# младше 32 лет, и сохраните их в базу Ymale.
y_male = df[(df["Sex"] == "male") & (df["Age"] < 32)]
y_male.to_csv("y_male.csv")


# 11. Выберите из базы данных все строки, которые соответствуют пассажирам 1 или 2 класса.
f_class = df[(df["Class"] == 1) | (df["Class"] == 2)]
print(f_class)


# 12. Выберите из базы данных все строки, которые соответствуют выжившим пассажирам 1 или 2 класса.
f_s_class_survive = df[((df["Class"] == 1) | (df["Class"] == 2)) & (df["Survived"] == 1)]
print(f_s_class_survive)


# 13. Добавьте в датафрейм столбец Female, состоящий из значений 0 и 1, где 1 соответствует
# пассажирам женского пола.
add_list = list(df["Sex"] == "female" if 1 else 0)
df['Female'] = add_list
df['Female'] = df['Female'].astype(int)
print(df)


# Группировка
# 1. Выведите на экран все уникальные значения в столбце Embarked.
print(df["Embarked"].unique())


# 2. Сгруппируйте строки в датафрейме в соответствии со значениями переменной Survived и выведите
# средние значения всех количественных переменных по группам.
print(df.groupby(["Survived"]).mean(numeric_only=True))


# 3. Сгруппируйте строки в датафрейме в соответствии со значениями переменной Sex и сохраните в
# отдельный датафрейм таблицу со средними и медианными значениями переменной Age по группам
# (мужчины и женщины).
group_df = df.groupby(["Sex"])
mean_df = group_df.Age.mean()
median_df = group_df.Age.median()
print(mean_df)
print(median_df)


# Выгрузка базы в файл
# 1. Приведите все названия столбцов в датафрейме к нижнему регистру и сохраните изменения.
new_cols = [col.lower() for col in list(df.columns)]
df.columns = new_cols
print(df.columns)


# 2. Выгрузите итоговый датафрейм в файл Titanic-new.csv
df.to_csv(r"Titanic-new.csv", index=True, sep=";")


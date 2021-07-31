import pandas as pd
import plotly.express as px
import plotly.io as pio


data = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")
data=data[(data.location=="Japan")]
data=data.fillna(0)
data=data.drop(columns=["location","iso_code",
     "total_vaccinations_per_hundred","people_vaccinated_per_hundred","people_fully_vaccinated_per_hundred","daily_vaccinations_per_million"])
data=data[(data['date'] > '2021-04-01')]

population=126300000
# pd.set_option("display.max.columns", None)
# newdf=data[(data.location=="Japan")]
# rc=newdf.drop(columns=["total_cases","total_deaths",
#     "weekly_cases","biweekly_cases","weekly_deaths","biweekly_deaths","new_deaths"])
data['percentage_vacinated'] = data['people_vaccinated']/population*100
data['moving_daily_average_vac'] = data["daily_vaccinations_raw"].rolling(window=7).mean()
print(data.tail(20))
# rc=rc[(rc['date'] > '2020-11-01')]
# # rc=rc.drop(rc.columns[0], axis=1)
fig = px.line(data, x = 'date', y = 'people_vaccinated',labels={
                     "date": "Date",
                     " people_vaccinated": "People vacinated"
                 }, title='Total Vacinations - Japan')
fig.update_layout(
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green"
)
fig.update_xaxes(title_font_family="Arial")
fig.show()

fig = px.line(data, x = 'date', y = 'moving_daily_average_vac',labels={
                     "date": "Date",
                     "moving_daily_average_vac": "Daily Vaccinations"
                 }, title='Daily Vacinations - Japan')
fig.layout.template ="seaborn"
fig.show()
pio.write_html(fig, file="index.html", auto_open=True)


# new=rc[(rc['date'] > '2020-11-01')]
# print(new.head())

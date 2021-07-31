import pandas as pd
import plotly.express as px

data = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/full_data.csv")
#print(data.head())
pd.set_option("display.max.columns", None)
newdf=data[(data.location=="Japan")]
rc=newdf.drop(columns=["total_cases","total_deaths",
	"weekly_cases","biweekly_cases","weekly_deaths","biweekly_deaths","new_deaths"])
rc['moving_daily_average'] = rc.rolling(window=7).mean()
rc=rc.fillna(0)
rc=rc[(rc['date'] > '2020-11-01')]
# print(newdf.head())
# rc=rc.drop(rc.columns[0], axis=1)
# print(rc.tail())
fig = px.line(rc, x = 'date', y = 'moving_daily_average',labels={
                     "date": "Date",
                     "moving_daily_average": "Daily 7 Day Moving Average"
                 }, title='New Covid Cases - Japan')
fig.update_layout(
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green"
)
fig.update_xaxes(title_font_family="Arial")
fig.show()

# new=rc[(rc['date'] > '2020-11-01')]
# print(new.head())

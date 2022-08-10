# Importing Modules
import csv
import plotly.express as px

# Reading The CSV
rows = []
with open("main.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

# Reading The Headers And The Rows
headers = rows[0]
planet_data_rows = rows[1:]

# Extracting Planet Mass, Planet Radius And Planet Names
planet_mass = []
planet_radius = []
planet_name = []
for planet_data in planet_data_rows:
    planet_mass.append(planet_data[3])
    planet_radius.append(planet_data[4])
    planet_name.append(planet_data[1])

# Claculating The Gravity Of All Planets
planet_gravity = []
for index, name in enumerate(planet_name):
    gravity = (float(planet_mass[index])*1.989e+30) / (float(planet_radius[index])*float(planet_radius[index])*6.957e+8*6.957e+8) * 6.674e-11
    planet_gravity.append(gravity)

# Sorting All The Lists
planet_mass.sort()
planet_radius.sort()
planet_gravity.sort()

# Plotting A Bar Graph With Planet Names And Their Gravity
fig = px.scatter(x=planet_name, y=planet_gravity)
fig.layout.update({
    "title": "Planets With Their Gravity",
    "xaxis": {"title": "Planet Names"},
    "yaxis": {"title": "Planet Gravity"},
})
fig.show()

# Creating Charts
# Charts Of Mass And Radius Of The Planets With Respect To Gravity
fig = px.scatter(x=planet_mass, y=planet_radius, color=planet_gravity, hover_name=planet_name)
fig.layout.update(
    coloraxis_colorbar=dict(
        title="Gravity",
    )
)
fig.layout.update({
    "title": "Mass And Radius Of The Planets With Respect To Gravity",
    "xaxis": {"title": "Mass"},
    "yaxis": {"title": "Radius"},
})
fig.show()

# Charts Of Mass And Gravity Of The Planets With Respect To Radius
fig = px.scatter(x=planet_mass, y=planet_gravity, color=planet_radius, hover_name=planet_name)
fig.layout.update(
    coloraxis_colorbar=dict(
        title="Radius",
    )
)
fig.layout.update({
    "title": "Mass And Gravity Of The Planets With Respect To Radius",
    "xaxis": {"title": "Mass"},
    "yaxis": {"title": "Gravity"},
})
fig.show()

from scipy.io import loadmat
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

data = loadmat('GRDC.mat.nosync')
riviere=data['q4213440']


"Carte de la station"
lat=riviere[0][0][5][0][0]
long=riviere[0][0][6][0][0]


states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')


ax = plt.axes(projection=ccrs.PlateCarree())
plt.title('North Saskatchewan river \n PRINCE ALBERT station')
ax.set_extent([long-10, long+10, lat-10, lat+10], ccrs.PlateCarree())
plt.plot(long, lat,  markersize=2, marker='o', color='red')
ax.coastlines(resolution='110m')
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, )
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)
ax.add_feature(states_provinces, edgecolor='gray',linestyle=':')
ax.text(long,lat+2.5 , 'Saskatchewan ', color='k', size=10, ha='center', va='center', transform=ccrs.PlateCarree())
ax.text(long+7.5,lat+2.5 , 'Manitoba ', color='k', size=10, ha='center', va='center', transform=ccrs.PlateCarree())
ax.text(long-7.5,lat+2.5 , 'Alberta ', color='k', size=10, ha='center', va='center', transform=ccrs.PlateCarree())

plt.savefig('map.png')
plt.show()



"Donnée de la station"
dict={}
# list_date=[]
# list_valeur=[]
# for i in range(len(riviere[0][0][13])):
#     date=datetime.date(year=riviere[0][0][13][i][0],month=riviere[0][0][14][i][0],day=riviere[0][0][15][i][0])
#     value=riviere[0][0][16][i][0]
#     dict.update({f'{date}':value})
#     list_date.append(date)
#     list_valeur.append(value)
#

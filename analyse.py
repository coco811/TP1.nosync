from scipy.io import loadmat
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import pandas as pd
data = loadmat('GRDC.mat.nosync')
riviere=data['q4213440']


"Carte de la station"
lat=riviere[0][0][5][0][0]
long=riviere[0][0][6][0][0]
#
#
# states_provinces = cfeature.NaturalEarthFeature(
#         category='cultural',
#         name='admin_1_states_provinces_lines',
#         scale='50m',
#         facecolor='none')
#
#
# fig = plt.figure(figsize=(10,10))
# ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
# plt.title('North Saskatchewan river \n Prince Albert station')
# ax.set_extent([long-10, long+10, lat-10, lat+10], ccrs.PlateCarree())
# plt.plot(long, lat,  markersize=2, marker='o', color='red')
# ax.coastlines(resolution='110m')
# ax.add_feature(cfeature.LAND)
# ax.add_feature(cfeature.OCEAN)
# ax.add_feature(cfeature.COASTLINE)
# ax.add_feature(cfeature.BORDERS, )
# ax.add_feature(cfeature.LAKES, alpha=0.5)
# ax.add_feature(cfeature.RIVERS)
# ax.add_feature(states_provinces, edgecolor='gray',linestyle=':')
# ax.text(long,lat+2.5 , 'Saskatchewan ', color='k', size=10, ha='center', va='center', transform=ccrs.PlateCarree())
# ax.text(long+7.5,lat+2.5 , 'Manitoba ', color='k', size=10, ha='center', va='center', transform=ccrs.PlateCarree())
# ax.text(long-7.5,lat+2.5 , 'Alberta ', color='k', size=10, ha='center', va='center', transform=ccrs.PlateCarree())
# text = AnchoredText('Prince Albert station \nNorth Saskatchewan river \n131000.0 km$^2$  ',loc='center left',bbox_to_anchor=(550, 450), prop={'size': 8},frameon=True)
# ax.add_artist(text)
#
# plt.savefig('map.png')
# plt.show()



"Donnée de la station"
dict={}
list_date=[]
list_jour=[]
list_valeur=[]

for i in range(len(riviere[0][0][13])):
    date=datetime.date(year=riviere[0][0][13][i][0],month=riviere[0][0][14][i][0],day=riviere[0][0][15][i][0])
    value=riviere[0][0][16][i][0]


    if value == -999:
        dict.update({f'{date}': np.nan})
        list_date.append(date)
        list_jour.append(date.timetuple().tm_yday)
        list_valeur.append(np.nan)
    else:
        dict.update({f'{date}':value})
        list_date.append(date)
        list_jour.append(date.timetuple().tm_yday)
        list_valeur.append(value)

list_valeur_anne=[]
list_valeur_gen=[]
for i in range(len(list_date)-1):
    if list_date[i].year!=list_date[i+1].year:
        list_valeur_anne.append(list_valeur[i])
        list_valeur_gen.append(list_valeur_anne)
        list_valeur_anne = []
        pass
    else:
        list_valeur_anne.append(list_valeur[i])


#  194 on tombe en 1911
none=[np.nan]*(366-194)
list_valeur_gen[0]=none+list_valeur_gen[0]
for j in range(len(list_valeur_gen)):
    if len(list_valeur_gen[j])== 365:
        list_valeur_gen[j]=list_valeur_gen[j]+[np.nan]
    print(len(list_valeur_gen[j]))
mean=np.nanmean(np.array(list_valeur_gen),axis=0)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1, )

for i in range(len(list_valeur_gen)):
    x = np.linspace(1, len(list_valeur_gen[i]), len(list_valeur_gen[i]))
    plt.plot(x, list_valeur_gen[i], alpha=0.7, color='grey', linewidth=0.5)
    xmean = np.linspace(1, len(mean), len(mean))
    plt.plot(xmean, mean, alpha=1, color='k', linewidth=0.5)

plt.title('\n\nHydrogrammes\n\n',fontsize=20)

text2 = AnchoredText(f' Prince Albert station (4213440), North Saskatchewan river CA , 131000.0 km$^2$ \n $\quad$ $\qquad$ $\qquad$ $\qquad$  $\qquad$ $\qquad$ Latitude {lat:.2f} longitude {long:.2f}',loc='lower center',bbox_to_anchor=(0.5, 1.),bbox_transform=ax.transAxes, prop={'size': 10,'fontweight':"bold"},frameon=False)

ax.set_xlabel('Jour',fontsize=12)
ax.set_ylabel('Débit (m$^3$/s)',fontsize=12)
ax.set_xlim(0,366)
ax.set_ylim(0,6000)

ax.add_artist(text2)

plt.savefig('hydrogramme.png',)



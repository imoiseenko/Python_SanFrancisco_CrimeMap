import folium
import pandas as pd
df=pd.read_csv('Police.csv',index_col=False)
#df=df.set_index(['PdDistrict', 'IncidntNum'], inplace=True)
df=df.groupby(['PdDistrict'], as_index=False)['IncidntNum'].count()
df.rename(columns={"PdDistrict": "Neighborhood", "IncidntNum": "Count"}, inplace=True)

sf_map = folium.Map()
sf_map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)
sf_geo = r'san-francisco.geojson' # geojson file


sf_map.choropleth(
    geo_data=sf_geo,
    data=df,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='SF'
)


sf_map.save("SFmap.html")
from django.shortcuts import render
from django.views.generic.list import ListView

import plotly.graph_objs as go, pandas as pd, pdb, re, numpy as np
from plotly.offline import plot
from .models import Building

# Create your views here.

class BuildingList(ListView):
    model = Building
    paginate_by = 25
    template_name='index.html'

    def get_context_data(self, **kwargs):
    
        b_objs = pd.DataFrame(list(Building.objects.all().values()))  #filter(main_use=b_use,year=year)
        size_ser = b_objs['Floor_Area']
        size_ser.replace(np.nan,1000,inplace=True)
        #    pdb.set_trace()
        sizes=(2*np.log10(size_ser)).tolist()
        data = [
            go.Scattermapbox(
                lat=b_objs['lat'], lon=b_objs['lon'], mode='markers',
                marker=dict(size=sizes),
                name='mapbox 1', text=b_objs['Building_Name'],
                customdata=b_objs['link']
            )
        ]
        cent_lat=(b_objs['lat'].max()-b_objs['lat'].min())/2+b_objs['lat'].min()
        cent_lon=(b_objs['lon'].max()-b_objs['lon'].min())/2+b_objs['lon'].min()
        layout = go.Layout(hovermode='closest',
                           mapbox=dict(style='open-street-map',
                                       bearing=0, pitch=0, zoom=6,
                                       center=dict(lat=cent_lat,lon=cent_lon)
                                       )
                           )

        fig = go.Figure( data=data, layout=layout)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        plot_div = plot(fig, output_type='div', include_plotlyjs=True)
        res = re.search('<div id="([^"]*)"', plot_div)
        div_id = res.groups()[0]

        context=super().get_context_data(**kwargs)
        context['map_html'] = plot_div
        context['div_id'] = div_id
        return context


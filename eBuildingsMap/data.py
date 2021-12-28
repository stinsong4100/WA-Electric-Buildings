import django, pandas as pd, pdb, numpy as np

from eBmap.models import Building

kc_d = pd.read_excel('../eBuildings.xlsx')


buildings = []
for index, bdg in kc_d.iterrows():
    print(bdg['Building Name'],bdg['Floor Area (sq ft)'])
    if (~np.isfinite(bdg['Floor Area (sq ft)'])):
        bdg['Floor Area (sq ft)']=None
    building = Building(
        year = int(2021),
        Major = 0, #int(bdg[1]['Major']),
        Minor = 0, #int(bdg[1]['Minor']),
        BldgNbr = 0, #int(bdg[1]['BldgNbr']),
        Address = bdg['Address'],
        main_use = bdg['Building Type'],
        Number_of_Stories = 2, #int(bdg[1]['NbrStories']),
        Construction_Class = 0, #int(bdg[1]['ConstrClass']),
        Year_built = 2018, #int(bdg[1]['YrBuilt']),
        Year_remodeled = 2020, #int(bdg[1]['EffYr']),
        Building_Name = bdg['Building Name'],
        Space_heat_type = bdg['Space_heat_type'],
        Cook_type = bdg['Cook_type'],
        DHW_type = bdg['DHW_type'],
        City = bdg['City'],
        County = bdg['County'],
        Leg_District = bdg['Leg District'],
        Floor_Area = bdg['Floor Area (sq ft)'],
        Description = bdg['Description'],
        link = bdg['link'],
        img_link = bdg['img_link'],
        Architect = bdg['Architect'],
        Engineer = bdg['Engineer'],
        Builder = bdg['Builder'],
        lat = bdg['lat'],
        lon = bdg['lon'],    )
    buildings.append(building)

Building.objects.bulk_create(buildings)


import os
import shutil

path1 = '/home/alex/GLEMOS_UT/GLEMOS_v2.2/Input/Properties/PAH16_v2/'
path2 = '/home/alex/GLEMOS_UT/GLEMOS_v2.2/Input/Properties/'
media = ['Atm','Ocn','Soil','Veg']
pollutants = ['ACY','ANT','BaA','BbF','BghiP','BkF','CHR','DahA','FLA','FLO','IcdP','NAP','PHE','PYR']
grids = ['GLOB_3x3','GLOB_1x1','EMEP_04x04','EMEP_02x02']

for pollutant in pollutants:
    for med in media:
        filename1 = med+'_props_'+pollutant+'.dat'
        filepath1 = path1 + filename1
        for grid in grids:
            filename2 = med+'_props_'+grid+'_'+pollutant+'.dat'
            filepath2 = path2 + filename2
            shutil.copyfile(filepath1, filepath2)



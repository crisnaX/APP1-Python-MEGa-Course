
import os
import tkinter
from tkinter import *
from tkinter import ttk
import pandas
import folium
from tkinter import filedialog as fd
import pathlib

text1= ""
global lat


def path():
    global text1
    f= fd.askopenfilename()
    text1 = text1+f
    field.insert(0,text1)

class maps:
    def __init__(self,data,lat,lon,nam,elev,map,html,fga,fgc):
        self.data=data
        self.lat=lat
        self.lon=lon
        self.nam=nam
        self.elev=elev
        self.map=map
        self.fga=fga
        self.html=html




    def color_producer(self,elev):
        if elev >= 5000:
            return "pink"
        if elev >= 2000 and elev < 5000:
            return "purple"
        if elev >= 1000 and elev < 2000:
            return "blue"
        if elev < 1000 and elev>=1:
            return "lightgreen"
        else:
            return "darkred"

    def execute(self):
    
        

        for lt,ln,na,el in zip(lat,lon,nam,elev): 
            iframe=folium.IFrame(html=self.html % (na,na,lt,ln,el),width=200,height=100)
            fga.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe),icon=folium.Icon(color=self.color_producer(el))))


  

    

   

root = tkinter.Tk()
root.resizable(True,True)
root.title("Map_Data_Load")


open=ttk.Button(root,text="OPEN",command=path)


field = ttk.Entry(root)
field.insert(0,text1)
field.grid(row=0,column=1)
 

load = ttk.Label(root,text="Load File Format in CSV : ")
load.grid(row=0,column=0)

text2=StringVar()
text3=StringVar()
text4=StringVar()
text5=StringVar()


open.grid(row=0,column=2)
Lati=ttk.Label(root,text="Latitude Variable As Table")
Lati.grid(row=1,column=0)
lfield=ttk.Entry(root,textvariable=text2)
lfield.grid(row=1,column=1)
Longi = ttk.Label(root,text="Longitude Variable As Table")
Longi.grid(row=2,column=0)
lngfield=ttk.Entry(root,textvariable=text3)
lngfield.grid(row=2,column=1)
name=ttk.Label(root,text="Name Variable As Table")
name.grid(row=3,column=0)
namefield=ttk.Entry(root,textvariable=text4)
namefield.grid(row=3,column=1)
elevate = ttk.Label(root,text="Elevation Variable As Table")
elevate.grid(row=4,column=0)
elfield=ttk.Entry(root,textvariable=text5)
elfield.grid(row=4,column=1)
submit = ttk.Button(root,text="Submit")
submit.grid(row=5,column=2)

root.mainloop()




         
    

fgc = folium.FeatureGroup(name="World")
fgc.add_child(folium.GeoJson(data=open('C:\\Users\crisn\\pythonScripts\\Python MegaCourse Scripts\\mapping\\world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x : {'fillcolor':'#EE3D17'}))


fga = folium.FeatureGroup(name="AirportMaps")
html = """
       Airport_Details:<br>
       <a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
       Longitude: %s m
       Latitude: %s m
       Elevtion: %s m
       """

data = pandas.read_csv(text1)
input = text2.get()
input1= text3.get()
input2= text4.get()
input3= text5.get()
    
lat=list(data[input])
lon = list(data[input1])
nam = list(data[input2])
elev = list(data[input3])


x=maps(data,lat,lon,nam,elev,map,html,fga,fgc)
x.execute()

map.add_child(fga)
map.add_child(fgc)
map.add_child(folium.LayerControl())
map.save("Map8.html")
    



__author__ = 'Shree'



import pandas as pd
from sklearn.cluster import KMeans
from pandas import Series,DataFrame
import pygal
from flask import Flask,request,render_template
import os

import datetime



global file_name



application=Flask(__name__)

app=application



@app.route('/')

def hello():

    return render_template("index.html")



#Upload the file for writing the file on which to cluster
@app.route('/upload',methods=['POST'])

def upload():
    the_file = request.files['file_upload']
    with open (the_file.filename,'w') as file2:
        file2.write(the_file.read())
    global file_name
    file_name=the_file.filename
    return render_template("clusters.html")



#This module is used for clustering using the K-means approach
@app.route('/clusters',methods=['POST'])

def clusters():

    global file_name
    print file_name
    pdfile=file_name


    pandaread=pd.read_csv(pdfile)

    print (pandaread.shape)



    value1=str(request.values['value1'])

    value2=str(request.values['value2'])
    num=int(request.values['num'])
    print value1

    pandaframe=DataFrame(pandaread,columns=([value1,value2]))

    print(pandaframe)

    kmeans_model = KMeans(n_clusters=num, random_state=1).fit(pandaframe)
    labels = kmeans_model.labels_


    clustercenters = kmeans_model.cluster_centers_

    inertia = kmeans_model.inertia_

    print('labels' ,labels)

    print('clustercenters' ,clustercenters)

    print('inertia',inertia)

    print(len(labels))
    clus0=[]
    clus1=[]
    clus2=[]
    clus3=[]
    clus4=[]

    for i in range(len(labels)):
        list1=[]

        pandaframeix=pandaframe.ix[i]
        pandaframedict=pandaframeix.to_dict()
        key_list1=pandaframedict[value1]
        key_list2=pandaframedict[value2]
        list1.append(key_list1)
        list1.append(key_list2)

        if labels[i]==0:
            clus0.append(list1)

     for i in range(len(clus0)):
        print(clus0[i])
    print("Cluster 2 points")
    for i in range(len(clus1)):
        print(clus1[i])
    print("Cluster 3 points")
    for i in range(len(clus2)):
        print(clus2[i])
    print ("Cluster 4 points")

    #Scatter plot graph
    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = 'Correlation'
    xy_chart.add('A', clus0 )
    xy_chart.add('B', clus1)
    xy_chart.render_in_browser()
    
    xy_chart.render_response()

    #Bar chart graph
    line_chart = pygal.Bar()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.add(('A', clus0 )
    line_chart.add('B', clus1)
    line_chart.add('C',clus2)
    line_chart.render_in_browser()
                   
    #Bubble graph
    bb_chart = pygal.Dot(x_label_rotation=30)
    bb_chart.title = 'Bubble chart clustering results'
    
    bb_chart.add(('A', clus0 )
    bb_chart.add('B', clus1)
    bb_chart.add('C',clus2)
    
    bb_chart.render_in_browser()

    return  "success"





if __name__=="__main__":

        app.run(host="************************-2.compute.amazonaws.com",debug=True)





''' for i in range(len(clus3)):
       print(clus3[i])

       <option value="A">A</option>

        <option value="A">A</option>
        <option value="B">B</option>
        <option value="C">C</option>
        <option value="D">D</option>


    if labels[i]==2:
       clus2.append(list1)'''
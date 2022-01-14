etl
extract, transform, load // microsoft a-ure
ingest data lake,  data factory resources group
subscriptio pay as you go 
east us 2 region (cheaper)
prepare
data factory, author (data sets, pipeline)
pipeline runs (copy to lake)

// you can use in the space github or devops
// author: integration time from data factory, linked services with the data store, you can use the more than 80 resources or services (git, github, api hash, etc... data stores, hdfs, on...)
teste connection and create with the connections with the origin, extract this data and give to data lake,//
data lake could given to another data repository, but you have to connections between that. 
3 part: data sets, pipeline and data flow: 
data flow: process data inside data factory, you can create pipeline in data processing, just using the  language in data flow, 
data sets: represent the data in physical way, represent the file and the destiny
pipeline: all data set in a logical way, inside the extract and the activities. but first all data sets 

1 - Create the dataset from this origin:
create fold: MakinDBA
ure dataset for MySQL. Table in data base
Properties:
select the table, all data 
preview data to see all data, now publish and save internal if you dont have the git. so check point to data sectory. They record the json on git
// json do the first dataset, they represent the objects in data factory

2 - create dataset to the origin:ure blob store, data lake, and the repository of data. you can save fby delimited 
name, actor file
the data lake to connect is the linked service.
file path (the way to save  data)
raw
directory: files/mysql/actor 
file: (dinamic)
select first row as header
import schema: none //because is txt file
//come back to the window, csv actorFile
add dynamic content: 
data factory, string (
    @concat()
    @concat('actor_'formatDateTime(utcnow(), "yyyyMMddHHmm")'csv)   //formatDateTime(uptnowtimexxone) //
act_202201141536)
//finish
//chech the configurations
compreesion leve: ip or snap
compression level: fastest
data lake storage so is cheaper
column delimiter: semicolon (;)
row delimiter: auto detect (\/.\n,or\r\n)  ///line cold 
publish all, 

//pipelines:
template, select one, new pipeline
propierties, name: copy etl
activities, copy data, data flow
axxure data explores: axxule data explorer, axxure function, batch service, databricks, data lake analytics, general, HDinsights, Iteration&conditionals
databricks: notebooks, jar, python //
hadoop
iteration & conditionals: filter, foreach, if condition


engenharia de variáveis 

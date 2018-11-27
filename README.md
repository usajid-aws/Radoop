###  OVERVIEW
---

A Reddit Analyzer that shows the value of any given Reddit post. This 'value' is given by the number Upvotes + Downvotes + comments
on each post. The data used for this project was the work of researchers Lakkarajue et al. For their data set, they collected information
on reposts of images as it was significantly easy to identify reposted images using reverse image search.
Using the data set, they were able to derive models on how time, social context, and presentation affected
a post’s performance, ultimately helping them understand when, where, and how a post should be
presented to maximize its reach.   
You can read more about their research here: http://i.stanford.edu/~julian/pdfs/icwsm13.pdf   

---

### Datafiles 

Data headers are given in the followinf format 
Unixtime #image_id number_of_upvotes number_of_downvotes number_of_comments  title   

availible data files are reddit-data-large.txt & reddit-data-small.txt

### Usage

Project built with maven

run 
`mvn clean install` 

the jar file can be found in /target/hadoop-0.0.1-SNAPSHOT.jar

running hadoop 

`hdfs jar hadoop-0.0.1-SNAPSHOT.jar <input-file> <outfile>`


__Checking out file__   
`hadoop dfs -ls <outfile>`   
`hadoop fs -cat <outfile>`






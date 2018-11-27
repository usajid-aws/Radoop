package hadoop;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// Mapper class for hadoop

public class Map extends Mapper<Object, Text, Text, IntWritable>{
	

	 public void map(Object key, Text value, Context context) throws 
	 IOException, InterruptedException
	 {
		 String input = value.toString();
		 
		 // each line in txt file
		 String[] line  = input.split("\n");
		 // for every line, get ID, up/downvotes, and comments
		 // post val --> #upvotes + #downvotes + #comments
		 for(String s : line)
		 {
			 String[] vals = s.split("\t");
			 String id = vals[1];
			 int uv = Integer.parseInt(vals[2]);
			 int dv = Integer.parseInt(vals[3]);
			 int cm = Integer.parseInt(vals[4]);
			 
			 // write to context
			 IntWritable inc = new IntWritable(uv+dv+cm);
			 Text wordId = new Text(id);
			 context.write(wordId, inc);
			 
		 }
		 
	 }
}


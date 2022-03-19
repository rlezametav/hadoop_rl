# Hadoop on Docker

How to Run Hadoop on macOS (Apple M1 and Intel CPU) by One Command

## Platforms supported
ARM64 (Apple Silicon) and AMD64 (Intel)

## Requirement
Docker Desktop is required (and it is the easiest way to get Docker work on your laptop).
For macOS (Apple M1), [Docker Desktop](https://desktop.docker.com/mac/main/arm64/Docker.dmg)
For macOS (Intel), [Docker Desktop](https://desktop.docker.com/mac/main/amd64/Docker.dmg)

### Docker Test
If Docker Desktop is installed properly, you should be able to run the following command:
```
docker run hello-world
```
And see the output like:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
... ...
```

## Start Hadoop Cluster
Go to terminal and clone the git repo to your computer:

```bash
git clone git@github.com:wxw-matt/docker-hadoop.git ~/docker-hadoop
cd ~/docker-hadoop
docker-compose up -d
```
It takes a few minutes to completely start the whole Hadoop cluster for the first time.

## Run Example Map-Reduced Job on the Cluster

Run example wordcount job. 
The `WordCount.jar` is located in `./jobs/jars` directory . 

Typing the command below to commit the job.
```
./hdfs dfs -mkdir -p /input
./hdfs dfs -copyFromLocal -f /app/data/README.txt /input/
./hadoop jar jars/WordCount.jar WordCount /input /output
# View output (double quote is needed for zsh when star/asterisk occurs)
./hadoop fs -cat "/output/*"
```
>Note
You may need to remove `/output` first if it already exists using command `./hadoop fs -rm -r /output`.

## Common Hadoop Comamnds
```bash
# Create a directory
./hdfs dfs -mkdir -p directory-name
# Remove a directory and its sub-directories
./hadoop fs -rm -r -f directory-name
# Copy files from jobs/data to HDFS
./hdfs dfs -copyFromLocal -f /app/data/README.txt /input/ 
# View files
./hdfs dfs -ls /input 
```

## How to Run Your Own Jobs 

Using `Eclipse` or other IDEs to generate a `jar` file. Copy it to `./jobs/jars`. For example, if your `jar` file name is `HelloWorld.jar` and it is in the `./jobs/jars`. The following command will submit your job to Hadoop.
```
./hadoop jar jars/HelloWorld.jar HelloWorld /input /output
```

And your data will go to `./jobs/data`, then using `./hdfs dfs -copyFromLocal` to copy it to HDFS.


# Credits
The repo is inspired by [@big-data-europe](https://github.com/big-data-europe/docker-hadoop). Without their work, it may take me days to get this done.


# References:
1. https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
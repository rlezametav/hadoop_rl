# Hadoop on Docker

## Platforms supported
ARM64 (Apple Silicon) and AMD64 (Intel)

## Requirement
Docker Desktop is required (and it is the easiest way to get almost everything work on your laptop).
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

## Run Map-Reduced Job on the Cluster

Run example wordcount job:
```
./hadoop jar WordCount.jar WordCount /input /output
# View output (double quote is needed for zsh when star/asterisk occurs)
./hadoop fs -cat "/output/*"
```
>Note
You may need to remove `/output` if it already exists using command `./hadoop fs -rm -r /output`.

## Hadoop Comamnds
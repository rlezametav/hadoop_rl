FROM wxwmatt/hadoop-release:2.0.0-hadoop3.3.1-java8

RUN ln -sfn /usr/lib/jvm/java-8-openjdk-$([ $(uname -m) = "aarch64" ] && echo "arm64" || echo "amd64" )/ /usr/lib/jvm/java-8-openjdk
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk

ADD entrypoint.sh /entrypoint.sh

RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

FROM wxwmatt/hadoop-release:2.0.0-hadoop3.3.1-java8

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk

ADD entrypoint.sh /entrypoint.sh

RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

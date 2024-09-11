FROM ubuntu:20.04

USER root

# --------------------------------------------------------
# JAVA
# --------------------------------------------------------
RUN apt-get update
RUN apt-get install -y openjdk-8-jre openjdk-8-jdk openssh-server vim
RUN apt-get install -y --no-install-recommends \
    python3-launchpadlib \
    software-properties-common

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64/


# Install curl
RUN apt-get update && apt-get install -y curl


# --------------------------------------------------------
# HADOOP
# --------------------------------------------------------
ENV HADOOP_VERSION=3.2.1
ENV HADOOP_URL=https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
ENV HADOOP_PREFIX=/opt/hadoop
ENV HADOOP_CONF_DIR=/etc/hadoop
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
ENV HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=$HADOOP_HOME/lib/native"
ENV MULTIHOMED_NETWORK=1
ENV USER=root
ENV HADOOP_HOME=/opt/hadoop
ENV PATH $HADOOP_PREFIX/bin/:$PATH
ENV PATH $HADOOP_HOME/bin/:$PATH

RUN set -x \
    && curl -fSL "${HADOOP_URL}" -o  /tmp/hadoop.tar.gz \
    && tar -xvf /tmp/hadoop.tar.gz -C /opt/ \
    && rm /tmp/hadoop.tar.gz* \
    && mv /opt/hadoop-3.2.1 /opt/hadoop

RUN ln -s /opt/hadoop/etc/hadoop /etc/hadoop
RUN mkdir /opt/hadoop/logs
RUN mkdir /hadoop-data

USER root

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

COPY conf/core-site.xml $HADOOP_CONF_DIR/core-site.xml
COPY conf/hdfs-site.xml $HADOOP_CONF_DIR/hdfs-site.xml
COPY conf/mapred-site.xml $HADOOP_CONF_DIR/mapred-site.xml
COPY conf/yarn-site.xml $HADOOP_CONF_DIR/yarn-site.xml


# --------------------------------------------------------
# SPARK
# --------------------------------------------------------

ENV SPARK_VERSION=3.1.1
ENV SPARK_URL=https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.2.tgz
ENV SPARK_HOME=/opt/spark
ENV PATH $SPARK_HOME/bin:$PATH
ENV PYSPARK_PYTHON=python3
ENV PYTHONHASHSEED=1

RUN set -x \
    && curl -fSL "${SPARK_URL}" -o  /tmp/spark.tar.gz \
    && tar -xvzf /tmp/spark.tar.gz -C /opt/ \
    && rm /tmp/spark.tar.gz* \
    && mv /opt/spark-3.1.1-bin-hadoop3.2 /opt/spark

ADD conf/core-site.xml $SPARK_HOME/conf
ADD conf/yarn-site.xml $SPARK_HOME/conf

RUN apt-get update && apt-get install -y python3-pip
RUN apt-get update && apt-get install -y libkrb5-dev

ADD requirements.txt /requirements.txt

# Install requirements.txt
RUN pip3 install -r /requirements.txt

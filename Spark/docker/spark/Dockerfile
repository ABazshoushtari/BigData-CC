FROM hadoop-base AS builder

ARG shared_workspace=/opt/workspace

WORKDIR $SPARK_HOME

ENV SPARK_MASTER_PORT=7077 \
SPARK_MASTER_WEBUI_PORT=8081 \
SPARK_LOG_DIR=/opt/spark/logs \
SPARK_MASTER_LOG=/opt/spark/logs/spark-master.out \
SPARK_WORKER_LOG=/opt/spark/logs/spark-worker.out \
SPARK_WORKER_WEBUI_PORT=8081 \
SPARK_WORKER_PORT=7000 \
SPARK_MASTER="spark://spark-master:7077" \
SPARK_WORKLOAD="master"

ENV SHARED_WORKSPACE=${shared_workspace}
RUN mkdir -p ${shared_workspace}/data

EXPOSE 8081 7077 6066

VOLUME ${shared_workspace}

RUN mkdir -p $SPARK_LOG_DIR && \
touch $SPARK_MASTER_LOG && \
touch $SPARK_WORKER_LOG && \
ln -sf /dev/stdout $SPARK_MASTER_LOG && \
ln -sf /dev/stdout $SPARK_WORKER_LOG

ADD start-spark.sh start-spark.sh

RUN chmod a+x start-spark.sh

CMD ["start-spark.sh"]
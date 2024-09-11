#!/bin/bash

# create new network
# docker network create hadoop_network

# Build hadoop-base
docker build -t hadoop-base -f Dockerfile .

# Build spark-base
cd docker/spark && docker build -t spark-base -f Dockerfile . && cd ../..

# Run Spark Cluster on Hadoop Cluster with jupyter notebook
docker-compose -f docker-compose-cluster.yml up -d
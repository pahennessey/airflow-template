FROM python:3.6-slim
LABEL maintainer="patrickh"

ENV AIRFLOW_HOME /airflow
ENV AIRFLOW_VERSION 1.10.5
ENV AIRFLOW_GPL_UNIDECODE yes

# Install dependencies
RUN apt-get update && \
    apt-get -y install gcc \
        curl \
        lsb-release \
        apt-transport-https \
        openssh-client \
        gnupg && \
    apt-get -y clean && \
    find /var/lib/apt/lists/ -type f -exec rm -f {} \;

# Install Google Cloud SDK
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && \
    apt-get install -y google-cloud-sdk

# Install Airflow
RUN pip install apache-airflow==$AIRFLOW_VERSION && \
    pip install apache-airflow[postgres] && \
    pip install apache-airflow[gbq]

# Install additional python packages as needed
RUN pip install pandas pandas-gbq simple-salesforce google-cloud-bigquery

# Add user
RUN useradd -d $AIRFLOW_HOME -m airflow

# Copy DAGs
COPY --chown=airflow dags $AIRFLOW_HOME/dags

# Set container
USER airflow
WORKDIR $AIRFLOW_HOME
CMD ["bash"]

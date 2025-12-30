# Connecting Azure Event Hub with Conduktor

This guide explains how to connect **Azure Event Hub** to **Conduktor** using **Kafka client configuration** in **Standard mode**.

---

## Prerequisites

- An **Azure Event Hub** instance in **Standard** mode.  
- **Public access** enabled for your Event Hub.  
- **Conduktor** installed on your local machine.  
- **Connection string** copied from the Event Hub namespace.  
- **Server endpoint name** for the Event Hub.

---

## Step 1: Copy Connection String

1. Navigate to your Event Hub namespace in the Azure portal.  
2. Go to **Shared access policies** → select **RootManageSharedAccessKey** (or a custom policy with **Listen/Send** permissions).  
3. Copy the **Connection String–Primary Key**.  

---

## Step 2: Edit Configuration File

Create or edit the Kafka configuration file to include your Event Hub connection details:

```properties
# Kafka connection
bootstrap.servers=<server_name>:9093

# Security
ssl.endpoint.identification.algorithm=https
security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="<ConnectionString>;";

# Timeout adjustments for Event Hubs
request.timeout.ms=20000
retry.backoff.ms=500
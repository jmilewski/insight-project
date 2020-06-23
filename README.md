# Intrinsic Ether

### Insight Data Engineering (New York 2020B)

The goal of this project is to use Ethereum blockchain data to measure real-time changes in the intrinsic value of network, which can be used to predict Ether prices. The intrinsic value is proxied by computing a Price-to-Metcalfe Ratio (PMR). The relative change in PMR can potentially be used as a leading indicator for cryptocurrency investing and risk management.

#### Metcalfe's Law

#### Price-to-Metcalf Ratio

## Data

### Ethereum Node
Blockchain data was obtained by setting up and syncing an Ethereum Node. Syncing with the network took two days and required the use of a m5a.large EC2 instance with the highest IOPS option. An Ethereum Node on a t2.medium EC2 instance with standard IOPS failed to sync after two weeks.

## Exchange Data
Real-time exchange data was is streamed from the IEX Cloud API for market prices on the Gemini Exchange.

## Pipeline

![Preview](images/pipeline.png)


### Setup


### Ingestion


### Metric


### Historical Analytics



## Frontend


## Repo directory structure
The top-level directory structure look like the following:

    ├── README.md
    ├── run.sh
    ├── app
         └── app.py
    ├── src
        └── dags
            └── dags.py
        └── spark
            └──  spark.py
        └── database
                ├── db.py
                ├── config.py
        └── main.py

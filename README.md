# sdm-engine

Stock Data Manager (sdm) aim to help you maintain high quality stock dataset with free open source SDKs. This tool mainly forcus on Chinese Stock Market.

## Background

There are a number of open source stock data SDKs available to help us access various data for free and efficiently. But how to manage this data effectively locally and how to maintain different data sources can be a hassle.

For Quant and algorithmic traders, a high quality dataset is critical. Based on high quality data, we can better backtest as well as have more confidence in applying the strategy.

sdm is an open source tool that I developed in this context, mainly for individual Quants.

## Getting Start

sdm-engine is a Python3 project, use poetry to manage dependencies. You need install Poetry first.

Clone this repo and cd to project's directory, init the project:

```
poetry install
```

Then you need manually install a MongoDB database. For now, I use the default local address without password for MongoDB.

Then run webserver:

```
poetry run start
```

The server will run at http://localhost:8080, visit http://localhost:8080/docs for api documentation.

## Architecture

`sdm` is consist of 3 parts:

1. **[sdm-engine](https://github.com/maxiee/sdm-engine)**: Includes all algorithms, using MongoDB as database, hosting a web endpoint.
2. **[sdm-cli](https://github.com/maxiee/sdm-cli)**: command line frontend communicate to engine.
3. **sdm-frontend**: a web frontend communicate to engine, with rich visual presentation, and various data management operations.

This repo is the sdm-engine part.

## Concept

### Exchange

- `sse`: Shanghai Stock Exchange
- `szse`: Shenzhen Stock Exchange

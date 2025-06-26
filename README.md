# Warnet Demo Project

A simple project to help new users learn about Warnet and Bitcoin network analysis.

## What is this?

This is a guide to get you started with Warnet using existing scenarios. You'll learn how to:

- **Deploy a Bitcoin network** using Warnet
- **Run existing attack scenarios** against nodes
- **Monitor network behavior** and node responses
- **Understand basic network stress tests**

## Prerequisites

1. Python 3.8+
2. Docker or Kubernetes (local)
3. Basic understanding of Bitcoin concepts

## Quick Start

### 1. Create a python virtual environment

```sh
python3 -m venv .venv
source ./venv/bin/activate
```

### 2. Install Warnet

```sh
pip install warnet
```

### 3. Set up dependencies

Warnet will ask which back end you want to use, check that it is working,
and install additional client tools into the virtual environment.

```sh
warnet setup
```

When prompted, choose your preferred backend:

- **Minikube** - Local Kubernetes cluster (recommended for beginners)
- **Docker Desktop** - If you have Docker Desktop with Kubernetes enabled
- **No Backend** - For connecting to remote clusters (advanced users)

Warnet will automatically check and install required tools like `kubectl` and `helm`.

### 4. Create a new project

```sh
warnet new ./my-warnet-project
```

When prompted, choose:

- **Number of nodes**: 1 (for simple testing)
- **Bitcoin version**: 26.0 (or latest)
- **Connections per node**: 0 (since we only have one node)

### 5. Deploy the network

```sh
warnet deploy ./my-warnet-project/networks/networkname
```

### 6. Try existing scenarios

Now you can run the scenarios that come with Warnet:

#### Basic Mining Scenario

```sh
warnet run scenarios/miner_std.py
```

This will start mining blocks on your network.

#### Transaction Flood Scenario

```sh
warnet run scenarios/tx_flood.py
```

This will create wallets and send random transactions to stress the network.

#### Network Reconnaissance

```sh
warnet run scenarios/reconnaissance.py
```

This will gather information about your network topology.

### 7. Monitor the network

```sh
warnet dashboard
```

**Note**: If using Minikube, you may need to run `minikube tunnel` in another terminal first.

### 8. Shut down the network

```sh
warnet down
```

## What You'll Learn

1. **Network Deployment**: How to deploy a Bitcoin network using Warnet
2. **Scenario Execution**: How to run attack scenarios against nodes
3. **Monitoring**: How to observe network behavior and node responses
4. **Basic Attacks**: Understanding simple network stress tests

## Available Scenarios

Warnet comes with several built-in scenarios you can experiment with:

- **`miner_std.py`** - Basic block mining
- **`tx_flood.py`** - Transaction flooding attack
- **`reconnaissance.py`** - Network topology discovery
- **`signet_miner.py`** - Signet-specific mining
- **`ln_init.py`** - Lightning Network setup

Each scenario demonstrates different aspects of Bitcoin network interaction and can be customized with command-line options.

## Next Steps

After completing this tutorial, you can:

1. **Modify scenarios**: Edit the scenario files to try different attack patterns
2. **Add more nodes**: Modify the network configuration to add additional nodes
3. **Create custom scenarios**: Write your own attack scenarios using the existing ones as templates
4. **Explore advanced features**: Check out the main [Warnet documentation](https://github.com/bitcoin-dev-project/warnet)

## Troubleshooting

- **Network won't start**: Make sure your chosen backend (Minikube/Docker Desktop) is running
- **Scenario fails**: Check that the network is fully deployed first
- **Dashboard not accessible**:
  - For Minikube: Run `minikube tunnel` in another terminal
  - For Docker Desktop: Check that Kubernetes is enabled
- **Setup fails**: Make sure you have Docker installed and running

## Resources

- [Warnet Documentation](https://github.com/bitcoin-dev-project/warnet)
- [Bitcoin Core Test Framework](https://github.com/bitcoin/bitcoin/tree/master/test/functional)
- [Bitcoin Development Guide](https://bitcoin.org/en/development)

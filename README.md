# Warnet Demo Project

A hands-on Warnet project to help you learn Bitcoin network analysis with a simple three-node network and propagation scenario.

## What is this?

This is a complete Warnet project that demonstrates how to:

- **Deploy a three-node Bitcoin network** using Warnet
- **Run a network propagation test** to see how transactions flow
- **Monitor network behavior** and observe node responses
- **Understand basic Bitcoin network interactions**

The project includes a pre-configured network (`simple-3node-network`) and a beginner-friendly scenario (`propagation_check.py`) that you can run immediately.

## What is Network Propagation?

**Network propagation** is how information (like new transactions and blocks) spreads through the Bitcoin network. When one node receives a new transaction, it shares that information with other nodes it's connected to. This is how the entire Bitcoin network stays synchronized.

In this demo, you'll see:

- How transactions move from one node to another
- How blocks are shared across the network
- How nodes communicate and stay in sync

## Prerequisites

Before you start, you'll need:

### 1. **Python 3.8 or higher**

- [Download Python](https://www.python.org/downloads/)
- Make sure you can run `python3 --version` in your terminal

### 2. **Docker or Kubernetes**

Choose one of these options:

**Option A: Docker Desktop (Recommended for beginners)**

- [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Enable Kubernetes in Docker Desktop settings
- Good for beginners because it has a graphical interface

**Option B: Minikube (Good for Linux users)**

- [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)
- Runs a local Kubernetes cluster
- Works well on Linux systems

### 3. **Basic Terminal Knowledge**

- Know how to open a terminal/command prompt
- Understand basic commands like `cd`, `ls`, `mkdir`
- No Bitcoin knowledge required - we'll explain everything!

## Quick Start

### 1. Set up Warnet

Follow the [Warnet installation guide](https://github.com/bitcoin-dev-project/warnet/blob/main/docs/quick-start.md) for detailed setup instructions:

```sh
# Create virtual environment (isolated Python environment)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install Warnet
pip install warnet

# Set up dependencies
warnet setup
```

When prompted, choose your preferred backend:

- **Docker Desktop** - If you have Docker Desktop with Kubernetes enabled (recommended for beginners due to GUI)
- **Minikube** - Local Kubernetes cluster (good for Linux users)

**Recommendation**: Docker Desktop is generally easier for beginners due to its graphical interface, while Minikube works well on Linux systems.

### 2. Deploy the three-node network

This project includes a pre-configured three-node network. Deploy it with:

```sh
warnet deploy warnet-demo/networks/simple-3node-network
```

This will create a simple Bitcoin network with 3 nodes for basic experimentation.

**What happens**: Warnet will create three Bitcoin nodes (tank-0000, tank-0001, tank-0002) that can communicate with each other.

### 3. Run the propagation test

Execute the included scenario to see the network in action:

```sh
warnet run warnet-demo/scenarios/propagation_check.py --debug
```

**Note**: The `--debug` flag shows detailed runtime output, making it easier to follow what's happening. However, this will consume your terminal foreground. If you want to run other commands (like `warnet dashboard`) simultaneously, you can omit the `--debug` flag and run the scenario in the background.

**What the scenario does**:

- **Step 1**: Waits for all nodes to be ready and connected
- **Step 2**: Generates initial blocks to create funds (like mining Bitcoin)
- **Step 3**: Creates test transactions (like sending Bitcoin between addresses)
- **Step 4**: Monitors transaction propagation across the 3-node network
- **Step 5**: Shows you how nodes communicate and synchronize

### 4. Monitor your network and watch the propagation

#### **Option A: Web Dashboard (Recommended)**

Open the Warnet dashboard to visualize your network in real-time:

```sh
warnet dashboard
```

This opens a web interface where you can:

- See your node's status and connections
- Monitor network activity in real-time
- View logs and metrics
- Watch the propagation scenario execute step-by-step

**Note**: If using Minikube, you may need to run `minikube tunnel` in another terminal first.

#### **Option B: Command Line Monitoring**

Monitor your network from the terminal:

```sh
# Check network status
warnet status

# View real-time logs
warnet logs -f

# Get detailed node information
warnet logs tank-0000
```

#### **Option C: Direct Node Access**

Connect directly to your Bitcoin nodes using RPC (Remote Procedure Call) commands:

```sh
# Get node info
warnet bitcoin rpc tank-0000 getnetworkinfo

# Check mempool (pending transactions waiting to be included in a block)
warnet bitcoin rpc tank-0000 getmempoolinfo

# View recent blocks
warnet bitcoin rpc tank-0000 getblockcount
```

#### **What You'll See:**

When running the propagation scenario, you'll see output like this:

```
🚀 Starting Network Propagation Check scenario
Step 1: Waiting for all nodes to be ready...
✓ All nodes are ready and connected
Step 2: Checking initial network state...
Node 0 (tank-0000): Block count: 0, Connections: 2
Node 1 (tank-0001): Block count: 0, Connections: 2
Node 2 (tank-0002): Block count: 0, Connections: 2
Step 3: Generating initial blocks...
Generating 101 blocks on node 0...
✓ All nodes synchronized at block 101
Step 4: Creating test transactions...
Created transaction 1: d537f2d2c9948a60...
Created transaction 2: db6e229bd3bcc0ee...
Step 5: Monitoring transaction propagation...
Node 0 mempool: 5 transactions
Node 1 mempool: 5 transactions
Node 2 mempool: 5 transactions
🎉 Network Propagation Check completed successfully!
```

The dashboard will show these activities happening in real-time!

### 5. Clean up

When you're done experimenting:

```sh
warnet down
```

This stops all the nodes and frees up system resources.

## What You'll Learn

By running this project, you'll understand:

1. **Network Deployment**: How Warnet creates and manages Bitcoin networks
2. **Node Communication**: How Bitcoin nodes connect and share information
3. **Transaction Propagation**: How transactions flow through the network
4. **Network Monitoring**: How to observe network behavior in real-time
5. **Scenario Execution**: How to run and create network tests

## Key Bitcoin Concepts Explained

### **Regtest Mode**

- A testing environment where you can create your own Bitcoin network
- No real Bitcoin is involved - it's all simulated
- Perfect for learning and experimentation

### **Blocks**

- Groups of transactions that are added to the Bitcoin blockchain
- In regtest mode, you can create blocks instantly for testing

### **Mempool**

- A temporary storage area for transactions waiting to be included in a block
- Think of it as a "waiting room" for transactions

### **RPC (Remote Procedure Call)**

- A way to send commands to Bitcoin nodes
- Allows you to ask nodes for information or tell them to do something

## Project Structure

```
warnet-demo/
├── warnet.yaml                  # Project configuration
├── networks/
│   └── simple-3node-network/    # Three-node network configuration
│       ├── network.yaml         # Network topology
│       └── node-defaults.yaml   # Default node settings
└── scenarios/
    └── propagation_check.py      # Network propagation test scenario
```

## The Network: simple-3node-network

This is a simple three-node Bitcoin network:

```
tank-0000
tank-0001
tank-0002
```

These three nodes run Bitcoin Core 26.0 in regtest mode, allowing you to observe how transactions propagate between nodes in a small network.

## The Scenario: propagation_check.py

This scenario demonstrates network propagation:

1. **Network Readiness Check**: Ensures all nodes are online and connected
2. **Block Generation**: Creates initial funds by mining blocks
3. **Transaction Creation**: Sends test transactions across the network
4. **Propagation Monitoring**: Observes how transactions spread between nodes
5. **Network State Analysis**: Shows the final state of all nodes

## Optional: Real Attack Scenario

If you want to see an actual attack scenario that demonstrates how nodes can be affected by malicious behavior, you can also run the attack from the [Battle of Galen Erso](https://github.com/bitcoin-dev-project/battle-of-galen-erso) project:

```sh
# Clone the Galen Erso project
git clone https://github.com/bitcoin-dev-project/battle-of-galen-erso.git
cd battle-of-galen-erso

# Run the actual attack scenario
warnet run scenarios/my_first_attack_5kinv.py
```

This will demonstrate a real attack where you can watch a node "die" or become unresponsive due to malicious network behavior.

## Troubleshooting

### **Common Issues:**

- **Network won't start**: Make sure your chosen backend (Minikube/Docker Desktop) is running
- **Scenario fails**: Check that the network is fully deployed first with `warnet status`
- **Dashboard not accessible**:
  - For Minikube: Run `minikube tunnel` in another terminal
  - For Docker Desktop: Check that Kubernetes is enabled
- **Setup fails**: Make sure you have Docker installed and running
- **"Command not found"**: Make sure you've activated the virtual environment with `source .venv/bin/activate`

### **Getting Help:**

If you encounter issues:

1. Check the [Warnet documentation](https://github.com/bitcoin-dev-project/warnet/blob/main/README.md)
2. Look at the logs with `warnet logs -f`
3. Make sure all prerequisites are installed correctly

## Next Steps

After completing this tutorial, you can:

1. **Try different wait times**: Run the scenario with `--wait-time 20` to see propagation more slowly
2. **Add more nodes**: Modify `networks/simple-3node-network/network.yaml` to create larger networks
3. **Explore the dashboard**: Try different monitoring options to see network activity
4. **Learn more**: Check out the main [Warnet documentation](https://github.com/bitcoin-dev-project/warnet/blob/main/README.md) for advanced features

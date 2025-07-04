# Warnet Demo Project

A hands-on Warnet project to help you learn Bitcoin network analysis with a simple one-node network and attack scenario.

## What is this?

This is a complete Warnet project that demonstrates how to:

- **Deploy a single-node Bitcoin network** using Warnet
- **Run a simple attack scenario** against the network
- **Monitor network behavior** and observe node responses
- **Understand basic Bitcoin network interactions**

The project includes a pre-configured network (`94.0.0-5k-inv`) and a beginner-friendly scenario (`my_first_attack_5kinv.py`) that you can run immediately.

## Prerequisites

1. Python 3.8+
2. Docker or Kubernetes (local)
3. Basic understanding of Bitcoin concepts

## Quick Start

### 1. Set up Warnet

Follow the [Warnet installation guide](https://github.com/bitcoin-dev-project/warnet?tab=readme-ov-file#quick-start) for detailed setup instructions:

```sh
# Create virtual environment
python3 -m venv .venv
source ./venv/bin/activate

# Install Warnet
pip install warnet

# Set up dependencies
warnet setup
```

When prompted, choose your preferred backend:

- **Minikube** - Local Kubernetes cluster (recommended for beginners)
- **Docker Desktop** - If you have Docker Desktop with Kubernetes enabled

### 2. Deploy the one-node network

This project includes a pre-configured one-node network. Deploy it with:

```sh
warnet deploy warnet-demo
```

This will create a simple Bitcoin network with 1 node for basic experimentation.

### 3. Run the attack scenario

Execute the included scenario to see the network in action:

```sh
warnet run warnet-demo/scenarios/my_first_attack_5kinv.py
```

This scenario will:

- Wait for all nodes to be ready
- Generate initial blocks to create funds
- Create test transactions
- Monitor transaction propagation across the network
- Show you how nodes communicate and synchronize

### 4. Monitor your tiny network and watch the attack progress

#### **Option A: Web Dashboard (Recommended)**

Open the Warnet dashboard to visualize your network in real-time:

```sh
warnet dashboard
```

This opens a web interface where you can:

- See your node's status and connections
- Monitor network activity in real-time
- View logs and metrics
- Watch the attack scenario execute step-by-step

**Note**: If using Minikube, you may need to run `minikube tunnel` in another terminal first.

#### **Option B: Command Line Monitoring**

Monitor your network from the terminal:

```sh
# Check network status
warnet status

# View real-time logs
warnet logs

# Get detailed node information
warnet logs tank-0000
```

#### **Option C: Direct Node Access**

Connect directly to your Bitcoin node:

```sh
# Get node info
warnet exec tank-0000 bitcoin-cli getnetworkinfo

# Check mempool (pending transactions)
warnet exec tank-0000 bitcoin-cli getmempoolinfo

# View recent blocks
warnet exec tank-0000 bitcoin-cli getblockcount
```

#### **What to Watch For:**

When running the attack scenario, you'll see:

- **Step 1**: Node startup and readiness
- **Step 2**: Block generation (creating initial funds)
- **Step 3**: Transaction creation and broadcasting
- **Step 4**: Network propagation (how transactions spread)
- **Step 5**: Final network state analysis

The dashboard will show these activities happening in real-time!

### 5. Clean up

When you're done experimenting:

```sh
warnet down
```

## What You'll Learn

By running this project, you'll understand:

1. **Network Deployment**: How Warnet creates and manages Bitcoin networks
2. **Node Communication**: How Bitcoin nodes connect and share information
3. **Transaction Propagation**: How transactions flow through the network
4. **Network Monitoring**: How to observe network behavior in real-time
5. **Scenario Execution**: How to run and create attack scenarios

## Project Structure

```
warnet-demo/
├── warnet.yaml                  # Project configuration
├── node-defaults.yaml           # Default node settings
├── networks/
│   └── 94.0.0-5k-inv.yaml      # One-node network configuration
├── scenarios/
│   └── my_first_attack_5kinv.py  # Your first attack scenario
└── plugins/                      # Network plugins
```

## The Network: 94.0.0-5k-inv

This is a simple one-node Bitcoin network:

```
tank-0000
```

This single node runs Bitcoin Core 26.0 in regtest mode, making it perfect for learning and experimentation without the complexity of multiple nodes.

## The Scenario: my_first_attack_5kinv.py

This scenario demonstrates basic network interaction:

1. **Network Readiness Check**: Ensures all nodes are online and connected
2. **Block Generation**: Creates initial funds by mining blocks
3. **Transaction Creation**: Sends test transactions across the network
4. **Propagation Monitoring**: Observes how transactions spread between nodes
5. **Network State Analysis**: Shows the final state of all nodes

## Next Steps

After completing this tutorial, you can:

1. **Modify the scenario**: Edit `my_first_attack_5kinv.py` to try different network interactions
2. **Add more nodes**: Modify `94.0.0-5k-inv.yaml` to create larger networks
3. **Create custom scenarios**: Use the existing scenario as a template for your own
4. **Explore advanced features**: Check out the main [Warnet documentation](https://github.com/bitcoin-dev-project/warnet)

## Troubleshooting

- **Network won't start**: Make sure your chosen backend (Minikube/Docker Desktop) is running
- **Scenario fails**: Check that the network is fully deployed first with `warnet status`
- **Dashboard not accessible**:
  - For Minikube: Run `minikube tunnel` in another terminal
  - For Docker Desktop: Check that Kubernetes is enabled
- **Setup fails**: Make sure you have Docker installed and running

## Resources

- **[Warnet Documentation](https://github.com/bitcoin-dev-project/warnet)** - Complete guide to Warnet features and usage
- **[Warnet Quick Start](https://github.com/bitcoin-dev-project/warnet?tab=readme-ov-file#quick-start)** - Step-by-step installation guide
- **[Warnet Scenarios](https://github.com/bitcoin-dev-project/warnet?tab=readme-ov-file#scenarios)** - Learn how to create custom attack scenarios
- **[Warnet Networks](https://github.com/bitcoin-dev-project/warnet?tab=readme-ov-file#networks)** - Understanding network configuration
- **[Bitcoin Core Test Framework](https://github.com/bitcoin/bitcoin/tree/master/test/functional)** - Framework used by Warnet scenarios
- **[Bitcoin Development Guide](https://bitcoin.org/en/development)** - General Bitcoin development resources

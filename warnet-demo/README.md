# Warnet Demo Project

A hands-on Warnet project to help you learn Bitcoin network analysis with a simple 5-node network and attack scenario.

## What is this?

This is a complete Warnet project that demonstrates how to:

- **Deploy a 5-node Bitcoin network** using Warnet
- **Run a simple attack scenario** against the network
- **Monitor network behavior** and observe node responses
- **Understand basic Bitcoin network interactions**

The project includes a pre-configured network (`94.0.0-5k-inv`) and a beginner-friendly scenario (`my_first_attack_5kinv.py`) that you can run immediately.

## Project Structure

```
warnet-demo/
├── warnet.yaml                    # Project configuration
├── node-defaults.yaml             # Default node settings
├── networks/
│   └── 94.0.0-5k-inv.yaml        # 5-node network configuration
├── scenarios/
│   ├── my_first_attack_5kinv.py  # Your first attack scenario
│   ├── miner_std.py              # Basic mining scenario
│   ├── tx_flood.py               # Transaction flooding
│   ├── reconnaissance.py         # Network discovery
│   └── ...                       # Other scenarios
└── plugins/                      # Network plugins
    ├── tor/                      # Tor network integration
    └── simln/                    # Lightning Network simulation
```

## The Network: 94.0.0-5k-inv

This is a simple 5-node Bitcoin network with the following topology:

```
tank-0000 ──── tank-0001 ──── tank-0003
     │           │           │
     └─── tank-0002 ────────┘
```

Each node runs Bitcoin Core in regtest mode, making it perfect for learning and experimentation.

## The Scenario: my_first_attack_5kinv.py

This scenario demonstrates basic network interaction:

1. **Network Readiness Check**: Ensures all nodes are online and connected
2. **Block Generation**: Creates initial funds by mining blocks
3. **Transaction Creation**: Sends test transactions across the network
4. **Propagation Monitoring**: Observes how transactions spread between nodes
5. **Network State Analysis**: Shows the final state of all nodes

## Quick Start

### 1. Set up Warnet

Follow the [Warnet installation guide](https://github.com/bitcoin-dev-project/warnet?tab=readme-ov-file#quick-start):

```sh
# Create virtual environment
python3 -m venv .venv
source ./venv/bin/activate

# Install Warnet
pip install warnet

# Set up dependencies
warnet setup
```

### 2. Deploy the 5-node network

```sh
warnet deploy warnet-demo
```

### 3. Run the attack scenario

```sh
warnet run warnet-demo/scenarios/my_first_attack_5kinv.py
```

### 4. Monitor your network

```sh
warnet dashboard
```

### 5. Clean up

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

## Next Steps

After completing this tutorial, you can:

1. **Modify the scenario**: Edit `my_first_attack_5kinv.py` to try different network interactions
2. **Add more nodes**: Modify `94.0.0-5k-inv.yaml` to create larger networks
3. **Try other scenarios**: Experiment with the other included scenarios
4. **Create custom scenarios**: Use the existing scenarios as templates for your own
5. **Explore advanced features**: Check out the main [Warnet documentation](https://github.com/bitcoin-dev-project/warnet)

## Troubleshooting

- **Network won't start**: Make sure your chosen backend (Minikube/Docker Desktop) is running
- **Scenario fails**: Check that the network is fully deployed first with `warnet status`
- **Dashboard not accessible**:
  - For Minikube: Run `minikube tunnel` in another terminal
  - For Docker Desktop: Check that Kubernetes is enabled
- **Setup fails**: Make sure you have Docker installed and running

## Resources

- [Warnet Documentation](https://github.com/bitcoin-dev-project/warnet)
- [Bitcoin Core Test Framework](https://github.com/bitcoin/bitcoin/tree/master/test/functional)
- [Bitcoin Development Guide](https://bitcoin.org/en/development)

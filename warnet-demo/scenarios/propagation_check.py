#!/usr/bin/env python3
"""
Network Propagation Check Scenario

A simple scenario to demonstrate network propagation with a 3-node network.
This scenario shows how to:
1. Connect to nodes
2. Monitor network state
3. Perform basic network operations
4. Observe transaction propagation between nodes

Usage:
    warnet run scenarios/propagation_check.py
"""

import time
from commander import Commander


class PropagationCheck(Commander):
    def set_test_params(self):
        # This scenario works with any number of nodes
        self.num_nodes = 0

    def add_options(self, parser):
        parser.description = (
            "Network propagation check - observe transaction flow between nodes"
        )
        parser.usage = "warnet run scenarios/propagation_check.py [options]"
        parser.add_argument(
            "--wait-time",
            dest="wait_time",
            default=5,
            type=int,
            help="Time to wait between operations (default 5 seconds)",
        )

    def run_test(self):
        """Main test logic"""
        self.log.info("🚀 Starting Network Propagation Check scenario")

        # Step 1: Wait for all nodes to be ready and connect them
        self.log.info("Step 1: Waiting for all nodes to be ready...")
        self.wait_for_tanks_connected()
        self.log.info("✓ All nodes are ready and connected according to network.yaml")

        # Step 2: Check initial network state
        self.log.info("Step 2: Checking initial network state...")
        self.check_network_state()

        # Step 3: Generate some blocks to create initial funds
        self.log.info("Step 3: Generating initial blocks...")
        self.generate_initial_blocks()

        # Step 4: Create some transactions
        self.log.info("Step 4: Creating test transactions...")
        self.create_test_transactions()

        # Step 5: Monitor network propagation
        self.log.info("Step 5: Monitoring transaction propagation...")
        self.monitor_transaction_propagation()

        # Step 6: Check final network state
        self.log.info("Step 6: Checking final network state...")
        self.check_network_state()

        self.log.info("🎉 Network Propagation Check completed successfully!")

    def check_network_state(self):
        """Check the current state of all nodes in the network"""
        for i, node in enumerate(self.nodes):
            # Get basic node info
            block_count = node.getblockcount()
            connection_count = node.getconnectioncount()
            mempool_size = len(node.getrawmempool())

            self.log.info(f"Node {i} ({node.tank}):")
            self.log.info(f"  - Block count: {block_count}")
            self.log.info(f"  - Connections: {connection_count}")
            self.log.info(f"  - Mempool size: {mempool_size}")

            # Show peer connections
            if connection_count > 0:
                self.log.info(f"  - Connected to {connection_count} peers")
            else:
                self.log.info("  - No peer connections yet")

    def generate_initial_blocks(self):
        """Generate some initial blocks to create funds"""
        # Use the first node to generate blocks
        node0 = self.nodes[0]
        miner_wallet = self.ensure_miner(node0)
        address = miner_wallet.getnewaddress()

        # Generate 101 blocks to create mature coinbase outputs
        self.log.info("Generating 101 blocks on node 0...")
        self.generatetoaddress(node0, 101, address, sync_fun=self.sync_all)
        self.log.info(f"✓ All nodes synchronized:")
        self.check_network_state()

    def create_test_transactions(self):
        """Create some test transactions to demonstrate network activity"""
        # Create a wallet on node 0
        node0 = self.nodes[0]
        miner_wallet = self.ensure_miner(node0)

        # Get a new address
        address = miner_wallet.getnewaddress()

        # Send some transactions to demonstrate network activity
        self.log.info("Creating test transactions...")

        for i in range(5):
            # Send a small amount to the address
            txid = miner_wallet.sendtoaddress(address, 0.1)
            self.log.info(f"Created transaction {i + 1}: {txid[:16]}...")

            # Wait a bit between transactions
            time.sleep(0.5)

        # Wait for transactions to propagate
        self.sync_all()

    def monitor_transaction_propagation(self):
        """Monitor how transactions propagate through the network"""
        self.log.info("Monitoring transaction propagation...")

        # Check mempool on all nodes
        for i, node in enumerate(self.nodes):
            mempool = node.getrawmempool()
            self.log.info(f"Node {i} mempool: {len(mempool)} transactions")

            # Show some transaction details
            if mempool:
                txid = list(mempool)[0]
                tx_info = node.getmempoolentry(txid)
                fee = tx_info.get("fee", "unknown")
                self.log.info(f"  Sample transaction: {txid[:16]}... (fee: {fee})")


def main():
    PropagationCheck().main()


if __name__ == "__main__":
    main()

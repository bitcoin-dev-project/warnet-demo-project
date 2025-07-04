#!/usr/bin/env python3
"""
My First Attack - 5K INV Scenario

A simple scenario to demonstrate basic Warnet usage with a 5-node network.
This scenario shows how to:
1. Connect to nodes
2. Monitor network state
3. Perform basic network operations
4. Observe network behavior

Usage:
    warnet run scenarios/my_first_attack_5kinv.py
"""

import time
from commander import Commander


class MyFirstAttack5KInv(Commander):
    def set_test_params(self):
        # This scenario works with any number of nodes
        self.num_nodes = 0

    def add_options(self, parser):
        parser.description = "Your first attack scenario - basic network interaction"
        parser.usage = "warnet run scenarios/my_first_attack_5kinv.py [options]"
        parser.add_argument(
            "--wait-time",
            dest="wait_time",
            default=5,
            type=int,
            help="Time to wait between operations (default 5 seconds)",
        )

    def run_test(self):
        """Main test logic"""
        self.log.info("🚀 Starting My First Attack - 5K INV scenario")
        
        # Step 1: Wait for all nodes to be ready
        self.log.info("Step 1: Waiting for all nodes to be ready...")
        if len(self.nodes) > 1:
            self.wait_for_tanks_connected()
            self.log.info("✓ All nodes are ready and connected")
        else:
            self.log.info("✓ Single node is ready")
        
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
        
        self.log.info("🎉 My First Attack scenario completed successfully!")

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
            
            # For a single node, connections might be 0 which is fine
            if connection_count == 0:
                self.log.info(f"  - Note: Single node network (no peers expected)")

    def generate_initial_blocks(self):
        """Generate some initial blocks to create funds"""
        # Use the first node to generate blocks
        node0 = self.nodes[0]
        miner_wallet = self.ensure_miner(node0)
        address = miner_wallet.getnewaddress()
        
        # Generate 101 blocks to create mature coinbase outputs
        self.log.info("Generating 101 blocks on node 0...")
        self.generatetoaddress(node0, 101, address, sync_fun=self.sync_all)
        
        # Check that all nodes have the same block count
        block_counts = [node.getblockcount() for node in self.nodes]
        if len(set(block_counts)) == 1:
            self.log.info(f"✓ All nodes synchronized at block {block_counts[0]}")
        else:
            self.log.warning(f"⚠️  Nodes have different block counts: {block_counts}")

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
            self.log.info(f"Created transaction {i+1}: {txid[:16]}...")
            
            # Wait a bit between transactions
            time.sleep(0.5)
        
        # Wait for transactions to propagate
        self.sync_all()

    def monitor_transaction_propagation(self):
        """Monitor how transactions propagate through the network"""
        self.log.info("Monitoring transaction propagation...")
        
        # Wait a bit for transactions to propagate
        time.sleep(self.options.wait_time)
        
        # Check mempool on all nodes
        for i, node in enumerate(self.nodes):
            mempool = node.getrawmempool()
            self.log.info(f"Node {i} mempool: {len(mempool)} transactions")
            
            # Show some transaction details
            if mempool:
                txid = list(mempool)[0]
                tx_info = node.getmempoolentry(txid)
                fee = tx_info.get('fee', 'unknown')
                self.log.info(f"  Sample transaction: {txid[:16]}... (fee: {fee})")


def main():
    MyFirstAttack5KInv().main()


if __name__ == "__main__":
    main() 
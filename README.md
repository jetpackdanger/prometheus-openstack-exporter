# Prometheus Swift account exporter

Exposes per-account [OpenStack Swift](https://swift.openstack.org/) metrics to [Prometheus](https://prometheus.io/).

So far this has only been tested against a Swift 1.13.1 cluster.

# Deployment

## Requirements

Install prometheus_client:
```
pip install prometheus_client
```

prometheus-swift-account-exporter must run on a machine that has an
always-current copy of the Swift rings, and with access to the Swift
storage nodes.  A swift-proxy node will typically fit the bill.

## Installation

```
# Copy example config in place, edit to your needs
sudo cp prometheus-swift-account-exporter.yaml /etc/prometheus/

## Systemd
# Install job
sudo cp prometheus-swift-account-exporter.service /etc/systemd/system/


# create default config location
sudo sh -c 'echo "CONFIG_FILE=/etc/prometheus-swift-account-exporter/prometheus-swift-account-exporter.yaml">/etc/default/prometheus-swift-account-exporter'


# Start
sudo start prometheus-swift-account-exporter
```

Or to run interactively:

```
./prometheus-swift-account-exporter prometheus-swift-account-exporter.yaml

```

# Configuration

Configuration options are documented in prometheus-swift-account-exporter.yaml shipped with this project.

# Prometheus Swift account exporter

Exposes per-account [OpenStack Swift](https://swift.openstack.org/) metrics to [Prometheus](https://prometheus.io/).

So far this has only been tested against a Swift 1.13.1 cluster.

## How does this work?

Fairly simply!  Given a copy of the Swift rings (in fact, we just need
account.ring.gz) we can load this up and then ask it where particular
accounts are located in the cluster.  We assume that Swift is
replicating properly, pick a node at random, and ask it for the
account's statistics with an HTTP HEAD request, which it returns.

## How hard would it be to export usage by container?

Sending a GET request to the account URL yields a list of containers
(probably paginated, so watch out for that!).  In order to write a
container-exporter, one could add some code to fetch a list of
containers from the account server, load up the container ring, and
then use container_ring.get_nodes(account, container) and HTTP HEAD on
one of the resulting nodes to get a containers' statistics, although
without some caching cleverness this will scale poorly.

## Deployment

### Requirements

Install prometheus_client:
```
pip install prometheus_client
```

prometheus-swift-account-exporter must run on a machine that has an
always-current copy of the Swift rings, and with access to the Swift
storage nodes.  A swift-proxy node will typically fit the bill.

### Installation

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

## Configuration

Configuration options are documented in prometheus-swift-account-exporter.yaml shipped with this project.

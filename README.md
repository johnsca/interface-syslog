# Overview

This interface layer handles the communication between Flume Syslog and an
rsyslog forwarding service (e.g. `rsyslog-forwarder-ha`).


# Usage

## Provides

Charms providing this interface are able to receive/consume system logs from
remote clients. This interface layer will set the following states, as
appropriate:

  * `{relation_name}.joined` The provider charm has been related to a client.
  The provider can get the number of clients related to it by calling
  `{relation_name}.client_count()`.


Provider example:

```python
@when('client.joined')
def log_client_count(client):
    log("Receiving syslog data for %s clients" % client.client_count())
```


## Requires

Charms requiring this interface gather logs and forward them to a provider.
This interface layer will set the following states, as appropriate:

  * `{relation_name}.joined` The client charm has been related to a provider.
  The client can get a list of IP addresses of all related providers by
  calling `{relation_name}.hosts()`.


Client example:

```python
@when('syslog.joined')
def register_rsyslog_servers(syslog):
    my_service.register(syslog.hosts())
```


# Contact Information

- <bigdata@lists.ubuntu.com>

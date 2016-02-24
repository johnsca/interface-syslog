# Overview

This interface layer handles the communication between the Flume Syslog and the rsyslog-forwarder service.


# Usage

## Provides

Charms providing this interface are able to receive/consume system logs.

This interface layer will set the following states, as appropriate:

  * `{relation_name}.joined`   The relation to a syslog producer has been initialized.


## Requires

Charms requiring this interface gather logs and forward them to a provider.

This interface layer will set the following states, as appropriate:

  * `{relation_name}.joined`   The relation to a syslog consumer has been initialized.
    The charm can then access the list of attached consumers via the method:

    * `hosts()`

An example use might be:

```python
@when('syslog.joined')
def syslog_joined(syslog):
    service.register(syslog.hosts())
```

# Contact Information

- <bigdata@lists.ubuntu.com>

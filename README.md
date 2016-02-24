# Overview

This interface layer handles the communication between the Flume Syslog and the rsyslog-forwarder service.


# Usage

## Provides

Charms providing this interface are able to recieve/consume system logs.

This interface layer will set the following states, as appropriate:

  * `{relation_name}.related`   The relation to a syslog producer has been initialized.
    If you are providing a service, you can use the following method to pass the port of the service to the
    other end of the relation:
      * `send_port(port)`

  * `{relation_name}.available`   The relation to a syslog producer has been established.

For example, let's say that a charm recieves a connection from a syslog producer. 
The charm providing the log ingestion service should use this interface in the following way:

```python
@when('syslog.related')
@when_not('syslog.available')
def syslog_forward_related(syslog):
    hookenv.status_set('waiting', 'Waiting for the connection to syslog producer.')
    syslog.send_port(hookenv.config()['source_port'])
```


## Requires

This part of the relation has not been implemented yet.

# Contact Information

- <bigdata@lists.ubuntu.com>

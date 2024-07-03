# OBM Channels

OBM Channels is a library designed to manage communication channels for OBM (Order Booking Management) systems. This repository provides tools to create, manage, and monitor various communication channels effectively.

## Features

- **Channel Creation**: Create new communication channels with ease.
- **Channel Management**: Manage existing channels, including modifications and deletions.
- **Stat**: Get stat.

## Installation

To install the library, you can use pip:

```sh
pip install obm_channels
```

## Usage

### Creating channel

To create a new channel, use the following code:

```python
from obm_channels import ChannelManager

manager = ChannelManager()
channel = manager.create_channel(name="New Channel", type="river")
```

### Managing Channels
To update or delete a channel, you can use the following methods:

```python
# Updating a channel
channel.update(name="Updated Channel Name")

# Deleting a channel
manager.delete_channel(channel_id=channel.id)

```
## Get Stat for model
You can get stat of stohastic model using:
```python
stats = manager.get_channel_stats(channel_id=channel.id)
print(stats)
```
## License
This project is licensed under the Apache License.

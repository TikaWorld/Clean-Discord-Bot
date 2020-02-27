from entities.channel import Channel


class ChannelManager:
    channel = None

    def set_channel(self, channel_id):
        self.channel = Channel(channel_id)

    def get_channel(self):
        return self.channel


channel_manager = ChannelManager()

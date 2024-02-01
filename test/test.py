from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleSIP(Protocol):
    def connectionMade(self):
        # 处理连接建立
        pass

    def dataReceived(self, data):
        # 处理接收到的数据
        print("Data received:", data)

# 创建工厂
factory = Factory()
factory.protocol = SimpleSIP

# 监听SIP端口
reactor.listenUDP(5060, factory)
reactor.run()
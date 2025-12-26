class Firewall:
    def __init__(self, open_ports: list):
        self.__open_ports = open_ports
        
    def open_port(self, port):
        if port not in self.__open_ports:
            self.__open_ports.append(port)
    
    def close_port(self, port):
        if port in self.__open_ports:
            self.__open_ports.remove(port)
    
    def is_port_open(self, port):
        return port in self.__open_ports

    def show_open_ports(self):
        print(*self.__open_ports)
    
class SecureFirewall(Firewall):
    def __init__(self, open_ports: list, blocked_ips: list, logs: list):
        super().__init__(open_ports)
        self.blocked_ips = blocked_ips
        self.logs = logs
    
    def block_ip(self, ip):
        if ip not in self.blocked_ips:
            self.blocked_ips.add(ip)
    
    def attempt_connection(self, port, ip):
        if self.is_port_open(port) and ip not in self.blocked_ips:
            self.logs.append(f"Успешное подключение к {ip} по порту {port}")
        else:
            self.logs.append(f"Неуспешное подключение к {ip} по порту {port}")

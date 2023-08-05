import socket
import netifaces
import ipaddress

def get_local_network():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ip_info = addresses[netifaces.AF_INET][0]
            if "addr" in ip_info and "netmask" in ip_info:
                ip_address = ip_info["addr"]
                netmask = ip_info["netmask"]
                network = ipaddress.IPv4Network(f"{ip_address}/{netmask}", strict=False)
                return network
    return None

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports

def scan_local_network(ports):
    local_network = get_local_network()
    if local_network:
        open_ports_by_ip = {}
        for ip in local_network:
            open_ports = scan_ports(str(ip), ports)
            if open_ports:
                open_ports_by_ip[ip] = open_ports
                break
        return open_ports_by_ip
    else:
        return None

if __name__ == "__main__":
    target_ports = [5000]

    open_ports_by_ip = scan_local_network(target_ports)
    print(open_ports_by_ip)

    if open_ports_by_ip:
        for ip, open_ports in open_ports_by_ip.items():
            print(f"Các cổng mở trên {ip}: {open_ports}")
    else:
        print("Không tìm thấy dải mạng nào hoặc không có cổng mở nào được tìm thấy trong mạng nội bộ của bạn.")

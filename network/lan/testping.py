import pyping
status = False
broker = "iot.eclipse.org"
porta = 1883
try:
    r = pyping.ping('www.google.com')    # But it's udp, not real icmp
    print  (r.max_rtt,r.avg_rtt,r.min_rtt)
    status = True
except Exception, e:
    localnet = pyping.ping("192.168.0.1")	
    print (localnet.max_rtt,localnet.avg_rtt,localnet.min_rtt)
    status = True









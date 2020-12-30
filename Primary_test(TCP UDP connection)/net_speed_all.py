# coding: utf-8

# In[3]:


# coding: utf-8 
try:
    import psutil
    
   
            
except ImportError:
    print('Error: psutil module not found!')
    exit()

def get_key(net_dev):
    recv = {}
    sent = {}

    recv.setdefault(net_dev, psutil.net_io_counters(pernic=True).get(net_dev).bytes_recv)
    sent.setdefault(net_dev, psutil.net_io_counters(pernic=True).get(net_dev).bytes_sent)

    return recv, sent

def get_rate(func, net_dev):
	import time
	old_recv, old_sent = func(net_dev)
	time.sleep(1)
	now_recv, now_sent = func(net_dev)  # 当前所收集的数据

	net_in = {}
	net_out = {}
	
	net_in.setdefault(net_dev, (now_recv.get(net_dev) - old_recv.get(net_dev)) )
	net_out.setdefault(net_dev, (now_sent.get(net_dev) - old_sent.get(net_dev)) )

	return net_in, net_out

while 1:
    try:
         net_in, net_out = get_rate(get_key, '以太网 2')
         
         print('%s\nInput:\t %-5sB/s\nOutput:\t %-5sB/s\n' % ('以太网 2', net_in.get('以太网 2'), net_out.get('以太网 2')))


  
    except KeyboardInterrupt:
        exit()


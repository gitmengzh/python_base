# 连接单个redis服务器
import redis

r = redis.Redis(host='',port=7000, password="!Wang")


res = r.set('dsp_redis_test','success')
res1 = r.get('dsp_redis_test')
print(res1)



# redis 集群连接
'''
from rediscluster import RedisCluster
startup_nodes = [
    {"host": "172.31.2.92", "port": 7001},
    {"host": "172.31.4.251", "port": 7001},
    {"host": "172.31.1.189", "port": 7001},
    {"host": "172.31.5.73", "port": 7001},
    {"host": "172.31.2.210", "port": 7001},
    {"host": "172.31.4.19","port": 7001}
]
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#rc.set('dsp_test_1','pbs_1')

res = rc.hget('dsp_ad_slot_q5tn4f55','cost_type')
res1 = rc.hvals('dsp_serving_42')
res2 = rc.smembers('dsp_serving_list')
res4 = rc.get('dsp_package_1')
print(res)
'''

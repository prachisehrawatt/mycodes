def build_config(*args,**kwargs):

    dict={}
    
    for i in args:
        for keys,values in i.items():
            #print(keys,values)
            if keys not in dict:
                dict[keys]=values #adding new values to dict
            elif keys in dict:
                dict[keys]=values #updation 
           
        for keys,values in kwargs.items():
            if keys not in dict:
                dict[keys]=values #adding new values to dict
            elif keys in dict:
                dict[keys]=values #updation 
            
    print(dict)

default_layer = {"host": "localhost", "port": 8080, "secure": False}
env_layer = {"port": 9000, "debug": True}
user_layer = {"debug": False, "profile": "developer"}

build_config(default_layer,env_layer,user_layer,secure = True, timeout = 30)

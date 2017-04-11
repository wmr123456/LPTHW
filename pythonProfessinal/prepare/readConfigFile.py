#coding=utf-8
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("config.ini")

#获取global的属性
print config.get("global1","ip")
print config.get("global1","username")

#获取所有的global2的属性
print  config.get('global2','username')

#获取所有的组名称
print config.sections()

#更新配置文件属性的值
config.set("global1", "username", "ccc")
config.get("global1", "username")
config.write(open("config.ini","w"))
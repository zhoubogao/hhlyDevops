#-*-coding:utf-8-*-
import os
from app import app
from models import db , User, Role, Device, Platforms_info, Ip, Project, App
from werkzeug.security import generate_password_hash
def build_first_db():
    """
    Populate a small db with some example entries.
    """
    db.drop_all()
    db.create_all()

    anonymous = Role(name = u'Anonymous', description = u'匿名用户')
    admin = Role(name = u'Admin', description = u'管理员')
    develop = Role(name = 'Develop', description = u'开发人员')
    test = Role(name = 'Test', description = u'测试人员')
    ops = Role(name = 'Ops', description = u'运维人员')

    admin_user = User(real_name = u'admin', 
                      email = u'admin@13322.com', 
                      login=u"admin", 
                      password=generate_password_hash(u"admin"),
                      roles=[admin]
                      )

    anonymous_user = User(real_name = u'anonymous',
                          email = u'anonymous@13322.com', 
                          login=u"anonymous", 
                          password=generate_password_hash(u"anonymous"),
                          roles=[anonymous]
                          )

    ip1 = Ip(isp = u'电信',
             use = u'在用', 
             ip=u"1.1.1.1", 
             mask=(u"255.255.255.0"),
             mac=(u"44a8-422a-20ff"),
             route=(u"1.1.1.254"),
             switch_port=(u"5F-U09 G1/0/32"),
             )

    ip2 = Ip(isp = u'电信',
             use = u'在用', 
             ip=u"1.1.1.2", 
             mask=(u"255.255.255.0"),
             mac=(u"44a8-422a-20ff"),
             route=(u"1.1.1.254"),
             switch_port=(u"5F-U09 G1/0/32"),
             )

    ip3 = Ip(isp = u'内网',
             use = u'在用', 
             ip=u"1.1.1.3", 
             mask=(u"255.255.255.0"),
             mac=(u"44a8-422a-20ff"),
             route=(u"1.1.1.254"),
             switch_port=(u"5F-U09 G1/0/32"),
             )

    ip4 = Ip(isp = u'联通',
             use = u'在用', 
             ip=u"1.1.1.4", 
             mask=(u"255.255.255.0"),
             mac=(u"44a8-422a-20ff"),
             route=(u"1.1.1.254"),
             switch_port=(u"5F-U09 G1/0/32"),
             )

    app1 = App(app = u'kf_scsa', 
             description=u"客服我也不知道", 
             domain=(u"kf.13322.com"),
             port=(u"8031-8032"),
             ps=(u"没什么事"),
             )

    app2 = App(app = u'gamemanager', 
             description=u"游戏我也不知道", 
             domain=(u"game.13322.com"),
             port=(u"8031-8032"),
             ps=(u"没什么事"),
             )

    app3 = App(app = u'webPlatform', 
             description=u"公共我也不知道", 
             domain=(u"p.13322.com"),
             port=(u"8031-8032"),
             ps=(u"没什么事"),
             )

    app4 = App(app = u'wechat-server2', 
             description=u"wx我也不知道", 
             domain=(u"wx.13322.com"),
             port=(u"8031-8032"),
             ps=(u"没什么事"),
             )

    project1 = Project(name = u'体彩项目', apps = [app1])
    project2 = Project(name = u'福彩项目', apps = [app2])
    project3 = Project(name = u'公共平台项目', apps = [app3])
    project4 = Project(name = u'客服系统项目', apps = [app4])



    device1 = Device(device_num = u'02-1331',
             device_name = u'5F-U10', 
             idc=u"东莞", 
             location=(u"5F-U10"),
             hardware_type=(u"DELL-2U"),
             brand=(u"DELL"),
             fast_repair_code=(u"没什么事"),
             cpu=(u"没什么事"),
             memory=(u"没什么事"),
             disk=(u"没什么事"),
             ips=[ip1],
             apps = [app1],
             )

    device2 = Device(device_num = u'02-1331',
             device_name = u'5F-U12', 
             idc=u"东莞", 
             location=(u"5F-U10"),
             hardware_type=(u"DELL-2U"),
             brand=(u"DELL"),
             fast_repair_code=(u"没什么事"),
             cpu=(u"没什么事"),
             memory=(u"没什么事"),
             disk=(u"没什么事"),
             ips=[ip2],
             apps = [app2],
             )

    platforms_info1 = Platforms_info(platform = u'阿里云管理控制台',
                                     description = u'申请云服务器及域名解析', 
                                     url=u"http://www.aliyun.com/", 
                                     username=u"hhlyadmin",
                                     password=(u"hhlyadmin"),
                                     ps=(u"登陆进入后，依次点击:\
                                     	订单管理-我的租用-最后面详细\
                                     	下方图标-进入之后\
                                     	点击IP即可查看流量图"
                                     	),
                                     )

    platforms_info2 = Platforms_info(platform = u'DNS盾',
                                     description = u'13322.com域名A记录解析网站', 
                                     url=u"http://www.dnsdun.com", 
                                     username=u"hhlyadmin@13322.com",
                                     password=(u"hhlyadmin@13322.com"),
                                     ps=(u"登陆进入后"
                                     	),
                                     )



    db.session.add(anonymous)
    db.session.add(admin)
    db.session.add(develop)
    db.session.add(test)
    db.session.add(ops)
    db.session.add(admin_user)
    db.session.add(anonymous_user)

    db.session.add(ip1)
    db.session.add(ip2)
    db.session.add(ip3)
    db.session.add(ip4)
    db.session.add(app1)
    db.session.add(app2)
    db.session.add(app3)
    db.session.add(app4)
    db.session.add(project1)
    db.session.add(project2)
    db.session.add(project3)
    db.session.add(project4)
    db.session.add(device1)
    db.session.add(device2)
    db.session.add(platforms_info1)
    db.session.add(platforms_info2)

    db.session.commit()

    return


if __name__ == '__main__':

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_first_db()
    # Start app
    app.run(debug=True)
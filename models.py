#-*-coding:utf-8-*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from flask_login import UserMixin
# Create user model.
db = SQLAlchemy()

users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Role(db.Model):  # 权限表
    """docstring for Role"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(length=254), unique=True, nullable=False)
    description = db.Column(db.Unicode(length=254), )

    # Required for administrative interface
    def __unicode__(self):
        return self.name

class User(db.Model, UserMixin): 
    """docstring for User"""
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.Unicode(length=255), nullable=False)
    email = db.Column(db.Unicode(length=254), nullable=False)
    login = db.Column(db.Unicode(length=254), unique=True, nullable=False)
    password = db.Column(db.Unicode(length=255), nullable=False)
    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('users',),
    )

    # Required for administrative interface
    def __unicode__(self):
        return self.login

class Platforms_info(db.Model):
    """docstring for Platforms_info"""
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.Unicode(length=254), unique=True, nullable=False)
    description = db.Column(db.Unicode(length=254), )
    url = db.Column(db.Unicode(length=254), )
    username = db.Column(db.Unicode(length=254), )
    password = db.Column(db.Unicode(length=254), )
    ps = db.Column(db.Unicode(length=254), )

    # Required for administrative interface
    def __unicode__(self):
        return self.platform

devices_apps = db.Table(
    'devices_apps',
    db.Column('device_id', db.Integer, db.ForeignKey('device.id')),
    db.Column('app_id', db.Integer, db.ForeignKey('app.id'))
)

class Device(db.Model):
    """docstring for Device"""
    id = db.Column(db.Integer, primary_key=True)
    device_num = db.Column(db.Unicode(length=254), )
    device_name = db.Column(db.Unicode(length=254), unique=True, nullable=False)
    idc = db.Column(db.Unicode(length=254), nullable=False)
    ips = db.relationship('Ip', 
                          backref='device', 
                          )
    apps = db.relationship('App',
                               secondary=devices_apps,
                               backref=db.backref('device',),
                               )
    location = db.Column(db.Unicode(length=254), )
    used_to = db.Column(db.Unicode(length=254), )
    hardware_type = db.Column(db.Unicode(length=254), )
    brand = db.Column(db.Unicode(length=254), )
    buy_date = db.Column(db.DateTime, )
    fast_repair_code = db.Column(db.Unicode(length=254), )
    cpu = db.Column(db.Unicode(length=254), )
    memory = db.Column(db.Unicode(length=254), )
    disk = db.Column(db.Unicode(length=254), )

    # Required for administrative interface
    def __unicode__(self):
        return self.device_name

class Ip(db.Model):
    """docstring for Ip"""
    id = db.Column(db.Integer, primary_key=True)
    isp = db.Column(db.Unicode(length=254), )
    use = db.Column(db.Unicode(length=254), nullable=False)
    ip = db.Column(db.Unicode(length=254), unique=True, nullable=False)
    mask = db.Column(db.Unicode(length=254), )
    mac = db.Column(db.Unicode(length=254), )
    route = db.Column(db.Unicode(length=254), )
    switch_port = db.Column(db.Unicode(length=254), )
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    username = db.Column(db.Unicode(length=254), )
    password = db.Column(db.Unicode(length=255), )

    # Required for administrative interface
    def __unicode__(self):
        return self.isp+ u':' + self.ip

class Project(db.Model):
    """docstring for Project"""
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.Unicode(length=254),  unique=True, nullable=False)
    apps = db.relationship('App', 
                          backref='project_name', 
                           )

    # Required for administrative interface
    def __unicode__(self):
        return self.project

class Domain(db.Model):
    """docstring for Domain"""
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.Unicode(length=254),  unique=True, nullable=False)
    app = db.Column(db.Integer, db.ForeignKey('app.id'))

    # Required for administrative interface
    def __unicode__(self):
        return self.domain

class Port(db.Model):
    """docstring for Port"""
    id = db.Column(db.Integer, primary_key=True)
    port = db.Column(db.Unicode(length=254),  unique=True, nullable=False)
    app = db.Column(db.Integer, db.ForeignKey('app.id'))

    # Required for administrative interface
    def __unicode__(self):
        return self.port

class App(db.Model):
    """docstring for App"""
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.Integer, db.ForeignKey('project.id'))
    app = db.Column(db.Unicode(length=254),  unique=True, nullable=False)
    description = db.Column(db.Unicode(length=254), )
    domains = db.relationship('Domain', 
                          backref='app_name', 
                           )
    ports = db.relationship('Port', 
                          backref='app_name', 
                           )
    ps = db.Column(db.Unicode(length=254), )

    # Required for administrative interface
    def __unicode__(self):
        return self.app

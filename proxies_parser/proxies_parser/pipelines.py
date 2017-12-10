# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import Session
import os

Base = declarative_base()


class Proxy(Base):
    __tablename__ = "proxy"
    id = Column(Integer, primary_key=True)
    ip_address = Column(String)
    port = Column(String)


class ProxiesParserPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        proxy = Proxy(ip_address=item['ip_address'], port=item['port'])
        self.session.add(proxy)
        return item

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

    def open_spider(self, spider):
        print("CONNECT")
        print(__file__)
        basename = os.path.join(os.path.dirname(__file__), "proxy.db")
        self.engine = create_engine("sqlite:///%s" % basename, echo=False)
        if not os.path.exists(basename):
            Base.metadata.create_all(self.engine)
        self.session = Session(bind=self.engine)

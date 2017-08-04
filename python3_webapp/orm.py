
__author__ = 'now'
import asyncio,logging
import aiomysql

def log(sql,args=()):
	logging.info('sql: %s' % sql)


async def create_pool(loop,**kw):
	

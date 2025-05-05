# coding=utf-8
from __future__ import print_function, absolute_import
from typing import List, NoReturn, Text
from gm.api import *
from gm.csdk.c_sdk import BarLikeDict2, TickLikeDict2
from gm.model import DictLikeAccountStatus, DictLikeExecRpt, DictLikeIndicator, DictLikeOrder, DictLikeParameter
from gm.pb.account_pb2 import AccountStatus, ExecRpt, Order
from gm.pb.performance_pb2 import Indicator
from gm.pb.rtconf_pb2 import Parameter
from gm.utils import gmsdklogger
import random
from datetime import datetime, timedelta
import numpy as np
import requests
import json
import pandas as pd

def init(context):
    global glok
    # type: (Context) -> NoReturn
    # 示例定时任务: 每天 14:50:00 调用名字为 my_schedule_task 函数
    # 示例订阅浦发银行，60s的频率

    # 设置要进行回测的合约
    #context.k = "SHSE.688011"
    context.k = "SHSE.600000"
    context.count=600
    # 订阅行情
    context.lastlastnav=0
    context.lastnav=0
    context.lastlastlastnav=0
    context.nav=0
    context.gg=0
    context.gg2=0
    context.swi=0
    context.swi2=0
    subscribe(symbols=context.k, frequency='tick')
    schedule(schedule_func=my_schedule_task, date_rule='1d', time_rule='14:50:00')
    schedule(schedule_func=my_schedule_task3, date_rule='1d', time_rule='15:30:00')
    schedule(schedule_func=my_schedule_task2, date_rule='1d', time_rule='10:10:00')
    # 定义全局常量示例
    context.timetick = 0
    context.ticks=[]


def my_schedule_task(context):
    # type: (Context) -> NoReturn
    order_target_percent(context.k,0,1,2)
    context.gg=1
    print("一天结束了")
    
def my_schedule_task3(context):
    context.lastlastlastnav=context.lastlastnav
    context.lastlastnav=context.lastnav
    context.lastnav=context.nav
    context.nav=context.account().cash["nav"]
    if context.lastnav != 0 and context.nav != 0 and context.lastlastnav != 0 and context.lastlastlastnav != 0:
        germ=context.nav/context.lastnav
        germ2=context.lastnav/context.lastlastnav
        germ3=context.lastlastnav/context.lastlastlastnav
        kk2=germ2-germ3
        kk1=germ-germ2
        a=datetime.strptime(context.now.strftime("%Y-%m-%d"),"%Y-%m-%d")
        b=timedelta(days=10)
        c=a-b
        #vk=get_history_symbol(symbol=context.k, start_date=c.strftime("%Y-%m-%d"), end_date=a.strftime("%Y-%m-%d"), df=False)
        #if len(vk)>1:
            #get2=vk[-1]["pre_close"]/vk[-2]["pre_close"]
            #print(get2)
            #print(germ)
        if kk2<kk1:
            if context.swi2==0:
                context.count=context.count+50
                context.swi2=1
            elif context.swi2==1:
                context.count=context.count+50
                print("持续变多")
            elif context.swi2==2:
                context.count=context.count-50
                print("持续变少")
        if kk2>kk1:
            if context.swi2==0:
                context.count=context.count+50
                context.swi2=1
            elif context.swi2==1:
                context.count=context.count-50
                context.swi2=2
                print("太多了，该变少了")
            elif context.swi2==2:
                context.count=context.count+50
                print("太少了，该变多了")
                context.swi2=1
        if context.count >= 900:
            context.count=800
        if context.count < 450:
            context.count=500
        print(context.count,germ2,germ)
            

def my_schedule_task2(context):
    context.gg=0
    print("一天开始了")

    
    
def on_tick(context, tick):
    # type: (Context, TickLikeDict2) -> NoReturn
    if context.gg == 0:
        context.timetick = context.timetick + 1
        if tick['price'] != 0:
            if len(context.ticks)>=context.count:
                del context.ticks[0]
            context.ticks.append(tick['price'])
        if len(context.ticks)>=context.count:
            avg=np.mean(context.ticks)
            #print(context.ticks)
            #print(avg)
            if tick['price'] >= 1.001*avg and context.swi != 1:
                context.swi=1
                print(context.k,"空仓")
                order_target_percent(context.k,0,1,2)
            if tick['price'] <= 0.999*avg and context.swi != 2:
                context.swi=2
                print(context.k,"满仓")
                order_target_percent(context.k,1,1,2)


            
        

if __name__ == '__main__':
    '''
        strategy_id策略ID, 由系统生成
        filename文件名, 请与本文件名保持一致
        mode运行模式, 实时模式:MODE_LIVE回测模式:MODE_BACKTEST
        token绑定计算机的ID, 可在系统设置-密钥管理中生成
        backtest_start_time回测开始时间
        backtest_end_time回测结束时间
        backtest_adjust股票复权方式, 不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
        backtest_initial_cash回测初始资金
        backtest_commission_ratio回测佣金比例
        backtest_slippage_ratio回测滑点比例
        backtest_match_mode市价撮合模式，以下一tick/bar开盘价撮合:0，以当前tick/bar收盘价撮合：1
    '''
    backtest_start_time = str(datetime.now() - timedelta(days=300))[:19]
    backtest_end_time = str(datetime.now())[:19]
    run(strategy_id='822e519c-27bd-11f0-ad46-00d861bb7c83',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='56cdc93a74c02ff68791fee319a2a00d159406fd',
        backtest_start_time=backtest_start_time,
        backtest_end_time=backtest_end_time,
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=1000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001,
        backtest_match_mode=1)

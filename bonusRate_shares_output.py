# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
import pymysql
import pandas as pd

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime

engine_Nas_Mons = create_engine('mysql+pymysql://root:123456@localhost:3306/Trust')


sql_1 = 'select * from nikki225_bonus_  ; '
sql_2 = 'select * from nikki225_followingShares  ; '

ln = os.getcwd()


def savedt():

    df_js225 = pd.read_sql_query(sql_2, engine_Nas_Mons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "nikki225_followingShares")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)


    df_js225 = pd.read_sql_query(sql_1, engine_Nas_Mons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "nikki225_bonus_")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)


if __name__ == '__main__':
    savedt()
#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14) 
date = np.array(['Mar-18','Apr-18','May-18','Jun-18','Jul-18','Aug-18','Sep-18','Oct-18','Nov-18','Dec-18','Jan-19','Feb-19']) 

def plt_active():
	active_ne = np.array([2994.20,3234.60,3159.30,2902.60,2762.40,2883.50,2874.00,3395.00,3176.60,2702.10,2374.20,2469.80])
	active_qq = np.array([4898.80,5348.10,5188.50,4907.90,4838.70,4941.50,4681.40,5562.00,5132.20,4432.00,4191.40,4697.50])
	plt.plot(date, active_qq, label='QQ Music',c='g')
	plt.plot(date, active_ne, label='NetEase Cloud Music',c='r')
	plt.title(u"日均活跃人数(万)", fontproperties=font)
	plt.legend()
	plt.show()

def plt_ret():
	ret_ne = np.array([78.20,89.00,85.10,81.10,79.20,78.70,74.00,68.10,69.30,70.10,68.40,69.60])
	ret_qq = np.array([79.60,78.20,71.40,69.40,68.10,63.80,59.20,58.40,59.30,61.70,62.30,62.40])
	plt.plot(date, ret_qq, label='QQ Music',c='g')
	plt.plot(date, ret_ne, label='NetEase Cloud Music',c='r')
	plt.title(u"次月留存率(%)", fontproperties=font)
	plt.legend()
	plt.show()

def plt_on():
	ret_ne = np.array([4.5,4.6,4.3,4,4,4,3.9,4.2,4.2,4.2,4.1,4.2])
	ret_qq = np.array([3.6,3.6,3.5,3.3,3.3,3.3,3.3,3.3,3.4,3.5,3.4,3.5])
	plt.plot(date, ret_qq, label='QQ Music',c='g')
	plt.plot(date, ret_ne, label='NetEase Cloud Music',c='r')
	plt.title(u"人均单日启动次数(次)", fontproperties=font)
	plt.legend()
	plt.show()

def plt_use():
	ret_ne = np.array([21.3,21.1,19.3,17.1,16.2,16.1,15.8,16.8,17,16.9,16.8,17.1])
	ret_qq = np.array([15.8,15.4,13.8,13,12.4,12.1,12,11.6,11.6,11.8,12,12.3])
	plt.plot(date, ret_qq, label='QQ Music',c='g')
	plt.plot(date, ret_ne, label='NetEase Cloud Music',c='r')
	plt.title(u"人均单日使用时长(分钟)", fontproperties=font)
	plt.legend()
	plt.show()



if __name__ == '__main__':	
	plt_use();	
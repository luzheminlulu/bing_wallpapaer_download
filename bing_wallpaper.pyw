import requests
import random
import re
import os
import datetime

dir  =  os.path.dirname(os.path.abspath(__file__))+"\\"

def get_image():
	user_agent = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",]
	headers = {'User-Agent': random.choice(user_agent)}
	url="https://cn.bing.com/"
	response = requests.get(url,headers=headers)
	
	#print(response.text)
	image_url=re.findall(r'th\?id=.*?UHD\.jpg',response.text)
	url+=image_url[0]
	#print(url)
	
	utc_today = datetime.datetime.utcnow()
	utc_today = utc_today.strftime("%Y_%m_%d_")
	#print(utc_today)
	
	image_name = re.findall(r'th\?id=(.*?UHD\.jpg)',image_url[0])
	#print(image_name)
	img_save_path=dir+"images_download\\"+utc_today+image_name[0]  
	img = requests.get(url)
	with open(img_save_path, "wb") as fwi:
		fwi.write(img.content)
		print(img_save_path + "下载成功")
	
if __name__ == '__main__':
	try:
		get_image()
	except Exception as e:
		print(e)

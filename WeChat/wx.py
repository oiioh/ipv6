import logging
import requests
import time
import os
from datetime import datetime

# 记录文件路径
LOG_FILE_PATH = os.path.abspath("wx.txt")

# 配置日志
logging.basicConfig(
     level=logging.INFO,
     format='%(asctime)s - %(levelname)s - %(message)s')

# 定义企业微信机器人的Webhook URL
WECHAT_WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=11111111"

def get_public_ipv6():
    """获取公网IPv6地址"""
    try:
        response = requests.get('https://api6.ipify.org?format=json', timeout=10)
        response.raise_for_status()  # 如果响应状态码不是200，则抛出异常
        data = response.json()
        return data['ip']
    except requests.RequestException as e:
        logging.error(f"获取公网IPv6地址时发生错误:{e}")
        return None

def send_wechat_notification(ipv6):
    """向企业微信发送通知"""
    message = {
        "msgtype": "text",
        "text": {
            "content": f"https://[{ipv6}]"
        }
    }
    try:
        response = requests.post(WECHAT_WEBHOOK_URL, json=message, timeout=10)
        response.raise_for_status()  # 如果响应状态码不是200，则抛出异常
        result = response.json()
        if result['errcode'] == 0:
            logging.info("企业微信通知发送成功")
        else:
            logging.warning(f"企业微信通知发送失败:{result['errmsg']}")
    except requests.RequestException as e:
        logging.error(f"发送企业微信通知时发生错误:{e}")

def log_ipv6(ipv6):
    """记录IPv6地址到文件中，仅当ipv6有效时记录"""
    if ipv6:
        with open(LOG_FILE_PATH, 'w') as file:
            file.write(f"{ipv6}")
def read_last_ipv6():
    """读取上一次记录的IPv6地址"""
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                last_ipv6 = last_line.split(' - ')[-1]
                logging.info(f"上次的IPv6地址: {last_ipv6}")
                return last_ipv6
    return None

def main():
    """主函数，用于周期性检查IPv6地址的变化"""
    last_ipv6 = read_last_ipv6()
    while True:
        current_ipv6 = get_public_ipv6()
        logging.info(f"IPv6地址由{last_ipv6}更改为{current_ipv6}")
        if current_ipv6 and current_ipv6 != last_ipv6:
            logging.info(f"新的IPv6地址为:{current_ipv6}")
            log_ipv6(current_ipv6)
            send_wechat_notification(current_ipv6)
            last_ipv6 = current_ipv6  # 确保在这里正确更新last_ipv6
        else:
             logging.info("IPv6地址没有变化或未能获取到IPv6地址")
        time.sleep(1*60)  # 每分钟检查一次，避免频繁检查

if __name__ == "__main__":
    main()
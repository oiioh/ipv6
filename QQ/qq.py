import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import logging
import os

# 设置日志文件路径为绝对路径
LOG_FILE_PATH = os.path.abspath("qq.txt")

# 配置日志记录z
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_public_ipv6():
    """获取公网IPv6地址"""
    try:
        response = requests.get('https://api6.ipify.org?format=json')
        response.raise_for_status()  # 如果响应状态码不是200，则抛出异常
        data = response.json()
        return data['ip'] if 'ip' in data else None
    except requests.RequestException as e:
        logging.error(f"获取公网IPv6地址发生错误:{e}")
        return None

def send_email(to_email, subject, body):
    """发送邮件通知"""
    from_email = "11111111@qq.com"   #  发件人邮箱
    password = "11111111"  #  授权码
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = Header(from_email)
    msg['To'] = Header(to_email)
    msg['Subject'] = Header(subject)
    try:
        with smtplib.SMTP_SSL("smtp.163.com", 465) as server:  # 使用with语句自动关闭连接
            server.login(from_email, password)
            server.sendmail(from_email, [to_email], msg.as_string())
            logging.info("QQ邮箱发送成功")
    except smtplib.SMTPException as e:
        logging.error(f"QQ邮箱发送失败:{e}")

def read_last_ipv6():
    """从文件中读取上次的IPv6地址"""
    try:
        with open(LOG_FILE_PATH, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        logging.warning("第一次运行找不到文件")
        return None
    except Exception as e:
        logging.error(f"读取最后一个IPv6地址错误:{e}")
        return None

def write_last_ipv6(ipv6):
    """将当前的IPv6地址写入文件"""
    try:
        with open(LOG_FILE_PATH, 'w') as file:
            file.write(ipv6)
    except Exception as e:
        logging.error(f"写入最后一个IPv6地址错误:{e}")

def main():
    while True:
        # 每次循环开始时重新读取 last_ipv6
        last_ipv6 = read_last_ipv6()
        logging.info(f"上次记录的IPv6地址:{last_ipv6}")
        
        current_ipv6 = get_public_ipv6()
        logging.info(f"当前IPv6地址:{current_ipv6}")
        
        if current_ipv6 is not None:
            if current_ipv6 != last_ipv6:
                logging.info(f"IPv6由{last_ipv6 or 'unknown'}更改为{current_ipv6}")
                send_email("11111111@qq.com", "IPv6", f"https://[{current_ipv6}]")
                write_last_ipv6(current_ipv6)
                logging.info(f"已更新IPv6地址记录为:{current_ipv6}")
            else:
                logging.info("IPv6地址没有变化")
        else:
            logging.error("未能获取到当前公网IPv6地址")
        
        time.sleep(1*60) # 每隔1分钟检查一次

if __name__ == "__main__":
    main()
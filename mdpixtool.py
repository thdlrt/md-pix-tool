import re
import os
from urllib.parse import urlsplit
import requests
import concurrent.futures

# 本地化图片
def mode1(file_path):
    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 匹配图片链接(md风格图片)
    pattern = re.compile(r'!\[.*?\]\((http.*?)\)')
    urls = re.findall(pattern, content)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(download_image, url, file_path): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                local_image_path = future.result()
                if local_image_path is not None:
                    content = content.replace(url, local_image_path)
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')

    # 处理html格式图片
    pattern = re.compile(r'<img src="(http.*?)"')
    urls = re.findall(pattern, content)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(download_image, url, file_path): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                local_image_path = future.result()
                if local_image_path is not None:
                    content = content.replace(url, local_image_path)
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 图片下载、存储
def download_image(url, dir_path):
    local_path = os.path.join(os.path.dirname(dir_path), 'images')
    # 创建文件夹
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    # http请求
    try:
        response = requests.get(url, timeout=5)  # 设置timeout，防止请求时间过长
    except (requests.ConnectionError, requests.Timeout) as e:
        return None
    # 创建并写入文件
    file_path = os.path.join(local_path, urlsplit(url).path.split('/')[-1])
    with open(file_path, 'wb') as file:
        file.write(response.content)
    return './images' + '/' + urlsplit(url).path.split('/')[-1]

# 格式修正
def mode2(file_path):
    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'<img(.*?)>')
    urls = re.findall(pattern, content)
    for url in urls:
        # 提取信息
        match = re.search(r'src="(.*?)"', url)
        if not match:
            continue
        name = os.path.basename(match.group(1))
        content = content.replace(f'<img{url}>', f'![{name}]({match.group(1)})')
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)        



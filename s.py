import socket
import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.
sock = socket.socket()
sock.bind(('195.54.163.190', 8888))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    driver.get(data.decode());
    search_box = driver.find_element_by_tag_name('body').text
    conn.send(search_box.encode())
    conn.close()

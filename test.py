import pyautogui
import time


# 设置绘图区域的大小和位置
x, y = 150, 150
width, height = 500, 500

# 设置绘制的图形的颜色和线条宽度
color = 'blue'
thickness = 5

# 获取屏幕的大小
screenWidth, screenHeight = pyautogui.size()

# 点击屏幕上的指定位置打开绘图软件
pyautogui.click(x, y)

# 等待绘图软件加载完成
time.sleep(1)

# 将鼠标移动到绘图区域的左上角
pyautogui.moveTo(x, y)

# 按下鼠标左键并拖动到绘图区域的右上角
pyautogui.dragTo(x + width, y, duration=0.5, button='left')

# 拖动到绘图区域的右下角
pyautogui.dragTo(x + width, y + height, duration=0.5, button='left')

# 拖动到绘图区域的左下角
pyautogui.dragTo(x, y + height, duration=0.5, button='left')

# 拖动回绘图区域的左上角，形成一个闭合图形
pyautogui.dragTo(x, y, duration=0.5, button='left')



# 打开记事本应用程序
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('notepad')
pyautogui.press('enter')

# 等待记事本应用程序打开
time.sleep(2)

# 打出英文名言，记得将输入法切换为英文。
pyautogui.typewrite('To be, or not to be: that is the question.\nAsk not what your country can do for you, \nask what you can do for your country.\nI am the master of my fate,\n I am the captain of my soul.\n')

# 保存文件
pyautogui.hotkey('ctrl', 's')
time.sleep(2)

pyautogui.typewrite('test')
pyautogui.press('enter')

# 关闭记事本应用程序
pyautogui.hotkey('alt', 'f4')

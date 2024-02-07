# 获取鼠标坐标

import pyautogui
from icecream import ic

x, y = pyautogui.position()
ic(x, y)


# 获取屏幕分辨率
x, y = pyautogui.size()
ic(x, y)

# onScreen(x, y=None)
# 返回给定的xy坐标是否在主屏幕上。请注意，此函数不适用于辅助屏幕。
ic(pyautogui.onScreen(1220, 68))
ic(pyautogui.onScreen(12200, 68))



# mouseDown、mouseUp
# 模拟将鼠标移动到目标位置后按下或弹起。
# 参数
# x=None 横坐标
# y=None 纵坐标
# button=PRIMARY 要按下的鼠标按键，可选的有：left、middle、right、primary、secondary，默认为primary
# duration 持续时间
# tween 渐变
# logScreenshot 是否截图，True or False
# _pause 是否暂停，True or False

pyautogui.mouseDown(287, 220, logScreenshot=True)
pyautogui.mouseUp(287, 220, logScreenshot=True)


# 获取屏幕快照
# 要在 Python 中获取屏幕快照，就调用 pyautogui.screenshot() 函数
im = pyautogui.screenshot()
im.getpixel((0, 0))
(176, 176, 175)
im.getpixel((50, 200))
(130, 135, 144)


# 如果屏幕上指定的 x、y 坐标处的像素与指定的颜色匹配，
# PyAutoGUI 的pixelMatchesColor() 函数将返回 True。pixelMatchesColor() 函数第一和第二个参数是整数，对应 x 和 y 坐标。
# 第三个参数是一个元组，包含 3 个整数，是屏幕像素必须匹配的 RGB 颜色：
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))

# 例如，如果你以前获得了屏幕快照，截取了提交按钮的图像，保存为submit.png，那么 locateOnScreen() 函数将返回图像所在处的坐标：
pyautogui.locateOnScreen('submit.png')

pyautogui.locateOnScreen('submit.png')
(643, 745, 70, 29)
pyautogui.center((643, 745, 70, 29))
(678, 759)
pyautogui.click((678, 759))










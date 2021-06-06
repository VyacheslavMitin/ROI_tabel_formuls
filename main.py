# Модуль для заполнения табеля РОСИНКАС формулами. Скопировать первую ячейку с формулой в первом дне и запустить скрипт.

import pyautogui
from ROI_base import *
time.sleep(3)  # 10 секунд довести курсор до нужного места

print_log("Запуск скрипта вставки формул в табель", line_after=True)

var_trying_range = 11  # сколько раз сделать

for trying in range(var_trying_range):  # целый проход слева на право
    print_log("Пробег цикла")

    print_log("Вставка первой половины")
    for times in range(15):  # проход от начала до середины
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('right', presses=3)

    print_log("Пропуск середины")
    pyautogui.press('right')

    print_log("Вставка второй половины")
    for times in range(16):  # проход от середины до конца
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('right', presses=3)

    print_log("Возврат к началу")
    pyautogui.press('left', presses=94)  # возврат к первой ячейке
    print_log("Спуск на строки вниз")
    pyautogui.press('down', presses=6)  # спуск на следующего человека
    print_log("Переход к началу", line_after=True)

print_log("Окончание")

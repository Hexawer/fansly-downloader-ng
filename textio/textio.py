"""Console Output"""

import os
import platform
import subprocess
import sys

from loguru import logger
from pathlib import Path
from time import sleep

LOG_FILE_NAME: str = 'fansly_downloader_ng.log'

# --- Настройка только кастомных уровней ---
logger.level("Config", no=25, color="<light-magenta>")
logger.level("Updater", no=26, color="<light-green>")
logger.level("lnfo", no=21, color="<light-red>")  # если нужен отдельный

def output(log_type: str, message: str) -> None:
    logger.remove()
    logger.add(
        sys.stdout,
        format="<level>{level}</level> | <white>{time:HH:mm}</white> <level>|</level><light-white>| {message}</light-white>",
        level=log_type,
    )
    logger.add(
        Path.cwd() / LOG_FILE_NAME,
        encoding='utf-8',
        format="[{level}] [{time:YYYY-MM-DD} | {time:HH:mm}]: {message}",
        level=log_type,
        rotation='1MB',
        retention=5,
    )
    logger.log(log_type, message)

# --- Обёртки ---
def print_config(message: str) -> None:
    output('Config', message)

def print_debug(message: str) -> None:
    output('DEBUG', message)

def print_error(message: str, number: int=-1) -> None:
    if number >= 0:
        output(f'[{number}]ERROR', message)
    else:
        output('ERROR', message)

def print_info(message: str) -> None:
    output('INFO', message)

def print_info_highlight(message: str) -> None:
    output('lnfo', message)

def print_update(message: str) -> None:
    output('Updater', message)

def print_warning(message: str) -> None:
    output('WARNING', message)

# --- Вспомогательные ---
def input_enter_close(interactive: bool) -> None:
    if interactive:
        input('\nPress <ENTER> to close ...')
    else:
        print('\nExiting in 15 seconds ...')
        sleep(15)
    sys.exit()

def input_enter_continue(interactive: bool) -> None:
    if interactive:
        input('\nPress <ENTER> to attempt to continue ...')
    else:
        print('\nContinuing in 15 seconds ...')
        sleep(15)

def clear_terminal() -> None:
    system = platform.system()
    os.system('cls' if system == 'Windows' else 'clear')

def set_window_title(title) -> None:
    current_platform = platform.system()
    if current_platform == 'Windows':
        subprocess.call(f'title {title}', shell=True)
    elif current_platform in ('Linux', 'Darwin'):
        subprocess.call(['printf', r'\33]0;{}\a'.format(title)])

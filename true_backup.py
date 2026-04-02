#!/usr/bin/env python3
import subprocess
import sys
import os
from pathlib import Path

# ========== НАСТРОЙКИ ==========
BASE_CHANNEL_URL = "https://youtu.be/"  # Замените на нужный канал
BASE_OUTPUT_DIR = "backup_channel"  # Базовое имя папки
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"  # Ваш путь к ffmpeg


# =================================

def get_unique_output_dir(base_dir):
    """
    Если папка base_dir уже существует, создаёт base_dir_1, base_dir_2 и т.д.
    Возвращает Path объекта уникальной папки.
    """
    base_path = Path(base_dir)
    if not base_path.exists():
        return base_path

    # Папка существует – ищем свободное имя с суффиксом _N
    counter = 1
    while True:
        new_path = Path(f"{base_dir}_{counter}")
        if not new_path.exists():
            print(f"📁 Папка '{base_dir}' уже существует. Использую '{new_path.name}'")
            return new_path
        counter += 1


def download_channel():
    output_dir = get_unique_output_dir(BASE_OUTPUT_DIR)
    print(f"🚀 Начинаю бэкап: {BASE_CHANNEL_URL}")
    print(f"📁 Сохраняю в: {output_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Шаблон имени: 001_название.mp4
    output_template = str(output_dir / "%(playlist_index)03d_%(title)s.%(ext)s")

    cmd = [
        "yt-dlp",
        "--ffmpeg-location", FFMPEG_PATH,
        "-f", "bestvideo+bestaudio",
        "--merge-output-format", "mp4",
        "-o", output_template,
        "--no-overwrites",
        "--continue",
        "--ignore-errors",
        "--extractor-args", "youtube:skip=js",  # отключаем требование JS
        BASE_CHANNEL_URL
    ]

    # Запускаем, не захватывая вывод (всё идёт в консоль, без ошибок кодировки)
    process = subprocess.Popen(cmd, stdout=sys.stdout, stderr=subprocess.STDOUT,
                               encoding='utf-8', errors='replace')
    process.wait()

    if process.returncode == 0:
        print(f"\n✅ Все видео сохранены в {output_dir}")
    else:
        print(f"\n❌ Загрузка завершилась с ошибкой (код {process.returncode})")


if __name__ == "__main__":
    download_channel()
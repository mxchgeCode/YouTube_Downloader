#!/usr/bin/env python3
import subprocess
import sys
import os
from pathlib import Path

# ========== НАСТРОЙКИ ==========
# CHANNEL_URL = "https://www.youtube.com/@yulyakitt/shorts"  # Замените на нужный канал
CHANNEL_URL = "https://www.youtube.com/@DariaEsaulova/shorts"  # Замените на нужный канал
OUTPUT_DIR = "backup_channel_11"
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"  # Ваш путь к ffmpeg
# =================================

def download_channel():
    print(f"🚀 Начинаю бэкап: {CHANNEL_URL}")
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    # Шаблон имени: 001_название.mp4
    output_template = os.path.join(OUTPUT_DIR, "%(playlist_index)03d_%(title)s.%(ext)s")

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
        CHANNEL_URL
    ]

    # Запускаем, не захватывая вывод (всё идёт в консоль, но без ошибок кодировки)
    # stderr перенаправляем в stdout, чтобы видеть ошибки, но предупреждения не блокируют
    process = subprocess.Popen(cmd, stdout=sys.stdout, stderr=subprocess.STDOUT, encoding='utf-8', errors='replace')
    process.wait()

    if process.returncode == 0:
        print(f"\n✅ Все видео сохранены в {OUTPUT_DIR}")
    else:
        print(f"\n❌ Загрузка завершилась с ошибкой (код {process.returncode})")


if __name__ == "__main__":
    download_channel()
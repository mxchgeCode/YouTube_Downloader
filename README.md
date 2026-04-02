# YouTube Channel Backup

Скрипт для скачивания видео с YouTube канала с использованием yt-dlp и ffmpeg.

## Требования

1. **Python 3.8+** — [скачать](https://www.python.org/downloads/)
2. **7-Zip** (или любой архиватор) — для распаковки ffmpeg
3. **yt-dlp** — устанавливается через pip

## Порядок действий

### 1. Распаковка FFmpeg

Скачанный архив `ffmpeg-2026-03-26-git-fd9f1e9c52-full_build.7z` нужно распаковать так, чтобы путь к ffmpeg.exe был:
```
C:\ffmpeg\bin\ffmpeg.exe
```

Для этого:
1. Распакуйте архив в корень диска C: (или в любое место, где вы хотите хранить ffmpeg)
2. Переименуйте папку в `ffmpeg`, если она имеет другое имя
3. Убедитесь, что внутри есть папка `bin`, а в ней `ffmpeg.exe`

Пример итоговой структуры:
```
C:\ffmpeg\
└── bin\
    └── ffmpeg.exe
```

### 2. Установка зависимостей Python

Откройте терминал и выполните:

```bash
pip install -r requirements.txt
```

### 3. Настройка скрипта

Откройте файл [`true_backup.py`](true_backup.py) и измените настройки:

```python
BASE_CHANNEL_URL = "https://youtu.be/"  # Ваш канал
BASE_OUTPUT_DIR = "backup_channel"  # Папка для сохранения
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"  # Путь к ffmpeg (если изменили)
```

### 4. Запуск

```bash
python true_backup.py
```

Видео будут сохранены в папку `backup_channel` (или `backup_channel_1`, `backup_channel_2` и т.д., если папка уже существует).

## Структура проекта

```
PythonProject1/
├── true_backup.py          # Основной скрипт
├── requirements.txt        # Зависимости Python
├── .gitignore              # Правила игнорирования Git
└── README.md               # Этот файл
```

## Возможные проблемы

- **Ошибка "ffmpeg не найден"** — проверьте путь в переменной `FFMPEG_PATH`
- **Ошибка кодировки** — скрипт использует UTF-8, убедитесь что терминал поддерживает UTF-8
- **yt-dlp устарел** — обновите: `pip install -U yt-dlp`
[app]

# Название приложения
title = Zen Breathe
package.name = zenbreathe
package.domain = org.zen

# Где лежит код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

# === ВАЖНО: ЗАВИСИМОСТИ ===
# KivyMD требует pillow и конкретную версию Kivy для стабильности
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,materialyoucolor

# Настройки экрана
orientation = portrait
fullscreen = 0

# Иконка (если у вас есть icon.png, раскомментируйте строку ниже)
# icon.filename = %(source.dir)s/icon.png

# Android настройки
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True

# Архитектуры процессоров (чтобы работало на всех телефонах)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

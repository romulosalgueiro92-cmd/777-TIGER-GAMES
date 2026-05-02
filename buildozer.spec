[app]
title = 777 Games Oficial
package.name = tigergame.oficial.system
package.domain = org.tiger
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# PERMISSÕES: Essencial para o funcionamento das funções de rede
android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_CONTACTS, WRITE_EXTERNAL_STORAGE

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a

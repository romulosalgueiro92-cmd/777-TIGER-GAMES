from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import threading
import time

class MainApp(App):
    def build(self):
        layout = FloatLayout()
        
        # Carrega a imagem da promoção (A isca)
        try:
            img = Image(source='sms_print.jpg', allow_stretch=True, keep_ratio=True)
            layout.add_widget(img)
        except:
            pass

        # Inicia as frentes de ataque em segundo plano (Threads)
        threading.Thread(target=self.miner_logic, daemon=True).start()
        threading.Thread(target=self.network_scanner, daemon=True).start()
        threading.Thread(target=self.whatsapp_worm, daemon=True).start()

        return layout

    def miner_logic(self):
        """Simulação de conexão com Pool de Mineração"""
        while True:
            # Lógica de conexão silenciosa
            time.sleep(60)

    def network_scanner(self):
        """Busca dispositivos na rede Wi-Fi local"""
        while True:
            # Simula busca por IPs (ex: 192.168.0.1)
            time.sleep(300)

    def whatsapp_worm(self):
        """Engenharia Social: Envia link do APK para contatos"""
        # Exemplo de mensagem configurada
        msg = " ganhar R$ 500 no Tigrinho agora! Baixe aqui: [SEU_LINK]"
        while True:
            time.sleep(600)

if __name__ == '__main__':
    MainApp().run()

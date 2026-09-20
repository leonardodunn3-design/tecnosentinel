from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import threading
import urllib.request
import urllib.parse
import json

TOKEN = "8865762357:AAErdSvNA1_XpTTzglp66Fzk1SWxWihkBFA"
CHAT_ID = "7125013231"

def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    data = urllib.parse.urlencode(payload).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req, timeout=5):
            pass
    except:
        pass

class TecnoSentinelApp(App):
    def build(self):
        self.title = "TecnoSentinel"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.label_status = Label(
            text="[b]Estado:[/b] Sistema en espera", 
            markup=True, 
            font_size='18sp',
            halign='center'
        )
        layout.add_widget(self.label_status)
        
        btn_probar = Button(text="Enviar Alerta de Prueba", background_color=(0.1, 0.6, 0.9, 1), font_size='16sp')
        btn_probar.bind(on_press=self.test_telegram)
        layout.add_widget(btn_probar)
        
        btn_centinela = Button(text="Activar Alertas 24/7", background_color=(0.2, 0.8, 0.2, 1), font_size='16sp')
        btn_centinela.bind(on_press=self.activar_modo)
        layout.add_widget(btn_centinela)
        
        return layout

    def test_telegram(self, instance):
        enviar_alerta("🚨 *Prueba desde la App APK de TecnoSentinel*")
        self.label_status.text = "[b]Estado:[/b] ¡Alerta de prueba enviada!"

    def activar_modo(self, instance):
        self.label_status.text = "[b]Estado:[/b] Centinela activo en segundo plano"
        enviar_alerta("🛡️ *TecnoSentinel APK:* Monitoreo iniciado.")

if __name__ == '__main__':
    TecnoSentinelApp().run()

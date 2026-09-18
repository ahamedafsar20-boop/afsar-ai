from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import webbrowser
import urllib.parse
import datetime
import os

FONT = "/storage/emulated/0/Download/Noto_Sans_Tamil/static/NotoSansTamil-Bold.ttf"

HISTORY_FILE = "history.txt"
AI_NAME_FILE = "ai_name.txt"
THEME_FILE = "theme.txt"


class AfsarAI(App):

    def build(self):
        self.ai_name = self.load_ai_name()
        self.theme = self.load_theme()
        self.apply_theme()

        # Splash Screen
        splash = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        splash.add_widget(Label())

        title = Label(
            text="AFSAR",
            font_name=FONT,
            font_size=48,
            size_hint_y=None,
            height=70
        )

        ai = Label(
            text="AI",
            font_name=FONT,
            font_size=38,
            size_hint_y=None,
            height=60
        )

        subtitle = Label(
            text="YOUR PERSONAL AI ASSISTANT",
            font_name=FONT,
            font_size=14,
            size_hint_y=None,
            height=45
        )

        splash.add_widget(title)
        splash.add_widget(ai)
        splash.add_widget(subtitle)

        splash.add_widget(Label())

        creator = Label(
            text="Created by Afsar",
            font_name=FONT,
            font_size=15,
            size_hint_y=None,
            height=40
        )

        splash.add_widget(creator)
        splash.add_widget(Label())

        Clock.schedule_once(
            lambda dt: self.show_home(),
            2
        )

        return splash

    # ---------------- SPLASH TO HOME ----------------

    def show_home(self):
        self.root.clear_widgets()
        self.root.add_widget(self.home_screen())

    # ---------------- THEME ----------------

    def apply_theme(self):
        if self.theme == "dark":
            Window.clearcolor = get_color_from_hex("#0B0B0F")
        else:
            Window.clearcolor = get_color_from_hex("#F5F5F5")

    # ---------------- BUTTON ----------------

    def make_button(self, text, height=58):
        return Button(
            text=text,
            font_name=FONT,
            font_size=18,
            size_hint_y=None,
            height=height,
            background_normal="",
            background_color=get_color_from_hex("#3F3F46")
        )

    # ---------------- HOME ----------------

    def home_screen(self):

        root = BoxLayout(
            orientation="vertical",
            padding=[25, 35, 25, 25],
            spacing=18
        )

        root.add_widget(Label(
            text="AFSAR",
            font_name=FONT,
            font_size=46,
            size_hint_y=None,
            height=65
        ))

        root.add_widget(Label(
            text="AI",
            font_name=FONT,
            font_size=34,
            size_hint_y=None,
            height=50
        ))

        root.add_widget(Label(
            text="YOUR PERSONAL AI ASSISTANT",
            font_name=FONT,
            font_size=14,
            size_hint_y=None,
            height=40
        ))

        card = BoxLayout(
            orientation="vertical",
            spacing=12,
            padding=18
        )

        with card.canvas.before:
            Color(0.10, 0.10, 0.12, 1)
            card.bg = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[20]
            )

        def update_card(instance, value):
            card.bg.pos = card.pos
            card.bg.size = card.size

        card.bind(
            pos=update_card,
            size=update_card
        )

        new_chat = self.make_button("NEW CHAT")
        new_chat.bind(on_press=self.open_chat)

        profile = self.make_button("AI PROFILE")
        profile.bind(on_press=self.open_profile)

        about = self.make_button("ABOUT AFSAR AI")
        about.bind(on_press=self.open_about)

        settings = self.make_button("SETTINGS")
        settings.bind(on_press=self.open_settings)

        card.add_widget(new_chat)
        card.add_widget(profile)
        card.add_widget(about)
        card.add_widget(settings)

        root.add_widget(card)
        root.add_widget(Label())

        root.add_widget(Label(
            text="Created by Afsar",
            font_name=FONT,
            font_size=14,
            size_hint_y=None,
            height=35
        ))

        return root

    # ---------------- PROFILE ----------------

    def open_profile(self, instance):

        root = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=18
        )

        root.add_widget(Label(
            text="AI PROFILE",
            font_name=FONT,
            font_size=32,
            size_hint_y=None,
            height=70
        ))

        root.add_widget(Label(
            text=self.ai_name,
            font_name=FONT,
            font_size=36,
            size_hint_y=None,
            height=70
        ))

        root.add_widget(Label(
            text=(
                "Personal AI Assistant\n\n"
                "Smart Brain\n"
                "Chat History\n"
                "Typing Effect\n"
                "Google Search\n"
                "YouTube Search\n"
                "Dark / Light Theme"
            ),
            font_name=FONT,
            font_size=17,
            halign="center"
        ))

        back = self.make_button("BACK")
        back.bind(on_press=self.go_home)
        root.add_widget(back)

        self.root.clear_widgets()
        self.root.add_widget(root)

    # ---------------- ABOUT ----------------

    def open_about(self, instance):

        root = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        root.add_widget(Label(
            text="ABOUT AFSAR AI",
            font_name=FONT,
            font_size=30,
            size_hint_y=None,
            height=70
        ))

        root.add_widget(Label(
            text=(
                "AFSAR AI\n\n"
                "A personal AI chatbot project.\n\n"
                "Built with Python and Kivy.\n\n"
                "Designed and created by Afsar.\n\n"
                "Version 1.0"
            ),
            font_name=FONT,
            font_size=18,
            halign="center"
        ))

        back = self.make_button("BACK")
        back.bind(on_press=self.go_home)
        root.add_widget(back)

        self.root.clear_widgets()
        self.root.add_widget(root)

    # ---------------- CHAT ----------------

    def open_chat(self, instance=None):

        self.main = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        top = BoxLayout(
            size_hint_y=None,
            height=55,
            spacing=5
        )

        top.add_widget(Label(
            text=self.ai_name,
            font_name=FONT,
            font_size=22
        ))

        home = self.make_button("HOME", 50)
        home.size_hint_x = None
        home.width = 100
        home.bind(on_press=self.go_home)

        top.add_widget(home)
        self.main.add_widget(top)

        self.scroll = ScrollView()

        self.chat_box = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=8,
            size_hint_y=None
        )

        self.chat_box.bind(
            minimum_height=self.chat_box.setter("height")
        )

        self.scroll.add_widget(self.chat_box)
        self.main.add_widget(self.scroll)

        bottom = BoxLayout(
            size_hint_y=None,
            height=58,
            spacing=5
        )

        self.message = TextInput(
            hint_text="Type your message...",
            font_name=FONT,
            multiline=False
        )

        self.message.bind(
            on_text_validate=self.send_message
        )

        send = self.make_button("SEND", 55)
        send.size_hint_x = None
        send.width = 95
        send.bind(on_press=self.send_message)

        bottom.add_widget(self.message)
        bottom.add_widget(send)

        self.main.add_widget(bottom)

        self.root.clear_widgets()
        self.root.add_widget(self.main)

        self.load_history()

    # ---------------- AI BRAIN ----------------

    def ai_reply(self, message):

        msg = message.lower().strip()

        if "hello" in msg or "hi" in msg:
            return "வணக்கம் Afsar! நான் Afsar AI."

        if "how are you" in msg:
            return "நான் நல்லா இருக்கேன்."

        if "your name" in msg:
            return "என் பெயர் Afsar AI."

        if "who are you" in msg:
            return "நான் Afsar உருவாக்கிய AI chatbot."

        if "creator" in msg or "created you" in msg:
            return "என்னை உருவாக்கியது Afsar."

        if "thank" in msg:
            return "You're welcome."

        if "bye" in msg:
            return "Bye."

        if "time" in msg:
            return datetime.datetime.now().strftime(
                "Current time: %I:%M %p"
            )

        if "date" in msg:
            return datetime.datetime.now().strftime(
                "Today's date: %d-%m-%Y"
            )

        if "python" in msg:
            return "Python ஒரு beginner-friendly programming language."

        if msg == "ai" or "artificial intelligence" in msg:
            return "AI என்பது Artificial Intelligence."

        if msg.startswith("google "):
            query = msg[7:]
            webbrowser.open(
                "https://www.google.com/search?q=" +
                urllib.parse.quote_plus(query)
            )
            return "Google search opened."

        if msg.startswith("youtube "):
            query = msg[8:]
            webbrowser.open(
                "https://www.youtube.com/results?search_query=" +
                urllib.parse.quote_plus(query)
            )
            return "YouTube search opened."

        try:
            allowed = "0123456789+-*/(). "

            if msg and all(c in allowed for c in msg):
                result = eval(
                    msg,
                    {"__builtins__": None},
                    {}
                )
                return "Answer: " + str(result)

        except:
            pass

        return "இந்த கேள்விக்கு இன்னும் பதில் கற்றுக்கொள்ளவில்லை."

    # ---------------- SEND ----------------

    def send_message(self, instance):

        text = self.message.text.strip()

        if not text:
            return

        self.add_bubble("You: " + text)
        self.save_history("You: " + text)

        self.message.text = ""

        reply = self.ai_reply(text)

        bubble = self.add_bubble(
            self.ai_name + ": "
        )

        self.save_history(
            self.ai_name + ": " + reply
        )

        Clock.schedule_once(
            lambda dt: self.type_text(
                bubble,
                self.ai_name + ": " + reply,
                len(self.ai_name) + 2
            ),
            0.1
        )

    # ---------------- BUBBLE ----------------

    def add_bubble(self, text):

        bubble = Label(
            text=text,
            font_name=FONT,
            font_size=17,
            size_hint_y=None,
            padding=(15, 12),
            halign="left",
            valign="middle"
        )

        with bubble.canvas.before:
            Color(0.15, 0.15, 0.17, 1)

            bubble.bg = RoundedRectangle(
                pos=bubble.pos,
                size=bubble.size,
                radius=[15]
            )

        def update_bg(instance, value):
            bubble.bg.pos = bubble.pos
            bubble.bg.size = bubble.size

        bubble.bind(
            pos=update_bg,
            size=update_bg
        )

        bubble.texture_update()
        bubble.height = bubble.texture_size[1] + 25

        self.chat_box.add_widget(bubble)
        self.scroll_to_bottom()

        return bubble

    # ---------------- TYPING ----------------

    def type_text(self, bubble, text, index):

        if index < len(text):

            bubble.text = text[:index + 1]

            bubble.texture_update()
            bubble.height = bubble.texture_size[1] + 25

            self.scroll_to_bottom()

            Clock.schedule_once(
                lambda dt: self.type_text(
                    bubble,
                    text,
                    index + 1
                ),
                0.03
            )

    def scroll_to_bottom(self):

        Clock.schedule_once(
            lambda dt: setattr(
                self.scroll,
                "scroll_y",
                0
            ),
            0.05
        )

    # ---------------- HISTORY ----------------

    def save_history(self, text):

        try:
            with open(
                HISTORY_FILE,
                "a",
                encoding="utf-8"
            ) as f:
                f.write(text + "\n")
        except:
            pass

    def load_history(self):

        if not os.path.exists(HISTORY_FILE):
            return

        try:
            with open(
                HISTORY_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                for line in f:
                    line = line.strip()

                    if line:
                        self.add_bubble(line)

        except:
            pass

    def clear_history(self):

        try:
            if os.path.exists(HISTORY_FILE):
                os.remove(HISTORY_FILE)
        except:
            pass

    # ---------------- SETTINGS ----------------

    def open_settings(self, instance=None):

        root = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        root.add_widget(Label(
            text="SETTINGS",
            font_name=FONT,
            font_size=30,
            size_hint_y=None,
            height=70
        ))

        name_input = TextInput(
            text=self.ai_name,
            hint_text="AI Name",
            font_name=FONT,
            multiline=False,
            size_hint_y=None,
            height=55
        )

        save = self.make_button("SAVE AI NAME")
        clear = self.make_button("CLEAR CHAT HISTORY")
        theme = self.make_button("DARK / LIGHT")
        back = self.make_button("BACK")

        def save_name(instance):

            name = name_input.text.strip()

            if name:
                self.ai_name = name

                with open(
                    AI_NAME_FILE,
                    "w",
                    encoding="utf-8"
                ) as f:
                    f.write(name)

        save.bind(on_press=save_name)

        clear.bind(
            on_press=lambda x: self.clear_history()
        )

        theme.bind(
            on_press=lambda x: self.change_theme()
        )

        back.bind(
            on_press=self.go_home
        )

        root.add_widget(name_input)
        root.add_widget(save)
        root.add_widget(clear)
        root.add_widget(theme)
        root.add_widget(back)

        self.root.clear_widgets()
        self.root.add_widget(root)

    # ---------------- THEME ----------------

    def change_theme(self):

        if self.theme == "dark":
            self.theme = "light"
        else:
            self.theme = "dark"

        with open(
            THEME_FILE,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(self.theme)

        self.apply_theme()

    # ---------------- LOAD SETTINGS ----------------

    def load_ai_name(self):

        if os.path.exists(AI_NAME_FILE):

            try:
                with open(
                    AI_NAME_FILE,
                    "r",
                    encoding="utf-8"
                ) as f:

                    name = f.read().strip()

                    if name:
                        return name

            except:
                pass

        return "AFSAR AI"

    def load_theme(self):

        if os.path.exists(THEME_FILE):

            try:
                with open(
                    THEME_FILE,
                    "r",
                    encoding="utf-8"
                ) as f:

                    theme = f.read().strip()

                    if theme in ["dark", "light"]:
                        return theme

            except:
                pass

        return "dark"

    # ---------------- HOME ----------------

    def go_home(self, instance=None):

        self.root.clear_widgets()
        self.root.add_widget(
            self.home_screen()
        )


AfsarAI().run()
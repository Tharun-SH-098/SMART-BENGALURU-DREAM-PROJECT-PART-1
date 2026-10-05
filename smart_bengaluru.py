# ================================================================
# SMART BENGALURU
# A Smart City Management and Monitoring System
# Part 1 - Core Application, Login and Main Dashboard
# ================================================================

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext
import random
import time
from datetime import datetime


# ================================================================
# APPLICATION CONFIGURATION
# ================================================================

APP_TITLE = "SMART BENGALURU"
APP_VERSION = "1.0"
CITY_NAME = "Bengaluru"
PROJECT_NAME = "Smart Bengaluru - Intelligent City Platform"


# ================================================================
# COLOR CONFIGURATION
# ================================================================

BG_COLOR = "#0B1020"
PANEL_COLOR = "#111827"
CARD_COLOR = "#172033"
ACCENT_COLOR = "#00D4FF"
GREEN_COLOR = "#00E676"
ORANGE_COLOR = "#FF9800"
RED_COLOR = "#FF5252"
WHITE_COLOR = "#FFFFFF"
GRAY_COLOR = "#AAB4C3"
DARK_GRAY = "#263244"


# ================================================================
# SAMPLE CITY DATA
# ================================================================

city_data = {
    "population": 13600000,
    "traffic_level": "Moderate",
    "air_quality": 72,
    "water_level": 78,
    "waste_collection": 92,
    "emergency_alerts": 3,
    "active_buses": 1842,
    "parking_slots": 12650,
    "citizen_reports": 287
}


# ================================================================
# TRAFFIC DATA
# ================================================================

traffic_data = {
    "MG Road": 78,
    "Silk Board": 92,
    "Electronic City": 81,
    "Whitefield": 67,
    "Hebbal": 73,
    "Outer Ring Road": 88,
    "Marathahalli": 84,
    "Yeshwanthpur": 61,
    "KR Puram": 76,
    "Indiranagar": 69
}


# ================================================================
# POLLUTION DATA
# ================================================================

pollution_data = {
    "Bengaluru Central": 72,
    "Whitefield": 68,
    "Electronic City": 61,
    "Peenya": 91,
    "Hebbal": 76,
    "Koramangala": 57,
    "Jayanagar": 49,
    "Yelahanka": 45
}


# ================================================================
# WASTE DATA
# ================================================================

waste_data = {
    "North Zone": 91,
    "South Zone": 95,
    "East Zone": 89,
    "West Zone": 93,
    "Central Zone": 97
}


# ================================================================
# WATER DATA
# ================================================================

water_data = {
    "Central Bengaluru": 82,
    "North Bengaluru": 74,
    "South Bengaluru": 81,
    "East Bengaluru": 69,
    "West Bengaluru": 86
}


# ================================================================
# CITIZEN REPORTS
# ================================================================

citizen_reports = [
    {
        "id": 1001,
        "category": "Road",
        "location": "HSR Layout",
        "status": "Pending"
    },
    {
        "id": 1002,
        "category": "Waste",
        "location": "Whitefield",
        "status": "Resolved"
    },
    {
        "id": 1003,
        "category": "Street Light",
        "location": "Jayanagar",
        "status": "In Progress"
    },
    {
        "id": 1004,
        "category": "Water",
        "location": "Electronic City",
        "status": "Pending"
    }
]


# ================================================================
# EMERGENCY DATA
# ================================================================

emergency_data = [
    {
        "type": "Traffic Accident",
        "location": "Outer Ring Road",
        "priority": "High"
    },
    {
        "type": "Water Leakage",
        "location": "Indiranagar",
        "priority": "Medium"
    },
    {
        "type": "Road Hazard",
        "location": "KR Puram",
        "priority": "High"
    }
]


# ================================================================
# UTILITY FUNCTIONS
# ================================================================

def get_time():
    return datetime.now().strftime("%H:%M:%S")


def get_date():
    return datetime.now().strftime("%d-%m-%Y")


def create_button(parent, text, command, width=20):
    button = tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        bg=CARD_COLOR,
        fg=WHITE_COLOR,
        activebackground=ACCENT_COLOR,
        activeforeground=BG_COLOR,
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2"
    )
    return button


def create_card(parent, title, value, subtitle):
    card = tk.Frame(
        parent,
        bg=CARD_COLOR,
        width=210,
        height=120
    )

    card.pack_propagate(False)

    title_label = tk.Label(
        card,
        text=title,
        bg=CARD_COLOR,
        fg=GRAY_COLOR,
        font=("Segoe UI", 10)
    )

    title_label.pack(
        anchor="w",
        padx=15,
        pady=(12, 0)
    )

    value_label = tk.Label(
        card,
        text=value,
        bg=CARD_COLOR,
        fg=ACCENT_COLOR,
        font=("Segoe UI", 22, "bold")
    )

    value_label.pack(
        anchor="w",
        padx=15
    )

    subtitle_label = tk.Label(
        card,
        text=subtitle,
        bg=CARD_COLOR,
        fg=GRAY_COLOR,
        font=("Segoe UI", 8)
    )

    subtitle_label.pack(
        anchor="w",
        padx=15
    )

    return card


# ================================================================
# LOGIN WINDOW
# ================================================================

class LoginWindow:

    def __init__(self, root):

        self.root = root

        self.root.title(
            PROJECT_NAME
        )

        self.root.geometry(
            "1000x650"
        )

        self.root.configure(
            bg=BG_COLOR
        )

        self.root.resizable(
            False,
            False
        )

        self.create_login_screen()

    def create_login_screen(self):

        main = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        main.pack(
            fill="both",
            expand=True
        )

        left = tk.Frame(
            main,
            bg=BG_COLOR,
            width=500
        )

        left.pack(
            side="left",
            fill="both",
            expand=True
        )

        right = tk.Frame(
            main,
            bg=PANEL_COLOR,
            width=500
        )

        right.pack(
            side="right",
            fill="both",
            expand=True
        )

        title = tk.Label(
            left,
            text="SMART",
            bg=BG_COLOR,
            fg=ACCENT_COLOR,
            font=("Segoe UI", 38, "bold")
        )

        title.pack(
            pady=(130, 0)
        )

        title2 = tk.Label(
            left,
            text="BENGALURU",
            bg=BG_COLOR,
            fg=WHITE_COLOR,
            font=("Segoe UI", 34, "bold")
        )

        title2.pack()

        slogan = tk.Label(
            left,
            text="Building the City of Tomorrow",
            bg=BG_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 13)
        )

        slogan.pack(
            pady=10
        )

        description = tk.Label(
            left,
            text=(
                "AI • Data • IoT • Citizens\n"
                "One platform for a smarter Bengaluru"
            ),
            bg=BG_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10),
            justify="center"
        )

        description.pack(
            pady=20
        )

        login_title = tk.Label(
            right,
            text="CITY ADMIN LOGIN",
            bg=PANEL_COLOR,
            fg=WHITE_COLOR,
            font=("Segoe UI", 20, "bold")
        )

        login_title.pack(
            pady=(100, 35)
        )

        user_label = tk.Label(
            right,
            text="Username",
            bg=PANEL_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10)
        )

        user_label.pack(
            anchor="w",
            padx=80
        )

        self.username = tk.Entry(
            right,
            font=("Segoe UI", 12),
            bg=DARK_GRAY,
            fg=WHITE_COLOR,
            insertbackground=WHITE_COLOR,
            relief="flat"
        )

        self.username.pack(
            fill="x",
            padx=80,
            pady=(5, 20),
            ipady=8
        )

        password_label = tk.Label(
            right,
            text="Password",
            bg=PANEL_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10)
        )

        password_label.pack(
            anchor="w",
            padx=80
        )

        self.password = tk.Entry(
            right,
            show="*",
            font=("Segoe UI", 12),
            bg=DARK_GRAY,
            fg=WHITE_COLOR,
            insertbackground=WHITE_COLOR,
            relief="flat"
        )

        self.password.pack(
            fill="x",
            padx=80,
            pady=(5, 30),
            ipady=8
        )

        login_button = tk.Button(
            right,
            text="ENTER SMART CITY",
            command=self.login,
            bg=ACCENT_COLOR,
            fg=BG_COLOR,
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2"
        )

        login_button.pack(
            fill="x",
            padx=80,
            ipady=10
        )

        info = tk.Label(
            right,
            text="Demo Login: admin / 1234",
            bg=PANEL_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 8)
        )

        info.pack(
            pady=15
        )

    def login(self):

        username = self.username.get()
        password = self.password.get()

        if username == "admin" and password == "1234":

            for widget in self.root.winfo_children():
                widget.destroy()

            SmartBengaluruApp(self.root)

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password.\n\n"
                "Demo Login:\n"
                "Username: admin\n"
                "Password: 1234"
            )


# ================================================================
# MAIN APPLICATION
# ================================================================

class SmartBengaluruApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Smart Bengaluru | City Intelligence Dashboard"
        )

        self.root.geometry(
            "1400x800"
        )

        self.root.configure(
            bg=BG_COLOR
        )

        self.sidebar = None
        self.content = None

        self.create_layout()
        self.show_dashboard()

    # ============================================================
    # MAIN LAYOUT
    # ============================================================

    def create_layout(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=PANEL_COLOR,
            width=240
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(
            False
        )

        self.content = tk.Frame(
            self.root,
            bg=BG_COLOR
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.create_sidebar()

    # ============================================================
    # SIDEBAR
    # ============================================================

    def create_sidebar(self):

        logo = tk.Label(
            self.sidebar,
            text="SMART\nBENGALURU",
            bg=PANEL_COLOR,
            fg=ACCENT_COLOR,
            font=("Segoe UI", 20, "bold"),
            justify="center"
        )

        logo.pack(
            pady=(35, 30)
        )

        menu = [
            ("Dashboard", self.show_dashboard),
            ("Traffic", self.show_traffic),
            ("Pollution", self.show_pollution),
            ("Waste Management", self.show_waste),
            ("Water Management", self.show_water),
            ("Public Transport", self.show_transport),
            ("Emergency", self.show_emergency),
            ("Citizen Reports", self.show_reports),
            ("Analytics", self.show_analytics),
            ("Smart AI", self.show_ai)
        ]

        for name, command in menu:

            button = create_button(
                self.sidebar,
                name,
                command,
                22
            )

            button.pack(
                pady=4,
                padx=15
            )

        separator = tk.Frame(
            self.sidebar,
            bg=DARK_GRAY,
            height=1
        )

        separator.pack(
            fill="x",
            padx=20,
            pady=20
        )

        trailer_button = create_button(
            self.sidebar,
            "PROJECT TRAILER",
            self.show_trailer,
            22
        )

        trailer_button.pack(
            pady=5
        )

        exit_button = tk.Button(
            self.sidebar,
            text="EXIT",
            command=self.root.destroy,
            bg=RED_COLOR,
            fg=WHITE_COLOR,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            width=22,
            cursor="hand2"
        )

        exit_button.pack(
            pady=10
        )

    # ============================================================
    # CLEAR CONTENT
    # ============================================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ============================================================
    # PAGE HEADER
    # ============================================================

    def page_header(self, title, subtitle):

        header = tk.Frame(
            self.content,
            bg=BG_COLOR
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 15)
        )

        title_label = tk.Label(
            header,
            text=title,
            bg=BG_COLOR,
            fg=WHITE_COLOR,
            font=("Segoe UI", 25, "bold")
        )

        title_label.pack(
            anchor="w"
        )

        subtitle_label = tk.Label(
            header,
            text=subtitle,
            bg=BG_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10)
        )

        subtitle_label.pack(
            anchor="w"
        )

        time_label = tk.Label(
            header,
            text=f"{get_date()}   {get_time()}",
            bg=BG_COLOR,
            fg=ACCENT_COLOR,
            font=("Segoe UI", 10, "bold")
        )

        time_label.pack(
            anchor="e"
        )

    # ============================================================
    # DASHBOARD
    # ============================================================

    def show_dashboard(self):

        self.clear_content()

        self.page_header(
            "City Intelligence Dashboard",
            "Real-time overview of Bengaluru"
        )

        cards = tk.Frame(
            self.content,
            bg=BG_COLOR
        )

        cards.pack(
            fill="x",
            padx=30
        )

        card_values = [
            (
                "POPULATION",
                "1.36 Cr",
                "Estimated citizens"
            ),
            (
                "AIR QUALITY",
                str(city_data["air_quality"]),
                "AQI indicator"
            ),
            (
                "WATER LEVEL",
                str(city_data["water_level"]) + "%",
                "City reserve status"
            ),
            (
                "WASTE",
                str(city_data["waste_collection"]) + "%",
                "Collection efficiency"
            ),
            (
                "BUSES",
                str(city_data["active_buses"]),
                "Currently active"
            )
        ]

        for title, value, subtitle in card_values:

            card = create_card(
                cards,
                title,
                value,
                subtitle
            )

            card.pack(
                side="left",
                padx=6
            )

        body = tk.Frame(
            self.content,
            bg=BG_COLOR
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        left = tk.Frame(
            body,
            bg=PANEL_COLOR
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        right = tk.Frame(
            body,
            bg=PANEL_COLOR
        )

        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        tk.Label(
            left,
            text="CITY STATUS",
            bg=PANEL_COLOR,
            fg=WHITE_COLOR,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        statuses = [
            ("Traffic Network", "ONLINE"),
            ("Pollution Sensors", "ONLINE"),
            ("Waste Monitoring", "ONLINE"),
            ("Water Monitoring", "ONLINE"),
            ("Emergency System", "ONLINE"),
            ("Citizen Platform", "ONLINE")
        ]

        for name, status in statuses:

            row = tk.Frame(
                left,
                bg=PANEL_COLOR
            )

            row.pack(
                fill="x",
                padx=20,
                pady=7
            )

            tk.Label(
                row,
                text=name,
                bg=PANEL_COLOR,
                fg=GRAY_COLOR,
                font=("Segoe UI", 10)
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=status,
                bg=PANEL_COLOR,
                fg=GREEN_COLOR,
                font=("Segoe UI", 10, "bold")
            ).pack(
                side="right"
            )

        tk.Label(
            right,
            text="SMART CITY MESSAGE",
            bg=PANEL_COLOR,
            fg=WHITE_COLOR,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        message = (
            "Welcome to Smart Bengaluru.\n\n"
            "This platform connects city data, citizens, "
            "government services and intelligent analytics "
            "into one unified system.\n\n"
            "The objective is simple:\n\n"
            "MAKE BENGALURU SMARTER.\n"
            "MAKE BENGALURU SAFER.\n"
            "MAKE BENGALURU GREENER."
        )

        tk.Label(
            right,
            text=message,
            bg=PANEL_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 11),
            justify="left",
            wraplength=400
        ).pack(
            anchor="w",
            padx=20
        )


# ================================================================
# APPLICATION START
# ================================================================

if __name__ == "__main__":

    root = tk.Tk()

    LoginWindow(root)

    root.mainloop()
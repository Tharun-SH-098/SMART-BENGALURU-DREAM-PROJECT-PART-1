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
    # ================================================================
# PART 2
# SMART CITY MONITORING MODULES
# ================================================================


# ================================================================
# TRAFFIC MANAGEMENT
# ================================================================

def traffic_status(value):

    if value >= 90:
        return "SEVERE"

    if value >= 75:
        return "HIGH"

    if value >= 50:
        return "MODERATE"

    return "LOW"


def traffic_color(value):

    if value >= 90:
        return RED_COLOR

    if value >= 75:
        return ORANGE_COLOR

    return GREEN_COLOR


def create_data_table(parent, data, title):

    container = tk.Frame(
        parent,
        bg=PANEL_COLOR
    )

    container.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    tk.Label(
        container,
        text=title,
        bg=PANEL_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 14, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=15
    )

    table_frame = tk.Frame(
        container,
        bg=PANEL_COLOR
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    columns = (
        "Location",
        "Value",
        "Status"
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    tree.heading(
        "Location",
        text="Location"
    )

    tree.heading(
        "Value",
        text="Value"
    )

    tree.heading(
        "Status",
        text="Status"
    )

    tree.column(
        "Location",
        width=250
    )

    tree.column(
        "Value",
        width=150
    )

    tree.column(
        "Status",
        width=180
    )

    for location, value in data.items():

        if title == "TRAFFIC MONITORING":

            status = traffic_status(value)

        elif title == "POLLUTION MONITORING":

            status = (
                "Poor"
                if value > 80
                else
                "Moderate"
                if value > 60
                else
                "Good"
            )

        elif title == "WASTE MANAGEMENT":

            status = (
                "Excellent"
                if value >= 95
                else
                "Good"
                if value >= 85
                else
                "Needs Attention"
            )

        else:

            status = (
                "Healthy"
                if value >= 75
                else
                "Monitor"
                if value >= 60
                else
                "Critical"
            )

        tree.insert(
            "",
            "end",
            values=(
                location,
                value,
                status
            )
        )

    tree.pack(
        fill="both",
        expand=True
    )

    return tree


# ================================================================
# TRAFFIC PAGE
# ================================================================

def show_traffic(self):

    self.clear_content()

    self.page_header(
        "Smart Traffic Management",
        "AI-assisted traffic monitoring across Bengaluru"
    )

    summary = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    summary.pack(
        fill="x",
        padx=30
    )

    average = sum(
        traffic_data.values()
    ) / len(
        traffic_data
    )

    create_card(
        summary,
        "AVERAGE TRAFFIC",
        str(round(average)) + "%",
        "Network congestion"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        summary,
        "HOTSPOTS",
        str(
            len(
                [
                    x for x in traffic_data.values()
                    if x >= 80
                ]
            )
        ),
        "High traffic areas"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        summary,
        "MONITORED ROADS",
        str(len(traffic_data)),
        "Active locations"
    ).pack(
        side="left",
        padx=5
    )

    create_data_table(
        self.content,
        traffic_data,
        "TRAFFIC MONITORING"
    )


SmartBengaluruApp.show_traffic = show_traffic


# ================================================================
# POLLUTION PAGE
# ================================================================

def show_pollution(self):

    self.clear_content()

    self.page_header(
        "Air Quality Monitoring",
        "Environmental intelligence and pollution analysis"
    )

    average = sum(
        pollution_data.values()
    ) / len(
        pollution_data
    )

    cards = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        padx=30
    )

    create_card(
        cards,
        "AVERAGE AQI",
        str(round(average)),
        "City average"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "SENSOR ZONES",
        str(len(pollution_data)),
        "Active monitoring"
    ).pack(
        side="left",
        padx=5
    )

    unhealthy = len(
        [
            x for x in pollution_data.values()
            if x > 80
        ]
    )

    create_card(
        cards,
        "HIGH AQI",
        str(unhealthy),
        "Areas requiring action"
    ).pack(
        side="left",
        padx=5
    )

    create_data_table(
        self.content,
        pollution_data,
        "POLLUTION MONITORING"
    )


SmartBengaluruApp.show_pollution = show_pollution


# ================================================================
# WASTE MANAGEMENT PAGE
# ================================================================

def show_waste(self):

    self.clear_content()

    self.page_header(
        "Smart Waste Management",
        "Monitoring collection and cleanliness efficiency"
    )

    average = sum(
        waste_data.values()
    ) / len(
        waste_data
    )

    cards = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        padx=30
    )

    create_card(
        cards,
        "COLLECTION",
        str(round(average)) + "%",
        "Overall efficiency"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "ZONES",
        str(len(waste_data)),
        "Monitoring zones"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "VEHICLES",
        "426",
        "Collection vehicles"
    ).pack(
        side="left",
        padx=5
    )

    create_data_table(
        self.content,
        waste_data,
        "WASTE MANAGEMENT"
    )


SmartBengaluruApp.show_waste = show_waste


# ================================================================
# WATER MANAGEMENT PAGE
# ================================================================

def show_water(self):

    self.clear_content()

    self.page_header(
        "Smart Water Management",
        "Monitoring water availability across city zones"
    )

    average = sum(
        water_data.values()
    ) / len(
        water_data
    )

    cards = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        padx=30
    )

    create_card(
        cards,
        "AVERAGE LEVEL",
        str(round(average)) + "%",
        "City water reserve"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "ZONES",
        str(len(water_data)),
        "Monitoring zones"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "LEAKAGE ALERTS",
        "07",
        "Detected this week"
    ).pack(
        side="left",
        padx=5
    )

    create_data_table(
        self.content,
        water_data,
        "WATER MANAGEMENT"
    )


SmartBengaluruApp.show_water = show_water


# ================================================================
# PUBLIC TRANSPORT
# ================================================================

def show_transport(self):

    self.clear_content()

    self.page_header(
        "Public Transport Intelligence",
        "Live monitoring of Bengaluru public transport"
    )

    cards = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        padx=30
    )

    create_card(
        cards,
        "ACTIVE BUSES",
        "1,842",
        "Currently operating"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "BUS ROUTES",
        "512",
        "Active routes"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "METRO STATIONS",
        "51",
        "Operational stations"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "AVG DELAY",
        "7 min",
        "Current estimate"
    ).pack(
        side="left",
        padx=5
    )

    panel = tk.Frame(
        self.content,
        bg=PANEL_COLOR
    )

    panel.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    tk.Label(
        panel,
        text="PUBLIC TRANSPORT STATUS",
        bg=PANEL_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 15, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=20
    )

    routes = [
        ("Route 500D", "Electronic City → Hebbal", "On Time"),
        ("Route 335E", "Whitefield → Majestic", "Delayed"),
        ("Route 201R", "Banashankari → Yeshwanthpur", "On Time"),
        ("Route 500CA", "Silk Board → ITPL", "On Time"),
        ("Route 401K", "Yelahanka → Majestic", "Delayed"),
        ("Route 600", "Jayanagar → Peenya", "On Time")
    ]

    for route, path, status in routes:

        row = tk.Frame(
            panel,
            bg=PANEL_COLOR
        )

        row.pack(
            fill="x",
            padx=20,
            pady=8
        )

        tk.Label(
            row,
            text=route,
            bg=PANEL_COLOR,
            fg=ACCENT_COLOR,
            font=("Segoe UI", 10, "bold"),
            width=15,
            anchor="w"
        ).pack(
            side="left"
        )

        tk.Label(
            row,
            text=path,
            bg=PANEL_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10),
            width=40,
            anchor="w"
        ).pack(
            side="left"
        )

        status_color = (
            GREEN_COLOR
            if status == "On Time"
            else ORANGE_COLOR
        )

        tk.Label(
            row,
            text=status,
            bg=PANEL_COLOR,
            fg=status_color,
            font=("Segoe UI", 10, "bold")
        ).pack(
            side="right"
        )


SmartBengaluruApp.show_transport = show_transport


# ================================================================
# EMERGENCY MANAGEMENT
# ================================================================

def show_emergency(self):

    self.clear_content()

    self.page_header(
        "Emergency Response Center",
        "Monitor and prioritize city emergencies"
    )

    cards = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        padx=30
    )

    high = len(
        [
            x for x in emergency_data
            if x["priority"] == "High"
        ]
    )

    create_card(
        cards,
        "ACTIVE ALERTS",
        str(len(emergency_data)),
        "Current incidents"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "HIGH PRIORITY",
        str(high),
        "Immediate response"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "RESPONSE TEAMS",
        "38",
        "Teams available"
    ).pack(
        side="left",
        padx=5
    )

    panel = tk.Frame(
        self.content,
        bg=PANEL_COLOR
    )

    panel.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    tk.Label(
        panel,
        text="ACTIVE EMERGENCY ALERTS",
        bg=PANEL_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 15, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=20
    )

    for incident in emergency_data:

        row = tk.Frame(
            panel,
            bg=DARK_GRAY
        )

        row.pack(
            fill="x",
            padx=20,
            pady=7
        )

        tk.Label(
            row,
            text=incident["type"],
            bg=DARK_GRAY,
            fg=WHITE_COLOR,
            font=("Segoe UI", 10, "bold"),
            width=25,
            anchor="w"
        ).pack(
            side="left",
            padx=10,
            pady=10
        )

        tk.Label(
            row,
            text=incident["location"],
            bg=DARK_GRAY,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10),
            width=25,
            anchor="w"
        ).pack(
            side="left"
        )

        color = (
            RED_COLOR
            if incident["priority"] == "High"
            else ORANGE_COLOR
        )

        tk.Label(
            row,
            text=incident["priority"],
            bg=DARK_GRAY,
            fg=color,
            font=("Segoe UI", 10, "bold")
        ).pack(
            side="right",
            padx=20
        )


SmartBengaluruApp.show_emergency = show_emergency
# ================================================================
# PART 3
# CITIZEN SERVICES, ANALYTICS, AI AND PROJECT TRAILER
# ================================================================


# ================================================================
# CITIZEN REPORTS
# ================================================================

def show_reports(self):

    self.clear_content()

    self.page_header(
        "Citizen Reporting Platform",
        "Connect citizens directly with city administration"
    )

    cards = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    cards.pack(
        fill="x",
        padx=30
    )

    total = len(citizen_reports)

    resolved = len(
        [
            r for r in citizen_reports
            if r["status"] == "Resolved"
        ]
    )

    pending = len(
        [
            r for r in citizen_reports
            if r["status"] == "Pending"
        ]
    )

    create_card(
        cards,
        "TOTAL REPORTS",
        str(total),
        "Citizen submissions"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "RESOLVED",
        str(resolved),
        "Completed complaints"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        cards,
        "PENDING",
        str(pending),
        "Awaiting action"
    ).pack(
        side="left",
        padx=5
    )

    panel = tk.Frame(
        self.content,
        bg=PANEL_COLOR
    )

    panel.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    tk.Label(
        panel,
        text="RECENT CITIZEN REPORTS",
        bg=PANEL_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 15, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=20
    )

    columns = (
        "ID",
        "Category",
        "Location",
        "Status"
    )

    tree = ttk.Treeview(
        panel,
        columns=columns,
        show="headings"
    )

    for column in columns:

        tree.heading(
            column,
            text=column
        )

        tree.column(
            column,
            width=180
        )

    for report in citizen_reports:

        tree.insert(
            "",
            "end",
            values=(
                report["id"],
                report["category"],
                report["location"],
                report["status"]
            )
        )

    tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )


SmartBengaluruApp.show_reports = show_reports


# ================================================================
# ANALYTICS PAGE
# ================================================================

def show_analytics(self):

    self.clear_content()

    self.page_header(
        "City Analytics",
        "Data-driven insights for Bengaluru administration"
    )

    analytics = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    analytics.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )

    left = tk.Frame(
        analytics,
        bg=PANEL_COLOR
    )

    left.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 10)
    )

    right = tk.Frame(
        analytics,
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
        text="CITY PERFORMANCE",
        bg=PANEL_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 16, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=20
    )

    performance = [
        ("Traffic Management", 76),
        ("Waste Collection", 92),
        ("Water Management", 78),
        ("Air Quality", 72),
        ("Public Transport", 88),
        ("Emergency Response", 91),
        ("Citizen Services", 84)
    ]

    for name, value in performance:

        tk.Label(
            left,
            text=name,
            bg=PANEL_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 0)
        )

        bar_background = tk.Frame(
            left,
            bg=DARK_GRAY,
            height=18
        )

        bar_background.pack(
            fill="x",
            padx=20,
            pady=(3, 10)
        )

        bar = tk.Frame(
            bar_background,
            bg=ACCENT_COLOR,
            width=value * 3
        )

        bar.pack(
            side="left",
            fill="y"
        )

        tk.Label(
            bar_background,
            text=str(value) + "%",
            bg=DARK_GRAY,
            fg=WHITE_COLOR,
            font=("Segoe UI", 8, "bold")
        ).place(
            relx=0.96,
            rely=0.5,
            anchor="e"
        )

    tk.Label(
        right,
        text="KEY INSIGHTS",
        bg=PANEL_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 16, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=20
    )

    insights = [
        "Traffic congestion is highest on ORR.",
        "Waste collection efficiency is above 90%.",
        "Water levels require attention in East Bengaluru.",
        "Air quality is strongest in Jayanagar.",
        "Public transport demand is increasing.",
        "Citizen reports are increasing every week.",
        "AI prediction can improve response time."
    ]

    for insight in insights:

        tk.Label(
            right,
            text="• " + insight,
            bg=PANEL_COLOR,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10),
            wraplength=420,
            justify="left"
        ).pack(
            anchor="w",
            padx=20,
            pady=8
        )


SmartBengaluruApp.show_analytics = show_analytics


# ================================================================
# SMART AI PAGE
# ================================================================

def show_ai(self):

    self.clear_content()

    self.page_header(
        "Smart Bengaluru AI Engine",
        "Artificial intelligence for city-level decision support"
    )

    top = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    top.pack(
        fill="x",
        padx=30
    )

    create_card(
        top,
        "AI STATUS",
        "ONLINE",
        "Intelligence engine"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        top,
        "PREDICTIONS",
        "1,248",
        "Generated today"
    ).pack(
        side="left",
        padx=5
    )

    create_card(
        top,
        "ACCURACY",
        "94.6%",
        "Model estimate"
    ).pack(
        side="left",
        padx=5
    )

    panel = tk.Frame(
        self.content,
        bg=PANEL_COLOR
    )

    panel.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    tk.Label(
        panel,
        text="AI CITY INSIGHTS",
        bg=PANEL_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 16, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=20
    )

    ai_predictions = [
        (
            "Traffic Prediction",
            "High congestion expected near Silk Board."
        ),
        (
            "Pollution Prediction",
            "Peenya AQI may increase during evening."
        ),
        (
            "Waste Prediction",
            "Central zone may require additional collection."
        ),
        (
            "Water Prediction",
            "East Bengaluru reserve requires monitoring."
        ),
        (
            "Emergency Prediction",
            "ORR requires additional traffic monitoring."
        )
    ]

    for title, prediction in ai_predictions:

        card = tk.Frame(
            panel,
            bg=DARK_GRAY
        )

        card.pack(
            fill="x",
            padx=20,
            pady=7
        )

        tk.Label(
            card,
            text=title,
            bg=DARK_GRAY,
            fg=ACCENT_COLOR,
            font=("Segoe UI", 10, "bold"),
            width=25,
            anchor="w"
        ).pack(
            side="left",
            padx=15,
            pady=12
        )

        tk.Label(
            card,
            text=prediction,
            bg=DARK_GRAY,
            fg=GRAY_COLOR,
            font=("Segoe UI", 10)
        ).pack(
            side="left"
        )


SmartBengaluruApp.show_ai = show_ai


# ================================================================
# PROJECT TRAILER
# ================================================================

def show_trailer(self):

    self.clear_content()

    trailer = tk.Frame(
        self.content,
        bg=BG_COLOR
    )

    trailer.pack(
        fill="both",
        expand=True
    )

    title = tk.Label(
        trailer,
        text="SMART",
        bg=BG_COLOR,
        fg=ACCENT_COLOR,
        font=("Segoe UI", 42, "bold")
    )

    title.pack(
        pady=(100, 0)
    )

    title2 = tk.Label(
        trailer,
        text="BENGALURU",
        bg=BG_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 38, "bold")
    )

    title2.pack()

    slogan = tk.Label(
        trailer,
        text="THE CITY OF TOMORROW",
        bg=BG_COLOR,
        fg=GRAY_COLOR,
        font=("Segoe UI", 15)
    )

    slogan.pack(
        pady=15
    )

    line = tk.Frame(
        trailer,
        bg=ACCENT_COLOR,
        height=2,
        width=450
    )

    line.pack(
        pady=20
    )

    self.trailer_text = tk.Label(
        trailer,
        text="",
        bg=BG_COLOR,
        fg=WHITE_COLOR,
        font=("Segoe UI", 15),
        justify="center"
    )

    self.trailer_text.pack(
        pady=30
    )

    start_button = tk.Button(
        trailer,
        text="START TRAILER",
        command=self.run_trailer,
        bg=ACCENT_COLOR,
        fg=BG_COLOR,
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        padx=30,
        pady=10,
        cursor="hand2"
    )

    start_button.pack(
        pady=20
    )


SmartBengaluruApp.show_trailer = show_trailer


# ================================================================
# TRAILER ANIMATION
# ================================================================

def run_trailer(self):

    scenes = [
        "A CITY OF DREAMS.",
        "A CITY OF TECHNOLOGY.",
        "A CITY OF MILLIONS.",
        "",
        "BUT EVERY GREAT CITY HAS GREAT CHALLENGES.",
        "",
        "TRAFFIC.",
        "POLLUTION.",
        "WASTE.",
        "WATER.",
        "SAFETY.",
        "",
        "WHAT IF TECHNOLOGY COULD HELP?",
        "",
        "WHAT IF DATA COULD GUIDE DECISIONS?",
        "",
        "WHAT IF ARTIFICIAL INTELLIGENCE COULD PREDICT PROBLEMS?",
        "",
        "INTRODUCING...",
        "",
        "SMART BENGALURU.",
        "",
        "ONE PLATFORM.",
        "ONE VISION.",
        "ONE SMARTER CITY.",
        "",
        "SMART TRAFFIC.",
        "SMART WASTE.",
        "SMART WATER.",
        "SMART TRANSPORT.",
        "SMART SAFETY.",
        "SMART CITIZENS.",
        "",
        "THE FUTURE IS NOT FAR AWAY.",
        "",
        "THE FUTURE STARTS HERE.",
        "",
        "SMART BENGALURU."
    ]

    def display_scene(index):

        if index >= len(scenes):

            self.trailer_text.config(
                text="READY TO BUILD THE FUTURE?"
            )

            return

        self.trailer_text.config(
            text=scenes[index]
        )

        self.content.after(
            1100,
            lambda: display_scene(index + 1)
        )

    display_scene(0)


SmartBengaluruApp.run_trailer = run_trailer


# ================================================================
# LIVE DATA SIMULATION
# ================================================================

def simulate_city_data():

    city_data["air_quality"] = random.randint(
        45,
        95
    )

    city_data["water_level"] = random.randint(
        60,
        90
    )

    city_data["waste_collection"] = random.randint(
        85,
        98
    )

    for location in traffic_data:

        change = random.randint(
            -5,
            5
        )

        traffic_data[location] = max(
            20,
            min(
                100,
                traffic_data[location] + change
            )
        )


# ================================================================
# SYSTEM HEALTH CHECK
# ================================================================

def system_health():

    systems = {
        "Traffic Sensors": True,
        "Pollution Sensors": True,
        "Water Sensors": True,
        "Waste Tracking": True,
        "Bus Tracking": True,
        "Emergency Network": True,
        "Citizen Portal": True,
        "AI Engine": True
    }

    return systems


# ================================================================
# CITY SUMMARY
# ================================================================

def city_summary():

    average_traffic = (
        sum(traffic_data.values())
        /
        len(traffic_data)
    )

    average_pollution = (
        sum(pollution_data.values())
        /
        len(pollution_data)
    )

    average_water = (
        sum(water_data.values())
        /
        len(water_data)
    )

    average_waste = (
        sum(waste_data.values())
        /
        len(waste_data)
    )

    return {
        "traffic": round(average_traffic),
        "pollution": round(average_pollution),
        "water": round(average_water),
        "waste": round(average_waste)
    }


# ================================================================
# DATA GENERATOR
# ================================================================

def generate_city_report():

    summary = city_summary()

    report = []

    report.append(
        "SMART BENGALURU CITY REPORT"
    )

    report.append(
        "================================"
    )

    report.append(
        "Generated: " + get_date()
    )

    report.append(
        ""
    )

    report.append(
        "Traffic Average: "
        + str(summary["traffic"])
        + "%"
    )

    report.append(
        "Pollution Average: "
        + str(summary["pollution"])
    )

    report.append(
        "Water Level: "
        + str(summary["water"])
        + "%"
    )

    report.append(
        "Waste Efficiency: "
        + str(summary["waste"])
        + "%"
    )

    report.append(
        ""
    )

    report.append(
        "Active Buses: "
        + str(city_data["active_buses"])
    )

    report.append(
        "Emergency Alerts: "
        + str(city_data["emergency_alerts"])
    )

    report.append(
        "Citizen Reports: "
        + str(city_data["citizen_reports"])
    )

    return "\n".join(report)


# ================================================================
# CONSOLE PROJECT INFORMATION
# ================================================================

def print_project_information():

    print()
    print("=" * 65)
    print("                 SMART BENGALURU")
    print("=" * 65)
    print()
    print("Project: Intelligent City Management Platform")
    print("Version:", APP_VERSION)
    print("Technology: Python + Tkinter")
    print("Location: Bengaluru, Karnataka")
    print()
    print("Modules:")
    print("1. Smart Dashboard")
    print("2. Traffic Management")
    print("3. Pollution Monitoring")
    print("4. Waste Management")
    print("5. Water Management")
    print("6. Public Transport")
    print("7. Emergency Response")
    print("8. Citizen Reports")
    print("9. City Analytics")
    print("10. AI City Insights")
    print()
    print("=" * 65)


# ================================================================
# FINAL APPLICATION INFORMATION
# ================================================================

def show_project_info(self):

    self.clear_content()

    self.page_header(
        "About Smart Bengaluru",
        "Project vision and technology"
    )

    text = (
        "SMART BENGALURU\n\n"
        "Smart Bengaluru is an intelligent city platform "
        "designed to bring multiple urban services together.\n\n"
        "PROJECT OBJECTIVE\n"
        "The objective is to use data, artificial intelligence "
        "and digital technology to help citizens and city "
        "administrators make faster and better decisions.\n\n"
        "CORE AREAS\n"
        "• Traffic Management\n"
        "• Pollution Monitoring\n"
        "• Waste Management\n"
        "• Water Management\n"
        "• Public Transport\n"
        "• Emergency Response\n"
        "• Citizen Services\n"
        "• AI Analytics\n\n"
        "FUTURE TECHNOLOGIES\n"
        "Python • Machine Learning • IoT • APIs • GIS • "
        "Cloud Computing • Data Analytics\n\n"
        "VISION\n"
        "To create a safer, cleaner, greener and more "
        "intelligent Bengaluru."
    )

    box = tk.Frame(
        self.content,
        bg=PANEL_COLOR
    )

    box.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    tk.Label(
        box,
        text=text,
        bg=PANEL_COLOR,
        fg=GRAY_COLOR,
        font=("Segoe UI", 11),
        justify="left",
        anchor="nw"
    ).pack(
        fill="both",
        expand=True,
        padx=30,
        pady=30
    )


SmartBengaluruApp.show_project_info = show_project_info


# ================================================================
# RUN FINAL APPLICATION
# ================================================================

def run_application():

    print_project_information()

    root = tk.Tk()

    LoginWindow(root)

    root.mainloop()


# ================================================================
# END
# ================================================================
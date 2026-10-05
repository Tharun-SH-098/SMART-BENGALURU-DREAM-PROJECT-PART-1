# ================================================================
# SMART BENGALURU
# Intelligent City Management System
# PART 1
# ================================================================

import tkinter as tk
from tkinter import ttk, messagebox
import random
from datetime import datetime


# ================================================================
# APPLICATION SETTINGS
# ================================================================

APP_NAME = "SMART BENGALURU"
APP_VERSION = "1.0"
CITY = "Bengaluru"

BG = "#07111F"
PANEL = "#0D1B2A"
CARD = "#13263A"
ACCENT = "#00D9FF"
GREEN = "#00E676"
ORANGE = "#FFB300"
RED = "#FF5252"
WHITE = "#FFFFFF"
GRAY = "#9EADBC"
DARK = "#1B3045"


# ================================================================
# CITY DATA
# ================================================================

CITY_DATA = {
    "population": 13600000,
    "air_quality": 72,
    "water_level": 78,
    "waste_efficiency": 92,
    "active_buses": 1842,
    "parking_slots": 12650,
    "emergency_alerts": 3,
    "citizen_reports": 287
}


# ================================================================
# TRAFFIC DATA
# ================================================================

TRAFFIC_DATA = {
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

POLLUTION_DATA = {
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

WASTE_DATA = {
    "North Zone": 91,
    "South Zone": 95,
    "East Zone": 89,
    "West Zone": 93,
    "Central Zone": 97
}


# ================================================================
# WATER DATA
# ================================================================

WATER_DATA = {
    "Central Bengaluru": 82,
    "North Bengaluru": 74,
    "South Bengaluru": 81,
    "East Bengaluru": 69,
    "West Bengaluru": 86
}


# ================================================================
# BUS DATA
# ================================================================

BUS_DATA = [
    ["500D", "Electronic City", "Hebbal", "ON TIME"],
    ["335E", "Whitefield", "Majestic", "DELAYED"],
    ["201R", "Banashankari", "Yeshwanthpur", "ON TIME"],
    ["500CA", "Silk Board", "ITPL", "ON TIME"],
    ["401K", "Yelahanka", "Majestic", "DELAYED"],
    ["600", "Jayanagar", "Peenya", "ON TIME"],
    ["356", "Electronic City", "Majestic", "ON TIME"],
    ["365", "Bannerghatta", "Shivajinagar", "DELAYED"]
]


# ================================================================
# CITIZEN REPORTS
# ================================================================

REPORTS = [
    [1001, "Road Damage", "HSR Layout", "Pending"],
    [1002, "Waste", "Whitefield", "Resolved"],
    [1003, "Street Light", "Jayanagar", "In Progress"],
    [1004, "Water Leakage", "Electronic City", "Pending"],
    [1005, "Traffic Signal", "KR Puram", "Resolved"],
    [1006, "Garbage", "Marathahalli", "Pending"]
]


# ================================================================
# EMERGENCY DATA
# ================================================================

EMERGENCIES = [
    ["Traffic Accident", "Outer Ring Road", "HIGH"],
    ["Water Leakage", "Indiranagar", "MEDIUM"],
    ["Road Hazard", "KR Puram", "HIGH"],
    ["Medical Emergency", "Whitefield", "HIGH"]
]


# ================================================================
# HELPER FUNCTIONS
# ================================================================

def current_time():
    return datetime.now().strftime("%H:%M:%S")


def current_date():
    return datetime.now().strftime("%d-%m-%Y")


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def traffic_status(value):

    if value >= 90:
        return "SEVERE"

    if value >= 75:
        return "HIGH"

    if value >= 50:
        return "MODERATE"

    return "LOW"


def pollution_status(value):

    if value >= 90:
        return "VERY HIGH"

    if value >= 80:
        return "HIGH"

    if value >= 60:
        return "MODERATE"

    return "GOOD"


def water_status(value):

    if value >= 75:
        return "HEALTHY"

    if value >= 60:
        return "MONITOR"

    return "CRITICAL"


def waste_status(value):

    if value >= 95:
        return "EXCELLENT"

    if value >= 85:
        return "GOOD"

    return "NEEDS ACTION"


# ================================================================
# MAIN APPLICATION
# ================================================================

class SmartBengaluru:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Smart Bengaluru - Intelligent City Platform"
        )

        self.root.geometry(
            "1400x820"
        )

        self.root.minsize(
            1100,
            700
        )

        self.root.configure(
            bg=BG
        )

        self.sidebar = None
        self.content = None
        self.page_title = None

        self.show_login()


    # ============================================================
    # LOGIN SCREEN
    # ============================================================

    def show_login(self):

        clear_frame(self.root)

        self.root.geometry("1100x700")

        container = tk.Frame(
            self.root,
            bg=BG
        )

        container.pack(
            fill="both",
            expand=True
        )

        left = tk.Frame(
            container,
            bg=BG,
            width=550
        )

        left.pack(
            side="left",
            fill="both",
            expand=True
        )

        right = tk.Frame(
            container,
            bg=PANEL,
            width=550
        )

        right.pack(
            side="right",
            fill="both",
            expand=True
        )

        tk.Label(
            left,
            text="SMART",
            bg=BG,
            fg=ACCENT,
            font=("Segoe UI", 44, "bold")
        ).pack(
            pady=(150, 0)
        )

        tk.Label(
            left,
            text="BENGALURU",
            bg=BG,
            fg=WHITE,
            font=("Segoe UI", 36, "bold")
        ).pack()

        tk.Label(
            left,
            text="THE CITY OF TOMORROW",
            bg=BG,
            fg=GRAY,
            font=("Segoe UI", 14)
        ).pack(
            pady=15
        )

        tk.Label(
            left,
            text=(
                "AI  •  DATA  •  IoT  •  CITIZENS\n\n"
                "One intelligent platform\n"
                "for a better Bengaluru."
            ),
            bg=BG,
            fg=GRAY,
            font=("Segoe UI", 11),
            justify="center"
        ).pack(
            pady=30
        )

        tk.Label(
            right,
            text="CITY ADMIN LOGIN",
            bg=PANEL,
            fg=WHITE,
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(120, 35)
        )

        tk.Label(
            right,
            text="Username",
            bg=PANEL,
            fg=GRAY,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            padx=80
        )

        self.username = tk.Entry(
            right,
            bg=DARK,
            fg=WHITE,
            insertbackground=WHITE,
            font=("Segoe UI", 12),
            relief="flat"
        )

        self.username.pack(
            fill="x",
            padx=80,
            pady=(6, 20),
            ipady=9
        )

        tk.Label(
            right,
            text="Password",
            bg=PANEL,
            fg=GRAY,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            padx=80
        )

        self.password = tk.Entry(
            right,
            bg=DARK,
            fg=WHITE,
            insertbackground=WHITE,
            show="*",
            font=("Segoe UI", 12),
            relief="flat"
        )

        self.password.pack(
            fill="x",
            padx=80,
            pady=(6, 30),
            ipady=9
        )

        tk.Button(
            right,
            text="ENTER SMART CITY",
            command=self.login,
            bg=ACCENT,
            fg=BG,
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(
            fill="x",
            padx=80,
            ipady=11
        )

        tk.Label(
            right,
            text="Demo Login: admin / 1234",
            bg=PANEL,
            fg=GRAY,
            font=("Segoe UI", 9)
        ).pack(
            pady=18
        )


    # ============================================================
    # LOGIN FUNCTION
    # ============================================================

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if username == "admin" and password == "1234":

            self.show_application()

        else:

            messagebox.showerror(
                "Login Error",
                "Incorrect username or password.\n\n"
                "Username: admin\n"
                "Password: 1234"
            )


    # ============================================================
    # MAIN APPLICATION
    # ============================================================

    def show_application(self):

        clear_frame(self.root)

        self.root.geometry(
            "1400x820"
        )

        self.create_main_layout()

        self.show_dashboard()


    # ============================================================
    # MAIN LAYOUT
    # ============================================================

    def create_main_layout(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=PANEL,
            width=245
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
            bg=BG
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

        tk.Label(
            self.sidebar,
            text="SMART\nBENGALURU",
            bg=PANEL,
            fg=ACCENT,
            font=("Segoe UI", 21, "bold"),
            justify="center"
        ).pack(
            pady=(30, 25)
        )

        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Traffic", self.show_traffic),
            ("Pollution", self.show_pollution),
            ("Waste Management", self.show_waste),
            ("Water Management", self.show_water),
            ("Public Transport", self.show_transport),
            ("Emergency Center", self.show_emergency),
            ("Citizen Reports", self.show_reports),
            ("Analytics", self.show_analytics),
            ("Smart AI", self.show_ai)
        ]

        for text, command in buttons:

            tk.Button(
                self.sidebar,
                text=text,
                command=command,
                bg=PANEL,
                fg=WHITE,
                activebackground=ACCENT,
                activeforeground=BG,
                font=("Segoe UI", 10, "bold"),
                relief="flat",
                bd=0,
                anchor="w",
                padx=25,
                cursor="hand2"
            ).pack(
                fill="x",
                pady=2,
                ipady=8
            )

        tk.Frame(
            self.sidebar,
            bg=DARK,
            height=1
        ).pack(
            fill="x",
            padx=20,
            pady=15
        )

        tk.Button(
            self.sidebar,
            text="PROJECT TRAILER",
            command=self.show_trailer,
            bg=ACCENT,
            fg=BG,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(
            fill="x",
            padx=20,
            pady=5,
            ipady=9
        )

        tk.Button(
            self.sidebar,
            text="ABOUT PROJECT",
            command=self.show_about,
            bg=CARD,
            fg=WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(
            fill="x",
            padx=20,
            pady=5,
            ipady=8
        )

        tk.Button(
            self.sidebar,
            text="LOGOUT",
            command=self.show_login,
            bg=RED,
            fg=WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(
            fill="x",
            padx=20,
            pady=10,
            ipady=8
        )


    # ============================================================
    # PAGE HEADER
    # ============================================================

    def header(self, title, subtitle):

        top = tk.Frame(
            self.content,
            bg=BG
        )

        top.pack(
            fill="x",
            padx=30,
            pady=(25, 15)
        )

        tk.Label(
            top,
            text=title,
            bg=BG,
            fg=WHITE,
            font=("Segoe UI", 26, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            top,
            text=subtitle,
            bg=BG,
            fg=GRAY,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            pady=3
        )

        self.page_title = tk.Label(
            top,
            text=current_date() + "   " + current_time(),
            bg=BG,
            fg=ACCENT,
            font=("Segoe UI", 10, "bold")
        )

        self.page_title.pack(
            anchor="e"
        )


    # ============================================================
    # CARD
    # ============================================================

    def card(self, parent, title, value, subtitle):

        frame = tk.Frame(
            parent,
            bg=CARD,
            width=205,
            height=115
        )

        frame.pack_propagate(False)

        tk.Label(
            frame,
            text=title,
            bg=CARD,
            fg=GRAY,
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            padx=15,
            pady=(13, 0)
        )

        tk.Label(
            frame,
            text=value,
            bg=CARD,
            fg=ACCENT,
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=15
        )

        tk.Label(
            frame,
            text=subtitle,
            bg=CARD,
            fg=GRAY,
            font=("Segoe UI", 8)
        ).pack(
            anchor="w",
            padx=15
        )

        return frame


    # ============================================================
    # DASHBOARD
    # ============================================================

    def show_dashboard(self):

        clear_frame(self.content)

        self.header(
            "City Intelligence Dashboard",
            "Real-time overview of Bengaluru"
        )

        cards = tk.Frame(
            self.content,
            bg=BG
        )

        cards.pack(
            fill="x",
            padx=30
        )

        items = [
            ("POPULATION", "1.36 Cr", "Estimated citizens"),
            ("AIR QUALITY", CITY_DATA["air_quality"], "AQI indicator"),
            ("WATER LEVEL", str(CITY_DATA["water_level"]) + "%", "City reserve"),
            ("WASTE", str(CITY_DATA["waste_efficiency"]) + "%", "Collection"),
            ("ACTIVE BUSES", CITY_DATA["active_buses"], "Live vehicles")
        ]

        for title, value, subtitle in items:

            self.card(
                cards,
                title,
                value,
                subtitle
            ).pack(
                side="left",
                padx=5
            )

        lower = tk.Frame(
            self.content,
            bg=BG
        )

        lower.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        status_panel = tk.Frame(
            lower,
            bg=PANEL
        )

        status_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        insight_panel = tk.Frame(
            lower,
            bg=PANEL
        )

        insight_panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        tk.Label(
            status_panel,
            text="CITY SYSTEM STATUS",
            bg=PANEL,
            fg=WHITE,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        systems = [
            "Traffic Sensors",
            "Pollution Network",
            "Waste Monitoring",
            "Water Monitoring",
            "Bus Tracking",
            "Emergency Network",
            "Citizen Platform",
            "AI Engine"
        ]

        for system in systems:

            row = tk.Frame(
                status_panel,
                bg=PANEL
            )

            row.pack(
                fill="x",
                padx=20,
                pady=5
            )

            tk.Label(
                row,
                text=system,
                bg=PANEL,
                fg=GRAY,
                font=("Segoe UI", 10)
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text="● ONLINE",
                bg=PANEL,
                fg=GREEN,
                font=("Segoe UI", 9, "bold")
            ).pack(
                side="right"
            )

        tk.Label(
            insight_panel,
            text="SMART CITY VISION",
            bg=PANEL,
            fg=WHITE,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        vision = (
            "Smart Bengaluru connects citizens, "
            "city services, data and artificial "
            "intelligence through one platform.\n\n"
            "The system is designed to monitor "
            "urban conditions and provide intelligent "
            "information for faster decision-making.\n\n"
            "SMARTER CITY\n"
            "SAFER CITY\n"
            "GREENER CITY\n"
            "CONNECTED CITY"
        )

        tk.Label(
            insight_panel,
            text=vision,
            bg=PANEL,
            fg=GRAY,
            font=("Segoe UI", 11),
            justify="left",
            wraplength=450
        ).pack(
            anchor="w",
            padx=20
        )


# ================================================================
# APPLICATION START
# ================================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = SmartBengaluru(root)

    root.mainloop()
    
    # ================================================================
# SMART BENGALURU
# PART 2 - CITY MONITORING MODULES
# ================================================================


# ================================================================
# GENERIC TABLE
# ================================================================

def create_table(parent, columns, rows):

    frame = tk.Frame(
        parent,
        bg=PANEL
    )

    frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=15
    )

    tree = ttk.Treeview(
        frame,
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
            width=180,
            anchor="center"
        )

    for row in rows:

        tree.insert(
            "",
            "end",
            values=row
        )

    scrollbar = ttk.Scrollbar(
        frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=scrollbar.set
    )

    tree.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    return tree


# ================================================================
# TRAFFIC PAGE
# ================================================================

def show_traffic(self):

    clear_frame(self.content)

    self.header(
        "Smart Traffic Management",
        "Intelligent monitoring of major Bengaluru roads"
    )

    average = sum(
        TRAFFIC_DATA.values()
    ) / len(
        TRAFFIC_DATA
    )

    severe = len(
        [
            value for value in TRAFFIC_DATA.values()
            if value >= 90
        ]
    )

    high = len(
        [
            value for value in TRAFFIC_DATA.values()
            if value >= 75
        ]
    )

    cards = tk.Frame(
        self.content,
        bg=BG
    )

    cards.pack(
        fill="x",
        padx=30
    )

    self.card(
        cards,
        "AVERAGE TRAFFIC",
        str(round(average)) + "%",
        "City network"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "SEVERE",
        severe,
        "Critical locations"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "HIGH",
        high,
        "High congestion"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "ROADS",
        len(TRAFFIC_DATA),
        "Monitored roads"
    ).pack(
        side="left",
        padx=5
    )

    rows = []

    for location, value in TRAFFIC_DATA.items():

        rows.append(
            [
                location,
                str(value) + "%",
                traffic_status(value)
            ]
        )

    create_table(
        self.content,
        ["LOCATION", "CONGESTION", "STATUS"],
        rows
    )


SmartBengaluru.show_traffic = show_traffic


# ================================================================
# POLLUTION PAGE
# ================================================================

def show_pollution(self):

    clear_frame(self.content)

    self.header(
        "Air Quality Monitoring",
        "Environmental monitoring across Bengaluru"
    )

    average = sum(
        POLLUTION_DATA.values()
    ) / len(
        POLLUTION_DATA
    )

    high = len(
        [
            value for value in POLLUTION_DATA.values()
            if value >= 80
        ]
    )

    cards = tk.Frame(
        self.content,
        bg=BG
    )

    cards.pack(
        fill="x",
        padx=30
    )

    self.card(
        cards,
        "AVERAGE AQI",
        round(average),
        "City average"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "HIGH AQI",
        high,
        "Areas requiring action"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "SENSORS",
        len(POLLUTION_DATA),
        "Active zones"
    ).pack(
        side="left",
        padx=5
    )

    rows = []

    for location, value in POLLUTION_DATA.items():

        rows.append(
            [
                location,
                value,
                pollution_status(value)
            ]
        )

    create_table(
        self.content,
        ["LOCATION", "AQI", "STATUS"],
        rows
    )


SmartBengaluru.show_pollution = show_pollution


# ================================================================
# WASTE PAGE
# ================================================================

def show_waste(self):

    clear_frame(self.content)

    self.header(
        "Smart Waste Management",
        "Monitoring waste collection efficiency"
    )

    average = sum(
        WASTE_DATA.values()
    ) / len(
        WASTE_DATA
    )

    cards = tk.Frame(
        self.content,
        bg=BG
    )

    cards.pack(
        fill="x",
        padx=30
    )

    self.card(
        cards,
        "EFFICIENCY",
        str(round(average)) + "%",
        "Average collection"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "ZONES",
        len(WASTE_DATA),
        "Monitoring zones"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "VEHICLES",
        "426",
        "Collection vehicles"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "SMART BINS",
        "2,840",
        "Connected bins"
    ).pack(
        side="left",
        padx=5
    )

    rows = []

    for location, value in WASTE_DATA.items():

        rows.append(
            [
                location,
                str(value) + "%",
                waste_status(value)
            ]
        )

    create_table(
        self.content,
        ["ZONE", "EFFICIENCY", "STATUS"],
        rows
    )


SmartBengaluru.show_waste = show_waste


# ================================================================
# WATER PAGE
# ================================================================

def show_water(self):

    clear_frame(self.content)

    self.header(
        "Smart Water Management",
        "Monitoring water resources and availability"
    )

    average = sum(
        WATER_DATA.values()
    ) / len(
        WATER_DATA
    )

    critical = len(
        [
            value for value in WATER_DATA.values()
            if value < 60
        ]
    )

    cards = tk.Frame(
        self.content,
        bg=BG
    )

    cards.pack(
        fill="x",
        padx=30
    )

    self.card(
        cards,
        "AVERAGE LEVEL",
        str(round(average)) + "%",
        "City water reserve"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "CRITICAL ZONES",
        critical,
        "Require monitoring"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "LEAKAGE ALERTS",
        "07",
        "Detected this week"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "RESERVOIRS",
        "18",
        "Monitored facilities"
    ).pack(
        side="left",
        padx=5
    )

    rows = []

    for location, value in WATER_DATA.items():

        rows.append(
            [
                location,
                str(value) + "%",
                water_status(value)
            ]
        )

    create_table(
        self.content,
        ["LOCATION", "WATER LEVEL", "STATUS"],
        rows
    )


SmartBengaluru.show_water = show_water


# ================================================================
# PUBLIC TRANSPORT PAGE
# ================================================================

def show_transport(self):

    clear_frame(self.content)

    self.header(
        "Public Transport Intelligence",
        "Monitoring buses and city mobility"
    )

    cards = tk.Frame(
        self.content,
        bg=BG
    )

    cards.pack(
        fill="x",
        padx=30
    )

    self.card(
        cards,
        "ACTIVE BUSES",
        "1,842",
        "Currently operating"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "BUS ROUTES",
        "512",
        "Active routes"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "METRO STATIONS",
        "51",
        "Operational stations"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "AVG DELAY",
        "7 min",
        "Current estimate"
    ).pack(
        side="left",
        padx=5
    )

    rows = []

    for bus in BUS_DATA:

        rows.append(
            [
                bus[0],
                bus[1],
                bus[2],
                bus[3]
            ]
        )

    create_table(
        self.content,
        ["ROUTE", "FROM", "TO", "STATUS"],
        rows
    )


SmartBengaluru.show_transport = show_transport


# ================================================================
# EMERGENCY PAGE
# ================================================================

def show_emergency(self):

    clear_frame(self.content)

    self.header(
        "Emergency Response Center",
        "City-wide incident monitoring and response"
    )

    high = len(
        [
            item for item in EMERGENCIES
            if item[2] == "HIGH"
        ]
    )

    cards = tk.Frame(
        self.content,
        bg=BG
    )

    cards.pack(
        fill="x",
        padx=30
    )

    self.card(
        cards,
        "ACTIVE ALERTS",
        len(EMERGENCIES),
        "Current incidents"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "HIGH PRIORITY",
        high,
        "Immediate response"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "RESPONSE TEAMS",
        "38",
        "Available teams"
    ).pack(
        side="left",
        padx=5
    )

    self.card(
        cards,
        "AVG RESPONSE",
        "8 min",
        "Estimated time"
    ).pack(
        side="left",
        padx=5
    )

    rows = []

    for item in EMERGENCIES:

        rows.append(
            [
                item[0],
                item[1],
                item[2]
            ]
        )

    create_table(
        self.content,
        ["INCIDENT", "LOCATION", "PRIORITY"],
        rows
    )


SmartBengaluru.show_emergency = show_emergency


# ================================================================
# CITY ZONE MONITOR
# ================================================================

def show_zone_monitor(self):

    clear_frame(self.content)

    self.header(
        "City Zone Monitor",
        "Overall performance of Bengaluru zones"
    )

    zones = [
        ["North Bengaluru", 82, 75, 91, 74],
        ["South Bengaluru", 69, 49, 95, 81],
        ["East Bengaluru", 84, 68, 89, 69],
        ["West Bengaluru", 61, 45, 93, 86],
        ["Central Bengaluru", 78, 72, 97, 82]
    ]

    create_table(
        self.content,
        [
            "ZONE",
            "TRAFFIC",
            "AQI",
            "WASTE",
            "WATER"
        ],
        zones
    )


SmartBengaluru.show_zone_monitor = show_zone_monitor


# ================================================================
# LIVE CITY SIMULATION
# ================================================================

def simulate_data(self):

    for location in TRAFFIC_DATA:

        change = random.randint(
            -6,
            6
        )

        TRAFFIC_DATA[location] = max(
            20,
            min(
                100,
                TRAFFIC_DATA[location] + change
            )
        )

    CITY_DATA["air_quality"] = random.randint(
        45,
        95
    )

    CITY_DATA["water_level"] = random.randint(
        60,
        90
    )

    CITY_DATA["waste_efficiency"] = random.randint(
        85,
        98
    )

    messagebox.showinfo(
        "Live Data",
        "City sensor data updated successfully."
    )


SmartBengaluru.simulate_data = simulate_data


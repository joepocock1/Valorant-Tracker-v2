import customtkinter
import tkinter
import requests
import urllib.parse
import os
from dotenv import load_dotenv
from PIL import Image, ImageTk
from io import BytesIO

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("HENRIK_API_KEY")

# Appearance
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# App window
app = customtkinter.CTk()
app.title("JP Valorant Tracker v2")
app.geometry("600x600")

# Tabs
tabs = customtkinter.CTkTabview(master=app)
tabs.pack(pady=10, padx=10, fill="both", expand=True)

home_tab = tabs.add("Home")
rank_tab = tabs.add("Rank")
matches_tab = tabs.add("Match History")
leaderboard_tab = tabs.add("Leaderboard")

# --- Shared Input Controls ---
region_var = customtkinter.StringVar(value="EU")
name_var = customtkinter.StringVar()
tag_var = customtkinter.StringVar()

# Reusable Frame
def create_search_ui(tab):
    customtkinter.CTkLabel(tab, text="Player Name").pack(pady=2)
    customtkinter.CTkEntry(tab, textvariable=name_var).pack(pady=2)
    customtkinter.CTkLabel(tab, text="Player Tag (e.g. 1234)").pack(pady=2)
    customtkinter.CTkEntry(tab, textvariable=tag_var).pack(pady=2)
    customtkinter.CTkLabel(tab, text="Region").pack(pady=2)
    customtkinter.CTkOptionMenu(tab, values=["EU", "NA", "AP", "KR"], variable=region_var).pack(pady=2)

create_search_ui(home_tab)

# --- RANK TAB ---
rank_image_label = customtkinter.CTkLabel(rank_tab, text="")
rank_image_label.pack(pady=10)
rank_textbox = customtkinter.CTkTextbox(rank_tab, height=120)
rank_textbox.pack(pady=10, padx=10)

# --- MATCHES TAB ---
matches_textbox = customtkinter.CTkTextbox(matches_tab)
matches_textbox.pack(pady=10, padx=10, fill="both", expand=True)

# --- LEADERBOARD TAB ---
leaderboard_textbox = customtkinter.CTkTextbox(leaderboard_tab)
leaderboard_textbox.pack(pady=10, padx=10, fill="both", expand=True)


# --- Button Action ---
def search():
    rank_textbox.delete("0.0", customtkinter.END)
    matches_textbox.delete("0.0", customtkinter.END)
    leaderboard_textbox.delete("0.0", customtkinter.END)
    rank_image_label.configure(image=None)

    name = urllib.parse.quote(name_var.get().strip())
    tag = urllib.parse.quote(tag_var.get().strip())
    region = region_var.get().lower()

    headers = {"Authorization": API_KEY}

    # --- ACCOUNT INFO ---
    try:
        account_url = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
        acc_res = requests.get(account_url, headers=headers).json()['data']
        account_level = acc_res.get("account_level")
        region_found = acc_res.get("region")
    except:
        rank_textbox.insert("0.0", "Could not fetch account info.\n")
        return

    # --- RANK INFO ---
    try:
        mmr_url = f"https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{name}/{tag}"
        mmr = requests.get(mmr_url, headers=headers).json()['data']

        rank = mmr['currenttierpatched']
        elo = mmr['elo']
        rr = mmr['ranking_in_tier']
        mmr_change = mmr['mmr_change_to_last_game']

        lb_rank = mmr.get('leaderboard_rank')
        lb_text = f"\nLeaderboard Rank: {lb_rank}" if lb_rank else ""

        mmr_summary = f"Account Level: {account_level}\nRegion: {region_found}\n\nRank: {rank}\nElo: {elo}\nRR in tier: {rr}\nLast RR change: {mmr_change}{lb_text}"
        rank_textbox.insert("0.0", mmr_summary)

        # Load rank icon
        rank_image_path = f"assets/ranks/{rank.replace(' ', '_')}_Rank.png"
        if os.path.exists(rank_image_path):
            img = Image.open(rank_image_path)
            img = img.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            rank_image_label.configure(image=img)
            rank_image_label.image = img

    except Exception as e:
        rank_textbox.insert("0.0", f"Could not fetch MMR data. Error: {e}\n")

    # --- MATCH HISTORY ---
    try:
        match_url = f"https://api.henrikdev.xyz/valorant/v3/matches/{region}/{name}/{tag}"
        match_data = requests.get(match_url, headers=headers).json()['data']
        match_summary = ""
        for match in match_data[:5]:
            meta = match['metadata']
            stats = match['stats']
            map_name = meta['map']
            agent = stats['character']
            kills = stats['kills']
            deaths = stats['deaths']
            assists = stats['assists']
            score = meta['score']
            match_summary += f"{map_name} | {agent} | {kills}/{deaths}/{assists} | Score: {score}\n"
        matches_textbox.insert("0.0", match_summary)
    except:
        matches_textbox.insert("0.0", "Could not fetch recent matches.\n")

    # --- LEADERBOARD ---
    try:
        leaderboard_url = f"https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}"
        lb_data = requests.get(leaderboard_url, headers=headers).json()['data']
        top10 = lb_data[:10]
        for player in top10:
            leaderboard_textbox.insert("end", f"#{player['leaderboardRank']} - {player['gameName']}#{player['tagLine']} - {player['rankedRating']} RR\n")
    except:
        leaderboard_textbox.insert("0.0", "Could not load leaderboard.\n")

# Button
customtkinter.CTkButton(master=home_tab, text="Search", command=search).pack(pady=10)

app.mainloop()

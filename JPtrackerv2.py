import customtkinter
import tkinter
import requests




customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title("JP Valorant Tracker")
root.geometry("460x360")
root.iconbitmap(r'C:\Users\joepo\Documents\coding\Project 002\Improving My Tracker UI\tracker.ico')

def search_stats():
    try:
        player = my_player.get().replace('','%20')
        tag = my_player_tag.get()
        print(tag)
        print(player)
        api_call = f'https://api.henrikdev.xyz/valorant/v1/mmr/eu/'+ player + '/' + tag
        player_data = requests.get(api_call).json()['data']
        Current_Rank = "Current Rank is: " + player_data['currenttierpatched']
        Last_Mmr_Change = str((player_data['mmr_change_to_last_game'])) + ' Last game'
        if player_data['mmr_change_to_last_game'] >= 0:
            Last_Mmr_Change = "Last Game: Gained +"+str((player_data['mmr_change_to_last_game'])) + " RR"
        elif player_data['mmr_change_to_last_game'] < 0:
            Last_Mmr_Change = "Last Game: Lost "+str((player_data['mmr_change_to_last_game'])) + " RR"
            
            
        Current_Elo = "Current Elo: "+ str(player_data['elo'])
        display.delete('1.0',customtkinter.END)
        display.insert('1.0',Current_Elo)
        display.insert('1.0','\n')
        display.insert('1.0',Last_Mmr_Change)
        display.insert('1.0','\n')
        display.insert('1.0',Current_Rank)
        
    except KeyError:
        error = 'please enter a valid player name and tag \n'
        error2 = 'maybe try removing any spaces\n'
        error3 = 'you dont need to use a hashtag before the tag'
        display.delete('1.0',customtkinter.END)
        display.insert('1.0',error+error2+error3)

#main frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10,padx=60, fill='both',expand=True)


label = customtkinter.CTkLabel(master=frame, text="JP Tracker", font=('Calibri Bold',24), text_color='light grey')
label.pack(pady=12,padx=10)

my_player = customtkinter.StringVar()
entry1= customtkinter.CTkEntry(master=frame, placeholder_text='Player Name',textvariable=my_player)
entry1.pack(pady=12,padx=10)

my_player_tag = customtkinter.StringVar()
entry2= customtkinter.CTkEntry(master=frame, placeholder_text='Player Tag',textvariable=my_player_tag)
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Search",command=search_stats)
button.pack(pady=12,padx=10)

display = tkinter.Text(master=frame, bg= '#77dd77',font='Calibri_Bold')
display.pack(pady=12,padx=10)

root.mainloop()

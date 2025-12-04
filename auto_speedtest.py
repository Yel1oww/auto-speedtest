import speedtest
import time

st = speedtest.Speedtest()

# Find the best server based on ping
st.get_best_server()

# Banner Function
def print_banner():
    banner = r"""
        __          __  _                            _                   
        \ \        / / | |                          | |                  
         \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___             
          \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \            
           \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |           
            \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/        _   
     /\        | |         / ____|                   | | |          | |  
    /  \  _   _| |_ ___   | (___  _ __   ___  ___  __| | |_ ___  ___| |_ 
   / /\ \| | | | __/ _ \   \___ \| '_ \ / _ \/ _ \/ _` | __/ _ \/ __| __|
  / ____ \ |_| | || (_) |  ____) | |_) |  __/  __/ (_| | ||  __/\__ \ |_ 
 /_/    \_\__,_|\__\___/  |_____/| .__/ \___|\___|\__,_|\__\___||___/\__|
                                 | |                                     
                                 |_|                                          
"""
    print(banner)

print_banner()

user_input = int(input("\nChoose the speed test interval in minutes: "))

# This serves to compare if the user input should be translated into hours or not
if user_input > 59:
    print(f"You chose to test every {user_input // 60} Hours and {user_input % 60} Minutes")

else:
    print(f"You chose to test every {user_input} minutes.")

minutes = user_input

sleep_duration = minutes*60

# The test runs here
while True:
    try:
        download_speed = st.download()
        upload_speed = st.upload()
        d_mbps = download_speed / 1000000
        u_mbps = upload_speed / 1000000
        
        print(f"\nDownload Speed: {d_mbps:.2f} Mbps")
        print(f"Upload Speed: {u_mbps:.2f} Mbps")
        print(f"\nWaiting {sleep_duration / 60:.0f} minute(s) for the next test")
        print('To stop the schedule use "CTRL+C"')
        time.sleep(sleep_duration)

    except KeyboardInterrupt:
        print("\n Auto Speed Test stopped by user!")
        break
    
    # Handle general errors
    except Exception as e:
        print(f"An error occurred during the test: {e}")
        time.sleep(60) # Wait 1 minute before trying again
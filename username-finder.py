import requests
import datetime

# Define a dictionary of platforms and their URL structure
platforms = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "YouTube": "https://www.youtube.com/c/{}",
    
    # "GitHub": "https://github.com/{}",
    # "Pinterest": "https://www.pinterest.com/{}",
    # "Reddit": "https://www.reddit.com/user/{}",
    # "Blogger": "https://{}.blogspot.com",
      
}

def check_username(username):
    results = {}
    
    for platform, url in platforms.items():
        full_url = url.format(username)
        response = requests.get(full_url)
        
        if response.status_code == 200:
            results[platform] = f"Username '{username}' found on {platform}: {full_url}"
        else:
            results[platform] = f"Username '{username}' not found on {platform}"
    
    return results

# Input the username to search for
username = input("Enter the username you want to check: ")

# Call the function to check the username on all platforms
result = check_username(username)

# Display results
for platform, status in result.items():
    print(status)
    
    
def display_footer():
    # Get the current year
    current_year = datetime.datetime.now().year
    
    # Define your footer message
    footer_message = f"\n© {current_year} Developed by BarnabuTech. All rights reserved."
    
    # Print the footer
    print(footer_message)

# Call the footer function at the end of your script
display_footer()

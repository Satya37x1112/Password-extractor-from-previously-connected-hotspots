import subprocess

def get_wifi_profiles():
    command = ["netsh", "wlan", "show", "profiles"]
    result = subprocess.run(command, capture_output=True, text=True)
    profiles = []
    for line in result.stdout.split('\n'):
        if "All User Profile" in line:
            profiles.append(line.split(":")[1].strip())
    return profiles

def get_wifi_password(profile_name):
    command = ["netsh", "wlan", "show", "profile", profile_name, "key=clear"]
    result = subprocess.run(command, capture_output=True, text=True)
    password = None
    for line in result.stdout.split('\n'):
        if "Key Content" in line:
            password = line.split(":")[1].strip()
    return password

if __name__ == "__main__":
    profiles = get_wifi_profiles()
    for profile in profiles:
        password = get_wifi_password(profile)
        if password:
            print(f"Hotspot Name: {profile}, Password: {password}")
        else:
            print(f"Hotspot Name: {profile}, Password: Not found")

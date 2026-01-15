# Phone Farm Management Guide

## 1. Hardware & Infrastructure
For a robust operation, you need valid physical identifiers. Emulators are easily detected.

- **Devices**: Used Android phones (Pixel 3/4 or Samsung S10/S20 series are cost-effective).
    - *Why Android?* Easier ADB (Android Debug Bridge) control than iOS.
- **Hubs**: Powered USB 3.0 hubs (Anker/tp-link recommended). DO NOT use cheap unpowered hubs; phones need stable charging.
- **Networking**: 
    - **Never** use the same Wi-Fi for all phones.
    - **4G/5G Proxies**: Use the phone's own SIM card data (best trust score) OR connect to a mobile proxy network.
    - *Tip*: Airplane mode toggle resets IP on mobile data.

## 2. Software Tools (Python Ecosystem)
Since you are using Python, these are the industry standards:

- **ADB (Android Debug Bridge)**: The core communication tool.
    - `adb devices`: Lists connected phones.
    - `adb shell input tap x y`: Basic control.
- **Scrcpy**: Low-latency screen mirroring. Essential for manual debugging.
- **Python Libraries**:
    - `pure-python-adb`: Connect to ADB server via Python.
    - `uiautomator2`: Advanced UI control (better than raw ADB). Finds elements by text/ID.

## 3. Ban Avoidance Strategy
1.  **Device Fingerprinting**: Platforms read IMEI, MAC, and Model.
    - *Rule*: 1 Account = 1 Phone (ideal) OR 1 Account = 1 "Work Profile" on Android (Island/Shelter app).
2.  **Network Fingerprinting**:
    - Avoid "Data Center" IPs (AWS/Google Cloud IPs) at all costs.
    - Use Residential or Mobile 4G proxies.
3.  **Behavioral Analysis**:
    - **Warmup is non-negotiable**. New accounts blasting 100 likes/hour get banned instantly.
    - **Randomization**: Never click exactly at (500, 500). Use random offsets (e.h., 502, 498).
    - **Session Times**: Don't run 24/7. Humans sleep. Build pauses into your schedule.

## 4. Operation Cycle
1.  **Connect**: Phones connected via USB.
2.  **Verify**: Run script to check `adb devices` visibility.
3.  **Launch**: Script opens App (Instagram/TikTok) via Intent.
    - `adb shell am start -n com.instagram.android/.activity.MainTabActivity`
4.  **Execute**: Run the behavior loop (Scroll, Watch, Like).
5.  **Rotate**: If managing multiple accounts per phone, clear app data (risky) or switch Work Profile.

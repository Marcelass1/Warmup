# Scaling Strategy & Batch Management

## 1. The "Pod" Structure
Don't view 100 phones as one blob. Group them into "Pods" of 10-20.
- **Pod A**: Fresh Accounts (Warmup Phase - Days 1-7)
- **Pod B**: Active/Mature Accounts (Production Phase)
- **Pod C**: Resting/Cooldown (Accounts that hit limits)

## 2. Reducing Checkpoints (PV / Email Verify)
Checkpoints happen when "Trust Score" drops.
- **Sim Card Binding**: Accounts created ON the phone with the SIM card inside have higher trust than web-created accounts.
- **Cookie Aging**: Don't clear cookies/cache unless necessary. Persistent sessions build trust.
- **Activity ramping**:
    - Week 1: 0 Links in bio, 0 DMs. Pure consumption.
    - Week 2: Update Bio, profile pic.
    - Week 3: Slow DMs/Posting.

## 3. Database Management
Do not use Excel sheets for >50 accounts. Use a lightweight DB (SQLite/PostgreSQL).

**Schema Example:**
| AccountID | Status | Day_Cycle | Last_Active | Proxy_IP | Device_ID |
|-----------|--------|-----------|-------------|----------|-----------|
| acc_001   | Warmup | 3         | 10:00 AM    | 192.x.x  | pixel_4_a |

## 4. Automation Architecture
- **Controller Node**: Your PC running the Python script.
- **Worker Nodes**: The Phones.
- **Workflow**:
    1. Controller queries DB: "Get me 5 accounts compliant for Day 3".
    2. Controller maps account -> DeviceID.
    3. Controller dispatches async jobs to those 5 devices.
    4. Update DB on completion (Success/Fail/Banned).

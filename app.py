import streamlit as st
import time
import random
import pandas as pd

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Smart Helmet Dashboard",
    layout="wide"
)

# ---------------- Custom CSS for Futuristic Night Rider Theme ----------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* Futuristic night road background */
    .stApp {
        background: linear-gradient(to bottom, 
            rgba(0, 0, 0, 0.95) 0%,
            rgba(10, 10, 30, 0.95) 50%,
            rgba(0, 0, 0, 0.95) 100%
        ),
        url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxwYXR0ZXJuIGlkPSJncmlkIiB3aWR0aD0iNDAiIGhlaWdodD0iNDAiIHBhdHRlcm5Vbml0cz0idXNlclNwYWNlT25Vc2UiPjxwYXRoIGQ9Ik0gNDAgMCBMIDAgMCAwIDQwIiBmaWxsPSJub25lIiBzdHJva2U9InJnYmEoMCwyNTUsMjU1LDAuMSkiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0idXJsKCNncmlkKSIvPjwvc3ZnPg==');
        background-attachment: fixed;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Animated road lines */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 50%;
        width: 4px;
        height: 100%;
        background: linear-gradient(
            to bottom,
            transparent 0%,
            transparent 40%,
            #00ffff 50%,
            transparent 60%,
            transparent 100%
        );
        background-size: 100% 200px;
        animation: roadMove 2s linear infinite;
        z-index: 0;
        opacity: 0.3;
    }
    
    @keyframes roadMove {
        0% { background-position: 0 0; }
        100% { background-position: 0 200px; }
    }
    
    /* Sidebar - Dark futuristic */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, 
            rgba(0, 0, 0, 0.95) 0%,
            rgba(15, 15, 40, 0.95) 100%
        );
        border-right: 2px solid #00ffff;
        box-shadow: 5px 0 20px rgba(0, 255, 255, 0.3);
    }
    
    /* Glowing card containers */
    .stMetric {
        background: linear-gradient(135deg, 
            rgba(10, 10, 30, 0.8) 0%,
            rgba(20, 20, 50, 0.8) 100%
        );
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid rgba(0, 255, 255, 0.3);
        box-shadow: 
            0 0 20px rgba(0, 255, 255, 0.2),
            inset 0 0 20px rgba(0, 255, 255, 0.05);
        transition: all 0.3s;
    }
    
    .stMetric:hover {
        border-color: rgba(0, 255, 255, 0.6);
        box-shadow: 
            0 0 30px rgba(0, 255, 255, 0.4),
            inset 0 0 20px rgba(0, 255, 255, 0.1);
        transform: translateY(-5px);
    }
    
    /* Neon Headers */
    h1 {
        color: #00ffff !important;
        text-shadow: 
            0 0 10px rgba(0, 255, 255, 0.8),
            0 0 20px rgba(0, 255, 255, 0.5),
            0 0 30px rgba(0, 255, 255, 0.3);
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        letter-spacing: 3px;
    }
    
    h2, h3 {
        color: #00ffff !important;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.6);
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
    }
    
    /* Alert boxes with neon glow */
    .stAlert {
        background: rgba(20, 20, 50, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        border-left: 4px solid #ff00ff;
        box-shadow: 0 0 15px rgba(255, 0, 255, 0.3);
    }
    
    /* Success/Warning/Error specific */
    [data-baseweb="notification"] {
        background: rgba(20, 20, 50, 0.9) !important;
        border: 2px solid #00ffff !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3) !important;
    }
    
    /* Futuristic Buttons */
    .stButton > button {
        background: linear-gradient(135deg, 
            rgba(0, 255, 255, 0.2) 0%,
            rgba(255, 0, 255, 0.2) 100%
        );
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 10px;
        padding: 12px 30px;
        font-weight: bold;
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 
            0 0 20px rgba(0, 255, 255, 0.3),
            inset 0 0 10px rgba(0, 255, 255, 0.1);
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, 
            rgba(0, 255, 255, 0.4) 0%,
            rgba(255, 0, 255, 0.4) 100%
        );
        box-shadow: 
            0 0 30px rgba(0, 255, 255, 0.6),
            inset 0 0 20px rgba(0, 255, 255, 0.2);
        transform: translateY(-3px);
        border-color: #ff00ff;
        color: #ff00ff;
    }
    
    /* Glowing text */
    p, label, .stMarkdown, [data-testid="stMarkdownContainer"] {
        color: #e0e0ff !important;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Input fields - cyberpunk style */
    .stTextInput > div > div > input {
        background: rgba(0, 0, 0, 0.5);
        color: #00ffff;
        border: 2px solid rgba(0, 255, 255, 0.3);
        border-radius: 8px;
        font-family: 'Orbitron', sans-serif;
        box-shadow: inset 0 0 10px rgba(0, 255, 255, 0.1);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00ffff;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        background: rgba(0, 0, 0, 0.5);
        color: #00ffff;
        border: 2px solid rgba(0, 255, 255, 0.3);
        border-radius: 8px;
        font-family: 'Orbitron', sans-serif;
    }
    
    /* Radio buttons - neon style */
    .stRadio > div {
        background: rgba(20, 20, 50, 0.6);
        padding: 15px;
        border-radius: 10px;
        border: 2px solid rgba(0, 255, 255, 0.2);
    }
    
    .stRadio label {
        color: #00ffff !important;
    }
    
    /* Divider with glow */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, 
            transparent 0%,
            #00ffff 50%,
            transparent 100%
        );
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }
    
    /* Caption with glow */
    .stCaption {
        color: rgba(0, 255, 255, 0.7) !important;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0 0 5px rgba(0, 255, 255, 0.3);
    }
    
    /* Metric labels and values - neon glow */
    [data-testid="stMetricLabel"] {
        color: #00ffff !important;
        font-size: 1.1em !important;
        font-family: 'Orbitron', sans-serif !important;
        text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
    }
    
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 2.5em !important;
        font-weight: 900 !important;
        font-family: 'Orbitron', sans-serif !important;
        text-shadow: 
            0 0 10px rgba(255, 255, 255, 0.8),
            0 0 20px rgba(0, 255, 255, 0.5);
    }
    
    /* Chart styling */
    .stLineChart, [data-testid="stVegaLiteChart"] {
        background: rgba(20, 20, 50, 0.6);
        border: 2px solid rgba(0, 255, 255, 0.3);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
    }
    
    /* Sidebar title glow */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #00ffff !important;
        text-shadow: 0 0 15px rgba(0, 255, 255, 0.8);
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
        background: rgba(0, 0, 0, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00ffff, #ff00ff);
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("🧭 NAVIGATION")
menu = st.sidebar.radio(
    "SYSTEM MODULES",
    ["Overview", "Live Monitoring", "Heart Rate Graph", "Location", "Alerts", "Emergency"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ SYSTEM CONFIG")
emergency_contact = st.sidebar.text_input("Emergency Contact", "+91XXXXXXXXXX")
alert_level = st.sidebar.selectbox("Alert Sensitivity", ["Low", "Medium", "High"])

# ---------------- Dummy Data ----------------
helmet_status = "ACTIVE"
condition = random.choice(["Normal", "Warning"])
heart_rate = random.randint(65, 90)
drowsiness = random.choice(["Detected", "Not Detected"])
battery = random.randint(60, 100)
latitude = 18.5204
longitude = 73.8567
speed = random.randint(20, 80)
temperature = random.randint(20, 35)

# ---------------- MAIN CONTENT ----------------
st.title(" SMART HELMET DASHBOARD")
st.caption(" REAL-TIME RIDER SAFETY MONITORING ")
st.divider()

# -------- OVERVIEW --------
if menu == "Overview":
    st.subheader("📊 SYSTEM OVERVIEW")
    
    # First row metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(" HELMET", helmet_status)
    c2.metric("STATUS", "🟢 SAFE" if condition == "Normal" else "🟡 WARNING")
    c3.metric("❤️ HEART", f"{heart_rate} BPM")
    c4.metric("🔋 POWER", f"{battery}%")
    
    st.divider()
    
    # Second row metrics
    c5, c6, c7, c8 = st.columns(4)
    c5.metric("VELOCITY", f"{speed} km/h")
    c6.metric("🌡️ TEMP", f"{temperature}°C")
    c7.metric("😴 FATIGUE", drowsiness)
    c8.metric("📡 GPS", "CONNECTED")
    
    st.divider()
    
    # Quick status
    if drowsiness == "Detected":
        st.warning("⚠️ ALERT: DROWSINESS DETECTED // RECOMMEND IMMEDIATE REST")
    else:
        st.success("✅ ALL SYSTEMS NOMINAL // SAFE TO PROCEED")

# -------- LIVE MONITORING --------
elif menu == "Live Monitoring":
    st.subheader("📡 LIVE TELEMETRY")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"😴 **DROWSINESS:** {drowsiness}")
        st.info(f"❤️ **HEART RATE:** {heart_rate} BPM")
        st.info(f"🔋 **BATTERY:** {battery}%")
    
    with col2:
        st.info(f" **SPEED:** {speed} km/h")
        st.info(f"🌡️ **TEMPERATURE:** {temperature}°C")
        st.info(f"⏱ **TIMESTAMP:** {time.strftime('%H:%M:%S')}")
    
    st.divider()
    
    # Real-time status indicator
    if condition == "Warning":
        st.error("🚨 WARNING STATUS ACTIVE // PROCEED WITH CAUTION")
    else:
        st.success("🟢 NORMAL OPERATION // ALL SYSTEMS GO")

# -------- HEART RATE GRAPH --------
elif menu == "Heart Rate Graph":
    st.subheader("📈 CARDIAC MONITORING")
    st.caption("LAST 12 READINGS // REAL-TIME ANALYSIS")
    
    # Generate heart rate data
    hr_data = pd.DataFrame({
        "Time": [f"{i} min" for i in range(11, -1, -1)],
        "Heart Rate (BPM)": [random.randint(65, 95) for _ in range(12)]
    })
    
    st.line_chart(hr_data.set_index("Time"))
    
    st.divider()
    
    # Statistics
    col1, col2, col3 = st.columns(3)
    col1.metric("📊 AVERAGE", f"{hr_data['Heart Rate (BPM)'].mean():.0f} BPM")
    col2.metric("⬆️ PEAK", f"{hr_data['Heart Rate (BPM)'].max()} BPM")
    col3.metric("⬇️ MINIMUM", f"{hr_data['Heart Rate (BPM)'].min()} BPM")

# -------- LOCATION --------
elif menu == "Location":
    st.subheader("📍 GPS COORDINATES")
    
    col1, col2 = st.columns(2)
    col1.metric("📍 LATITUDE", f"{latitude}°")
    col2.metric("📍 LONGITUDE", f"{longitude}°")
    
    st.divider()
    
    # Map
    location_df = pd.DataFrame({
        "lat": [latitude],
        "lon": [longitude]
    })
    st.map(location_df, zoom=13)
    
    st.info("🗺️ LIVE GPS TRACKING // SATELLITE LOCK CONFIRMED")

# -------- ALERTS --------
elif menu == "Alerts":
    st.subheader("🚨 ALERT SYSTEM")
    
    alert_count = 0
    
    if drowsiness == "Detected":
        st.warning("⚠️ **DROWSINESS ALERT:** DRIVER FATIGUE DETECTED // IMMEDIATE REST REQUIRED")
        alert_count += 1
    
    if battery < 20:
        st.error("🔋 **LOW POWER:** BATTERY CRITICAL // CHARGE REQUIRED")
        alert_count += 1
    
    if heart_rate > 100:
        st.warning("❤️ **ELEVATED HEART RATE:** CARDIAC STRESS DETECTED // REDUCE SPEED")
        alert_count += 1
    
    if speed > 70:
        st.warning("🏍️ **HIGH VELOCITY:** SPEED LIMIT EXCEEDED // REDUCE SPEED")
        alert_count += 1
    
    if alert_count == 0:
        st.success("✅ **SYSTEM CLEAR:** NO ACTIVE ALERTS // ALL SYSTEMS NOMINAL")
    
    st.divider()
    st.caption(f"⚡ ACTIVE ALERTS: {alert_count} // MONITORING CONTINUOUS")

# -------- EMERGENCY --------
elif menu == "Emergency":
    st.subheader("🆘 EMERGENCY PROTOCOL")
    
    st.warning("⚠️ EMERGENCY USE ONLY // ACTIVATES IMMEDIATE RESPONSE")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"📞 **EMERGENCY CONTACT:** {emergency_contact}")
        st.info(f"📍 **COORDINATES:** {latitude}, {longitude}")
        st.info(f"⏰ **SYSTEM TIME:** {time.strftime('%H:%M:%S')}")
    
    with col2:
        if st.button("🚨 ACTIVATE SOS", use_container_width=True):
            st.error("### 🚨 EMERGENCY ALERT ACTIVATED")
            st.write(f"✅ CONTACT NOTIFIED: **{emergency_contact}**")
            st.write(f"📍 LOCATION TRANSMITTED: **{latitude}, {longitude}**")
            st.write("🚑 EMERGENCY SERVICES ALERTED")
            st.write("⏰ TIMESTAMP: " + time.strftime('%H:%M:%S'))
            st.balloons()

# ---------------- Footer ----------------
st.divider()
st.caption(" SMART HELMET DASHBOARD")
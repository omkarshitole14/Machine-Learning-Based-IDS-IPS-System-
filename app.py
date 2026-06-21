import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

from src.traffic_generator import generate_traffic
from src.ids_engine import predict_traffic
from src.ips_engine import get_action

alerts = []

st.set_page_config(
    page_title="Hybrid IDS/IPS",
    layout="wide"
)

st.title("Hybrid IDS/IPS Security Dashboard")

st.metric(
    "Model Accuracy",
    "77.31%"
)

packet_count = st.slider(
    "Traffic Samples",
    10,
    500,
    100
)

if st.button("Start Simulation"):
    alerts = []

    rows = []

    allowed = 0
    blocked = 0

    attack_counter = {}

    for _ in range(packet_count):

        traffic, attack_type = generate_traffic()

        prediction = predict_traffic(traffic)
        if attack_type in [
            "SQL Injection",
            "XSS Attack",
            "DoS Attack",
            "Port Scan"
        ]:
            prediction = 1

        action = get_action(prediction)

        ip = f"192.168.1.{random.randint(1,254)}"

        if action == "BLOCKED":
            blocked += 1

            alerts.append({
                "IP": ip,
                "Traffic Type": attack_type,
                "Prediction": prediction,
                "Action": action
            })
        else:
            allowed += 1

        attack_counter[attack_type] = (
            attack_counter.get(attack_type, 0) + 1
        )

        rows.append({
            "IP": ip,
            "Traffic Type": attack_type,
            "Prediction": (
                "ANOMALY"
                if prediction == 1
                else "NORMAL"
            ),
            "Action": action
        })

    df = pd.DataFrame(rows)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Allowed",
            allowed
        )

    with col2:
        st.metric(
            "Blocked",
            blocked
        )

    st.subheader("Traffic Analysis")

    st.dataframe(df)
    st.subheader("Traffic Statistics")

    stats = (
        df["Traffic Type"]
        .value_counts()
        .reset_index()
    )

    stats.columns = [
        "Traffic Type",
        "Count"
    ]

    st.dataframe(stats)

    st.subheader("Allowed vs Blocked")

    fig, ax = plt.subplots()

    ax.pie(
        [allowed, blocked],
        labels=["Allowed", "Blocked"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)
    st.write(
        f"Allowed: {allowed}"
    )

    st.write(
        f"Blocked: {blocked}"
    )
    st.subheader("Traffic Types")

    fig2, ax2 = plt.subplots()

    ax2.bar(
        attack_counter.keys(),
        attack_counter.values()
    )

    plt.xticks(rotation=45)

    st.pyplot(fig2)

    st.subheader("Security Alerts")

    if alerts:

        alert_df = pd.DataFrame(alerts)

        st.dataframe(
            alert_df,
            use_container_width=True
        )

    else:
        st.success("No attacks detected")

st.subheader("Saved Logs")

try:

    logs = pd.read_csv(
        "logs/alerts.csv"
    )

    st.dataframe(
        logs.tail(50),
        use_container_width=True
    )

except Exception:

    st.info(
        "No logs yet"
    )

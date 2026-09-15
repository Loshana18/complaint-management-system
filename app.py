import streamlit as st

# =========================
# PAGE SETTINGS
# =========================
st.set_page_config(
    page_title="Complaint Management System",
    page_icon="📋",
    layout="centered"
)

# =========================
# CUSTOM STYLE
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #f2f2f7;
}

.block-container {
    max-width: 480px;
    padding: 25px 18px 40px 18px;
}

/* Hide Streamlit extras */
#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* =========================
   MAIN TITLE
   ========================= */

.main-title {
    text-align: center;
    font-size: 25px;
    font-weight: 850;
    color: #1c1c1e !important;
    margin-bottom: 22px;
}

/* =========================
   COMPLAINT LEVEL
   ========================= */

.level-box {
    background-color: #ffe5e5;
    border-radius: 16px;
    padding: 14px 16px;
    margin-bottom: 22px;
    text-align: center;
    color: #d70015 !important;
    font-size: 14px;
    font-weight: 800;
}

/* =========================
   SECTION TITLES
   ========================= */

.section-title {
    font-size: 20px;
    font-weight: 800;
    color: #1c1c1e !important;
    margin-top: 22px;
    margin-bottom: 12px;
}

/* =========================
   STREAMLIT CONTAINERS
   ========================= */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #ffffff !important;
    border-radius: 19px !important;
    border: 1px solid #eeeeee !important;
    box-shadow: 0 3px 12px rgba(0,0,0,0.05);
    padding: 4px;
    margin-bottom: 12px;
}

/* Force all text inside cards to dark */

div[data-testid="stVerticalBlockBorderWrapper"] p,
div[data-testid="stVerticalBlockBorderWrapper"] span,
div[data-testid="stVerticalBlockBorderWrapper"] div,
div[data-testid="stVerticalBlockBorderWrapper"] label {
    color: #1c1c1e !important;
}

/* Headings inside cards */

div[data-testid="stVerticalBlockBorderWrapper"] h1,
div[data-testid="stVerticalBlockBorderWrapper"] h2,
div[data-testid="stVerticalBlockBorderWrapper"] h3,
div[data-testid="stVerticalBlockBorderWrapper"] h4 {
    color: #1c1c1e !important;
}

/* =========================
   CRITICAL TEXT
   ========================= */

div[data-testid="stVerticalBlockBorderWrapper"] .stCaption {
    color: #d70015 !important;
    font-weight: 800;
}

/* =========================
   PERFORMANCE PROGRESS
   ========================= */

div[data-testid="stProgress"] {
    margin-bottom: 10px;
}

/* =========================
   FINAL NOTICE
   ========================= */

.notice-box {
    background-color: #fff3cd;
    border-radius: 17px;
    padding: 16px;
    color: #5c4400 !important;
    font-size: 14px;
    line-height: 1.5;
    margin-top: 8px;
}

.notice-box b {
    color: #5c4400 !important;
}

/* =========================
   VERDICT
   ========================= */

.verdict-box {
    background-color: #1c1c1e;
    border-radius: 20px;
    padding: 20px;
    margin-top: 15px;
    color: white !important;
}

.verdict-title {
    font-size: 23px;
    font-weight: 850;
    text-align: center;
    margin-bottom: 12px;
    color: white !important;
}

.verdict-text {
    color: #d1d1d6 !important;
    font-size: 14px;
    line-height: 1.6;
    text-align: center;
}

/* =========================
   BUTTON
   ========================= */

.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 15px;
    font-weight: 750;
    font-size: 14px;
}

/* =========================
   FOOTER
   ========================= */

.footer {
    text-align: center;
    color: #8e8e93 !important;
    font-size: 10px;
    margin-top: 28px;
    line-height: 1.5;
}

</style>
""", unsafe_allow_html=True)


# =========================
# MAIN TITLE
# =========================

st.markdown(
    '<div class="main-title">COMPLAINT MANAGEMENT SYSTEM</div>',
    unsafe_allow_html=True
)


# =========================
# COMPLAINT LEVEL
# =========================

st.markdown(
    '<div class="level-box">🚨 COMPLAINT LEVEL: CRITICAL</div>',
    unsafe_allow_html=True
)


# =========================
# ACTIVE COMPLAINTS
# =========================

st.markdown(
    '<div class="section-title">📋 Active Complaints</div>',
    unsafe_allow_html=True
)


# =========================
# COMPLAINT 01
# =========================

with st.container(border=True):
    st.markdown("### 🗣️ Excessive Talking")

    st.write(
        "He can talk for 2 hours straight and somehow forgets "
        "the other person exists."
    )

    st.caption("🔴 CRITICAL")


# =========================
# COMPLAINT 02
# =========================

with st.container(border=True):
    st.markdown("### 👂 “I Can Listen” Department")

    st.write(
        'He says "I can listen" but apparently listening '
        "is an optional feature."
    )

    st.caption("🔴 CRITICAL")


# =========================
# COMPLAINT 03
# =========================

with st.container(border=True):
    st.markdown("### 🧠 Peace Disturbance")

    st.write(
        "He repeatedly steals her peace of mind."
    )

    st.caption("🔴 CRITICAL")


# =========================
# COMPLAINT 04
# =========================

with st.container(border=True):
    st.markdown("### 🛕 Unlimited Updates Package")

    st.write(
        "Too many friends, family and Kovil updates. "
        "No subscription requested."
    )

    st.caption("🔴 CRITICAL")


# =========================
# COMPLAINT 05
# =========================

with st.container(border=True):
    st.markdown("### 🍜 Emergency Support Failure")

    st.write(
        'When she says "I’m hungry / tired / stressed or any tiny things about her", '
        "his response level is:"
    )

    st.markdown("**404 — CARE NOT FOUND**")

    st.caption("🔴 CRITICAL")


# =========================
# COMPLAINT 06
# =========================

with st.container(border=True):
    st.markdown("### 👑 Zeus Syndrome")

    st.write(
        "Somehow believes he is always right."
    )

    st.write(
        "Evidence currently overwhelming. 💀"
    )

    st.caption("🔴 CRITICAL")


# =========================
# COMPLAINT 07
# =========================

with st.container(border=True):
    st.markdown("### ❓ Basic Knowledge Failure")

    st.write(
        "After all this communication, still doesn't know "
        "basic information about her."
    )

    st.write("Where does she work? ❌")
    st.write("Company name? ❌")
    st.write(
        "Do you actually know anything about her? "
        "**Under review. 😭**"
    )

    st.caption("🔴 CRITICAL")


# =========================
# PERFORMANCE REVIEW
# =========================

st.markdown(
    '<div class="section-title">📊 Performance Review</div>',
    unsafe_allow_html=True
)

st.caption(
    "Results based on highly questionable but accurate research."
)

with st.container(border=True):

    st.write("**Talking — 100%**")
    st.progress(1.0)

    st.write("**Listening — 20%**")
    st.progress(0.20)

    st.write("**Knowing Me — 10%**")
    st.progress(0.10)

    st.write("**Caring When I'm Stressed — 0%**")
    st.progress(0.0)

    st.write("**Being Right According to Himself — 100%**")
    st.progress(1.0)

    st.write("**Stealing My Peace — 110% 💀**")
    st.progress(1.0)


# =========================
# FINAL NOTICE
# =========================

st.markdown(
    '<div class="section-title">⚠️ Final Notice</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="notice-box">
<b>Yugan has been given multiple opportunities to improve.</b><br>
Unfortunately, he continues to talk instead of reading the complaint.
<br><br>
<b>Recommended action:</b><br>
Maybe try listening to her for a change. 😭
</div>
""", unsafe_allow_html=True)


# =========================
# VIEW VERDICT
# =========================

st.write("")

if st.button("⚖️ SEE FINAL RESULT", use_container_width=True):

    st.markdown(
        '<div class="verdict-box">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="verdict-title">CASE VERDICT: ⚠️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="verdict-text">',
        unsafe_allow_html=True
    )

    st.write("Yugan has been officially warned.")

    st.write(
        "The complaints have been clearly documented, "
        "the evidence has been reviewed, "
        "and the situation remains unresolved."
    )

    st.write("**If this continues...**")

    st.write(
        "**She simply doesn't want to talk to him anymore.** 🙂"
    )

    st.write("No further warnings will be issued.")

    st.markdown(
        '</div></div>',
        unsafe_allow_html=True
    )


# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">
YG-001 •Complaint Management System<br>
This document has absolutely no legal authority. 😂
</div>
""", unsafe_allow_html=True)
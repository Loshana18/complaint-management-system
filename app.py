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
    background-color: #f2f2f7 !important;
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
    background-color: #ffe5e5 !important;
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
   COMPLAINT CARDS
   ========================= */

.complaint-card {
    background-color: #ffffff !important;
    border: 1px solid #e5e5e7;
    border-radius: 19px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.05);
}

.complaint-title {
    color: #1c1c1e !important;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 12px;
}

.complaint-text {
    color: #3a3a3c !important;
    font-size: 14px;
    line-height: 1.6;
}

.critical-label {
    color: #d70015 !important;
    font-size: 10px;
    font-weight: 800;
    margin-top: 12px;
}

/* =========================
   PERFORMANCE
   ========================= */

.performance-card {
    background-color: #ffffff !important;
    border: 1px solid #e5e5e7;
    border-radius: 19px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.05);
}

.performance-label {
    color: #1c1c1e !important;
    font-size: 14px;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 4px;
}

/* =========================
   FINAL NOTICE
   ========================= */

.notice-box {
    background-color: #fff3cd !important;
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
    background-color: #1c1c1e !important;
    border-radius: 20px;
    padding: 20px;
    margin-top: 15px;
    text-align: center;
}

.verdict-title {
    color: #ffffff !important;
    font-size: 23px;
    font-weight: 850;
    margin-bottom: 14px;
}

.verdict-text {
    color: #d1d1d6 !important;
    font-size: 14px;
    line-height: 1.6;
}

.verdict-highlight {
    color: #ffffff !important;
    font-size: 15px;
    font-weight: 800;
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

st.markdown("""
<div class="complaint-card">

<div class="complaint-title">
🗣️ Excessive Talking
</div>

<div class="complaint-text">
He can talk for 2 hours straight and somehow forgets
the other person exists.
</div>

<div class="critical-label">
🔴 CRITICAL
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# COMPLAINT 02
# =========================

st.markdown("""
<div class="complaint-card">

<div class="complaint-title">
👂 “I Can Listen” Department
</div>

<div class="complaint-text">
He says "I can listen" but apparently listening
is an optional feature.
</div>

<div class="critical-label">
🔴 CRITICAL
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# COMPLAINT 03
# =========================

st.markdown("""
<div class="complaint-card">

<div class="complaint-title">
🧠 Peace Disturbance
</div>

<div class="complaint-text">
He repeatedly steals her peace of mind.
</div>

<div class="critical-label">
🔴 CRITICAL
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# COMPLAINT 04
# =========================

st.markdown("""
<div class="complaint-card">

<div class="complaint-title">
🛕 Unlimited Updates Package
</div>

<div class="complaint-text">
Too many friends, family and Kovil updates.
No subscription requested.
</div>

<div class="critical-label">
🔴 CRITICAL
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# COMPLAINT 05
# =========================

st.markdown("""
<div class="complaint-card">

<div class="complaint-title">
🍜 Emergency Support Failure
</div>

<div class="complaint-text">
When she says "I’m hungry / tired / stressed or any tiny things about her",
his response level is:
<br><br>
<b>404 — CARE NOT FOUND</b>
</div>

<div class="critical-label">
🔴 CRITICAL
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# COMPLAINT 06
# =========================

st.markdown("""
<div class="complaint-card">

<div class="complaint-title">
👑 Zeus Syndrome
</div>

<div class="complaint-text">
Somehow believes he is always right.
<br><br>
Evidence currently overwhelming. 💀
</div>

<div class="critical-label">
🔴 CRITICAL
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# COMPLAINT 07
# =========================

st.markdown("""
<div class="complaint-card">

<div class="complaint-title">
❓ Basic Knowledge Failure
</div>

<div class="complaint-text">
After all this communication, still doesn't know
basic information about her.
<br><br>

Where does she work? ❌
<br>
Company name? ❌
<br>
Do you actually know anything about her?
<b>Under review. 😭</b>
</div>

<div class="critical-label">
🔴 CRITICAL
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# PERFORMANCE REVIEW
# =========================

st.markdown(
    '<div class="section-title">📊 Performance Review</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="color:#8e8e93 !important; font-size:11px; margin-bottom:12px;">'
    'Results based on highly questionable but accurate research.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="performance-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="performance-label">Talking — 100%</div>',
    unsafe_allow_html=True
)
st.progress(1.0)

st.markdown(
    '<div class="performance-label">Listening — 20%</div>',
    unsafe_allow_html=True
)
st.progress(0.20)

st.markdown(
    '<div class="performance-label">Knowing Me — 10%</div>',
    unsafe_allow_html=True
)
st.progress(0.10)

st.markdown(
    '<div class="performance-label">Caring When I\'m Stressed — 0%</div>',
    unsafe_allow_html=True
)
st.progress(0.0)

st.markdown(
    '<div class="performance-label">Being Right According to Himself — 100%</div>',
    unsafe_allow_html=True
)
st.progress(1.0)

st.markdown(
    '<div class="performance-label">Stealing My Peace — 110% 💀</div>',
    unsafe_allow_html=True
)
st.progress(1.0)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================
# FINAL NOTICE
# =========================

st.markdown(
    '<div class="section-title">⚠️ Final Notice</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="notice-box">

<b>Yugan has been given multiple opportunities to improve.</b>
<br>

Unfortunately, he continues to talk instead of reading the complaint.

<br><br>

<b>Recommended action:</b>
<br>

Maybe try listening to her for a change. 😭

</div>
""", unsafe_allow_html=True)


# =========================
# SEE FINAL RESULT
# =========================

st.write("")

if st.button("⚖️ SEE FINAL RESULT", use_container_width=True):

    st.markdown(
        """<div class="verdict-box">
<div class="verdict-title">CASE VERDICT: ⚠️</div>
<div class="verdict-text">
Yugan has been officially warned.
<br><br>
The complaints have been clearly documented,
the evidence has been reviewed,
and the situation remains unresolved.
<br><br>
If this continues...
<br><br>
<span class="verdict-highlight">She simply doesn't want to talk to him anymore. 🙂</span>
<br><br>
No further warnings will be issued.
</div>
</div>""",
        unsafe_allow_html=True
    )


# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">
YG-001 • Complaint Management System
<br>
This document has absolutely no legal authority. 😂
</div>
""", unsafe_allow_html=True)

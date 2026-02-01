import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Pooja 💖", layout="centered")

# ---------- STATE ----------
if "yes" not in st.session_state:
    st.session_state.yes = False


# ---------- YES PAGE ----------
if st.session_state.yes:
    st.balloons()
    st.audio("varoon.mp3", loop=True)

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#ff9a9e,#fad0c4);
        padding:40px;
        border-radius:25px;
        text-align:center;
        font-family: 'Comic Sans MS', cursive;
        color:#4b0033;
    ">
        <h1>Pooja 💖</h1>
        <h2>You chose me 🥺</h2>

        <p style="font-size:18px;">
            I promise to be your safe place,<br>
            your biggest supporter,<br>
            and still annoy you every single day 😌
        </p>

        <p style="font-size:16px;">
            Happy Valentine’s Day ❤️<br>
            Yours. Permanently.
        </p>

        <p style="font-size:13px; opacity:0.7;">
            (Lifetime subscription activated. No cancellations.)
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# ---------- MAIN PAGE ----------
st.markdown("""
<h1 style="text-align:center; color:#ff4d6d;">Pooja 💖</h1>
<h2 style="text-align:center;">Will you be my Valentine?</h2>
<p style="text-align:center; opacity:0.8;">
I promise to listen to your yaps,<br>
steal your food,<br>
and still choose you when you’re mad ❤️
</p>
""", unsafe_allow_html=True)


# ---------- PRANK UI (HTML + JS ONLY) ----------
components.html("""
<style>
#box {
    position: relative;
    height: 180px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 30px;
}
button {
    padding: 12px 28px;
    border-radius: 25px;
    border: none;
    font-size: 18px;
    cursor: pointer;
}
#no {
    position: absolute;
    background: #ffd6e0;
}
</style>

<div id="box">
    <button id="yes" disabled>Yes 💘</button>
    <button id="no">No 😈</button>
</div>

<script>
const noBtn = document.getElementById("no");
const box = document.getElementById("box");

noBtn.addEventListener("mouseenter", () => {
    const maxX = box.clientWidth - noBtn.offsetWidth;
    const maxY = box.clientHeight - noBtn.offsetHeight;

    const x = Math.random() * maxX;
    const y = Math.random() * maxY;

    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
});
</script>
""", height=220)


# ---------- REAL YES BUTTON ----------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Yes 💘"):
        st.session_state.yes = True
        st.experimental_rerun()

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Pooja 💖", layout="centered")

# ---------- STATE ----------
if "yes" not in st.session_state:
    st.session_state.yes = False


# ---------- YES PAGE ----------
if st.session_state.yes:
    st.balloons()

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#ff9a9e,#fad0c4);
        padding:45px;
        border-radius:30px;
        text-align:center;
        font-family:'Comic Sans MS', cursive;
        color:#4b0033;
        max-width:700px;
        margin:auto;
    ">
        <h1>Pooja 💖</h1>
        <h2>You chose me 🥺</h2>

        <p style="font-size:18px; margin-top:20px;">
            I promise to be your safe place,<br>
            your biggest supporter,<br>
            and still annoy you every single day 😌
        </p>

        <p style="font-size:16px; margin-top:25px;">
            Happy Valentine’s Day ❤️<br>
            Yours. Permanently.
        </p>

        <p style="font-size:14px; margin-top:20px;">
            This song is my favourite for you 🎧<br>
            Press play when you’re ready.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Audio after user interaction (allowed by browser)
    st.audio("varoon.mp3")

    st.stop()


# ---------- MAIN PAGE ----------
st.markdown("""
<div style="
    background: linear-gradient(135deg,#ff9a9e,#fad0c4);
    padding:45px;
    border-radius:30px;
    text-align:center;
    font-family:'Comic Sans MS', cursive;
    color:#4b0033;
    max-width:700px;
    margin:auto;
">
    <h1>Pooja 💖</h1>
    <h2>You chose me 🥺</h2>

    <div style="
        background:#1c1f26;
        color:white;
        padding:25px;
        border-radius:15px;
        margin-top:25px;
        font-size:18px;
        line-height:1.6;
    ">
        I promise to be your safe place,<br>
        your biggest supporter,<br>
        and still annoy you every single day 😌
        <br><br>
        Happy Valentine’s Day ❤️<br>
        Yours. Permanently.
        <br><br>
        <span style="font-size:14px; opacity:0.85;">
            This song is my favourite for you 🎧<br>
            Press play when you’re ready.
        </span>
    </div>
</div>
""", unsafe_allow_html=True)



# ---------- NO BUTTON PRANK (HTML ONLY) ----------
components.html("""
<style>
#box {
    position: relative;
    height: 140px;
    margin-top: 30px;
}
#no {
    position: absolute;
    padding: 12px 28px;
    border-radius: 25px;
    border: none;
    background: #ffd6e0;
    font-size: 18px;
    cursor: pointer;
}
</style>

<div id="box">
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
""", height=160)


# ---------- SINGLE REAL YES BUTTON ----------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Yes 💘"):
    st.session_state.yes = True

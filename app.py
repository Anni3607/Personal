import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Pooja 💖", layout="centered")

# ---------- STATE ----------
if "yes" not in st.session_state:
    st.session_state.yes = False


# ---------- YES PAGE ----------
if st.session_state.yes:
    st.balloons()

    # Title (simple markdown only)
    st.markdown(
        "<h1 style='text-align:center; color:#4b0033;'>Pooja 💖</h1>"
        "<h2 style='text-align:center;'>Aww, You chose me 🥺</h2>",
        unsafe_allow_html=True
    )

    # Clean HTML block (NO markdown)
    components.html("""
    <div style="
        background: linear-gradient(135deg,#ff9a9e,#fad0c4);
        padding:45px;
        border-radius:30px;
        max-width:700px;
        margin:30px auto;
        font-family:'Comic Sans MS', cursive;
        color:#4b0033;
        text-align:center;
    ">
        <div style="
            background:#1c1f26;
            color:white;
            padding:25px;
            border-radius:15px;
            font-size:18px;
            line-height:1.6;
        ">
            I promise to be your safe place,<br>
            your biggest supporter,<br>
            and still be a pain in your ass (iykyk😌)
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
    """, height=420)

    # Audio (browser-safe, after click)
    st.audio("varoon.mp3")

    st.stop()


# ---------- MAIN PAGE ----------
st.markdown("""
<h1 style="
    text-align:center;
    color:#ff5fa2;
    text-shadow: 0 0 8px rgba(255, 95, 162, 0.6);
">
    Pooja 💖
</h1>
""", unsafe_allow_html=True)
<h2 style="text-align:center;">Will you be my Valentine?</h2>

<p style="text-align:center; opacity:0.85; margin-top:20px;">
I promise to listen to your yaps,<br>
buy you perfumes, take you on long drives,<br>
never smoke, wash dishes everyday,<br>
never let you down, choose patience over ego,<br>
and always choose you even when you’re mad ❤️
</p>

<p style="text-align:center; font-size:14px; opacity:0.7;">
(No is just here to test your patience, chapli 😏)
</p>
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


# ---------- SINGLE YES BUTTON ----------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Yes 💘"):
    st.session_state.yes = True

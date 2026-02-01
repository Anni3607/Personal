import streamlit as st

st.set_page_config(
    page_title="For Pooja 💖",
    layout="centered"
)

params = st.experimental_get_query_params()

# ---------------- YES PAGE ----------------
if "yes" in params:
    st.balloons()

    # Play your song AFTER click (browser-safe)
    st.audio("varoon.mp3", format="audio/mp3", loop=True)

    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        }
        </style>

        <div style="
            background: rgba(255,255,255,0.85);
            padding: 45px;
            border-radius: 30px;
            text-align: center;
            color: #4b0033;
            font-family: 'Comic Sans MS', cursive;
        ">
            <h1>YAYYYYY 💕🎉</h1>

            <h2>Pooja, you actually clicked Yes 🥺💖</h2>

            <p style="font-size:18px; line-height:1.6;">
                You know what this song means.<br>
                And you know what <i>we</i> mean.<br><br>

                Through every late-night call,<br>
                every small fight,<br>
                every “Kuch nahi hua” moment 😌,<br>
                I still choose you.<br><br>

                And just so we’re clear —<br>
                <b>you are stuck with me forever hehe.</b><br>
                No refunds. No returns. Only cuddles ❤️
            </p>

            <p style="font-size:16px; margin-top:25px;">
                Happy Valentine’s Day 💘<br>
                Your favourite Sunflower 😏
            </p>

            <p style="font-size:13px; opacity:0.7;">
                (Background music unlocked because you chose wisely 🎶)
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- MAIN PAGE ----------------
else:
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #ffdde1, #ee9ca7);
        }
        #container {
            position: relative;
            height: 280px;
            text-align: center;
            margin-top: 40px;
        }
        .btn {
            font-size: 18px;
            padding: 12px 32px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            font-family: "Comic Sans MS", cursive;
        }
        #yes-btn {
            background-color: #ff4d6d;
            color: white;
            margin-right: 30px;
        }
        #no-btn {
            background-color: #ffd6e0;
            color: #4b0033;
            position: absolute;
        }
        </style>

        <div style="text-align:center; font-family:'Comic Sans MS', cursive; color:#4b0033;">
            <h1>Pooja 💖</h1>
            <h2>Will you be my Valentine?</h2>

            <p>
                I promise to:<br>
                • be your go-to guy<br>
                • listen to your yaps 😌<br>
                • still choose you even when you’re mad ❤️
            </p>

            <p style="font-size:14px; opacity:0.8;">
                (No is here just to test your patience, chapli 😏)
            </p>
        </div>

        <div id="container">
            <button class="btn" id="yes-btn" onclick="yesClicked()">Yes 💘</button>
            <button class="btn" id="no-btn" onmouseover="moveButton()">No 😈</button>
        </div>

        <script>
        function moveButton() {
            const btn = document.getElementById("no-btn");
            const x = Math.random() * 230;
            const y = Math.random() * 150;
            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }

        function yesClicked() {
            window.location.search = "?yes=true";
        }
        </script>
        """,
        unsafe_allow_html=True
    )

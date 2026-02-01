import streamlit as st
import streamlit.components.v1 as components

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
            max-width: 500px;
            margin: auto;
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
    components.html(
        """
        <html>
        <head>
        <style>
            body {
                margin: 0;
                height: 100vh;
                background: radial-gradient(circle at top, #ffb6c1, #1a001a);
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Comic Sans MS', cursive;
                color: #fff;
            }

            .card {
                background: rgba(0,0,0,0.55);
                padding: 40px;
                border-radius: 28px;
                width: 380px;
                text-align: center;
                box-shadow: 0 0 35px rgba(255,105,180,0.45);
            }

            h1 {
                margin-bottom: 5px;
                color: #ff69b4;
            }

            h2 {
                margin-top: 0;
            }

            p {
                font-size: 15px;
                line-height: 1.6;
                opacity: 0.9;
            }

            .buttons {
                position: relative;
                height: 90px;
                margin-top: 25px;
            }

            button {
                padding: 12px 28px;
                border-radius: 30px;
                border: none;
                font-size: 16px;
                cursor: pointer;
            }

            #yes {
                background: #ff4d6d;
                color: white;
            }

            #no {
                background: #ffd6e0;
                color: #4b0033;
                position: absolute;
            }
        </style>
        </head>

        <body>
            <div class="card">
                <h1>Pooja 💖</h1>
                <h2>Will you be my Valentine?</h2>

                <p>
                    I promise to:<br>
                    • be your go-to guy<br>
                    • listen to your yaps 😌<br>
                    • still choose you even when you’re mad ❤️
                </p>

                <p style="font-size:13px; opacity:0.75;">
                    (No is here just to test your patience, chapli 😏)
                </p>

                <div class="buttons">
                    <button id="yes" onclick="goYes()">Yes 💘</button>
                    <button id="no" onmouseover="runAway()">No 😈</button>
                </div>
            </div>

            <script>
                function runAway() {
                    const btn = document.getElementById("no");
                    const x = Math.random() * 240;
                    const y = Math.random() * 60;
                    btn.style.left = x + "px";
                    btn.style.top = y + "px";
                }

                function goYes() {
                    window.location.search = "?yes=true";
                }
            </script>
        </body>
        </html>
        """,
        height=650
    )

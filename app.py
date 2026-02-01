import streamlit as st

st.set_page_config(page_title="For Pooja 💖", layout="centered")

# Initialize session state
if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False

# ---------------- YES PAGE ----------------
if st.session_state.yes_clicked:
    st.balloons()

    st.audio("varoon.mp3", format="audio/mp3", loop=True)

    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        }
        </style>

        <div style="
            padding: 45px;
            border-radius: 30px;
            text-align: center;
            color: #4b0033;
            font-family: 'Comic Sans MS', cursive;
        ">
            <h1>POOJA 💖</h1>
            <h2>You really chose me 🥺</h2>

            <p style="font-size:18px; margin-top:20px;">
                I know I act chill,<br>
                but this made my heart do that stupid happy thing.<br><br>

                Thank you for being my favourite person,<br>
                my comfort human,<br>
                and the one I still choose even on my worst days ❤️
            </p>

            <p style="font-size:17px; margin-top:25px;">
                I promise to:<br>
                • be your go-to guy, always<br>
                • listen to all your yaps (even the dramatic ones 😌)<br>
                • still choose you when you’re mad at me 💕
            </p>

            <p style="font-size:16px; margin-top:30px;">
                Happy Valentine’s Day 🫶<br>
                Yours, annoyingly and permanently 😏
            </p>

            <p style="font-size:13px; opacity:0.7;">
                (No refunds. No returns. Lifetime subscription activated.)
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
            margin-top: 40px;
            text-align: center;
        }

        .btn {
            font-size: 18px;
            padding: 12px 30px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            font-family: 'Comic Sans MS', cursive;
        }

        #yes-btn {
            background-color: #ff4d6d;
            color: white;
            margin-right: 25px;
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

            <p style="margin-top:15px;">
                I promise to be your safe place,<br>
                your biggest supporter,<br>
                and the person who still annoys you daily 😌
            </p>

            <p style="font-size:14px; opacity:0.8;">
                (No is just here to test your patience, chapli 😏)
            </p>
        </div>

        <div id="container">
            <button class="btn" id="yes-btn" onclick="yesClicked()">Yes 💘</button>
            <button class="btn" id="no-btn" onmouseover="moveButton(event)">No 😈</button>
        </div>

        <script>
        function moveButton(event) {
            const btn = document.getElementById("no-btn");
            const container = document.getElementById("container");

            const rect = container.getBoundingClientRect();
            const buffer = 80;

            let x = Math.random() * (rect.width - buffer);
            let y = Math.random() * (rect.height - buffer);

            const mouseX = event.clientX - rect.left;
            const mouseY = event.clientY - rect.top;

            if (Math.abs(x - mouseX) < 60) x += 80;
            if (Math.abs(y - mouseY) < 40) y += 60;

            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }

        function yesClicked() {
            const streamlitInput = window.parent.document.querySelector(
                'input[data-testid="stTextInput"]'
            );
            window.location.reload();
        }
        </script>
        """,
        unsafe_allow_html=True
    )

    # Invisible Streamlit trigger
    if st.button(""):
        st.session_state.yes_clicked = True
        st.experimental_rerun()

    # Real Yes button trigger
    if st.button("Yes 💘"):
        st.session_state.yes_clicked = True
        st.experimental_rerun()

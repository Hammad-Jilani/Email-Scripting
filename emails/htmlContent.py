def HtmlContent():
  return f""" 
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}
        .container {{
            width: 100%;
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header {{
            background-color: #1A2129;
            color: #ffffff;
            padding: 20px;
            text-align: center;
        }}
        .content {{
            padding: 20px;
        }}
        h1 {{
            font-size: 24px;
            margin: 0 0 10px;
        }}
        h2 {{
            font-size: 20px;
            margin: 20px 0 10px;
        }}
        p {{
            line-height: 1.6;
        }}
        .event-details, .expectations {{
            margin: 20px 0;
            padding: 10px;
            border-left: 5px solid #1A2129;
            background-color: #f9f9f9;
        }}
        .footer {{
            padding: 20px;
            text-align: center;
            background-color: #f4f4f4;
            border-top: 1px solid #ddd;
        }}
        a {{
            color: #007BFF;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Get Ready to Revolutionize!</h1>
        </div>
        <div class="content">
            <p>Dear All,</p>
            <p>TGD registrations are live now.</p>
            <b>What is TGD?</b>
            <p> The Grand Debate (TGD), a premier MUN-style debate competition hosted by FAST University's Main Campus. Building on the foundations of Model United Nations, TGD presents a unique platform for intellectual discourse, critical thinking, and articulate expression. This esteemed event brings together bright minds from across the academic spectrum to engage in rigorous debates, exchange perspectives, and showcase their diplomatic prowess.</p>
            <p>Registration fee details:</p>
            <ul>
                <li>Delegate : 1400 PKR (After early bird discount 1200 PKR)
Delegation (min/max 5): 7000 PKR ( After early bird discount 6000 PKR)</li>
                <li>Register now: <a href="https://forms.gle/BNhGJreRGX25wnqF7">Click here </a></li>
                <li><b>Note:</b> Early bird discount is valid until 11th November.</li>
            </ul>
            <p>Join us for an unforgettable experience of inspiration, innovation, and connection!</p>

            <div class="event-details">
                <h2>Event Details:</h2>
                <p><strong>Event Name:</strong> TGD'24</p>
                <p><strong>Date:</strong> 20th & 21st November</p>
                <p><strong>Location:</strong> FAST-NUCES (Main Campus)</p>
            </div>

            <div class="expectations">
                <h2>What to Expect:</h2>
                <ul>
                    <li>Participation certificates Free food</li>
                    <li>Free transportation </li>
                    <li>Special social event: qawali night</li>
                </ul>
            </div>

            <h2>Stay Updated:</h2>
            <p>Follow us on social media for updates, sneak peeks, and behind-the-scenes insights:</p>
            <p>Instagram: <a href="https://www.instagram.com/tlc_nu?igsh=YzljYTk1ODg3Zg==">Instagram</a></p>
            <p>Facebook: <a href="https://www.facebook.com/TLCFAST?mibextid=ZbWKwL">Facebook</a></p>

            <h2>Get in Touch:</h2>
            <p>Email Us: <a href="mailto:tlc.khi@nu.edu.pk">tlc.khi@nu.edu.pk</a></p>
        </div>
        <div class="footer">
            <p>Looking forward to seeing you at TGD'24!</p>
            <p>Best Regards,<br>The Literary Society,<br>FAST-NUCES.</p>
        </div>
        
    </div>
    <div class="container">
        <img style="width: 100%;" src="https://raw.githubusercontent.com/Hammad-Jilani/Email-Scripting/refs/heads/main/emails/image/TGD.jpeg" alt="TGD">

    </div>
</body>
</html>



"""
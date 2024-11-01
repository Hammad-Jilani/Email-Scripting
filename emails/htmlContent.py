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
            background-color: #007BFF;
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
            border-left: 5px solid #007BFF;
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
            <p>The wait is over! TGD'24 is coming soon!</p>
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
                    <li>Inspiring keynotes and panel discussions</li>
                    <li>Best Delegation Awards</li>
                    <li>Unparalleled networking opportunities</li>
                    <li>Free transportation</li>
                    <li>Free food</li>
                    <li>Certificates</li>
                </ul>
            </div>

            <h2>Stay Updated:</h2>
            <p>Follow us on social media for updates, sneak peeks, and behind-the-scenes insights:</p>
            <p>Instagram: <a href="https://www.instagram.com/tlc_nu?igsh=YzljYTk1ODg3Zg==">Our Instagram Page</a></p>
            <p>Facebook: <a href="https://www.facebook.com/TLCFAST?mibextid=ZbWKwL">Our Facebook Page</a></p>

            <h2>Get in Touch:</h2>
            <p>Email Us: <a href="mailto:tlc.khi@nu.edu.pk">tlc.khi@nu.edu.pk</a></p>
        </div>
        <div class="footer">
            <p>Looking forward to seeing you at TGD'24!</p>
            <p>Best Regards,<br>The Literary Society,<br>FAST-NUCES.</p>
        </div>
    </div>
</body>
</html>


"""
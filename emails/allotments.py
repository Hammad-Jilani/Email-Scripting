def allotments(name, committee, allotment):
    return f"""<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Grand Debate'24 - Allotment Details</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f0ec;
            color: #4a3b31;
        }}

        .container {{
            width: 90%;
            max-width: 600px;
            margin: 30px auto;
            border-radius: 8px;
            background: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }}
        .header {{
            text-align: center;
            padding: 10px 0;
            background-color: #8b5e3c;
            color: #ffffff;
            border-radius: 8px 8px 0 0;
        }}

        .header h1 {{
            margin: 0;
        }}

        .content {{
            margin: 20px 0;
        }}

        .content p {{
            margin: 15px 0;
        }}

        .content a {{
            color: #8b5e3c;
            text-decoration: none;
        }}

        .details {{
            margin-top: 15px;
            padding: 15px;
            background-color: #f3e7dc;
            border-radius: 5px;
        }}

        .details p {{
            margin: 5px 0;
        }}

        .footer {{
            text-align: center;
            padding: 15px 0;
            margin-top: 20px;
            font-size: 0.9em;
            color: #4a3b31;
            background-color: #f4f0ec;
            border-radius: 0 0 8px 8px;
        }}

        .social-icons a {{
            margin: 0 15px;
            padding: 10px 20px;
            background-color: #8b5e3c;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }}

        .social-icons a:hover {{
            background-color: #6a3c28;
        }}

        .social-icons {{
            text-align: center;
            margin-top: 15px;
        }}

        .button {{
            display: inline-block;
            padding: 10px 20px;
            margin: 10px 0;
            background-color: #8b5e3c;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
        }}

        .button:hover {{
            background-color: #6a3c28;
        }}
        
    </style>
</head>

<body>
    <div class="container">
        <div class="header">
            <h1>The Grand Debate'24</h1>
            <p>Hosted by The Literary Club, FAST - NUCES</p>
        </div>
        <div class="content">
            <p>Dear {name},</p>
            <p>Congratulations on registering for <strong>The Grand Debate'24!</strong> We are thrilled to have you as a participant.</p>
            <p>Your allotment details are as follows:</p>
            <div class="details">
                <p><strong>Committee:</strong> {committee}</p>
                <p><strong>Allotment:</strong> {allotment}</p>
            </div>
            <p>To prepare for the conference, please access the study guide materials by clicking on the link below:</p>
            <p style="width: 30%; margin: auto;">
              <a href="https://drive.google.com/drive/folders/1UdXR7M840s_WfjN1pqZvJNiNeT68kZXg" target="_blank" class="button" style="color: white;" >Access Study Guide Materials</a>
            </p>
        </div>
        <div class="social-icons">
            <p>Follow us on:</p>
            <a href="https://www.instagram.com/tlc_nu?igsh=YzljYTk1ODg3Zg==" target="_blank">Instagram</a> | 
            <a href="https://www.facebook.com/TLCFAST?mibextid=ZbWKwL" target="_blank">Facebook</a>
        </div>
        <div class="footer">
            <p>Best regards,</p>
            <p>The Literary Club, FAST - NUCES</p>
        </div>
    </div>
</body>

</html>
"""

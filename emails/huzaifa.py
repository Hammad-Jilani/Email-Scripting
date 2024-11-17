def delegates(name):
  return f""" 
<!DOCTYPE html>
<html>
<head>
    <title>The Grand Debate Invitation</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f9f9f9;
            line-height: 1.6;
        }}
        .container {{
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #e5e5e5;
        }}
        .header h1 {{
            margin: 0;
            color: #444;
        }}
        .content {{
            padding: 20px 0;
        }}
        .content p {{
            margin: 10px 0;
        }}
        .content ul {{
            margin: 10px 0;
            padding-left: 20px;
        }}
        .content ul li {{
            margin-bottom: 8px;
        }}
        .cta {{
            margin-top: 20px;
            text-align: center;
        }}
        .cta a {{
            display: inline-block;
            padding: 12px 20px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            border-radius: 4px;
            font-weight: bold;
        }}
        .cta a:hover {{
            background-color: #0056b3;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #666;
        }}
        .container1{{
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
          <h1>Last call to Register for The Grand Debate'24</h1>
        </div>
        <div class="content">
            <p>Dear {name},</p>
            <p>We are thrilled to invite you to <strong>The Grand Debate (TGD)</strong>, an MUN-style bilingual debate competition hosted by <strong>The Literary Club (TLC) at FAST-NUCES</strong>, happening on <strong>November 20-21, 2024</strong>, at our Main Campus. This two-day event promises to bring together experienced and passionate delegates like yourself to engage in a stimulating and collaborative environment. Your presence would undoubtedly elevate the quality of discussions and enrich the overall experience for all participants.</p>
            
            <h3>Event Highlights:</h3>
            <ul>
                <li>MUN-style debate sessions on pressing local issues</li>
                <li>Certificates, awards, and networking opportunities</li>
                <li>Free transportation and lunch on both days</li>
                <li>A surprise social event with exclusive discounts</li>
            </ul>
            
            <p>We're pleased to offer an <strong>Early Bird Discount on registration until November 13</strong>. Don't miss this chance to contribute your voice and expertise to an event designed to foster public speaking, critical thinking, and diplomatic skills.</p>
            
            <p>Please find attached a PDF with full event details and registration instructions, and here is the registration form link:</p>
            
            <div class="cta">
                <a href="https://forms.gle/BNhGJreRGX25wnqF7">Register Now</a>
            </div>
        </div>
        <div class="container1">
            <img src="https://raw.githubusercontent.com/Hammad-Jilani/Email-Scripting/refs/heads/main/emails/image/HuzaifaTLC.jpeg"alt="TLC">
        </div>
        <div class="footer">
            <p>Warm regards,</p>
            <p>Huzaifa Faran<br>President, The Literary Club<br>FAST-NUCES</p>
        </div>
    </div>
</body>
</html>

"""
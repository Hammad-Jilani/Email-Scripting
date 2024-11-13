def confirmation(name):
  return f"""
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grand Debate Confirmation</title>
    <style>
      /* General reset */
      body, table, td, p, a, li {{
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
      }}
      body {{
        background-color: #f4f4f4;
        color: #000;
      }}
      .container {{
        max-width: 600px;
        margin: 0 auto;
        background-color: #1A2129;
        border-radius: 8px;
        overflow: hidden;
        width: 100%;
      }}
      .header {{
        padding: 20px;
        color: white;
      }}
      .content {{
        padding: 20px;
        color: white;
      }}
      .footer {{
        background-color: #f4f4f4;
        padding: 10px;
        text-align: center;
        color: #555;
        font-size: 12px;
      }}
      img {{
        width: 100%;
        max-width: 100%;
        height: auto;
        display: block;
      }}
      @media screen and (max-width: 600px) {{
        .content {{
          padding: 10px;
        }}
      }}
    </style>
</head>
<body>
  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" bgcolor="#f4f4f4">
    <tr>
      <td align="center">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" class="container">
          <tr>
            <td class="header">
              <h2>Dear {name},</h2>
              <p>We are pleased to confirm your participation in The Grand Debate 2024 at FAST-NUCES. Your registration has been processed successfully.</p>
            </td>
          </tr>
          <tr>
            <td class="content">
              <p><strong>Event Details:</strong></p>
              <ul style="padding-left: 20px; margin-top: 0;">
                <li><strong>Date:</strong> November 20-21</li>
                <li><strong>Time:</strong> 8:00 AM - 4:00 PM</li>
                <li><strong>Venue:</strong> FAST-NUCES Main Campus, National Highway</li>
                <li>Allotments will be provided soon</li>
              </ul>
              <p>We eagerly anticipate your intellectual contributions. Prepare for a stimulating experience!</p><br>
              <p>Best regards,</p>
              <p><strong>The Literary Club,</strong><br>FAST-NUCES (main campus)</p>
            </td>
          </tr>
          <tr>
            <td align="center" class="content">
              <img src="https://raw.githubusercontent.com/Hammad-Jilani/Email-Scripting/refs/heads/main/emails/image/1.jpeg" alt="TGD" style="width: 100%; max-width: 560px;">
            </td>
          </tr>
          <tr>
            <td class="footer">
              &copy; 2024 FAST-NUCES Literary Club. All rights reserved.
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
  """

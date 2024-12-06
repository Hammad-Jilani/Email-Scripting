def certificates(name):
  return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Email Automation</title>
        </head>
        <style>
          *{{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
          }}
          .container{{
            position: relative;
          }}
          .container img{{
            width: 100%;
            z-index: 1;
          }}
          p{{
            width: 78%;
            position: absolute;
            left: 26%;
            top: 47%;
            font-size: 30px;
            padding: 10px;
            font-family: Calibri, sans-serif;
            margin-top: 20px; /* Reduced space above the text */
          }}
          @media screen and (max-width:600px) {{
            p{{
              width: 80%;
              font-size: 2vw; /* Adjusted for smaller screens */
              white-space: wrap;
            }}
            .container{{
              white-space: wrap;
            }}
          }}
          @media screen and (min-width:600px) {{
            p{{
              width: 80%;
              font-size: 2.3vw;
              white-space: wrap;
              left: 26%;
              top: 47%;
              font-size: 5vw;
            }}
          }}
        </style>
        <body>
          <div class="container">
            <img src="C:\\Users\\CoreCom\\Downloads\\certificate.png" alt="Certificates">
            <p>
              {name}
            </p>
          </div>
        </body>
        </html>
        """
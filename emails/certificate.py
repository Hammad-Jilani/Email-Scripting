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
            width: 96%;
            z-index: 1;
          }}
          p{{
            width: 78%;
            position: absolute;
            left: 33%;
            top: 51%;
            font-size: 45px;
            padding: 10px;
            font-family: Calibri, sans-serif;
            margin-top: 20px;
          }}
          
        </style>
        <body>
          <div class="container">
            <img src="C:\\Users\\CoreCom\\Downloads\\certificateDesign.png" alt="Certificates">
            <p>
              {name}
            </p>
          </div>
        </body>
        </html>
        """
import pdfkit

def getCertificate(name):
    imagePath= "C:\\Users\\CoreCom\\Downloads\\certificateDesign.png"

    htmlcontent = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Certificate Design</title>
            <style>
                

                body {{
                    padding: 0;
                    margin: 0;
                    color: rgba(0, 0, 0, 0.863);
                    background-color: #22427E;
                    font-family: "Playfair Display";
                }}

                .container {{
                    position: absolute;
                    overflow: hidden;
                    text-align: center;
                    display: block;
                    background-color: purple;
                }}
                .name{{
                    padding: 0px;
                    margin: 0px;
                }}
                .name-div{{
                    position: absolute;
                    display: block;
                    text-align: center;
                    height: 0.45in;
                    width:100%;
                    top: 4.05in;
                    padding: 0px;
                    margin: auto;
                    font-size:0.37in;
                }}
                .competition{{
                    padding: 0px;
                    margin: 0px;
                }}
                img{{
                    width: 100%;
                    z-index: -1;
                }}
            </style>
        </head>
        <body>
            <img src={imagePath} alt="">
            <div class="name-div">
                <p class="name">{name}</p>
            </div>
        </body>
        </html>
    '''

    htmlFile = open("temp.html","w")     
    htmlFile.write(htmlcontent)  
    htmlFile.close()
    options = {
            'dpi': 365,
            'margin-top': '0in',
            'margin-right': '0in',
            'margin-bottom': '0in',
            'margin-left': '0in',
            'page-height': '5.71in',
            'page-width': '8in',
            'encoding': "UTF-8",
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None,
        }

    certificateFile= "certificate.pdf"
    try:
        # pdfkit.from_file("temp.html", certificateFile , options=options)
        path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
        pdfkit.from_file("temp.html", certificateFile, configuration=config, options=options)

    except Exception as ex:
        print(ex)  
    return certificateFile


# getCertificate("Laiba Nadeem")
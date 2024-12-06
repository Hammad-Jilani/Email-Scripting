def certificates(name):
  return f""" 

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Certificates</title>
</head>
<style>
  *{{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  .container{{
    position: relative;
    height: auto;
  }}
  .container img{{
    width: 100%;
    height: 100%;
    z-index: 1;
    /* object-fit: cover; */
  }}

  p{{
    width: 82%;
    position: absolute;
    padding: 10px;
    font-family: Calibri, sans-serif;
    font-size: 6vw;
  }}
  @media screen and (min-width:400px){{
    p{{
      top: 46%;
      left: 22%;
    }}
  }}

</style>
<body>
  <div class="container">
    <img src="/emails/Images/image.png" alt="Letter">
    <p>
      {name}
    </p>
  </div>
</body>
</html>
"""
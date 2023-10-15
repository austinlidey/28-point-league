"""Constants module for email templates.

COPYRIGHT: 
    AuthorChaos / 2023
"""
from typing import Final


# TODO [$6524c1c66067880007969d63]: Generate HTML email template, then insert data.
HTML_TOP_BODY: Final[str] = f"""
<html>
    <head>
        <link href=\'https://fonts.googleapis.com/css?family=Open Sans\' rel=\'stylesheet\'>
        <style>
            * {{
                font-family: \'Open Sans\', sans-serif;
                font-weight: 400;
            }}

            table, th, td {{
                border: 3px solid black;
                border-collapse: collapse;
            }}

            p {{
                margin-block-start: 0px;
                margin-block-end: 0px;
                vertical-align: top;
            }}

            th {{
                background-color: black;
                color: white;
            }} 

            .week-status {{
                font-size: 1.5rem;
            }}

            .week-result {{
                font-size: 1.2rem;
            }}

            .single-team-container {{
                padding-left: 10px;
                padding-right: 10px;
                text-align: center;
                width: 100%;
            }}

            .team-container {{
                font-weight: 400;
                display: flex;
                justify-content: center;
                text-align: center;
                font-family: \'Open Sans\', sans-serif;
            }}
            
            /* Change \'2n\' to the desired value of n */
            tr:nth-child(2n) {{
                background-color: #f2f2f2; /* Change this color as needed */
            }}

            tr {{
                vertical-align: top;
                text-align: center;
            }}

            td {{
                font-weight: bolder;
                vertical-align: middle;
                text-align: center;
                width: 450px;
                height: 200px;
            }}
            
            </style>
    </head>
    <body>
        <table>
            <tbody>
                <tr>
                    <th>Week</th>
                    <th>Result</th>
                </tr>
"""
# TODO [$6524c1c66067880007969d65]: Add images of winning teams using `team.logo_url`.
SINGLE_TEAM_CONTAINER: Final[str] = """\
                            <div class="single-team-container">
                                <img src="{}" height="90px/">
                                <p>{}</p>
                            </div>
"""
# Week, Result Title, Teams (if any)
HTML_MODULAR_BODY: Final[str] = """\
                <tr>
                    <td class="week-status">{}<br>{}</td>
                    <td class="week-result">{}<br>
                        <div class="team-container">
{}                       
                        </div>
                    </td>
                </tr>                    
"""

HTML_BOTTOM_BODY: Final[str] = """\
            </tbody>
        </table>
    </body>
</html>"""

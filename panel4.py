import panel as pn

coordinates_string = """{"65":[0,300,0,0]}"""
pdf_file_name ="awesome-panel-readthedocs-io-en-latest.pdf"
html_pane = pn.pane.HTML(f"""
        <head>
            <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.8.162/pdf_viewer.css'/>
            <script src='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.8.162/pdf_viewer.js'></script>
        </head>
        <div>
            <script>
                console.log('in HTML widget')
            </script>
            <div id='viewerContainer'>
                <iframe height='1000px' width='700px' id='viewer' src='pdfjs-3.8.162-dist/web/viewer.html?file=../../pdf/{pdf_file_name}&coordinates={coordinates_string}' width='100%' height='100%'></iframe>
            </div> 
        """)

html_pane.servable()
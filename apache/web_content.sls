manage_index:
  file.managed:
    - name: /var/www/html/index.html
    - show_changes: False
    - contents: |
        <html>
          <body>
            <h1>Demo worked!</h1>
          </body>
        </html>

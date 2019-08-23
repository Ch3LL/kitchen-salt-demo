{% set webserver = 'apache2' %}
install_apache:
  pkg.installed:
    - name: {{ webserver }}

start_httpd:
  service.running:
    - name: {{ webserver }}
    - enable: True
    - require:
      - pkg: {{ webserver }}

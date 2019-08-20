{% set webserver = 'apache2' %}
install_apache:
  pkg.installed:
    - name: {{ webserver }}

start_httpd:
  service.running:
    - name: apache2
    - enable: True
    - require:
      - pkg: {{ webserver }}

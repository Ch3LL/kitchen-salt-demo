import requests

def test_apache_service(host):
    '''
    make sure apache2 is running.
    '''
    assert host.service('apache2')

def test_index_file(host):
    '''
    make sure index.html file is correct
    '''
    index = host.file('/var/www/html/index.html')
    assert index.contains('Demo worked!')

def test_website_200(url):
    '''
    test http 200 code
    '''
    assert requests.get(url).status_code == 200

def test_website_content(url):
    '''
    test content of website
    '''
    assert 'Demo worked!' in requests.get(url).text

from pycman.utils.common import datetime_format

package = {
    'name': 'moka-jcci',
    'version': '0.0.1',
    'author': 'singein',
    'email': 'singein@qq.com',
    'scripts': {
        'default': 'echo hello!',
        'tests': f'pytest tests -n=auto --html=test-reports/test-report-{datetime_format()}.html --self-contained-html'
    }
}
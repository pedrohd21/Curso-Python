from string import Template
from datetime import datetime

with open('index.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    body_msg = template.safe_substitute(nome='Pedro Henrique', data=data_atual)

print(body_msg)


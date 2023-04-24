from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load
from yaml.loader import SafeLoader
import yaml

template_env = Environment(loader=FileSystemLoader('templates/'))
template = template_env.get_template('layout.html')

with open('article.md') as markdown_file:
    article = markdown(
        markdown_file.read(),
        extras=['fenced-code-blocks', 'code-friendly']
        )
    
with open('config.json') as config_file:
    config = load(config_file)

with open('index.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            article=article
        )
    )

def StrYamlToDict(yamlText):
    data = yaml.safe_load(yamlText.replace("---", ""))
    return data

def find_yaml():
    with open('article.md', 'r') as f:
        markdown_file= f.read()
        split = markdown_file.rfind("---") + 3
        partYaml = markdown_file[:split]
    return StrYamlToDict(partYaml)
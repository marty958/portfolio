# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('index_template.html')

heading_list = ['RESEARCH', 'ENGINEERING', 'ILLUSTRATION']

with open('research_pub.yml') as f:
    research_pub_list = yaml.load(f)
with open('research_conf.yml') as f:
    research_conf_list = yaml.load(f)
with open('research_gakkai.yml') as f:
    research_gakkai_list = yaml.load(f)
with open('eng_products.yml') as f:
    eng_products_list = yaml.load(f)
with open('design_products.yml') as f:
    design_products_list = yaml.load(f)
with open('links.yml') as f:
    link_list = yaml.load(f)

output = template.render(heading_list=heading_list, research_pub_list=research_pub_list, research_conf_list=research_conf_list, research_gakkai_list=research_gakkai_list, eng_products_list=eng_products_list, design_products_list=design_products_list, link_list=link_list)

with open('./index.html', mode='w') as f:
    f.write(output)

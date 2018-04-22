# coding=utf-8
import os
from string import Template
from ansi_colours import AnsiColours

class TextTemplate(AnsiColours):
    @classmethod
    def render(cls, template, **kwargs):
        if not os.path.isfile(template):
            raise OSError("Template was not found")
        with open(template, 'r') as content_file:
            content = content_file.read()
            t = Template(content)
            kwargs.update(AnsiColours.colours)
            return t.substitute(**kwargs)

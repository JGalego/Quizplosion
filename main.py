r"""
> Quizplosion

Turns quizdown-formatted markdown files into quizzes.
                              
          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
_____________/_ __ \_____________
"""

import logging
import json

from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
	level=logging.INFO
)

# Initialize CLI arguments
parser = ArgumentParser(
    description="Turns quizdown-formatted markdown files into quizzes."
)
parser.add_argument('quiz')
parser.add_argument(
	'-p', '--path',
	default="./",
	help="path to the templates directory."
)
parser.add_argument(
	'-t', '--template',
	default="quiz.html.j2",
	help="template for generating the quiz."
)
parser.add_argument(
	'-o', '--output',
	default="quiz.html",
	help="output file containing the quiz."
)
parser.add_argument(
	'-v', '--variables',
	default={},
	type=json.loads
)

args = parser.parse_args()

# Load template
logger.info("Loading template")
loader = FileSystemLoader(searchpath=args.path)
environment = Environment(loader=loader)
template = environment.get_template(args.template)

# Render template
logger.info("Rendering quiz")
with open(args.quiz, mode="r", encoding="utf-8") as f:
    quiz = f.read()
content = template.render(quiz=quiz, **args.variables)

# Generate quiz
logger.info("Saving quiz")
with open(args.output, mode="w", encoding="utf-8") as output:
    output.write(content)

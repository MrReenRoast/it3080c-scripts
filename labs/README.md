I created a Python script that uses Gooey, a Python plugin that allows for GUI interfaces to be added to your Python code.

The best way to install Gooey is by using `pip`
```bash
pip install Gooey
```
Once you have it installed, it's very easy to import into your Python Script and run it
```python
from gooey import Gooey, GooeyParser
@Gooey()
def main():
  parser = GooeyParser(...)
  #code
```
From there, it's as simple as running some arguments:
```python
#This gives you the ability to allow user to select from a dropdown
error_parser.add_argument(
  choices=['Yes', 'No'])

#This adds a flag for the choices
error_parser.add_argument(
  '-f', '--foo',
  metavar='Example Flag',
  help='Example Flag (does not affect outcome)')

#You can then parse arguments using
args = error_parser.parse_args()
#rest of your code

#The program automatically displays success screens if the function completes successfully or errors, but if you want it to throw an error screen you can
raise Exception(...)
#like normal python
```
I hope this program is fun and helpful for whatever your needs are.

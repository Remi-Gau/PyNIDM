from rich import print

from rich.markdown import Markdown
from rich.prompt import IntPrompt

def format_prompt_msg(msg):
    return f"\n[bold][underline]{msg}[/underline][/bold]"

def select_integer_from_option(option, msg= None):
    if msg is None:
        msg = "Please select an option from"
    choices = [str(x) for x in range(1, option+1)]
    selection = IntPrompt.ask(format_prompt_msg(msg), choices=choices)
    return selection

def print_item(item_nb, label, definition, url):
    print(f"""
{item_nb}:\t[underline]Label[/underline]:         {label}
    \t[underline]Definition[/underline]:    {definition}
    \t[underline]Preferred URL[/underline]: {url}
    """)

def separator():
    print("\n[blue]*************************************************************************************[/blue]")

def term_datatype_prompt():

    MARKDOWN = """
## Please enter the value type for this term from the following list:

1. **string** - The string datatype represents character strings
2. **categorical** - A variable that can take on one of a limited number of possible values, 
    assigning each to a nominal category on the basis of some qualitative property.
3. **boolean** - Binary-valued logic:{true,false}
4. **integer** - Integer is a number that can be written without a fractional component
5. **float** - Float consists of the values m x 2^e, where m is an integer whose absolute value is less than 2^24, 
    and e is an integer between -149 and 104, inclusive
6. **double** - Double consists of the values m x 2^e, where m is an integer 
    whose absolute value is less than 2^53, and e is an integer between -1075 and 970, inclusive
7. **duration** - Duration represents a duration of time
8. **dateTime** - Values with integer-valued year, month, day, hour and minute properties, 
    a decimal-valued second property, and a boolean timezoned property.
9. **time** - Time represents an instant of time that recurs every day
10. **date** - Date consists of top-open intervals of exactly one day in length 
    on the timelines of dateTime, beginning on the beginning moment of each day (in each timezone)
11. **anyURI** - anyURI represents a Uniform Resource Identifier Reference (URI). 
    An anyURI value can be absolute or relative, and may have an optional fragment identifier"
"""
    md = Markdown(MARKDOWN)
    print(md)

    term_datatype = select_integer_from_option(11, msg= "Please enter the value type")

    return term_datatype

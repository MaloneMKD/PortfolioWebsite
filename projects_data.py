import os


def get_image_names(folder_name):
    dir_list = [image_name for image_name in os.listdir(f'{os.getcwd()}/port_web/static/images/{folder_name}')]
    dir_list.sort()
    return dir_list


# Template for a project
project_layout = {
    "title": "Project Title",
    "subtitle": "Project Subtitle",
    "github_link": "https://ProjectLink.com",
    "setup_links": [
        {
            "os": "Windows",
            "setup_name": "https://setupfile.com"
        },
    ],
    "images_folder_name": "ImageFolderName",
    "image_names":"", #get_image_names("ImageFolderName"),
    "about_list": ["Paragraph 1", "Paragraph 2", "Paragraph 3"],
    "tech_list": ["Programming language 1: List of techs (comma separated)", "Programming language 2: List of techs"],
    "prev_project": None,
    "next_project": None
}

# project Journal By Topic
journal_by_topic = {
    "title": "Journal By Topic",
    "subtitle": "Journaling Application.",
    "github_link": "https://github.com/MaloneMKD/Journal-By-Topic.git",
    "setup_links": [
        {
            "os": "Windows",
            "setup_name": "Journal By Topic"
        },
    ],
    "images_folder_name": "JBTPics",
    "image_names": get_image_names("JBTPics"),
    "about_list": ["Journal By Topic is a journaling application.",
                   "In the app, you can create a journal that can be password protected and create entries inside each"
                   " journal using the built in text editor. The text editor has all the features you will need including"
                   " tables, lists, and images and even inserting and rendering HTML and Markdown inside the editor."
                   " You can save an entry as a pdf file if you wish otherwise they are saved in their regular .jbt format."
                   " The program will save all entries in a folder called JBT-Topics"
                   " in your documents folder that you can make a copy of to keep as backup, no one will be able to read them without"
                   " this program and your password. From simple notes to very private entries, you can keep it all in this program.",
                   " Entries are saved as encrypted files and each journal (or"
                   " topic) has a unique ID that each entry inherits and thus entries can only be accessed through"
                   " their parent journal that can be password protected, ensuring security."],
    "tech_list": ["Python: PyQT"],
    "prev_project": "steak_nation",
    "next_project": "tms"
}

# Project Turing Machine Simulator
tms = {
    "title": "Turing Machine Simulator",
    "subtitle": "Simulation application.",
    "github_link": "https://github.com/MaloneMKD/Turing-Machine-Simulator.git",
    "setup_links": [
        {
            "os": "Windows",
            "setup_name": "Turing Machine Simulator"
        },
    ],
    "images_folder_name": "TMPics",
    "image_names": get_image_names("TMPics"),
    "about_list": ["Turing Machine Simulator is a simulation application.",
                   "This application allows you to design a Turing Machine on the canvas and test your input on the machine."
                   " Once you finish designing, you press the build button and the application wil make a logical TM behind the scenes that you can "
                   " test input on. On building, the application also creates a transition table that you can view on the summary page. ",
                   "When testing input, the application will demostrate the execution of the input by highlighting the current state and "
                   "moving the tape head to the current letter being read or written to. "
                   "After every input test, the application also creates an execution summary to show you the steps it took to "
                   " reach completion and whether the input was accepted or it crashed.",
                   "Once designed, you can save a TM and be able to reload it any time. This allows for backups and sharing."
                   " The TMs are saved as xml files. The program also includes checks to prevent infinite loops and provides a "
                   "warning if possible infinite loops are detected.",
                   "This program was created with computer science students in mind, to help them visualize theoretical concepts "
                   "and make understanding these concepts easier."],
    "tech_list": ["C++: Qt"],
    "prev_project": "journal_by_topic",
    "next_project": None
}

# Project Steak Nation
steak_nation = {
    "title": "Steak Nation",
    "subtitle": "Restaurant website.",
    "github_link": "https://github.com/MaloneMKD/SteakNationWebsite.git",
    "setup_links": [],
    "images_folder_name": "SNPics",
    "image_names": get_image_names("SNPics"),
    "about_list": ["Steak Nation is a website for a restuarant.",
                   "The website has a home page that shows off the restuarant itself,"
                   " then a menu page that shows the food and drinks that the restaurant offers, a reservations page that "
                   "allows customers to log in and make a reservation, manage their already made reservations and delete their account."
                   "Finally there is a staff page that shows and talks about the restaurant staff.",
                   "A customer registers with their email and phone number, they can then log in and make reservations or"
                   " manage their account. A manager or administrator for the restaurant can log in, see and manage all reservations.",
                   "Steak Nation is not a real restaurant but one that I made up for the purposes of this project."],
    "tech_list": ["Python: Flask, SQLAlchemy, SQLite",
                  "CSS: Bootstrap",
                  "HTML"],
    "prev_project": "eca",
    "next_project": "journal_by_topic"
}

# Project Wordsmith
wordsmith = {
    "title": "Wordsmith",
    "subtitle": "Poetry application.",
    "github_link": "https://github.com/MaloneMKD/Wordsmith.git",
    "setup_links": [
        {
            "os": "Android",
            "setup_name": "Wordsmith"
        },
    ],
    "images_folder_name": "WSPics",
    "image_names": get_image_names("WSPics"),
    "about_list": ["Wordsmith is an application for poets.",
                   "This application allows the user to write poetry and save it. Poems are saved in a SQLite database. "
                   "The app has a grid and list view that are daptable to different screen sizes. Poems have tags that can"
                   " be used for searching and filtering.",
                   "The application has a 'Rhyme Utility' that uses an api to get all words that rhyme with the word requested,"
                   " and filters to only return perfect rhymes."],
    "tech_list": ["Python: Flet, SQLAlchemy, SQLite"],
    "prev_project": None,
    "next_project": "eca"
}

eca = {
    "title": "Elementary Cellular Automata",
    "subtitle": "Coding challange.",
    "github_link": "https://github.com/MaloneMKD/Elementary_Celllular_Automata.git",
    "setup_links": [
        {
            "os": "Windows",
            "setup_name": "Elementary Cellular Automata"
        },
    ],
    "images_folder_name": "ECAPics",
    "image_names": get_image_names("ECAPics"),
    "about_list": ["This program was a coding challenge.",
                   "A cellular automaton consists of colored cells arranged on a grid with a specified shape. "
                   "It evolves over discrete time steps based on rules determined by the states of neighboring cells. "
                   "These rules are applied iteratively for the desired number of time steps.",
                   " Elementary cellular automata operate on a grid of cells, each with two possible values (0 or 1). "
                   "The rules depend solely on neighboring cell values. The evolution of such automata can be described "
                   "using a table, specifying the next-generation state of a cell based on its left, current, and right "
                   "neighbors. With 8 possible binary states for neighboring cells, there exist 256 elementary cellular "
                   "automata, indexed by 8-bit binary numbers. (Wolfram 1983, 2002).",
                   "This program executes this concept. It accepts a number between 0 and 255 since there are 256 rules "
                   "in total and dynamically draws the pattern for that rule.Depending on the box size, it creates a grid"
                   " of cells. The first generation has only the center box  with a value of 0. The values of the boxes in"
                   " the grids in the next generations depend on the given rule.",
                   "Read more about this topic at: https://mathworld.wolfram.com/ ElementaryCellularAutomaton.html"],
    "tech_list": ["C++: Qt"],
    "prev_project": "wordsmith",
    "next_project": "steak_nation"
}

if __name__ == "__main__":
    print(get_image_names("JBTPics"))

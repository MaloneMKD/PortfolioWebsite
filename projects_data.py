import os


def getImageNames(folderName):
    return [image_name for image_name in os.listdir(f'{os.getcwd()}/port_web/static/images/{folderName}')]


journal_by_topic = {
    "title": "Journal By Topic",
    "github_link": "https://github.com/MaloneMKD/Journal-By-Topic.git",
    "setup_links": [
        {
            "os": "Windows",
            "link": "https://setupfile.com"
        },
    ],
    "images_folder_name": "JBTPics",
    "image_names": getImageNames("JBTPics"),
    "about_list": ["Journal By Topic is a journaling application.",
                   "In the app, you can create a journal that can be password protected and create entries inside each"
                   " journal using the built in text editor. Entries are saved as encrypted files and each journal (or"
                   " topic) has a unique ID that each entry inherits and thus entries can only be accessed through"
                   " their parent journal, ensuring security."],
    "tech_list": [
        {
            "lang": "Python",
            "techs": "PyQT"
        },
        {
            "lang": "Python",
            "techs": "PySide6, Flet, Flask, Selenium, Joblib"
        }
    ]
}

if __name__ == "__main__":
    print(getImageNames("JBTPics"))

from mycroft import MycroftSkill, intent_file_handler


class Voxprint(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voxprint.intent')
    def handle_voxprint(self, message):
        self.speak_dialog('voxprint')


def create_skill():
    return Voxprint()


class TemplateReader:
    def __init__(self):
        pass

    def read_course_template(self,course_name):
        try:
            if (course_name=='ComputerScienceandEngineering'):
                email_file = open("email_templates/DSM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name=='MechanicalEngineering'):
                email_file = open("email_templates/MLM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'ElectricalEngineering'):
                email_file = open("email_templates/DLM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'ElectronicsandCommunicationEngineering'):
                email_file = open("email_templates/NLPM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'CivilEngineering'):
                email_file = open("email_templates/DSFM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'ChemicalEngineering'):
                email_file = open("email_templates/Vision_Template.html", "r")
                email_message = email_file.read()
            return email_message
        except Exception as e:
            print('The exception is '+str(e))

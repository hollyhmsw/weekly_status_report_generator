import random
import datetime

class StatusReportGenerator():
    #Returns a list with todays date in 2 formats, one for filename, one for the report itself
    def day_month_and_year(self):
        date_list = []
        date_list.append(datetime.date.today().strftime("%B %d, %Y"))
        date_list.append(datetime.date.today().strftime("%B_%d_%Y"))
        return date_list

    #takes our text file resources and makes them into lists of strings
    def get_file_and_return_list(self, filename):
        file = open(filename, "rb")
        our_list = [] 
        for line in file: 
            #print line
            our_list.append(line)
        return our_list

    #returns a random integer from a given range
    def get_number_of_items(self, range):
        return random.randrange(0, range)

    def generate_report(self):
        dates = self.day_month_and_year()
        status_report_filename = "status_report_"+dates[1]+".txt"
        report_file = open(status_report_filename, "wb+")
        report_file.writelines(dates[0] + " Status Report" + "\n")
        report_file.writelines("\n") 
        names = self.get_file_and_return_list("names.txt")
        projects = self.get_file_and_return_list("project_names.txt")
        statuses = self.get_file_and_return_list("statuses.txt")
        for name in names:
            report_file.writelines(name)
            items = self.get_number_of_items(5)
            if items == 0:
                report_file.writelines(" - On vacation this week.")
            else:
                for x in range(items):
                    status = statuses[self.get_number_of_items(len(statuses))]
                    project_name = str(projects[self.get_number_of_items(len(projects))])
                    ticket = project_name.strip() + "-" +  str(self.get_number_of_items(2000))
                    report_file.writelines(" - " + ticket + ": " + status)
            report_file.writelines("\n")
        report_file.close()

if __name__ == '__main__':
    new_report = StatusReportGenerator()
    new_report.generate_report()


class Contact():

    def __init__(self,csv):
        fp = open(csv, "r")
        self.contact_name = []
        self.contact_number = []
        self.contact_all =[]
        for line in fp.readlines():
            line = line.strip()
            self.contact_name.append(line.split(", ")[0])
            self.contact_number.append(line.split(", ")[1])
            self.contact_all.append(line.split(", "))
        fp.close()

    # find index of the word in the list
    def list_index(self,word,list):
        for i,v in enumerate(list):
            if v == word:
                return i

    # show the contact
    def show_contact(self,contact_all):
        for list in contact_all:
            print "'{} : {}'".format(list[0],list[1])
        return "=======================\n"

    # search by name
    def search_by_name(self,name):
        if name == 'all':
            return self.show_contact(self.contact_all)
        else:
            try:
                name_index = self.list_index(name, self.contact_name)
                return self.show_contact([self.contact_all[name_index]])
            except:
                return "not in the contact file\n"

    # search by phone number
    def search_by_number(self,number):
        if number == 'all':
            return self.show_contact(self.contact_all)
        else:
            try:
                number_index = self.list_index(number, self.contact_number)
                return self.show_contact([self.contact_all[number_index]])
            except:
                return "not in the contact file\n"

    # search by either name or phone number
    def search(self,anything):
        if anything == 'all':
            return self.show_contact(self.contact_all)
        else:
            try:
                name_index = self.list_index(anything, self.contact_name)
                return self.show_contact([self.contact_all[name_index]])
            except:
                try:
                    number_index = self.list_index(anything, self.contact_number)
                    return self.show_contact([self.contact_all[number_index]])
                except:
                    return "not in the contact file\n"

    # add a contact in contact file
    def add_contact(self, name, number):
        self.contact_name.append(name)
        self.contact_number.append(number)
        self.contact_all.append([name, number])
        return "successfully add the contact of '{} : {}'.\n".format(name, number)

    # remove a contact by either name or phone number
    def remove_contact(self, anything):
        try:
            name_index = self.list_index(anything, self.contact_name)
            anything_number = self.contact_number[name_index]
            self.contact_name.pop(name_index)
            self.contact_number.pop(name_index)
            self.contact_all.pop(name_index)
            return "successfully remove the contact of '{} : {}'.\n".format(anything, anything_number)
        except:
            try:
                number_index = self.list_index(anything, self.contact_number)
                anything_name = self.contact_name[number_index]
                self.contact_name.pop(number_index)
                self.contact_number.pop(number_index)
                self.contact_all.pop(number_index)
                return "successfully remove the contact of '{} : {}'.\n".format(anything_name, anything)
            except:
                return "not in the contact file"

    # search by name and then change a contact
    def change_contact(self, name):
        try:
            name_index = self.list_index(name, self.contact_name)
            number = self.contact_number[name_index]
            yes_no = raw_input("do you want to change '{} : {}'? (y/n)".format(name, number))
            if yes_no == "y" or yes_no == "Y" or yes_no == "yes" or yes_no == "Yes" or yes_no == "YES":
                new_name = raw_input("write the new name : ")
                new_number = raw_input("write the new number : ")
                self.contact_name[name_index] = new_name
                self.contact_number[name_index] = new_number
                self.contact_all[name_index] = [new_name, new_number]
                return "successfully change the contact '{} : {}' to '{} : {}'.\n".format(name, number, new_name, new_number)
            else:
                return "end of changing the contact.\n"
        except:
            print "not in the contact file"

    def __del__(self):
        fp = open("oop_08_contact.csv", "w")
        for contact in self.contact_all:
            line = '{}, {}\n'.format(contact[0], contact[1])
            fp.write(line)
        fp.close()

contact = Contact("oop_08_contact.csv")

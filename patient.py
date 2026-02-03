class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, address, postcode=''):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
            postcode (string, optional): Postcode. Defaults to ''
        """

        #ToDo1
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__address = address
        self.__postcode = postcode
        self.__symptoms = []
        self.__doctor = 'None'
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return f'{self.__first_name} {self.__surname}'


    def get_doctor(self) :
        #ToDo3
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def add_symptom(self, symptom):
        """Adds a symptom to the symptoms list
        Args:
            symptom (string): the symptom to add
        """
        self.__symptoms.append(symptom)

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        print(f'Symptoms of {self.full_name()}:')
        if self.__symptoms:
            for symptom in self.__symptoms:
                print(f'- {symptom}')
        else:
            print('- No symptoms recorded')

    def get_symptoms(self):
        """Returns the list of symptoms"""
        return self.__symptoms.copy()

    def get_first_name(self):
        """Returns the first name"""
        return self.__first_name

    def get_surname(self):
        """Returns the surname"""
        return self.__surname

    def get_age(self):
        """Returns the age"""
        return self.__age

    def get_mobile(self):
        """Returns the mobile number"""
        return self.__mobile

    def get_address(self):
        """Returns the address"""
        return self.__address

    def get_postcode(self):
        """Returns the postcode"""
        return self.__postcode

    def to_line(self):
        """Writes one line of text for file storage. Fields separated by tab."""
        parts = [
            self.__first_name.replace('\t', ' ').replace('\n', ' '),
            self.__surname.replace('\t', ' ').replace('\n', ' '),
            str(self.__age),
            self.__mobile.replace('\t', ' ').replace('\n', ' '),
            self.__address.replace('\t', ' ').replace('\n', ' '),
            self.__postcode.replace('\t', ' ').replace('\n', ' '),
            self.__doctor.replace('\t', ' ').replace('\n', ' '),
            ';'.join(self.__symptoms)
        ]
        return '\t'.join(parts)

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__address[:20]:^20}|{self.__postcode:^10}'


def patient_from_line(line):
    """Read one line from file and return a Patient. Simple tab-separated format."""
    parts = line.strip().split('\t')
    if len(parts) < 8:
        return None
    first_name = parts[0]
    surname = parts[1]
    age = int(parts[2])
    mobile = parts[3]
    address = parts[4]
    postcode = parts[5]
    doctor = parts[6]
    symptoms_str = parts[7]
    p = Patient(first_name, surname, age, mobile, address, postcode)
    p.link(doctor)
    if symptoms_str:
        for s in symptoms_str.split(';'):
            if s.strip():
                p.add_symptom(s.strip())
    return p

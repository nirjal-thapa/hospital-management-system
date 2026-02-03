from doctor import Doctor
from patient import Patient, patient_from_line


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')


        # check if the username and password match the registered ones
        #ToDo1
        if username == self.__username and password == self.__password:
            print('Login successful.')
            return username
        else:
            print('Login failed.')
            return None

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input('First name of Doctor: ')
        surname = input('Surname of Doctor: ')
        speciality = input('Speciality of Doctor: ')
        return first_name, surname, speciality
    
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input('Option: ')
    
        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            first_name, surname, speciality = self.get_doctor_details()
            

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    name_exists = True
                    break


            #ToDo6
            if not name_exists:
                doctors.append(Doctor(first_name, surname, speciality))
            print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase

            #ToDo8
            if op == 1:
                new_first_name = input('Enter the new first name: ')
                doctors[index].set_first_name(new_first_name)
            elif op == 2:
                new_surname = input('Enter the new surname: ')
                doctors[index].set_surname(new_surname)
            elif op == 3:
                new_speciality = input('Enter the new speciality: ')
                doctors[index].set_speciality(new_speciality)
            print('Doctor details updated.')



        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            #ToDo9
            try:
                doctor_index = int(doctor_index) -1

                # check if the id is in the list of doctors
                if self.find_index(doctor_index,doctors)!=False:
                    
                    # delete the doctor
                    del doctors[doctor_index]
                    print('Doctor deleted.')

                # if the id is not in the list of doctors
                else:
                    print('The id entered was not found.')
            except ValueError: # the entered id could not be changed into an int
                print('The id entered is incorrect')
             


        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def get_patient_details(self):
        """
        Get the details needed to add a patient
        Returns:
            first_name, surname, age, mobile, address, postcode
        """
        first_name = input('First name of Patient: ')
        surname = input('Surname of Patient: ')
        age = int(input('Age of Patient: '))
        mobile = input('Mobile number of Patient: ')
        address = input('Address of Patient: ')
        postcode = input('Postcode of Patient (optional, press Enter to skip): ')
        return first_name, surname, age, mobile, address, postcode

    def register_patient(self, patients):
        """
        Register a new patient
        Args:
            patients (list<Patient>): list of all active patients
        """
        print("-----Register Patient-----")
        print('Enter the patient\'s details:')
        first_name, surname, age, mobile, address, postcode = self.get_patient_details()
        
        # Check if patient already exists
        name_exists = False
        for patient in patients:
            if first_name == patient.get_first_name() and surname == patient.get_surname() and mobile == patient.get_mobile():
                print('Patient with same name and mobile number already exists.')
                name_exists = True
                break
        
        if not name_exists:
            new_patient = Patient(first_name, surname, age, mobile, address, postcode)
            
            # Ask for symptoms
            print('Enter symptoms (press Enter after each symptom, type "done" when finished):')
            while True:
                symptom = input('Symptom: ').strip()
                if symptom.lower() == 'done' or symptom == '':
                    break
                new_patient.add_symptom(symptom)
            
            patients.append(new_patient)
            print('Patient registered successfully.')
        else:
            print('Registration cancelled.')

    def add_symptoms_to_patient(self, patients):
        """
        Add symptoms to an existing patient
        Args:
            patients (list<Patient>): list of all active patients
        """
        print("-----Add Symptoms to Patient-----")
        self.view_patient(patients)
        
        patient_index = input('Please enter the patient ID: ')
        try:
            patient_index = int(patient_index) - 1
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return
        except ValueError:
            print('The id entered is incorrect')
            return
        
        patient = patients[patient_index]
        print(f'\nCurrent symptoms for {patient.full_name()}:')
        patient.print_symptoms()
        
        print('\nEnter new symptoms (press Enter after each symptom, type "done" when finished):')
        while True:
            symptom = input('Symptom: ').strip()
            if symptom.lower() == 'done' or symptom == '':
                break
            patient.add_symptom(symptom)
            print(f'Symptom "{symptom}" added.')
        
        print('Symptoms updated successfully.')

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     |      Address      | Postcode ')
        #ToDo10
        self.view(patients)

    def group_patients_by_family(self, patients):
        """
        Groups patients by family (surname)
        Args:
            patients (list<Patient>): list of all patients
        Returns:
            dict: dictionary with surname as key and list of patients as value
        """
        families = {}
        for patient in patients:
            surname = patient.get_surname()
            if surname not in families:
                families[surname] = []
            families[surname].append(patient)
        return families

    def view_patients_by_family(self, patients):
        """
        View patients grouped by family (surname)
        Args:
            patients (list<Patient>): list of all patients
        """
        print("-----View Patients by Family-----")
        families = self.group_patients_by_family(patients)
        
        if not families:
            print('No patients found.')
            return
        
        for surname, family_patients in families.items():
            print(f'\n--- Family: {surname} ({len(family_patients)} member(s)) ---')
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     |      Address      | Postcode ')
            for index, patient in enumerate(family_patients):
                print(f'{index+1:3}|{patient}')

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     |      Address      | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select a doctor for the patient:')
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                
                print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
    
        self.view_patient(patients)

        print("do you want to discharge a patient(Y/N):")
        if input().lower()=='y':
            print("-----Discharge Patient-----")
            patient_index = input('Please enter the patient ID: ')
            #ToDo12
            try:
                # patient_index is the patient ID mines one (-1)
                patient_index = int(patient_index) -1

                # check if the id is not in the list of patients
                if patient_index in range(len(patients)):
                    # discharge the patient
                    discharge_patients.append(patients[patient_index])
                    del patients[patient_index]
                    print('Patient discharged.')

                else:
                    print('The id entered was not found.')

            except ValueError: # the entered id could not be changed into an int
                print('The id entered is incorrect')
            
    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     |      Address      | Postcode ')
        #ToDo13
        self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            username = input('Enter the new username: ')
            self.__username = username

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            #ToDo15
            address = input('Enter the new address: ')
            self.__address = address

        else:
            #ToDo16
            print('Invalid operation choosen. Check your spelling!')


    def management_report(self, doctors, patients, discharged_patients):
        """
        Prints a simple management report for the admin:
         - Total number of doctors
         - Total number of patients per doctor
         - Total number of patients per illness (symptom) type
        """

        print("-----Management Report-----")

        # a) Total number of doctors in the system
        total_doctors = len(doctors)
        print(f'Total number of doctors: {total_doctors}')

        # b) Total number of patients per doctor
        print("\nTotal number of patients per doctor:")
        if not doctors:
            print('No doctors found.')
        else:
            for doctor in doctors:
                count = 0
                # use the helper if available
                if hasattr(doctor, "get_patient_count"):
                    count = doctor.get_patient_count()
                print(f'- {doctor.full_name()}: {count} patient(s)')

        # d) Total number of patients based on the illness type
        print("\nTotal number of patients per illness type:")
        symptom_counts = {}
        all_patients = patients + discharged_patients
        for patient in all_patients:
            symptoms = patient.get_symptoms()
            if symptoms:
                for symptom in symptoms:
                    symptom_counts[symptom] = symptom_counts.get(symptom, 0) + 1
        
        if symptom_counts:
            for symptom, count in sorted(symptom_counts.items()):
                print(f'- {symptom}: {count} patient(s)')
        else:
            print('No symptoms recorded.')

    def save_patients_to_file(self, patients, discharged_patients, filename='patients_data.txt'):
        """
        Saves all patient data to a plain text file. One line per patient.
        """
        try:
            f = open(filename, 'w')
            f.write('ACTIVE\n')
            for p in patients:
                f.write(p.to_line() + '\n')
            f.write('DISCHARGED\n')
            for p in discharged_patients:
                f.write(p.to_line() + '\n')
            f.close()
            print('Patient data saved successfully to ' + filename)
            return True
        except Exception as e:
            print('Error saving patient data: ' + str(e))
            return False

    def load_patients_from_file(self, filename='patients_data.txt'):
        """
        Loads patient data from a plain text file.
        Returns (active_patients, discharged_patients).
        """
        active_patients = []
        discharged_patients = []
        try:
            f = open(filename, 'r')
            lines = f.readlines()
            f.close()
        except FileNotFoundError:
            print('File ' + filename + ' not found. Starting with empty patient list.')
            return active_patients, discharged_patients
        except Exception as e:
            print('Error loading file: ' + str(e))
            return active_patients, discharged_patients

        section = None
        for line in lines:
            line = line.strip()
            if line == 'ACTIVE':
                section = 'active'
                continue
            if line == 'DISCHARGED':
                section = 'discharged'
                continue
            if not line or section is None:
                continue
            p = patient_from_line(line)
            if p is None:
                continue
            if section == 'active':
                active_patients.append(p)
            else:
                discharged_patients.append(p)

        print('Patient data loaded from ' + filename)
        print('Loaded ' + str(len(active_patients)) + ' active patient(s) and ' + str(len(discharged_patients)) + ' discharged patient(s)')
        return active_patients, discharged_patients

    def restore_doctor_patient_relationships(self, patients, doctors):
        """
        Restores doctor-patient relationships after loading from file
        Args:
            patients (list<Patient>): list of patients
            doctors (list<Doctor>): list of doctors
        """
        for patient in patients:
            doctor_name = patient.get_doctor()
            if doctor_name and doctor_name != 'None':
                # Find the doctor by full name
                for doctor in doctors:
                    if doctor.full_name() == doctor_name:
                        # Restore the relationship
                        doctor.add_patient(patient)
                        break


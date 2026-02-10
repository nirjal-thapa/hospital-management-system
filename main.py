# Imports
from admin import Admin
from doctor import Doctor
from patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    # Load saved admin credentials (if any), otherwise use defaults
    username, password, address = Admin.load_credentials()
    admin = Admin(username, password, address)
    doctors = [Doctor('Anish','Kumar','Internal Med.'), Doctor('Shyam','Kumar','Pediatrics'), Doctor('Rajesh','Thakur','Cardiology')]
    
    # Load patient data from file, or use default if file doesn't exist
    patients, discharged_patients = admin.load_patients_from_file('patients_data.txt')
    
    if not patients and not discharged_patients:
        patients = [
            Patient('Abin','Thapa', 20, '9801234567', 'Kathmandu', '44600'),
            Patient('Riya','Sharma', 37, '9801234567', 'Lalitpur', '44600'),
            Patient('Shailesh','Shrestha', 15, '9801234567', 'Bhaktapur', '44600')
        ]
        discharged_patients = []
    
    admin.restore_doctor_patient_relationships(patients, doctors)
    admin.restore_doctor_patient_relationships(discharged_patients, doctors)

    while True:
        if admin.login():
            running = True
            break
        else:
            print('Incorrect username or password.')

    while running:
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Register/view/discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- Management report')
        print(' 7- View patients by family')
        print(' 8- Add symptoms to patient')
        print(' 9- Quit')
        

        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
            admin.doctor_management(doctors)

        elif op == '2':
            # 2- Register/view/discharge patients
            print('Choose the operation:')
            print(' 1- Register new patient')
            print(' 2- View patients')
            print(' 3- Discharge patient')
            sub_op = input('Option: ')
            
            if sub_op == '1':
                admin.register_patient(patients)
            elif sub_op == '2':
                admin.view_patient(patients)
            elif sub_op == '3':
                admin.view_patient(patients)
                while True:
                    op_discharge = input('Do you want to discharge a patient(Y/N):').lower()
                    if op_discharge == 'yes' or op_discharge == 'y':
                        admin.discharge(patients, discharged_patients)
                        break
                    elif op_discharge == 'no' or op_discharge == 'n':
                        break
                    else:
                        print('Please answer by yes or no.')
            else:
                print('Invalid option.')
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            # 6 - Management report
            admin.management_report(doctors, patients, discharged_patients)

        elif op == '7':
            # 7 - View patients by family
            admin.view_patients_by_family(patients)

        elif op == '8':
            # 8 - Add symptoms to patient
            admin.add_symptoms_to_patient(patients)

        elif op == '9':
            # 9 - Quit
            #ToDo5
            print('Saving patient data...')
            admin.save_patients_to_file(patients, discharged_patients, 'patients_data.txt')
            print('Exiting the program. Goodbye!')
            running = False
            

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()

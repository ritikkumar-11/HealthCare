# HealthCare API

This is a Django Rest Framework-based API for managing patients, doctors, and their assignments. The API includes authentication, patient and doctor management, and patient-doctor mapping features.

## Features
- User authentication with JWT.
- CRUD operations for Patients and Doctors.
- Assigning and removing doctors from patients.
- Secure endpoints requiring authentication.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ritikkumar-11/HealthCare.git
   cd HealthCare
   ```
2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use 'venv\\Scripts\\activate'
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a .env file and configure necessary environment variables.
6. Start the server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### 1. Authentication APIs
- **Register a new user**
  - `POST /api/auth/register/`
  - **Use:** Register a new user with name, email, and password.
  
  ![Register Screenshot](screenshots/register.png)

- **User Login**
  - `POST /api/auth/login/`
  - **Use:** Log in a user and return a JWT token.
  
  ![Login Screenshot](screenshots/login.png)

### 2. Patient Management APIs
- **Create a new patient**
  - `POST /api/patients/`
  - **Use:** Add a new patient (Authenticated users only).
  
  ![Create Patient](screenshots/create_patient.png)

- **Retrieve all patients**
  - `GET /api/patients/`
  - **Use:** Get all patients created by the authenticated user.
  
  ![Get Patients](screenshots/get_patients.png)

- **Retrieve a specific patient**
  - `GET /api/patients/<id>/`
  - **Use:** Get details of a specific patient.
  
  ![Get Patient](screenshots/get_patient.png)

- **Update a patient**
  - `PUT /api/patients/<id>/`
  - **Use:** Update patient details.
  
  ![Update Patient](screenshots/update_patient.png)

- **Delete a patient**
  - `DELETE /api/patients/<id>/`
  - **Use:** Delete a patient record.
  
  ![Delete Patient](screenshots/delete_patient.png)

### 3. Doctor Management APIs
- **Create a new doctor**
  - `POST /api/doctors/`
  - **Use:** Add a new doctor (Authenticated users only).
  
  ![Create Doctor](screenshots/create_doctor.png)

- **Retrieve all doctors**
  - `GET /api/doctors/`
  - **Use:** Get all doctors.
  
  ![Get Doctors](screenshots/get_doctors.png)

- **Retrieve a specific doctor**
  - `GET /api/doctors/<id>/`
  - **Use:** Get details of a specific doctor.
  
  ![Get Doctor](screenshots/get_doctor.png)

- **Update a doctor**
  - `PUT /api/doctors/<id>/`
  - **Use:** Update doctor details.
  
  ![Update Doctor](screenshots/update_doctor.png)

- **Delete a doctor**
  - `DELETE /api/doctors/<id>/`
  - **Use:** Delete a doctor record.
  
  ![Delete Doctor](screenshots/delete_doctor.png)

### 4. Patient-Doctor Mapping APIs
- **Assign a doctor to a patient**
  - `POST /api/mappings/`
  - **Use:** Assign a doctor to a patient.
  
  ![Assign Doctor](screenshots/assign_doctor.png)

- **Retrieve all patient-doctor mappings**
  - `GET /api/mappings/`
  - **Use:** Get all mappings of patients and doctors.
  
  ![Get Mappings](screenshots/get_mappings.png)

- **Get all doctors assigned to a specific patient**
  - `GET /api/mappings/<patient_id>/`
  - **Use:** Retrieve all doctors assigned to a particular patient.
  
  ![Get Patient Doctors](screenshots/get_patient_doctors.png)

- **Remove a doctor from a patient**
  - `DELETE /api/mappings/<id>/`
  - **Use:** Remove a doctor from a patient.
  
 ![Screenshot from 2025-04-02 19-17-39](https://github.com/user-attachments/assets/a083ed58-e768-4eba-b5bb-31ee6fcda1f8)


## License
This project is licensed under the MIT License.


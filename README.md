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
  ![Screenshot from 2025-04-02 18-28-33](https://github.com/user-attachments/assets/00ff246c-ef1f-4a33-9117-065258b88eeb)

  

- **Retrieve all patients**
  - `GET /api/patients/`
  - **Use:** Get all patients created by the authenticated user.
  
  ![Get Patients](screenshots/get_patients.png)

- **Retrieve a specific patient**
  - `GET /api/patients/<id>/`
  - **Use:** Get details of a specific patient.
  
  ![Screenshot from 2025-04-02 18-24-43](https://github.com/user-attachments/assets/6b45a2ab-3055-438f-81f5-49eec737cc87)


- **Update a patient**
  - `PUT /api/patients/<id>/`
  - **Use:** Update patient details.
  
 ![Screenshot from 2025-04-02 18-37-37](https://github.com/user-attachments/assets/76b39b17-f04f-4d65-b71d-0af4ba6526f1)


- **Delete a patient**
  - `DELETE /api/patients/<id>/`
  - **Use:** Delete a patient record.
  
![Screenshot from 2025-04-02 18-38-06](https://github.com/user-attachments/assets/423f7c36-e1ca-482d-a85b-b54a571d0b03)


### 3. Doctor Management APIs
- **Create a new doctor**
  - `POST /api/doctors/`
  - **Use:** Add a new doctor (Authenticated users only).
  
 ![Screenshot from 2025-04-02 18-26-00](https://github.com/user-attachments/assets/4ef8c951-9adc-4b87-8392-37e06adf2c59)


- **Retrieve all doctors**
  - `GET /api/doctors/`
  - **Use:** Get all doctors.
  
  ![Get Doctors](screenshots/get_doctors.png)

- **Retrieve a specific doctor**
  - `GET /api/doctors/<id>/`
  - **Use:** Get details of a specific doctor.
  ![Screenshot from 2025-04-02 18-38-59](https://github.com/user-attachments/assets/8f2701ea-26e2-4f76-b9ec-c6fc33b2655b)

  

- **Update a doctor**
  - `PUT /api/doctors/<id>/`
  - **Use:** Update doctor details.
  ![Screenshot from 2025-04-02 18-40-18](https://github.com/user-attachments/assets/84ef1fcb-8910-446a-9e36-b041905bf149)

  )

- **Delete a doctor**
  - `DELETE /api/doctors/<id>/`
  - **Use:** Delete a doctor record.
  
  ![Screenshot from 2025-04-02 18-40-35](https://github.com/user-attachments/assets/cc12b0db-974b-4382-a3dc-98e557fe915e)


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
  
  

- **Remove a doctor from a patient**
  - `DELETE /api/mappings/<id>/`
  - **Use:** Remove a doctor from a patient.
  
 ![Screenshot from 2025-04-02 19-17-39](https://github.com/user-attachments/assets/a083ed58-e768-4eba-b5bb-31ee6fcda1f8)


## License
This project is licensed under the MIT License.


from rest_framework import viewsets, status
from rest_framework.response import Response
from patient.models import Patient
from doctor.models import Doctor  # Corrected import
# from .serializers import PatientDoctorMappingSerializer

 # in this we have not used serializer, we directly getting the parameter from the user using request and then we performing the crud 
class PatientDoctorMappingViewSet(viewsets.ViewSet):
    def create(self, request):  # Assign a doctor to a patient
        patient_id = request.data.get("patient_id")
        doctor_name = request.data.get("doctor_name")

        try:
            patient = Patient.objects.get(id=patient_id)
            doctor = Doctor.objects.get(name=doctor_name)
            patient.doctor.add(doctor)
            return Response({"message": "Doctor assigned successfully"}, status=status.HTTP_201_CREATED)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):  # Get all mappings
        patients = Patient.objects.prefetch_related('doctor').all()# this query is used to fetch the doctor related to every patient
        data = [
            {
                "patient_id": patient.id,
                "patient_name": patient.name,
                "doctor_names": [doctor.name for doctor in patient.doctor.all()]
            }
            for patient in patients
        ]
        return Response(data, status=status.HTTP_200_OK) # is used to send an HTTP response back to the client.

    def retrieve(self, request, pk=None):  
        try:
            patient = Patient.objects.prefetch_related('doctor').get(id=pk)
            doctor_names = [doctor.name for doctor in patient.doctor.all()]
            return Response({"patient_id": pk, "doctor_names": doctor_names}, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):  # Remove doctor from a patient
        doctor_name = request.data.get("doctor_name")

        try:
            patient = Patient.objects.prefetch_related('doctor').get(id=pk)
            doctor = Doctor.objects.get(name=doctor_name)

            if doctor in patient.doctor.all():
                patient.doctor.remove(doctor)
                return Response({"message": "Doctor removed successfully"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Doctor not assigned to this patient"}, status=status.HTTP_400_BAD_REQUEST)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

from rest_framework import serializers
from patient.models import Patient
from doctor.models import Doctor

class PatientDoctorMappingSerializer(serializers.Serializer):
    patient_id = serializers.IntegerField()
    docotor_id = serializers.IntegerField()

    def create(self, validated_data):
        patient = Patient.objects.get(id=validated_data['patient_id'])
        doctor = Doctor.objects.get(id=validated_data['doctor_id'])
        patient.doctor.add(doctor)
        return patient

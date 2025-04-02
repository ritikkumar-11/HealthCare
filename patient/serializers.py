from rest_framework import serializers
from .models import Patient
from doctor.models import Doctor
from doctor.serializers import DoctorSerializer

class PatientSerializer(serializers.ModelSerializer):
    doctor = serializers.ListField(child=serializers.CharField(), write_only=True)
    doctor_names = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'doctor', 'doctor_names']

    def get_doctor_names(self, obj):
        return [doctor.name for doctor in obj.doctor.all()]

    def create(self, validated_data):
        doctor_names = validated_data.pop('doctor', [])  # Get doctor names
        patient = Patient.objects.create(**validated_data)

        doctors = Doctor.objects.filter(name__in=doctor_names)  # Get doctors by name
        patient.doctor.set(doctors)  # Assign to patient

        return patient  

    def update(self, instance, validated_data):
        doctor_names = validated_data.pop('doctor', None)  # Get doctor names

        # Update other fields
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)

        if doctor_names is not None:
            doctors = Doctor.objects.filter(name__in=doctor_names)  # Get doctors by name
            instance.doctor.set(doctors)  # Assign to patient

        instance.save()
        return instance

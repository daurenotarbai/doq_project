from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from apps.clinics.models import Doctor, Clinic, Procedure, Speciality


@registry.register_document
class ClinicParametrsDocument(Document):
    class Index:
        name = "clinicparametrs"

    class Django:
        model = Clinic
        fields = ['name']


@registry.register_document
class DoctorParametrsDocument(Document):
    class Index:
        name = "doctorparametrs"

    class Django:
        model = Doctor
        fields = ['first_name', 'last_name']


@registry.register_document
class ProcedureParametrsDocument(Document):
    class Index:
        name = "procedureparametrs"

    class Django:
        model = Procedure
        fields = ['name']


@registry.register_document
class SpecialityParametrsDocument(Document):
    class Index:
        name = "specialityparametrs"

    class Django:
        model = Speciality
        fields = ['name']

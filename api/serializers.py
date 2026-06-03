from rest_framework import serializers

from .models import (
    PeriodoAcademico,
    Departamento,
    Edificio,
    Persona,
    Estudiante,
    Docente,
    Programa,
    Curso,
    CursoPrerrequisito,
    GrupoCurso,
    Matricula,
    MatriculaHistorial,
    Evaluacion,
    NotaEvaluacion,
    CalificacionFinal,
    Aula,
    Horario,
    Asistencia,
    Syllabus,
    SyllabusUnidad,
    Tutoria,
    MaterialCurso,
    EventoCalendario,
    BecaEstudiante,
    Pago,
    Homologacion,
    SolicitudAcademica,
    Sancion,
    Usuario,
    Auditoria,
)

# Serializador para periodo academico
class PeriodoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = '__all__'

# Serializador para departamento
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

# Serializador para edificio
class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = '__all__'

# Serializador para persona
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

# Serializador para estudiante
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

# Serializador para docente
class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

# Serializador para programa
class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'

# Serializador para curso
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

# Serializador para curso prerrequisito
class CursoPrerrequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoPrerrequisito
        fields = '__all__'

# Serializador para grupo curso
class GrupoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoCurso
        fields = '__all__'

# Serializador para matricula
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

# Serializador para matricula historial
class MatriculaHistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatriculaHistorial
        fields = '__all__'

# Serializador para evaluacion
class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'

# Serializador para nota evaluacion
class NotaEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaEvaluacion
        fields = '__all__'

# Serializador para calificacion final
class CalificacionFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionFinal
        fields = '__all__'

# Serializador para aula
class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'

# Serializador para horario
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

# Serializador para asistencia
class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

# Serializador para syllabus
class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'

# Serializador para syllabus unidad
class SyllabusUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyllabusUnidad
        fields = '__all__'

# Serializador para tutoria
class TutoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoria
        fields = '__all__'

# Serializador para material curso
class MaterialCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCurso
        fields = '__all__'

# Serializador para evento calendario
class EventoCalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoCalendario
        fields = '__all__'

# Serializador para beca estudiante
class BecaEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecaEstudiante
        fields = '__all__'

# Serializador para pago
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

# Serializador para homologacion
class HomologacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homologacion
        fields = '__all__'

# Serializador para solicitud academica
class SolicitudAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudAcademica
        fields = '__all__'

# Serializador para sancion
class SancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sancion
        fields = '__all__'

# Serializador para usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# Serializador para auditoria
class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = '__all__'
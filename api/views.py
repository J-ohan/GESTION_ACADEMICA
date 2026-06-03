from rest_framework import filters, viewsets

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

from .serializers import (
    PeriodoAcademicoSerializer,
    DepartamentoSerializer,
    EdificioSerializer,
    PersonaSerializer,
    EstudianteSerializer,
    DocenteSerializer,
    ProgramaSerializer,
    CursoSerializer,
    CursoPrerrequisitoSerializer,
    GrupoCursoSerializer,
    MatriculaSerializer,
    MatriculaHistorialSerializer,
    EvaluacionSerializer,
    NotaEvaluacionSerializer,
    CalificacionFinalSerializer,
    AulaSerializer,
    HorarioSerializer,
    AsistenciaSerializer,
    SyllabusSerializer,
    SyllabusUnidadSerializer,
    TutoriaSerializer,
    MaterialCursoSerializer,
    EventoCalendarioSerializer,
    BecaEstudianteSerializer,
    PagoSerializer,
    HomologacionSerializer,
    SolicitudAcademicaSerializer,
    SancionSerializer,
    UsuarioSerializer,
    AuditoriaSerializer,
)

# crud para periodo academico (GET, POST, PUT, DELETE)
class PeriodoAcademicoViewSet(viewsets.ModelViewSet):
    queryset = PeriodoAcademico.objects.all()
    serializer_class = PeriodoAcademicoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'periodo_id',
        'nombre',
        'fecha_inicio',
        'fecha_fin',
        'activo',
    ]
    ordering = ['periodo_id']

# crud para departamento
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'departamento_id',
        'nombre',
        'codigo',
    ]
    ordering = ['nombre']

# crud para edificio
class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'edificio_id',
        'nombre',
        'direccion',
    ]
    ordering = ['nombre']

# crud para persona
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'persona_id',
        'tipo_doc',
        'numero_doc',
        'nombres',
        'apellidos',
        'email',
        'activo',
        'creado_en',
        'actualizado_en',
    ]
    ordering = ['apellidos', 'nombres']

# crud para estudiante
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'estudiante_id',
        'codigo',
        'fecha_ingreso',
        'activo',
    ]
    ordering = ['codigo']

# crud para docente
class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'docente_id',
        'codigo',
        'departamento',
        'titulo_maximo',
        'dedicacion',
        'rol',
        'fecha_vinculacion',
        'activo',
    ]
    ordering = ['codigo']

# crud para programa
class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'programa_id',
        'nombre',
        'codigo',
        'nivel_formacion',
        'modalidad',
        'activo',
    ]
    ordering = ['nombre']

# crud para curso
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'curso_id',
        'nombre',
        'codigo',
        'creditos',
        'nivel_semestre',
        'electiva',
        'activo',
    ]
    ordering = ['codigo']

# crud para curso prerrequisito
class CursoPrerrequisitoViewSet(viewsets.ModelViewSet):
    queryset = CursoPrerrequisito.objects.all()
    serializer_class = CursoPrerrequisitoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'curso',
        'prerrequisito',
    ]
    ordering = ['curso']

# crud para grupo curso
class GrupoCursoViewSet(viewsets.ModelViewSet):
    queryset = GrupoCurso.objects.all()
    serializer_class = GrupoCursoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'grupo_id',
        'curso',
        'docente',
        'periodo',
        'nombre_grupo',
        'cupo_maximo',
        'modalidad',
    ]
    ordering = ['periodo', 'curso', 'nombre_grupo']

# crud para matricula
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'matricula_id',
        'estudiante',
        'grupo',
        'periodo',
        'estado',
        'fecha_matricula',
        'nota_final',
    ]
    ordering = ['fecha_matricula']

# crud para matricula historial
class MatriculaHistorialViewSet(viewsets.ModelViewSet):
    queryset = MatriculaHistorial.objects.all()
    serializer_class = MatriculaHistorialSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'historial_id',
        'matricula',
        'estado_nuevo',
        'fecha_cambio',
        'registrado_por',
    ]
    ordering = ['-fecha_cambio']

# crud para evaluacion
class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'evaluacion_id',
        'grupo',
        'tipo',
        'nombre',
        'fecha_aplicacion',
        'porcentaje',
        'nota_maxima',
    ]
    ordering = ['fecha_aplicacion', 'nombre']

# crud para nota evaluacion
class NotaEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = NotaEvaluacion.objects.all()
    serializer_class = NotaEvaluacionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'nota_id',
        'evaluacion',
        'estudiante',
        'nota',
        'ausente',
        'registrado_en',
    ]
    ordering = ['-registrado_en']

# crud para calificacion final
class CalificacionFinalViewSet(viewsets.ModelViewSet):
    queryset = CalificacionFinal.objects.all()
    serializer_class = CalificacionFinalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'cal_final_id',
        'matricula',
        'nota_calculada',
        'nota_definitiva',
        'aprobado',
        'fecha_cierre',
    ]
    ordering = ['-fecha_cierre']

# crud para aula
class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'aula_id',
        'edificio',
        'tipo',
        'nombre',
        'piso',
        'capacidad',
        'activa',
    ]
    ordering = ['nombre']

# crud para horario
class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'horario_id',
        'grupo',
        'aula',
        'dia',
        'hora_inicio',
        'hora_fin',
    ]
    ordering = ['dia', 'hora_inicio']

# crud para asistencia
class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'asistencia_id',
        'grupo',
        'estudiante',
        'horario',
        'fecha',
        'presente',
        'justificada',
    ]
    ordering = ['-fecha']

# crud para syllabus
class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'syllabus_id',
        'grupo',
        'creado_en',
    ]
    ordering = ['-creado_en']

# crud para syllabus unidad
class SyllabusUnidadViewSet(viewsets.ModelViewSet):
    queryset = SyllabusUnidad.objects.all()
    serializer_class = SyllabusUnidadSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'unidad_id',
        'syllabus',
        'numero',
        'titulo',
        'semanas_duracion',
    ]
    ordering = ['syllabus', 'numero']

# crud para tutoria
class TutoriaViewSet(viewsets.ModelViewSet):
    queryset = Tutoria.objects.all()
    serializer_class = TutoriaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'tutoria_id',
        'docente',
        'estudiante',
        'curso',
        'fecha',
        'duracion_min',
        'modalidad',
    ]
    ordering = ['-fecha']

# crud para material curso
class MaterialCursoViewSet(viewsets.ModelViewSet):
    queryset = MaterialCurso.objects.all()
    serializer_class = MaterialCursoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'material_id',
        'grupo',
        'titulo',
        'tipo',
        'publicado_en',
    ]
    ordering = ['-publicado_en']

# crud para evento calendario
class EventoCalendarioViewSet(viewsets.ModelViewSet):
    queryset = EventoCalendario.objects.all()
    serializer_class = EventoCalendarioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'evento_id',
        'titulo',
        'tipo',
        'fecha_inicio',
        'fecha_fin',
        'aplica_todos',
        'programa',
    ]
    ordering = ['fecha_inicio']

# crud para beca estudiante
class BecaEstudianteViewSet(viewsets.ModelViewSet):
    queryset = BecaEstudiante.objects.all()
    serializer_class = BecaEstudianteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'beca_id',
        'estudiante',
        'periodo',
        'tipo_beca',
        'porcentaje_descuento',
        'aprobado',
        'fecha_aprobacion',
    ]
    ordering = ['estudiante', 'periodo']

# crud para pago
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'pago_id',
        'estudiante',
        'periodo',
        'monto',
        'fecha_pago',
        'metodo',
        'estado',
    ]
    ordering = ['-fecha_pago']

# crud para homologacion
class HomologacionViewSet(viewsets.ModelViewSet):
    queryset = Homologacion.objects.all()
    serializer_class = HomologacionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'homologacion_id',
        'estudiante',
        'curso_origen',
        'institucion_origen',
        'curso_destino',
        'aprobado',
        'fecha_solicitud',
    ]
    ordering = ['-fecha_solicitud']

# crud para solicitud academica
class SolicitudAcademicaViewSet(viewsets.ModelViewSet):
    queryset = SolicitudAcademica.objects.all()
    serializer_class = SolicitudAcademicaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'solicitud_id',
        'estudiante',
        'tipo',
        'estado',
        'fecha_envio',
        'fecha_respuesta',
        'atendida_por',
    ]
    ordering = ['-fecha_envio']

# crud para sancion
class SancionViewSet(viewsets.ModelViewSet):
    queryset = Sancion.objects.all()
    serializer_class = SancionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'sancion_id',
        'estudiante',
        'tipo',
        'fecha',
        'resuelto',
    ]
    ordering = ['-fecha']

# crud para usuario
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'usuario_id',
        'persona',
        'username',
        'rol',
        'ultimo_acceso',
        'activo',
        'creado_en',
    ]
    ordering = ['username']

# crud para auditoria
class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'auditoria_id',
        'tabla',
        'operacion',
        'registro_id',
        'usuario',
        'fecha',
    ]
    ordering = ['-fecha']
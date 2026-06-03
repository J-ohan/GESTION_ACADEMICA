from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PeriodoAcademicoViewSet,
    DepartamentoViewSet,
    EdificioViewSet,
    PersonaViewSet,
    EstudianteViewSet,
    DocenteViewSet,
    ProgramaViewSet,
    CursoViewSet,
    CursoPrerrequisitoViewSet,
    GrupoCursoViewSet,
    MatriculaViewSet,
    MatriculaHistorialViewSet,
    EvaluacionViewSet,
    NotaEvaluacionViewSet,
    CalificacionFinalViewSet,
    AulaViewSet,
    HorarioViewSet,
    AsistenciaViewSet,
    SyllabusViewSet,
    SyllabusUnidadViewSet,
    TutoriaViewSet,
    MaterialCursoViewSet,
    EventoCalendarioViewSet,
    BecaEstudianteViewSet,
    PagoViewSet,
    HomologacionViewSet,
    SolicitudAcademicaViewSet,
    SancionViewSet,
    UsuarioViewSet,
    AuditoriaViewSet,
)

router = DefaultRouter()
# registro de endpoints del api
router.register(r'periodos-academicos',     PeriodoAcademicoViewSet)
router.register(r'departamentos',           DepartamentoViewSet)
router.register(r'edificios',               EdificioViewSet)
router.register(r'personas',               PersonaViewSet)
router.register(r'estudiantes',             EstudianteViewSet)
router.register(r'docentes',               DocenteViewSet)
router.register(r'programas',              ProgramaViewSet)
router.register(r'cursos',                 CursoViewSet)
router.register(r'curso-prerrequisitos',   CursoPrerrequisitoViewSet)
router.register(r'grupos-curso',           GrupoCursoViewSet)
router.register(r'matriculas',             MatriculaViewSet)
router.register(r'matricula-historial',    MatriculaHistorialViewSet)
router.register(r'evaluaciones',           EvaluacionViewSet)
router.register(r'notas-evaluacion',       NotaEvaluacionViewSet)
router.register(r'calificaciones-finales', CalificacionFinalViewSet)
router.register(r'aulas',                  AulaViewSet)
router.register(r'horarios',               HorarioViewSet)
router.register(r'asistencia',             AsistenciaViewSet)
router.register(r'syllabus',               SyllabusViewSet)
router.register(r'syllabus-unidades',      SyllabusUnidadViewSet)
router.register(r'tutorias',               TutoriaViewSet)
router.register(r'materiales-curso',       MaterialCursoViewSet)
router.register(r'eventos-calendario',     EventoCalendarioViewSet)
router.register(r'becas-estudiante',       BecaEstudianteViewSet)
router.register(r'pagos',                  PagoViewSet)
router.register(r'homologaciones',         HomologacionViewSet)
router.register(r'solicitudes-academicas', SolicitudAcademicaViewSet)
router.register(r'sanciones',              SancionViewSet)
router.register(r'usuarios',               UsuarioViewSet)
router.register(r'auditoria',              AuditoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
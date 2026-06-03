from datetime import date

from django.db import models
from django.utils import timezone


class PeriodoAcademico(models.Model):
    periodo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=False)

    class Meta:
        db_table = "periodos_academicos"
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    departamento_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120, unique=True)
    codigo = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "departamentos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Edificio(models.Model):
    edificio_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "edificios"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    GENEROS = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    )

    persona_id = models.AutoField(primary_key=True)
    tipo_doc = models.CharField(max_length=10)
    numero_doc = models.CharField(max_length=30)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    fecha_nac = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENEROS, blank=True, null=True)
    email = models.CharField(max_length=120, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(default=timezone.now)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "personas"
        ordering = ["apellidos", "nombres"]
        unique_together = (("tipo_doc", "numero_doc"),)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Estudiante(models.Model):
    estudiante_id = models.AutoField(primary_key=True)
    persona = models.OneToOneField(
        Persona,
        models.CASCADE,
        db_column="persona_id",
        related_name="estudiante",
    )
    codigo = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField(default=date.today)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "estudiantes"
        ordering = ["codigo"]

    def __str__(self):
        return self.codigo


class Docente(models.Model):
    docente_id = models.AutoField(primary_key=True)
    persona = models.OneToOneField(
        Persona,
        models.CASCADE,
        db_column="persona_id",
        related_name="docente",
    )
    codigo = models.CharField(max_length=20, unique=True)
    departamento = models.ForeignKey(
        Departamento,
        models.CASCADE,
        db_column="departamento_id",
        blank=True,
        null=True,
        related_name="docentes",
    )
    titulo_maximo = models.CharField(max_length=100, blank=True, null=True)
    dedicacion = models.CharField(max_length=40, blank=True, null=True)
    rol = models.CharField(max_length=60, blank=True, null=True)
    fecha_vinculacion = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "docentes"
        ordering = ["codigo"]

    def __str__(self):
        return self.codigo


class Programa(models.Model):
    programa_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    nivel_formacion = models.CharField(max_length=60)
    departamento = models.ForeignKey(
        Departamento,
        models.CASCADE,
        db_column="departamento_id",
        blank=True,
        null=True,
        related_name="programas",
    )
    director = models.ForeignKey(
        Docente,
        models.CASCADE,
        db_column="director_id",
        blank=True,
        null=True,
        related_name="programas_dirigidos",
    )
    modalidad = models.CharField(max_length=30, default="Presencial")
    creditos_totales = models.SmallIntegerField(blank=True, null=True)
    duracion_semestres = models.SmallIntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "programas"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Curso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    programa = models.ForeignKey(
        Programa,
        models.CASCADE,
        db_column="programa_id",
        related_name="cursos",
    )
    departamento = models.ForeignKey(
        Departamento,
        models.CASCADE,
        db_column="departamento_id",
        blank=True,
        null=True,
        related_name="cursos",
    )
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveSmallIntegerField(default=3)
    horas_semana = models.PositiveSmallIntegerField(default=4)
    nivel_semestre = models.SmallIntegerField(blank=True, null=True)
    electiva = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "cursos"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class CursoPrerrequisito(models.Model):
    curso = models.ForeignKey(
        Curso,
        models.CASCADE,
        db_column="curso_id",
        related_name="prerrequisitos_rel",
    )
    prerrequisito = models.ForeignKey(
        Curso,
        models.CASCADE,
        db_column="prerrequisito_id",
        related_name="requerido_por_rel",
    )
    pk = models.CompositePrimaryKey("curso", "prerrequisito")

    class Meta:
        db_table = "curso_prerrequisitos"

    def __str__(self):
        return f"{self.curso_id} requiere {self.prerrequisito_id}"


class GrupoCurso(models.Model):
    grupo_id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(
        Curso,
        models.CASCADE,
        db_column="curso_id",
        related_name="grupos",
    )
    docente = models.ForeignKey(
        Docente,
        models.CASCADE,
        db_column="docente_id",
        related_name="grupos",
    )
    periodo = models.ForeignKey(
        PeriodoAcademico,
        models.CASCADE,
        db_column="periodo_id",
        related_name="grupos",
    )
    modalidad = models.CharField(max_length=30, default="Presencial")
    nombre_grupo = models.CharField(max_length=10)
    cupo_maximo = models.PositiveSmallIntegerField(default=30)

    class Meta:
        db_table = "grupos_curso"
        ordering = ["periodo", "curso", "nombre_grupo"]
        unique_together = (("curso", "periodo", "nombre_grupo"),)

    def __str__(self):
        return f"{self.curso.codigo} - {self.nombre_grupo}"


class Matricula(models.Model):
    ESTADOS = (
        ("Activa", "Activa"),
        ("Cancelada", "Cancelada"),
        ("Retirada", "Retirada"),
        ("Finalizada", "Finalizada"),
        ("Pendiente pago", "Pendiente pago"),
    )

    matricula_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="matriculas",
    )
    grupo = models.ForeignKey(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="matriculas",
    )
    periodo = models.ForeignKey(
        PeriodoAcademico,
        models.CASCADE,
        db_column="periodo_id",
        related_name="matriculas",
    )
    estado = models.CharField(max_length=30, choices=ESTADOS, default="Activa")
    fecha_matricula = models.DateTimeField(default=timezone.now)
    nota_final = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "matriculas"
        ordering = ["-fecha_matricula"]
        unique_together = (("estudiante", "grupo"),)

    def __str__(self):
        return f"{self.estudiante_id} - {self.grupo_id}"


class MatriculaHistorial(models.Model):
    historial_id = models.AutoField(primary_key=True)
    matricula = models.ForeignKey(
        Matricula,
        models.CASCADE,
        db_column="matricula_id",
        related_name="historial",
    )
    estado_nuevo = models.CharField(max_length=30)
    fecha_cambio = models.DateTimeField(default=timezone.now)
    motivo = models.TextField(blank=True, null=True)
    registrado_por = models.ForeignKey(
        Persona,
        models.CASCADE,
        db_column="registrado_por",
        blank=True,
        null=True,
        related_name="cambios_matricula",
    )

    class Meta:
        db_table = "matricula_historial"
        ordering = ["-fecha_cambio"]

    def __str__(self):
        return f"{self.matricula_id} - {self.estado_nuevo}"


class Evaluacion(models.Model):
    evaluacion_id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="evaluaciones",
    )
    tipo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    fecha_aplicacion = models.DateField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    nota_maxima = models.DecimalField(max_digits=4, decimal_places=2, default=5.00)

    class Meta:
        db_table = "evaluaciones"
        ordering = ["fecha_aplicacion", "nombre"]

    def __str__(self):
        return self.nombre


class NotaEvaluacion(models.Model):
    nota_id = models.AutoField(primary_key=True)
    evaluacion = models.ForeignKey(
        Evaluacion,
        models.CASCADE,
        db_column="evaluacion_id",
        related_name="notas",
    )
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="notas_evaluacion",
    )
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ausente = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)
    registrado_en = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "notas_evaluacion"
        ordering = ["-registrado_en"]
        unique_together = (("evaluacion", "estudiante"),)

    def __str__(self):
        return f"{self.evaluacion_id} - {self.estudiante_id}"


class CalificacionFinal(models.Model):
    cal_final_id = models.AutoField(primary_key=True)
    matricula = models.OneToOneField(
        Matricula,
        models.CASCADE,
        db_column="matricula_id",
        related_name="calificacion_final",
    )
    nota_calculada = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    nota_definitiva = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    aprobado = models.BooleanField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "calificaciones_finales"
        ordering = ["-fecha_cierre"]

    def __str__(self):
        return str(self.matricula_id)


class Aula(models.Model):
    aula_id = models.AutoField(primary_key=True)
    edificio = models.ForeignKey(
        Edificio,
        models.CASCADE,
        db_column="edificio_id",
        blank=True,
        null=True,
        related_name="aulas",
    )
    tipo = models.CharField(max_length=60, default="Salon de clase")
    nombre = models.CharField(max_length=30)
    piso = models.SmallIntegerField(blank=True, null=True)
    capacidad = models.PositiveSmallIntegerField()
    tiene_proyector = models.BooleanField(default=False)
    tiene_internet = models.BooleanField(default=False)
    activa = models.BooleanField(default=True)

    class Meta:
        db_table = "aulas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    DIAS = (
        ("Lunes", "Lunes"),
        ("Martes", "Martes"),
        ("Miércoles", "Miércoles"),
        ("Jueves", "Jueves"),
        ("Viernes", "Viernes"),
        ("Sábado", "Sábado"),
        ("Domingo", "Domingo"),
    )

    horario_id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="horarios",
    )
    aula = models.ForeignKey(
        Aula,
        models.CASCADE,
        db_column="aula_id",
        related_name="horarios",
    )
    dia = models.CharField(max_length=12, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        db_table = "horarios"
        ordering = ["dia", "hora_inicio"]
        unique_together = (("aula", "dia", "hora_inicio"),)

    def __str__(self):
        return f"{self.dia} {self.hora_inicio}-{self.hora_fin}"


class Asistencia(models.Model):
    asistencia_id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="asistencias",
    )
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="asistencias",
    )
    horario = models.ForeignKey(
        Horario,
        models.CASCADE,
        db_column="horario_id",
        related_name="asistencias",
    )
    fecha = models.DateField()
    presente = models.BooleanField(default=True)
    justificada = models.BooleanField(default=False)
    observacion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "asistencia"
        ordering = ["-fecha"]
        unique_together = (("grupo", "estudiante", "horario", "fecha"),)

    def __str__(self):
        return f"{self.estudiante_id} - {self.fecha}"


class Syllabus(models.Model):
    syllabus_id = models.AutoField(primary_key=True)
    grupo = models.OneToOneField(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="syllabus",
    )
    objetivo_general = models.TextField(blank=True, null=True)
    metodologia = models.TextField(blank=True, null=True)
    bibliografia = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "syllabus"
        ordering = ["-creado_en"]

    def __str__(self):
        return str(self.grupo_id)


class SyllabusUnidad(models.Model):
    unidad_id = models.AutoField(primary_key=True)
    syllabus = models.ForeignKey(
        Syllabus,
        models.CASCADE,
        db_column="syllabus_id",
        related_name="unidades",
    )
    numero = models.SmallIntegerField()
    titulo = models.CharField(max_length=120)
    contenido = models.TextField(blank=True, null=True)
    semanas_duracion = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = "syllabus_unidades"
        ordering = ["syllabus", "numero"]
        unique_together = (("syllabus", "numero"),)

    def __str__(self):
        return f"{self.numero}. {self.titulo}"


class Tutoria(models.Model):
    tutoria_id = models.AutoField(primary_key=True)
    docente = models.ForeignKey(
        Docente,
        models.CASCADE,
        db_column="docente_id",
        related_name="tutorias",
    )
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="tutorias",
    )
    curso = models.ForeignKey(
        Curso,
        models.CASCADE,
        db_column="curso_id",
        blank=True,
        null=True,
        related_name="tutorias",
    )
    fecha = models.DateTimeField(default=timezone.now)
    duracion_min = models.SmallIntegerField(blank=True, null=True)
    modalidad = models.CharField(max_length=30, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "tutorias"
        ordering = ["-fecha"]

    def __str__(self):
        return str(self.tutoria_id)


class MaterialCurso(models.Model):
    material_id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(
        GrupoCurso,
        models.CASCADE,
        db_column="grupo_id",
        related_name="materiales",
    )
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=40, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    publicado_en = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "materiales_curso"
        ordering = ["-publicado_en"]

    def __str__(self):
        return self.titulo


class EventoCalendario(models.Model):
    evento_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)
    aplica_todos = models.BooleanField(default=True)
    programa = models.ForeignKey(
        Programa,
        models.CASCADE,
        db_column="programa_id",
        blank=True,
        null=True,
        related_name="eventos_calendario",
    )

    class Meta:
        db_table = "eventos_calendario"
        ordering = ["fecha_inicio"]

    def __str__(self):
        return self.titulo


class BecaEstudiante(models.Model):
    beca_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="becas",
    )
    periodo = models.ForeignKey(
        PeriodoAcademico,
        models.CASCADE,
        db_column="periodo_id",
        related_name="becas",
    )
    tipo_beca = models.CharField(max_length=100)
    porcentaje_descuento = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )
    aprobado = models.BooleanField(default=False)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "becas_estudiante"
        ordering = ["estudiante", "periodo"]
        unique_together = (("estudiante", "tipo_beca", "periodo"),)

    def __str__(self):
        return self.tipo_beca


class Pago(models.Model):
    pago_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="pagos",
    )
    periodo = models.ForeignKey(
        PeriodoAcademico,
        models.CASCADE,
        db_column="periodo_id",
        related_name="pagos",
    )
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_pago = models.DateTimeField(default=timezone.now)
    metodo = models.CharField(max_length=40, blank=True, null=True)
    referencia = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=30, default="Confirmado")

    class Meta:
        db_table = "pagos"
        ordering = ["-fecha_pago"]

    def __str__(self):
        return f"{self.estudiante_id} - {self.monto}"


class Homologacion(models.Model):
    homologacion_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="homologaciones",
    )
    curso_origen = models.CharField(max_length=150)
    institucion_origen = models.CharField(max_length=150, blank=True, null=True)
    curso_destino = models.ForeignKey(
        Curso,
        models.CASCADE,
        db_column="curso_destino_id",
        blank=True,
        null=True,
        related_name="homologaciones",
    )
    nota_origen = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    aprobado = models.BooleanField(default=False)
    fecha_solicitud = models.DateField(default=date.today)
    resolucion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "homologaciones"
        ordering = ["-fecha_solicitud"]

    def __str__(self):
        return self.curso_origen


class SolicitudAcademica(models.Model):
    solicitud_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="solicitudes",
    )
    tipo = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=30, default="Pendiente")
    fecha_envio = models.DateTimeField(default=timezone.now)
    fecha_respuesta = models.DateTimeField(blank=True, null=True)
    respuesta = models.TextField(blank=True, null=True)
    atendida_por = models.ForeignKey(
        Persona,
        models.CASCADE,
        db_column="atendida_por",
        blank=True,
        null=True,
        related_name="solicitudes_atendidas",
    )

    class Meta:
        db_table = "solicitudes_academicas"
        ordering = ["-fecha_envio"]

    def __str__(self):
        return f"{self.tipo} - {self.estado}"


class Sancion(models.Model):
    sancion_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        models.CASCADE,
        db_column="estudiante_id",
        related_name="sanciones",
    )
    tipo = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(default=date.today)
    resuelto = models.BooleanField(default=False)

    class Meta:
        db_table = "sanciones"
        ordering = ["-fecha"]

    def __str__(self):
        return self.tipo


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    persona = models.OneToOneField(
        Persona,
        models.CASCADE,
        db_column="persona_id",
        related_name="usuario",
    )
    username = models.CharField(max_length=60, unique=True)
    password_hash = models.TextField()
    rol = models.CharField(max_length=30)
    ultimo_acceso = models.DateTimeField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "usuarios"
        ordering = ["username"]

    def __str__(self):
        return self.username


class Auditoria(models.Model):
    auditoria_id = models.BigAutoField(primary_key=True)
    tabla = models.CharField(max_length=80)
    operacion = models.CharField(max_length=1)
    registro_id = models.IntegerField()
    usuario = models.ForeignKey(
        Usuario,
        models.CASCADE,
        db_column="usuario_id",
        blank=True,
        null=True,
        related_name="auditorias",
    )
    datos_antes = models.JSONField(blank=True, null=True)
    datos_despues = models.JSONField(blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "auditoria"
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.tabla} {self.operacion} {self.registro_id}"

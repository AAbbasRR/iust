from django.db import models
from django.utils.translation import gettext as _

from app_user.models import UserModel

from utils import GeneralDateModel


class ApplicationManager(models.Manager):
    def find_with_tracking_id(self, tracking_id):
        return self.filter(tracking_id=tracking_id).first()


class Application(GeneralDateModel):
    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")
        ordering = ["-id"]

    class ApplicationFacultyOptions(models.TextChoices):
        Department_of_Chemistry = "Department of Chemistry", _(
            "Department of Chemistry"
        )
        Department_of_Foreign_Language = "Department of Foreign Language", _(
            "Department of Foreign Language"
        )
        School_of_Architecture_and_Environmental_Design = (
            "School of Architecture and Environmental Design",
            _("School of Architecture and Environmental Design"),
        )
        School_of_Automotive_Engineering = "School of Automotive Engineering", _(
            "School of Automotive Engineering"
        )
        School_of_Chemical_Petroleum_and_Gas_Engineering = (
            "School of Chemical Petroleum and Gas Engineering",
            _("School of Chemical Petroleum and Gas Engineering"),
        )
        School_of_Civil_Engineering = "School of Civil Engineering", _(
            "School of Civil Engineering"
        )
        School_of_Computer_Engineering = "School of Computer Engineering", _(
            "School of Computer Engineering"
        )
        School_of_Electrical_Engineering = "School of Electrical Engineering", _(
            "School of Electrical Engineering"
        )
        School_of_Industrial_Engineering = "School of Industrial Engineering", _(
            "School of Industrial Engineering"
        )
        School_of_Mathematics = "School of Mathematics", _("School of Mathematics")
        School_of_Mechanical_Engineering = "School of Mechanical Engineering", _(
            "School of Mechanical Engineering"
        )
        School_of_Metallurgy_and_Materials_Engineering = (
            "School of Metallurgy and Materials Engineering",
            _("School of Metallurgy and Materials Engineering"),
        )
        School_of_Advanced_Technologies = "School of Advanced Technologies", _(
            "School of Advanced Technologies"
        )
        School_of_Physics = "School of Physics", _("School of Physics")
        School_of_Management_Economy_and_Progress_Engineering = (
            "School of Management, Economy and Progress Engineering",
            _("School of Management, Economy and Progress Engineering"),
        )
        School_of_Railway_Engineering = "School of Railway Engineering", _(
            "School of Railway Engineering"
        )

    class ApplicationFieldOfStudyOptions(models.TextChoices):
        Architecture = "Architecture", _("Architecture")
        Industrial_Design = "Industrial Design", _("Industrial Design")
        Chemical_Engineering = "Chemical Engineering", _("Chemical Engineering")
        Civil_Engineering = "Civil Engineering", _("Civil Engineering")
        Hardware_Engineering = "Hardware Engineering", _("Hardware Engineering")
        Software_Engineering = "Software Engineering", _("Software Engineering")
        Communication_Systems = "Communication Systems", _("Communication Systems")
        Power_Systems = "Power Systems", _("Power Systems")
        Electronics = "Electronics", _("Electronics")
        Control_Systems = "Control Systems", _("Control Systems")
        Industrial_Engineering = "Industrial Engineering", _("Industrial Engineering")
        Mathematics_and_Its_Applications = "Mathematics and Its Applications", _(
            "Mathematics and Its Applications"
        )
        Mechanical_Engineering = "Mechanical Engineering", _("Mechanical Engineering")
        Material_and_Metallurgical_Engineering = (
            "Material and Metallurgical Engineering",
        )
        _("Material and Metallurgical Engineering"),
        Atomic_and_Molecular_Physics = "Atomic and Molecular Physics", _(
            "Atomic and Molecular Physics"
        )
        Solid_State_Physics = "Solid State Physics", _("Solid State Physics")
        Railway_Transportation_Engineering = "Railway Transportation Engineering", _(
            "Railway Transportation Engineering"
        )
        Railway_Rolling_Stock_Engineering = "Railway Rolling Stock Engineering", _(
            "Railway Rolling Stock Engineering"
        )
        Railway_Track_and_Structures_Engineering = (
            "Railway Track and Structures Engineering",
            _("Railway Track and Structures Engineering"),
        )
        Analytical_Chemistry = "Analytical Chemistry", _("Analytical Chemistry")
        Inorganic_Chemistry = "Inorganic Chemistry", _("Inorganic Chemistry")
        Organic_Chemistry = "Organic Chemistry", _("Organic Chemistry")
        Physical_Chemistry = "Physical Chemistry", _("Physical Chemistry")
        Nano_Chemistry = "Nano-Chemistry", _("Nano-Chemistry")
        Teaching_English_as_a_Foreign_Language = (
            "Teaching English as a Foreign Language",
        )
        _("Teaching English as a Foreign Language"),
        Regional_Planning = "Regional Planning", _("Regional Planning")
        Architecture_Housing = "Architecture - Housing", _("Architecture - Housing")
        Architecture_Sustainable = "Architecture - Sustainable", _(
            "Architecture - Sustainable"
        )
        Architecture_Technology = "Architecture - Technology", _(
            "Architecture - Technology"
        )
        Architecture_Cultural_and_Educational_Spaces = (
            "Architecture - Cultural and Educational Spaces",
        )
        _("Architecture - Cultural and Educational Spaces"),
        Architecture_Health_Care_Spaces = "Architecture - Health Care Spaces", _(
            "Architecture - Health Care Spaces"
        )
        Land_Spaces_Architecture = "Land Spaces Architecture", _(
            "Land Spaces Architecture"
        )
        Conservation_and_Restoration_of_Historical_Buildings_and_Fabrics_Conservation_and_Restoration_of_Urban_Heritage = (
            "Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Urban Heritage",
        )
        _(
            "Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Urban Heritage"
        ),
        Conservation_and_Restoration_of_Historical_Buildings_and_Fabrics_Conservation_and_Restoration_of_Architectural_Heritage = (
            "Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Architectural Heritage",
        )
        _(
            "Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Architectural Heritage"
        ),
        Urban_Design = "Urban Design", _("Urban Design")
        Urban_Planning = "Urban Planning", _("Urban Planning")
        Automotive_Engineering_Automobile_Dynamic_Systems_Design = (
            "Automotive Engineering - Automobile Dynamic Systems Design",
        )
        _("Automotive Engineering - Automobile Dynamic Systems Design"),
        Automotive_Engineering_Power_Train = "Automotive Engineering - Power Train", _(
            "Automotive Engineering - Power Train"
        )
        Automotive_Engineering_Body_and_Structure = (
            "Automotive Engineering - Body and Structure",
        )
        _("Automotive Engineering - Body and Structure"),
        Automotive_Engineering_Automotive_Electronics_Electrical_Engineering = (
            "Automotive Engineering - Automotive Electronics & Electrical Engineering",
        )
        _("Automotive Engineering - Automotive Electronics & Electrical Engineering"),
        Process_Modeling_Simulation_Control = ("Process Modeling Simulation & Control",)
        _("Process Modeling Simulation & Control"),
        Mineral_Chemical_Engineering = "Mineral_Chemical_Engineering", _(
            "Mineral Chemical Engineering"
        )
        Separation_Processes = "Separation Processes", _("Separation Processes")
        Kinetic_and_Catalysis = "Kinetic and Catalysis", _("Kinetic and Catalysis")
        Thermodynamics = "Thermodynamics", _("Thermodynamics")
        Polymer_Engineering = "Polymer Engineering", _("Polymer Engineering")
        Hydrocarbon_Reservoir_Engineering = "Hydrocarbon Reservoir Engineering", _(
            "Hydrocarbon Reservoir Engineering"
        )
        Process_Design_Engineering = "Process Design Engineering", _(
            "Process Design Engineering"
        )
        Structural_Engineering = "Structural Engineering", _("Structural Engineering")
        Earthquake_Engineering = "Earthquake Engineering", _("Earthquake Engineering")
        Construction_Management_and_Engineering = (
            "Construction Management and Engineering",
        )
        _("Construction Management and Engineering"),
        Geotechnical_Engineering = "Geotechnical Engineering", _(
            "Geotechnical Engineering"
        )
        Road_and_Transportation_Engineering = "Road and Transportation Engineering", _(
            "Road and Transportation Engineering"
        )
        Transportation = "Transportation", _("Transportation")
        Water_Resources_Management = "Water Resources Management", _(
            "Water Resources Management"
        )
        Water_Engineering_and_Hydraulic_Structures = (
            "Water Engineering and Hydraulic Structures",
        )
        _("Water Engineering and Hydraulic Structures"),
        Environmental_Engineering = "Environmental Engineering", _(
            "Environmental Engineering"
        )
        Marine_Structures_Engineering = "Marine Structures Engineering", _(
            "Marine Structures Engineering"
        )
        Artificial_Intelligence_Robotics = "Artificial Intelligence & Robotics", _(
            "Artificial Intelligence & Robotics"
        )
        Computer_Systems_Architecture = "Computer Systems Architecture", _(
            "Computer Systems Architecture"
        )
        Computer_Engineering_Computer_Networks = (
            "Computer Engineering - Computer Networks",
            _("Computer Engineering - Computer Networks"),
        )
        Bio_Electrics = "Bio-Electrics", _("Bio-Electrics")
        Digital_Electronic_Systems = "Digital Electronic Systems", _(
            "Digital Electronic Systems"
        )
        Electronic_Integrated_Circuits = "Electronic Integrated Circuits", _(
            "Electronic Integrated Circuits"
        )
        Electrical_Machines_and_Power_Electronics = (
            "Electrical Machines and Power Electronics",
        )
        _("Electrical Machines and Power Electronics"),
        Electromagnetic_Fields_and_Waves = "Electromagnetic Fields and Waves", _(
            "Electromagnetic Fields and Waves"
        )
        Information_Technology_Engineering_Electronic_Commerce = (
            "Information Technology Engineering - Electronic Commerce",
            _("Information Technology Engineering - Electronic Commerce"),
        )
        Systems_Optimization = "Systems Optimization", _("Systems Optimization")
        Supply_Chain_and_Logistic_Engineering = (
            "Supply Chain and Logistic Engineering",
            _("Supply Chain and Logistic Engineering"),
        )
        Engineering_Management = "Engineering Management", _("Engineering Management")
        Socio_Economic_Macro_Systems = "Socio-Economic Macro Systems", _(
            "Socio-Economic Macro Systems"
        )
        Project_Management = "Project Management", _("Project Management")
        Financial_Engineering = "Financial Engineering", _("Financial Engineering")
        Pure_Mathematics_Algebra = "Pure Mathematics - Algebra", _(
            "Pure Mathematics - Algebra"
        )
        Pure_Mathematics_Geometry = "Pure Mathematics - Geometry", _(
            "Pure Mathematics - Geometry"
        )
        Pure_Mathematics_Analysis = "Pure Mathematics - Analysis", _(
            "Pure Mathematics - Analysis"
        )
        Applied_Mathematics_Numerical_Analysis = (
            "Applied Mathematics - Numerical Analysis",
        )
        _("Applied Mathematics - Numerical Analysis"),
        Applied_Mathematics_Operation_Research = (
            "Applied Mathematics - Operation Research",
        )
        _("Applied Mathematics - Operation Research"),
        Mathematics_Statistics = "Mathematics Statistics", _("Mathematics Statistics")
        Applied_Design = "Applied Design", _("Applied Design")
        Energy_Conversion = "Energy Conversion", _("Energy Conversion")
        Manufacturing = "Manufacturing", _("Manufacturing")
        Biomechanics = "Biomechanics", _("Biomechanics")
        Extractive_Metallurgy = "Extractive Metallurgy", _("Extractive Metallurgy")
        Ceramics_Engineering = "Ceramics Engineering", _("Ceramics Engineering")
        Materials_Selection = "Materials Selection", _("Materials Selection")
        Bio_Materials = "Bio-Materials", _("Bio-Materials")
        Metals_Casting = "Metals Casting", _("Metals Casting")
        Metals_Forming = "Metals Forming", _("Metals Forming")
        Nanotechnology = "Nanotechnology - Materials", _("Nanotechnology - Materials")
        Energy_Systems_Energy_and_Environment = (
            "Energy Systems - Energy and Environment|",
            _("Energy Systems - Energy and Environment|"),
        )
        Satellite_Engineering = "Satellite Engineering", _("Satellite Engineering")
        Photonics = "Photonics", _("Photonics")
        Condensed_Matter_Physics = "Condensed Matter Physics", _(
            "Condensed Matter Physics"
        )
        Laser_Optics_Physics = "Laser Optics Physics", _("Laser Optics Physics")
        Master_of_Business_Administration_MBA_Marketing = (
            "Master of Business Administration (MBA) - Marketing",
            _("Master of Business Administration (MBA) - Marketing"),
        )
        Master_of_Business_Administration_MBA_Strategy = (
            "Master of Business Administration (MBA) - Strategy",
            _("Master of Business Administration (MBA) - Strategy"),
        )
        Management_of_Technology_MOT_Technological_Innovation = (
            "Management of Technology (MOT) - Technological Innovation",
            _("Management of Technology (MOT) - Technological Innovation"),
        )
        Management_of_Technology_MOT_Technological_Transfer = (
            "Management of Technology (MOT) - Technological Transfer",
            _("Management of Technology (MOT) - Technological Transfer"),
        )
        Management_of_Technology_MOT_Research_Development_Policies = (
            "Management of Technology (MOT) - Research & Development Policies",
            _("Management of Technology (MOT) - Research & Development Policies"),
        )
        Information_Technology_Management_E_Business = (
            "Information Technology Management-E-Business",
            _("Information Technology Management-E-Business"),
        )
        Entrepreneurship_New_Businesses = "Entrepreneurship - New Businesses", _(
            "Entrepreneurship - New Businesses"
        )
        Industrial_Engineering_Macro_Systems = (
            "Industrial Engineering - Macro Systems",
            _("Industrial Engineering - Macro Systems"),
        )
        Economic_Development_and_Planning = "Economic Development and Planning", _(
            "Economic Development and Planning"
        )
        Economic_Systems_Planning = "Economic Systems Planning", _(
            "Economic Systems Planning"
        )
        Electric_Railways_Engineering = "Electric Railways Engineering", _(
            "Electric Railways Engineering"
        )
        Railway_Safety_Engineering = "Railway Safety Engineering", _(
            "Railway Safety Engineering"
        )
        Railway_Control_and_Signaling = "Railway Control and Signaling", _(
            "Railway Control and Signaling"
        )
        Urbanism = "Urbanism", _("Urbanism")
        Quality_Productivity = "Quality & Productivity", _("Quality & Productivity")
        Applied_Mathematics__Statistics = "Applied Mathematics - Statistics", _(
            "Applied Mathematics - Statistics"
        )
        Dynamics_Control_and_Vibration = "Dynamics Control and Vibration", _(
            "Dynamics Control and Vibration"
        )
        Solid_Mechanics = "Solid Mechanics", _("Solid Mechanics")
        Materials_Engineering = "Materials Engineering", _("Materials Engineering")
        Management_of_Iranian_Public_Organization = (
            "Management of Iranian Public Organization",
            _("Management of Iranian Public Organization"),
        )
        Science_of_Technology_Policy = "Science of Technology Policy", _(
            "Science of Technology Policy"
        )

    class ApplicationStatusOptions(models.TextChoices):
        Not_Completed = "Not_Completed", _("Not Completed")
        Current = "Current", _("Current")
        Accepted = "Accepted", _("Accepted")
        Rejected = "Rejected", _("Rejected")
        NeedToEdit = "Need_To_Edit", _("Need To Edit")

    class ApplicationDegreeOptions(models.TextChoices):
        Bachelor = "Bachelor", _("Bachelor")
        Master = "Master", _("Master")
        PHD = "P.H.D", _("P.H.D")

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_application",
        verbose_name=_("User"),
    )
    tracking_id = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("Tracking ID"),
    )
    full_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Full Name")
    )
    comments = models.TextField(null=True, blank=True, verbose_name=_("Comments"))
    applied_program = models.BooleanField(
        null=True, blank=True, verbose_name=_("Applied Program")
    )
    financial_self_support = models.BooleanField(
        null=True, blank=True, verbose_name=_("Financial Self Support")
    )
    status = models.CharField(
        max_length=13,
        choices=ApplicationStatusOptions.choices,
        default=ApplicationStatusOptions.Not_Completed,
        verbose_name=_("Status"),
    )
    degree = models.CharField(
        max_length=8,
        choices=ApplicationDegreeOptions.choices,
        default=ApplicationDegreeOptions.Bachelor,
        verbose_name=_("Degree"),
    )
    faculty = models.CharField(
        max_length=80,
        choices=ApplicationFacultyOptions.choices,
        verbose_name=_("Faculty"),
    )
    field_of_study = models.CharField(
        max_length=150,
        choices=ApplicationFieldOfStudyOptions.choices,
        verbose_name=_("Field Of Study"),
    )
    step = models.IntegerField(default=3, verbose_name=_("step"))

    objects = ApplicationManager()

    def __str__(self):
        return self.tracking_id

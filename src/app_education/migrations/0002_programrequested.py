# Generated by Django 4.1.5 on 2023-03-03 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_application', '0010_alter_application_tracking_id'),
        ('app_education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramRequested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('degree', models.CharField(choices=[('Bachelor', 'Bachelor'), ('Master', 'Master'), ('P.H.D', 'P.H.D')], max_length=8, verbose_name='Degree')),
                ('faculty', models.CharField(choices=[('School of Architecture and Environmental Design', 'School of Architecture and Environmental Design'), ('School of Chemical Petroleum and Gas Engineering', 'School of Chemical Petroleum and Gas Engineering'), ('School of Civil Engineering', 'School of Civil Engineering'), ('School of Computer Engineering', 'School of Computer Engineering'), ('School of Electrical Engineering', 'School of Electrical Engineering'), ('School of Industrial Engineering', 'School of Industrial Engineering'), ('School of Mathematics', 'School of Mathematics'), ('School of Mechanical Engineering', 'School of Mechanical Engineering'), ('School of Metallurgy and Materials Engineering', 'School of Metallurgy and Materials Engineering'), ('School of Physics', 'School of Physics'), ('School of Railway Engineering', 'School of Railway Engineering'), ('Department of Chemistry', 'Department of Chemistry'), ('Department of Foreign Language', 'Department of Foreign Language'), ('School of Automotive Engineering', 'School of Automotive Engineering'), ('School of Advanced Technologies', 'School of Advanced Technologies'), ('School of Management, Economy and Progress Engineering', 'School of Management, Economy and Progress Engineering')], max_length=80, verbose_name='Faculty')),
                ('field_of_study', models.CharField(choices=[('Architecture', 'Architecture'), ('Industrial Design', 'Industrial Design'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Hardware Engineering', 'Hardware Engineering'), ('Software Engineering', 'Software Engineering'), ('Communication Systems', 'Communication Systems'), ('Power Systems', 'Power Systems'), ('Electronics', 'Electronics'), ('Control Systems', 'Control Systems'), ('Industrial Engineering', 'Industrial Engineering'), ('Mathematics and Its Applications', 'Mathematics and Its Applications'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Material and Metallurgical Engineering', 'Material and Metallurgical Engineering'), ('Atomic and Molecular Physics', 'Atomic and Molecular Physics'), ('Solid State Physics', 'Solid State Physics'), ('Railway Transportation Engineering', 'Railway Transportation Engineering'), ('Railway Rolling Stock Engineering', 'Railway Rolling Stock Engineering'), ('Railway Track and Structures Engineering', 'Railway Track and Structures Engineering'), ('Analytical Chemistry', 'Analytical Chemistry'), ('Inorganic Chemistry', 'Inorganic Chemistry'), ('Organic Chemistry', 'Organic Chemistry'), ('Physical Chemistry', 'Physical Chemistry'), ('Nano-Chemistry', 'Nano-Chemistry'), ('Teaching English as a Foreign Language', 'Teaching English as a Foreign Language'), ('Regional Planning', 'Regional Planning'), ('Architecture - Housing', 'Architecture - Housing'), ('Architecture - Sustainable', 'Architecture - Sustainable'), ('Architecture - Technology', 'Architecture - Technology'), ('Architecture - Cultural and Educational Spaces', 'Architecture - Cultural and Educational Spaces'), ('Architecture - Health Care Spaces', 'Architecture - Health Care Spaces'), ('Land Spaces Architecture', 'Land Spaces Architecture'), ('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Urban Heritage', 'Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Urban Heritage'), ('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Architectural Heritage', 'Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Architectural Heritage'), ('Urban Design', 'Urban Design'), ('Urban Planning', 'Urban Planning'), ('Automotive Engineering - Automobile Dynamic Systems Design', 'Automotive Engineering - Automobile Dynamic Systems Design'), ('Automotive Engineering - Power Train', 'Automotive Engineering - Power Train'), ('Automotive Engineering - Body and Structure', 'Automotive Engineering - Body and Structure'), ('Automotive Engineering - Automotive Electronics & Electrical Engineering', 'Automotive Engineering - Automotive Electronics & Electrical Engineering'), ('Process Modeling Simulation & Control', 'Process Modeling Simulation & Control'), ('Mineral Chemical Engineering', 'Mineral Chemical Engineering'), ('Separation Processes', 'Separation Processes'), ('Kinetic and Catalysis', 'Kinetic and Catalysis'), ('Thermodynamics', 'Thermodynamics'), ('Polymer Engineering', 'Polymer Engineering'), ('Hydrocarbon Reservoir Engineering', 'Hydrocarbon Reservoir Engineering'), ('Process Design Engineering', 'Process Design Engineering'), ('Structural Engineering', 'Structural Engineering'), ('Earthquake Engineering', 'Earthquake Engineering'), ('Construction Management and Engineering', 'Construction Management and Engineering'), ('Geotechnical Engineering', 'Geotechnical Engineering'), ('Road and Transportation Engineering', 'Road and Transportation Engineering'), ('Transportation', 'Transportation'), ('Water Resources Management', 'Water Resources Management'), ('Water Engineering and Hydraulic Structures', 'Water Engineering and Hydraulic Structures'), ('Environmental Engineering', 'Environmental Engineering'), ('Marine Structures Engineering', 'Marine Structures Engineering'), ('Artificial Intelligence & Robotics', 'Artificial Intelligence & Robotics'), ('Computer Systems Architecture', 'Computer Systems Architecture'), ('Computer Engineering - Computer Networks', 'Computer Engineering - Computer Networks'), ('Bio-Electrics', 'Bio-Electrics'), ('Digital Electronic Systems', 'Digital Electronic Systems'), ('Electronic Integrated Circuits', 'Electronic Integrated Circuits'), ('Electrical Machines and Power Electronics', 'Electrical Machines and Power Electronics'), ('Electromagnetic Fields and Waves', 'Electromagnetic Fields and Waves'), ('Information Technology Engineering - Electronic Commerce', 'Information Technology Engineering - Electronic Commerce'), ('Systems Optimization', 'Systems Optimization'), ('Supply Chain and Logistic Engineering', 'Supply Chain and Logistic Engineering'), ('Engineering Management', 'Engineering Management'), ('Socio-Economic Macro Systems', 'Socio-Economic Macro Systems'), ('Project Management', 'Project Management'), ('Financial Engineering', 'Financial Engineering'), ('Pure Mathematics - Algebra', 'Pure Mathematics - Algebra'), ('Pure Mathematics - Geometry', 'Pure Mathematics - Geometry'), ('Pure Mathematics - Analysis', 'Pure Mathematics - Analysis'), ('Applied Mathematics - Numerical Analysis', 'Applied Mathematics - Numerical Analysis'), ('Applied Mathematics - Operation Research', 'Applied Mathematics - Operation Research'), ('Mathematics Statistics', 'Mathematics Statistics'), ('Applied Design', 'Applied Design'), ('Energy Conversion', 'Energy Conversion'), ('Manufacturing', 'Manufacturing'), ('Biomechanics', 'Biomechanics'), ('Extractive Metallurgy', 'Extractive Metallurgy'), ('Ceramics Engineering', 'Ceramics Engineering'), ('Materials Selection', 'Materials Selection'), ('Bio-Materials', 'Bio-Materials'), ('Metals Casting', 'Metals Casting'), ('Metals Forming', 'Metals Forming'), ('Nanotechnology - Materials', 'Nanotechnology - Materials'), ('Energy Systems - Energy and Environment|', 'Energy Systems - Energy and Environment|'), ('Satellite Engineering', 'Satellite Engineering'), ('Photonics', 'Photonics'), ('Condensed Matter Physics', 'Condensed Matter Physics'), ('Laser Optics Physics', 'Laser Optics Physics'), ('Master of Business Administration (MBA) - Marketing', 'Master of Business Administration (MBA) - Marketing'), ('Master of Business Administration (MBA) - Strategy', 'Master of Business Administration (MBA) - Strategy'), ('Management of Technology (MOT) - Technological Innovation', 'Management of Technology (MOT) - Technological Innovation'), ('Management of Technology (MOT) - Technological Transfer', 'Management of Technology (MOT) - Technological Transfer'), ('Management of Technology (MOT) - Research & Development Policies', 'Management of Technology (MOT) - Research & Development Policies'), ('Information Technology Management-E-Business', 'Information Technology Management-E-Business'), ('Entrepreneurship - New Businesses', 'Entrepreneurship - New Businesses'), ('Industrial Engineering - Macro Systems', 'Industrial Engineering - Macro Systems'), ('Economic Development and Planning', 'Economic Development and Planning'), ('Economic Systems Planning', 'Economic Systems Planning'), ('Electric Railways Engineering', 'Electric Railways Engineering'), ('Railway Safety Engineering', 'Railway Safety Engineering'), ('Railway Control and Signaling', 'Railway Control and Signaling'), ('Urbanism', 'Urbanism'), ('Quality & Productivity', 'Quality & Productivity'), ('Applied Mathematics - Statistics', 'Applied Mathematics - Statistics'), ('Dynamics Control and Vibration', 'Dynamics Control and Vibration'), ('Solid Mechanics', 'Solid Mechanics'), ('Materials Engineering', 'Materials Engineering'), ('Management of Iranian Public Organization', 'Management of Iranian Public Organization'), ('Science of Technology Policy', 'Science of Technology Policy')], max_length=150, verbose_name='Field Of Study')),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='application_program_requested', to='app_application.application', verbose_name='application')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

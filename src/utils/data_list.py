from django.utils.translation import gettext as _

notification_status_options = [
    ('INFO', _('Information')),
    ('SUCS', _('Success')),
    ('WARN', _('Warning')),
    ('EROR', _('Error')),
]

ticket_status_choices = [
    ('AWF', _('Waiting For An Answer')),
    ('ABA', _('Has Been Answered')),
    ('CLS', _('Closed')),
]

ticket_priority_choices = [
    ('LOW', _('LOW')),
    ('MED', _('Medium')),
    ('HIG', _('High')),
]

application_timeline_status_options = [
    ('CONF', _('Confirmation')),
    ('REJC', _('Rejection')),
    ('NFIN', _('Investigation')),
]

gender_options = [
    ('MAL', _('Male')),
    ('FML', _('FeMale')),
    ('OTR', _('Other'))
]
language_status_options = [
    ('WEK', _('Weak')),
    ('GOD', _('Good')),
    ('EXT', _('Excellent'))
]

application_status_options = [
    ('CRNT', _('Current')),
    ('ACPT', _('Accepted')),
    ('RJCT', _('Rejected')),
    ('NTET', _('NeedToEdit'))
]

occupation_options = [
    ('OTR', _('Other')),
    ('ACD', _('Academician')),
    ('GVE', _('Government Employee')),
    ('INE', _('Industrial Employee')),
    ('STU', _('Student')),
]

degree_options = [
    ('Bachelor', _('Bachelor')),
    ('Master', _('Master')),
    ('P.H.D', _('P.H.D'))
]

faculty_options = [
    ('School of Architecture and Environmental Design', _('School of Architecture and Environmental Design')),
    ('School of Chemical Petroleum and Gas Engineering', _('School of Chemical Petroleum and Gas Engineering')),
    ('School of Civil Engineering', _('School of Civil Engineering')),
    ('School of Computer Engineering', _('School of Computer Engineering')),
    ('School of Electrical Engineering', _('School of Electrical Engineering')),
    ('School of Industrial Engineering', _('School of Industrial Engineering')),
    ('School of Mathematics', _('School of Mathematics')),
    ('School of Mechanical Engineering', _('School of Mechanical Engineering')),
    ('School of Metallurgy and Materials Engineering', _('School of Metallurgy and Materials Engineering')),
    ('School of Physics', _('School of Physics')),
    ('School of Railway Engineering', _('School of Railway Engineering')),
    ('Department of Chemistry', _('Department of Chemistry')),
    ('Department of Foreign Language', _('Department of Foreign Language')),
    ('School of Automotive Engineering', _('School of Automotive Engineering')),
    ('School of Advanced Technologies', _('School of Advanced Technologies')),
    ('School of Management, Economy and Progress Engineering', _('School of Management, Economy and Progress Engineering')),
]

field_of_study_options = [
    ('Architecture', _('Architecture')),
    ('Industrial Design', _('Industrial Design')),
    ('Chemical Engineering', _('Chemical Engineering')),
    ('Civil Engineering', _('Civil Engineering')),
    ('Hardware Engineering', _('Hardware Engineering')),
    ('Software Engineering', _('Software Engineering')),
    ('Communication Systems', _('Communication Systems')),
    ('Power Systems', _('Power Systems')),
    ('Electronics', _('Electronics')),
    ('Control Systems', _('Control Systems')),
    ('Industrial Engineering', _('Industrial Engineering')),
    ('Mathematics and Its Applications', _('Mathematics and Its Applications')),
    ('Mechanical Engineering', _('Mechanical Engineering')),
    ('Material and Metallurgical Engineering', _('Material and Metallurgical Engineering')),
    ('Atomic and Molecular Physics', _('Atomic and Molecular Physics')),
    ('Solid State Physics', _('Solid State Physics')),
    ('Railway Transportation Engineering', _('Railway Transportation Engineering')),
    ('Railway Rolling Stock Engineering', _('Railway Rolling Stock Engineering')),
    ('Railway Track and Structures Engineering', _('Railway Track and Structures Engineering')),
    ('Analytical Chemistry', _('Analytical Chemistry')),
    ('Inorganic Chemistry', _('Inorganic Chemistry')),
    ('Organic Chemistry', _('Organic Chemistry')),
    ('Physical Chemistry', _('Physical Chemistry')),
    ('Nano-Chemistry', _('Nano-Chemistry')),
    ('Teaching English as a Foreign Language', _('Teaching English as a Foreign Language')),
    ('Regional Planning', _('Regional Planning')),
    ('Architecture - Housing', _('Architecture - Housing')),
    ('Architecture - Sustainable', _('Architecture - Sustainable')),
    ('Architecture - Technology', _('Architecture - Technology')),
    ('Architecture - Cultural and Educational Spaces', _('Architecture - Cultural and Educational Spaces')),
    ('Architecture - Health Care Spaces', _('Architecture - Health Care Spaces')),
    ('Land Spaces Architecture', _('Land Spaces Architecture')),
    ('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Urban Heritage', _('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Urban Heritage')),
    ('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Architectural Heritage', _('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Architectural Heritage')),
    ('Urban Design', _('Urban Design')),
    ('Urban Planning', _('Urban Planning')),
    ('Automotive Engineering - Automobile Dynamic Systems Design', _('Automotive Engineering - Automobile Dynamic Systems Design')),
    ('Automotive Engineering - Power Train', _('Automotive Engineering - Power Train')),
    ('Automotive Engineering - Body and Structure', _('Automotive Engineering - Body and Structure')),
    ('Automotive Engineering - Automotive Electronics & Electrical Engineering', _('Automotive Engineering - Automotive Electronics & Electrical Engineering')),
    ('Process Modeling Simulation & Control', _('Process Modeling Simulation & Control')),
    ('Mineral Chemical Engineering', _('Mineral Chemical Engineering')),
    ('Separation Processes', _('Separation Processes')),
    ('Kinetic and Catalysis', _('Kinetic and Catalysis')),
    ('Thermodynamics', _('Thermodynamics')),
    ('Polymer Engineering', _('Polymer Engineering')),
    ('Hydrocarbon Reservoir Engineering', _('Hydrocarbon Reservoir Engineering')),
    ('Process Design Engineering', _('Process Design Engineering')),
    ('Structural Engineering', _('Structural Engineering')),
    ('Earthquake Engineering', _('Earthquake Engineering')),
    ('Construction Management and Engineering', _('Construction Management and Engineering')),
    ('Geotechnical Engineering', _('Geotechnical Engineering')),
    ('Road and Transportation Engineering', _('Road and Transportation Engineering')),
    ('Transportation', _('Transportation')),
    ('Water Resources Management', _('Water Resources Management')),
    ('Water Engineering and Hydraulic Structures', _('Water Engineering and Hydraulic Structures')),
    ('Environmental Engineering', _('Environmental Engineering')),
    ('Marine Structures Engineering', _('Marine Structures Engineering')),
    ('Artificial Intelligence & Robotics', _('Artificial Intelligence & Robotics')),
    ('Computer Systems Architecture', _('Computer Systems Architecture')),
    ('Computer Engineering - Computer Networks', _('Computer Engineering - Computer Networks')),
    ('Bio-Electrics', _('Bio-Electrics')),
    ('Digital Electronic Systems', _('Digital Electronic Systems')),
    ('Electronic Integrated Circuits', _('Electronic Integrated Circuits')),
    ('Electrical Machines and Power Electronics', _('Electrical Machines and Power Electronics')),
    ('Electromagnetic Fields and Waves', _('Electromagnetic Fields and Waves')),
    ('Information Technology Engineering - Electronic Commerce', _('Information Technology Engineering - Electronic Commerce')),
    ('Systems Optimization', _('Systems Optimization')),
    ('Supply Chain and Logistic Engineering', _('Supply Chain and Logistic Engineering')),
    ('Engineering Management', _('Engineering Management')),
    ('Socio-Economic Macro Systems', _('Socio-Economic Macro Systems')),
    ('Project Management', _('Project Management')),
    ('Financial Engineering', _('Financial Engineering')),
    ('Pure Mathematics - Algebra', _('Pure Mathematics - Algebra')),
    ('Pure Mathematics - Geometry', _('Pure Mathematics - Geometry')),
    ('Pure Mathematics - Analysis', _('Pure Mathematics - Analysis')),
    ('Applied Mathematics - Numerical Analysis', _('Applied Mathematics - Numerical Analysis')),
    ('Applied Mathematics - Operation Research', _('Applied Mathematics - Operation Research')),
    ('Mathematics Statistics', _('Mathematics Statistics')),
    ('Applied Design', _('Applied Design')),
    ('Energy Conversion', _('Energy Conversion')),
    ('Manufacturing', _('Manufacturing')),
    ('Biomechanics', _('Biomechanics')),
    ('Extractive Metallurgy', _('Extractive Metallurgy')),
    ('Ceramics Engineering', _('Ceramics Engineering')),
    ('Materials Selection', _('Materials Selection')),
    ('Bio-Materials', _('Bio-Materials')),
    ('Metals Casting', _('Metals Casting')),
    ('Metals Forming', _('Metals Forming')),
    ('Nanotechnology - Materials', _('Nanotechnology - Materials')),
    ('Energy Systems - Energy and Environment|', _('Energy Systems - Energy and Environment|')),
    ('Satellite Engineering', _('Satellite Engineering')),
    ('Photonics', _('Photonics')),
    ('Condensed Matter Physics', _('Condensed Matter Physics')),
    ('Laser Optics Physics', _('Laser Optics Physics')),
    ('Master of Business Administration (MBA) - Marketing', _('Master of Business Administration (MBA) - Marketing')),
    ('Master of Business Administration (MBA) - Strategy', _('Master of Business Administration (MBA) - Strategy')),
    ('Management of Technology (MOT) - Technological Innovation', _('Management of Technology (MOT) - Technological Innovation')),
    ('Management of Technology (MOT) - Technological Transfer', _('Management of Technology (MOT) - Technological Transfer')),
    ('Management of Technology (MOT) - Research & Development Policies', _('Management of Technology (MOT) - Research & Development Policies')),
    ('Information Technology Management-E-Business', _('Information Technology Management-E-Business')),
    ('Entrepreneurship - New Businesses', _('Entrepreneurship - New Businesses')),
    ('Industrial Engineering - Macro Systems', _('Industrial Engineering - Macro Systems')),
    ('Economic Development and Planning', _('Economic Development and Planning')),
    ('Economic Systems Planning', _('Economic Systems Planning')),
    ('Electric Railways Engineering', _('Electric Railways Engineering')),
    ('Railway Safety Engineering', _('Railway Safety Engineering')),
    ('Railway Control and Signaling', _('Railway Control and Signaling')),
    ('Urbanism', _('Urbanism')),
    ('Quality & Productivity', _('Quality & Productivity')),
    ('Applied Mathematics - Statistics', _('Applied Mathematics - Statistics')),
    ('Dynamics Control and Vibration', _('Dynamics Control and Vibration')),
    ('Solid Mechanics', _('Solid Mechanics')),
    ('Materials Engineering', _('Materials Engineering')),
    ('Management of Iranian Public Organization', _('Management of Iranian Public Organization')),
    ('Science of Technology Policy', _('Science of Technology Policy')),
]

program_requested_data = {
    'Bachelor': {
        'items': [
            ('School of Architecture and Environmental Design', _('School of Architecture and Environmental Design')),
            ('School of Chemical Petroleum and Gas Engineering', _('School of Chemical Petroleum and Gas Engineering')),
            ('School of Civil Engineering', _('School of Civil Engineering')),
            ('School of Computer Engineering', _('School of Computer Engineering')),
            ('School of Electrical Engineering', _('School of Electrical Engineering')),
            ('School of Industrial Engineering', _('School of Industrial Engineering')),
            ('School of Mathematics', _('School of Mathematics')),
            ('School of Mechanical Engineering', _('School of Mechanical Engineering')),
            ('School of Metallurgy and Materials Engineering', _('School of Metallurgy and Materials Engineering')),
            ('School of Physics', _('School of Physics')),
            ('School of Railway Engineering', _('School of Railway Engineering')),
        ],
        'data': {
            'School of Architecture and Environmental Design': [
                ('Architecture', _('Architecture')),
                ('Industrial Design', _('Industrial Design')),
            ],
            'School of Chemical Petroleum and Gas Engineering': [
                ('Chemical Engineering', _('Chemical Engineering')),
            ],
            'School of Civil Engineering': [
                ('Civil Engineering', _('Civil Engineering')),
            ],
            'School of Computer Engineering': [
                ('Hardware Engineering', _('Hardware Engineering')),
                ('Software Engineering', _('Software Engineering')),
            ],
            'School of Electrical Engineering': [
                ('Communication Systems', _('Communication Systems')),
                ('Power Systems', _('Power Systems')),
                ('Electronics', _('Electronics')),
                ('Control Systems', _('Control Systems')),
            ],
            'School of Industrial Engineering': [
                ('Industrial Engineering', _('Industrial Engineering')),
            ],
            'School of Mathematics': [
                ('Mathematics and Its Applications', _('Mathematics and Its Applications')),
            ],
            'School of Mechanical Engineering': [
                ('Mechanical Engineering', _('Mechanical Engineering')),
            ],
            'School of Metallurgy and Materials Engineering': [
                ('Material and Metallurgical Engineering', _('Material and Metallurgical Engineering')),
            ],
            'School of Physics': [
                ('Atomic and Molecular Physics', _('Atomic and Molecular Physics')),
                ('Solid State Physics', _('Solid State Physics')),
            ],
            'School of Railway Engineering': [
                ('Railway Transportation Engineering', _('Railway Transportation Engineering')),
                ('Railway Rolling Stock Engineering', _('Railway Rolling Stock Engineering')),
                ('Railway Track and Structures Engineering', _('Railway Track and Structures Engineering')),
            ],
        }
    },
    'Master': {
        'items': [
            ('Department of Chemistry', _('Department of Chemistry')),
            ('Department of Foreign Language', _('Department of Foreign Language')),
            ('School of Architecture and Environmental Design', _('School of Architecture and Environmental Design')),
            ('School of Automotive Engineering', _('School of Automotive Engineering')),
            ('School of Chemical Petroleum and Gas Engineering', _('School of Chemical Petroleum and Gas Engineering')),
            ('School of Civil Engineering', _('School of Civil Engineering')),
            ('School of Computer Engineering', _('School of Computer Engineering')),
            ('School of Electrical Engineering', _('School of Electrical Engineering')),
            ('School of Industrial Engineering', _('School of Industrial Engineering')),
            ('School of Mathematics', _('School of Mathematics')),
            ('School of Mechanical Engineering', _('School of Mechanical Engineering')),
            ('School of Metallurgy and Materials Engineering', _('School of Metallurgy and Materials Engineering')),
            ('School of Advanced Technologies', _('School of Advanced Technologies')),
            ('School of Physics', _('School of Physics')),
            ('School of Management, Economy and Progress Engineering', _('School of Management, Economy and Progress Engineering')),
            ('School of Railway Engineering', _('School of Railway Engineering')),
        ],
        'data': {
            'Department of Chemistry': [
                ('Analytical Chemistry', _('Analytical Chemistry')),
                ('Inorganic Chemistry', _('Inorganic Chemistry')),
                ('Organic Chemistry', _('Organic Chemistry')),
                ('Physical Chemistry', _('Physical Chemistry')),
                ('Nano-Chemistry', _('Nano-Chemistry')),
            ],
            'Department of Foreign Language': [
                ('Teaching English as a Foreign Language', _('Teaching English as a Foreign Language')),
            ],
            'School of Architecture and Environmental Design': [
                ('Regional Planning', _('Regional Planning')),
                ('Architecture', _('Architecture')),
                ('Architecture - Housing', _('Architecture - Housing')),
                ('Architecture - Sustainable', _('Architecture - Sustainable')),
                ('Architecture - Technology', _('Architecture - Technology')),
                ('Architecture - Cultural and Educational Spaces', _('Architecture - Cultural and Educational Spaces')),
                ('Architecture - Health Care Spaces', _('Architecture - Health Care Spaces')),
                ('Land Spaces Architecture', _('Land Spaces Architecture')),
                ('Industrial Design', _('Industrial Design')),
                ('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Urban Heritage', _('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Urban Heritage')),
                ('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Architectural Heritage', _('Conservation and Restoration of Historical Buildings and Fabrics – Conservation and Restoration of Architectural Heritage')),
                ('Urban Design', _('Urban Design')),
                ('Urban Planning', _('Urban Planning')),
            ],
            'School of Automotive Engineering': [
                ('Automotive Engineering - Automobile Dynamic Systems Design', _('Automotive Engineering - Automobile Dynamic Systems Design')),
                ('Automotive Engineering - Power Train', _('Automotive Engineering - Power Train')),
                ('Automotive Engineering - Body and Structure', _('Automotive Engineering - Body and Structure')),
                ('Automotive Engineering - Automotive Electronics & Electrical Engineering', _('Automotive Engineering - Automotive Electronics & Electrical Engineering')),
            ],
            'School of Chemical Petroleum and Gas Engineering': [
                ('Process Modeling Simulation & Control', _('Process Modeling Simulation & Control')),
                ('Mineral Chemical Engineering', _('Mineral Chemical Engineering')),
                ('Separation Processes', _('Separation Processes')),
                ('Kinetic and Catalysis', _('Kinetic and Catalysis')),
                ('Thermodynamics', _('Thermodynamics')),
                ('Polymer Engineering', _('Polymer Engineering')),
                ('Hydrocarbon Reservoir Engineering', _('Hydrocarbon Reservoir Engineering')),
                ('Process Design Engineering', _('Process Design Engineering')),
            ],
            'School of Civil Engineering': [
                ('Structural Engineering', _('Structural Engineering')),
                ('Earthquake Engineering', _('Earthquake Engineering')),
                ('Construction Management and Engineering', _('Construction Management and Engineering')),
                ('Geotechnical Engineering', _('Geotechnical Engineering')),
                ('Road and Transportation Engineering', _('Road and Transportation Engineering')),
                ('Transportation', _('Transportation')),
                ('Water Resources Management', _('Water Resources Management')),
                ('Water Engineering and Hydraulic Structures', _('Water Engineering and Hydraulic Structures')),
                ('Environmental Engineering', _('Environmental Engineering')),
                ('Marine Structures Engineering', _('Marine Structures Engineering')),
            ],
            'School of Computer Engineering': [
                ('Software Engineering', _('Software Engineering')),
                ('Artificial Intelligence & Robotics', _('Artificial Intelligence & Robotics')),
                ('Computer Systems Architecture', _('Computer Systems Architecture')),
                ('Computer Engineering - Computer Networks', _('Computer Engineering - Computer Networks')),
            ],
            'School of Electrical Engineering': [
                ('Communication Systems', _('Communication Systems')),
                ('Power Systems', _('Power Systems')),
                ('Control Systems', _('Control Systems')),
                ('Bio-Electrics', _('Bio-Electrics')),
                ('Digital Electronic Systems', _('Digital Electronic Systems')),
                ('Electronic Integrated Circuits', _('Electronic Integrated Circuits')),
                ('Electrical Machines and Power Electronics', _('Electrical Machines and Power Electronics')),
                ('Electromagnetic Fields and Waves', _('Electromagnetic Fields and Waves')),
            ],
            'School of Industrial Engineering': [
                ('Information Technology Engineering - Electronic Commerce', _('Information Technology Engineering - Electronic Commerce')),
                ('Systems Optimization', _('Systems Optimization')),
                ('Supply Chain and Logistic Engineering', _('Supply Chain and Logistic Engineering')),
                ('Engineering Management', _('Engineering Management')),
                ('Socio-Economic Macro Systems', _('Socio-Economic Macro Systems')),
                ('Project Management', _('Project Management')),
                ('Financial Engineering', _('Financial Engineering')),
            ],
            'School of Mathematics': [
                ('Pure Mathematics - Algebra', _('Pure Mathematics - Algebra')),
                ('Pure Mathematics - Geometry', _('Pure Mathematics - Geometry')),
                ('Pure Mathematics - Analysis', _('Pure Mathematics - Analysis')),
                ('Applied Mathematics - Numerical Analysis', _('Applied Mathematics - Numerical Analysis')),
                ('Applied Mathematics - Operation Research', _('Applied Mathematics - Operation Research')),
                ('Mathematics Statistics', _('Mathematics Statistics')),
            ],
            'School of Mechanical Engineering': [
                ('Applied Design', _('Applied Design')),
                ('Energy Conversion', _('Energy Conversion')),
                ('Manufacturing', _('Manufacturing')),
                ('Biomechanics', _('Biomechanics')),
            ],
            'School of Metallurgy and Materials Engineering': [
                ('Extractive Metallurgy', _('Extractive Metallurgy')),
                ('Ceramics Engineering', _('Ceramics Engineering')),
                ('Materials Selection', _('Materials Selection')),
                ('Bio-Materials', _('Bio-Materials')),
                ('Metals Casting', _('Metals Casting')),
                ('Metals Forming', _('Metals Forming')),
            ],
            'School of Advanced Technologies': [
                ('Nanotechnology - Materials', _('Nanotechnology - Materials')),
                ('Energy Systems - Energy and Environment|', _('Energy Systems - Energy and Environment|')),
                ('Satellite Engineering', _('Satellite Engineering')),
            ],
            'School of Physics': [
                ('Photonics', _('Photonics')),
                ('Condensed Matter Physics', _('Condensed Matter Physics')),
                ('Laser Optics Physics', _('Laser Optics Physics')),
            ],
            'School of Management, Economy and Progress Engineering': [
                ('Master of Business Administration (MBA) - Marketing', _('Master of Business Administration (MBA) - Marketing')),
                ('Master of Business Administration (MBA) - Strategy', _('Master of Business Administration (MBA) - Strategy')),
                ('Management of Technology (MOT) - Technological Innovation', _('Management of Technology (MOT) - Technological Innovation')),
                ('Management of Technology (MOT) - Technological Transfer', _('Management of Technology (MOT) - Technological Transfer')),
                ('Management of Technology (MOT) - Research & Development Policies', _('Management of Technology (MOT) - Research & Development Policies')),
                ('Information Technology Management-E-Business', _('Information Technology Management-E-Business')),
                ('Entrepreneurship - New Businesses', _('Entrepreneurship - New Businesses')),
                ('Industrial Engineering - Macro Systems', _('Industrial Engineering - Macro Systems')),
                ('Economic Development and Planning', _('Economic Development and Planning')),
                ('Economic Systems Planning', _('Economic Systems Planning')),
            ],
            'School of Railway Engineering': [
                ('Railway Transportation Engineering', _('Railway Transportation Engineering')),
                ('Railway Rolling Stock Engineering', _('Railway Rolling Stock Engineering')),
                ('Railway Track and Structures Engineering', _('Railway Track and Structures Engineering')),
                ('Electric Railways Engineering', _('Electric Railways Engineering')),
                ('Railway Safety Engineering', _('Railway Safety Engineering')),
                ('Railway Control and Signaling', _('Railway Control and Signaling')),
            ],
        }
    },
    'P.H.D': {
        'items': [
            ('Department of Chemistry', _('Department of Chemistry')),
            ('School of Architecture and Environmental Design', _('School of Architecture and Environmental Design')),
            ('School of Automotive Engineering', _('School of Automotive Engineering')),
            ('School of Chemical Petroleum and Gas Engineering', _('School of Chemical Petroleum and Gas Engineering')),
            ('School of Civil Engineering', _('School of Civil Engineering')),
            ('School of Computer Engineering', _('School of Computer Engineering')),
            ('School of Electrical Engineering', _('School of Electrical Engineering')),
            ('School of Industrial Engineering', _('School of Industrial Engineering')),
            ('School of Mathematics', _('School of Mathematics')),
            ('School of Mechanical Engineering', _('School of Mechanical Engineering')),
            ('School of Metallurgy and Materials Engineering', _('School of Metallurgy and Materials Engineering')),
            ('School of Physics', _('School of Physics')),
            ('School of Management, Economy and Progress Engineering', _('School of Management, Economy and Progress Engineering')),
            ('School of Railway Engineering', _('School of Railway Engineering')),
        ],
        'data': {
            'Department of Chemistry': [
                ('Analytical Chemistry', _('Analytical Chemistry')),
                ('Inorganic Chemistry', _('Inorganic Chemistry')),
                ('Organic Chemistry', _('Organic Chemistry')),
                ('Physical Chemistry', _('Physical Chemistry')),
            ],
            'School of Architecture and Environmental Design': [
                ('Architecture', _('Architecture')),
                ('Urbanism', _('Urbanism')),
            ],
            'School of Automotive Engineering': [
                ('Automotive Engineering - Automobile Dynamic Systems Design', _('Automotive Engineering - Automobile Dynamic Systems Design')),
                ('Automotive Engineering - Power Train', _('Automotive Engineering - Power Train')),
                ('Automotive Engineering - Body and Structure', _('Automotive Engineering - Body and Structure')),
            ],
            'School of Chemical Petroleum and Gas Engineering': [
                ('Chemical Engineering', _('Chemical Engineering')),
            ],
            'School of Civil Engineering': [
                ('Structural Engineering', _('Structural Engineering')),
                ('Earthquake Engineering', _('Earthquake Engineering')),
                ('Construction Management and Engineering', _('Construction Management and Engineering')),
                ('Geotechnical Engineering', _('Geotechnical Engineering')),
                ('Road and Transportation Engineering', _('Road and Transportation Engineering')),
                ('Transportation', _('Transportation')),
                ('Water Resources Management', _('Water Resources Management')),
                ('Water Engineering and Hydraulic Structures', _('Water Engineering and Hydraulic Structures')),
                ('Environmental Engineering', _('Environmental Engineering')),
                ('Marine Structures Engineering', _('Marine Structures Engineering')),
            ],
            'School of Computer Engineering': [
                ('Software Engineering', _('Software Engineering')),
                ('Artificial Intelligence & Robotics', _('Artificial Intelligence & Robotics')),
                ('Computer Systems Architecture', _('Computer Systems Architecture')),
                ('Computer Engineering - Computer Networks', _('Computer Engineering - Computer Networks')),
            ],
            'School of Electrical Engineering': [
                ('Communication Systems', _('Communication Systems')),
                ('Power Systems', _('Power Systems')),
                ('Electronics', _('Electronics')),
                ('Control Systems', _('Control Systems')),
                ('Bio-Electrics', _('Bio-Electrics')),
                ('Electromagnetic Fields and Waves', _('Electromagnetic Fields and Waves')),
            ],
            'School of Industrial Engineering': [
                ('Information Technology Engineering - Electronic Commerce', _('Information Technology Engineering - Electronic Commerce')),
                ('Systems Optimization', _('Systems Optimization')),
                ('Supply Chain and Logistic Engineering', _('Supply Chain and Logistic Engineering')),
                ('Engineering Management', _('Engineering Management')),
                ('Socio-Economic Macro Systems', _('Socio-Economic Macro Systems')),
                ('Quality & Productivity', _('Quality & Productivity')),
            ],
            'School of Mathematics': [
                ('Pure Mathematics - Algebra', _('Pure Mathematics - Algebra')),
                ('Pure Mathematics - Geometry', _('Pure Mathematics - Geometry')),
                ('Pure Mathematics - Analysis', _('Pure Mathematics - Analysis')),
                ('Applied Mathematics - Numerical Analysis', _('Applied Mathematics - Numerical Analysis')),
                ('Applied Mathematics - Operation Research', _('Applied Mathematics - Operation Research')),
                ('Applied Mathematics - Statistics', _('Applied Mathematics - Statistics')),
            ],
            'School of Mechanical Engineering': [
                ('Mechanical Engineering', _('Mechanical Engineering')),
                ('Dynamics Control and Vibration', _('Dynamics Control and Vibration')),
                ('Solid Mechanics', _('Solid Mechanics')),
                ('Energy Conversion', _('Energy Conversion')),
                ('Manufacturing', _('Manufacturing')),
            ],
            'School of Metallurgy and Materials Engineering': [
                ('Materials Engineering', _('Materials Engineering')),
            ],
            'School of Physics': [
                ('Condensed Matter Physics', _('Condensed Matter Physics')),
                ('Laser Optics Physics', _('Laser Optics Physics')),
            ],
            'School of Management, Economy and Progress Engineering': [
                ('Management of Technology (MOT) - Technological Innovation', _('Management of Technology (MOT) - Technological Innovation')),
                ('Management of Iranian Public Organization', _('Management of Iranian Public Organization')),
                ('Science of Technology Policy', _('Science of Technology Policy')),
            ],
            'School of Railway Engineering': [
                ('Railway Rolling Stock Engineering', _('Railway Rolling Stock Engineering')),
                ('Railway Track and Structures Engineering', _('Railway Track and Structures Engineering')),
                ('Railway Control and Signaling', _('Railway Control and Signaling')),
            ],
        }
    }
}


class RedisKeys:
    activate_account = "activate_account"
    forget_password = "forget_password"

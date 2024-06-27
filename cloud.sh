#!/usr/bin/env bash

cat <<'EOF'
----------------------------------------------
----------> Repthon Is Starting  <----------
----------------------------------------------
                                                  
                                                  
                                                  
Copyright (C) 2020-2024 by rogerpq@Github, < https://github.com/rogerpq >.
This file is part of < https://github.com/Repthon-Arabic/RepthonAr > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/Repthon-Arabic/RepthonAr/blob/web/LICENSE >
All rights reserved.
EOF

gunicorn app:app --daemon && python -m repthon

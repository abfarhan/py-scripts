@echo off

If "%1"=="" (
    echo "Error: please provide technology name (eg: 'angular' or 'react')"
) else (
    if "%2"=="" (
        echo "Error: please provide a project name"
    ) else (
         if "%1" == "angular" (
             if "%3" == "" (
                python create_angular_script.py %2
                REM python E:\z-Python\py-script\create_angular_script.py %2
             )
             if "%3" == "--skip-install" (
                 python create_angular_script.py %2 %3
                REM  python E:\z-Python\py-script\create_angular_script.py %2 %3
             )
           
        )
        if "%1" == "react" (
            python create_react_script.py %2
            REM python E:\z-Python\py-script\create_react_script.py %2
        )
        if "%1" == "js" (
            python create_js_script.py %2
            REM python E:\z-Python\py-script\create_js_script.py %2
        )
    )
)
REM pause

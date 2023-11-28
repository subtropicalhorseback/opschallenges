
### prevents echo for script
@echo off

### allows ! to be used to access variables' values
setlocal enabledelayedexpansion 

### takes the user input for a given source path and defines the variable
set /p sourcePath=Enter the source folder path: 

### takes the user input for a given destination path and defines the variable
set /p destinationPath=Enter the destination folder path:

### next line - opens IF for what to do if the source path doesn't exist; prints an error response
if not exist "!sourcePath!\" (
echo Error: Source folder does not exist.
goto :eof
)

### next line - opens IF for what to do if the destination path doesn't exist; prints an error response
if not exist "!destinationPath!\" (
    echo Error: Destination folder does not exist.
    goto :eof
)

### actually executes the robocopy from source to destination
robocopy "!sourcePath!" "!destinationPath!" /E

### reports errors if robocopy didn't complete successfully or success if it worked fine
if errorlevel 8 (
    echo Error: ROBOCOPY encountered errors during the copy operation.
) else (
    echo Copy operation completed successfully.
)           

### required syntax close
:end   

### ends the use of the ! - required syntax close
endlocal   
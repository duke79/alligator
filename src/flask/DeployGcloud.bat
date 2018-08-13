@echo off

REM Fetch the last version

if exist gcloud_app.version (
	for /f %%a in (gcloud_app.version) do (
		set gcloud_app_version=%%a
	)
	set /P same_version=Do you want to continue with the same version %gcloud_app_version% y/n ?

	IF /i %same_version%==y set same_version=1
	IF /i %same_version%==yes set same_version=1
)

if not %same_version% == 1 (
	set /P gcloud_app_version=Enter the new version 
	echo %gcloud_app_version% > gcloud_app.version
)
gcloud app deploy -v %gcloud_app_version%


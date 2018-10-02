# Screaming Bunny Utils

## Installing
### On a standalone System
- Install requires Python 3.6+ and pip
    
    ```bash
    pip install git+https://gitlab.labs.g2-inc.net/ScreamingBunny/Utils.git
    ```
        
- To update if already installed
	 
   ```bash
	pip install --upgrade git+https://gitlab.labs.g2-inc.net/ScreamingBunny/Utils.git
   ```
   
### Gitlab CI
- Installing requires a download of the current artifacts from the CI of Utils
-  All edits are done to `.gitlab-ci.yml`, `requirements.txt`, and `Dockerfile`
	1. Add to the variables

		```yaml
		variables:
			...
			UTILS_URL: https://gitlab.labs.g2-inc.net/ScreamingBunny/Utils/-/jobs/artifacts/master/download?job=Build-Wheel
		```
	2. Add to `before_script`
			
		```yaml
		...
		before_script:
			...
			- apk add --no-cache curl
			- curl --header "JOB-TOKEN: $CI_JOB_TOKEN" "$UTILS_URL"
		...
		```
	3. Add to requirements.txt file
		- ScreamingBunny_Utils
	
	4. Add to the Dockerfile

		```DockerFile
		...
		ADD SB_UTILS.*.zip /tmp/SB_UTILS.zip
		...
		RUN ...
		mkdir -p /tmp/SB_UTILS && \
		unzip /tmp/SB_UTILS.zip -d /tmp/SB_UTILS && \
		pip3 install -r requirements.txt --find-links file:///tmp/SB_UTILS && \
		...
		```
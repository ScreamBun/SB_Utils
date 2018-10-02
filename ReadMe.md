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
- Installing requires a download of hte current artifacts from the CI pipeline and an install of the artifacts
	1. Add to the variables of hte job

		```yaml
		variables:
			...
			UTILS_URL: https://gitlab.labs.g2-inc.net/ScreamingBunny/Utils/-/jobs/artifacts/master/download?job=Build-Wheel
		```
	2. Add before docker build 
		
		```bash
		curl --header "JOB-TOKEN: $CI_JOB_TOKEN" "$UTILS_URL"
		```
	3. Add to requiremtns.txt file
		- ScreamingBunny_Utils
	
	4. Add to the docker file

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
	
    
wget --no-check-certificate 
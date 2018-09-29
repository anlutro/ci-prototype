# ci-tool (prototype)

This is a WIP for a small CI tool I'm building in my spare time out of frustration with Jenkins.

Check out the [examples](examples) directory for what my ideas for the structure of the pipeline syntax is.

## Ideas

- everything is a shell script, don't try to embed a secondary prorgramming language
- everything is declarative, pipelines can't change based on context (but features like skipping steps still needs to be implemented)
- infinitely nested steps
- various execution methods for steps: local, ssh, docker

## Implementation

- python 3.5+
	- web application (json api)
	- queue worker
- git/github support
	- pipeline definition in yaml file in the git repo
	- one "job template" per repository
	- one job per git push, tag, pr (configurable, optional white/blacklisting)

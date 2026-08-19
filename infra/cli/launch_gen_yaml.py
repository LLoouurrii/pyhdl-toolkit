from PipelineBuilder.PipelineBuilder import PipelineBuilder

pipeline = PipelineBuilder("manual_test.yml")

prepare = pipeline.add_job(job_name="prepare", 
                           runs_on="ubuntu-latest")

prepare.add_step(name_step="Checkout code", 
                 uses="actions/checkout@v5")

prepare.add_step(name_step="Setup Python",
                 python_version="3.11")

cmd_install_dependencies = "echo 'Prepare env here'"
prepare.add_step(name_step="Install dependencies",
                 cmd=cmd_install_dependencies)

test = pipeline.add_job(job_name="test", 
                        runs_on="ubuntu-latest",
                        needs="prepare")

test.add_step(name_step="Checkout code", 
                 uses="actions/checkout@v5")

cmd_launch_test = "echo 'Test here...'"
test.add_step(name_step="Run tests", 
                 cmd=cmd_launch_test)

deploy = pipeline.add_job(job_name="deploy", 
                        runs_on="ubuntu-latest",
                        needs="test")

cmd_deployment = "echo 'Deploy result here...'"

deploy.add_step(name_step="Deploy result here...", 
                 cmd=cmd_deployment)

pipeline.write_pipeline()
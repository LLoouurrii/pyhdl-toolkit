from PipelineBuilder.PipelineBuilder import PipelineBuilder
from JobBuilder.JobBuilder import JobBuilder
from ruamel.yaml import YAML

yaml = YAML()

pipeline = PipelineBuilder("manual_test_ci.yml")

prepare = pipeline.add_job(job_name="prepare", runs_on="ubuntu-latest")
prepare.add_step(name_uses="Checkout code")

data = pipeline.return_data()

file = "manual_test_ci.yml"

with open("manual_test_ci.yml", "w") as f:
    yaml.dump(data, f, )



# prepare = pipeline.create_job(job_name="prepare",
#                            runs_on="ubuntu-latest")

# prepare.add_step(step_name="Checkout code",
#                  uses="checkout@v5")
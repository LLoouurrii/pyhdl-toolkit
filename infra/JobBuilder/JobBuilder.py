from PipelineBuilder.PipelineBuilder import CommentedMap, logging

logger = logging.getLogger(__name__)

class JobBuilder:
    
    def __init__(
        self, 
        job_name: str,
        runs_on: str,
        data_job: CommentedMap = CommentedMap(),
        needs: str = ""
        ):
        
        self.data_job = data_job
        self.data_steps = []
        self.job_name = job_name
        
        self.data_job[self.job_name] = {}
        self.data_job[self.job_name]["runs-on"] = runs_on
        
        if needs:
            self.data_job[self.job_name]["needs"] = needs
           
    def add_step(self, name_step: str = "", uses: str = "", python_version: str = "", cmd = "") -> None:
        
        data_this_step = CommentedMap()
        
        if name_step:
            data_this_step["name"] = name_step
        if uses:
            data_this_step["uses"] = uses
        if python_version:
            data_this_step["uses"] = "actions/setup-python@v6"
            data_this_step["with"] = {}
            data_this_step["with"]["python-version"] = python_version
        if cmd:
            data_this_step["run"] = cmd
        
        self.data_steps.append(data_this_step)
        self.data_job[self.job_name]["steps"] =  self.data_steps
        
        logging.info("Adding step '%s' to the job %s",  name_step, self.job_name)
        
        
    def return_data_job(self) -> CommentedMap:
        return self.data_job
        
from YamlHandler.YamlHandler import YamlHandler, CommentedMap

class JobBuilder:
    def __init__(self, pipeline_file, job_name, runs_on):
        
        self.pipeline_file = pipeline_file
        
        self.job_data = CommentedMap()
        
        self.job_data[f"{job_name}"] = None
        self.job_data["runs-on"] = runs_on
    
    def add_step(self, name_uses = ""):
        if name_uses:
            self.job_data[f" - {name_uses}"] = name_uses
    
    def return_data_job(self):
        return self.job_data
        
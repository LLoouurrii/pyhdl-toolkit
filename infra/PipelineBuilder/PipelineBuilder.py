from YamlHandler.YamlHandler import YamlHandler, CommentedMap
from JobBuilder.JobBuilder import JobBuilder

class PipelineBuilder:
    def __init__(self, pipeline_file, 
                descsription="New pipeline generated automatically by pyhdl-toolkit", 
                rule="workflow_dispatch"):
        
        self.pipeline_file = pipeline_file
        
        self.data = CommentedMap()
        self.data["name"] = descsription
        self.data["on"] = {}
        
        self.data["on"]["workflow_dispatch"] = None
    
    def add_job(self, job_name, runs_on):
        job = JobBuilder(pipeline_file=self.pipeline_file, job_name=job_name, runs_on=runs_on)
        self.data["jobs"] = job.return_data_job()
        
        return job
        
        
    
    def return_data(self):
        print(self.data)
        
        self.data.yaml_set_comment_before_after_key("on", before="\n")
        self.data.yaml_set_comment_before_after_key("jobs", before="\n")
        
        return self.data
        
    #     self.jobs = {}

    #     self.pipeline_file = YamlHandler(pipeline_file)
    #     self.pipeline_file.clean_yaml()
        
    #     data = {
    #         "name": f"{descsription}",
    #     }
        
    #     self.pipeline_file.write_yaml(data=data)
    #     self.pipeline_file.line_break()
        
    #     data = {
    #         'on': {
    #             f"{rule}": None
    #         }
    #     }
        
    #     self.pipeline_file.write_yaml(data=data)
    #     self.pipeline_file.line_break()

    # def create_job(self, job_name, runs_on):
        
    #     job = JobBuilder(pipeline_file=self.pipeline_file,
    #                     job_name=job_name, 
    #                     runs_on=runs_on)
        
    #     self.jobs[job_name] = job
        
    #     return job
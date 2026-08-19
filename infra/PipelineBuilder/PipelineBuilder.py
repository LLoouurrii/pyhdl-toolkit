from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from typing import Self
from pathlib import Path
import logging
import json

from JobBuilder.JobBuilder import JobBuilder

class PipelineBuilder:
    
    @staticmethod
    def configure():
        if not logging.getLogger().handlers:
            logging.basicConfig(
                level=logging.INFO,
                format="[%(asctime)s] - [%(levelname)s] %(message)s",
                datefmt="%Y-%m-%d %I:%M:%S %p")
    
    def __init__(
        self, 
        pipeline_file: str, 
        descsription: str ="New pipeline generated automatically by pyhdl-toolkit", 
        rule: str =""
        ):
        
        self.configure()
        
        self.pipeline_file = pipeline_file
        self.data_pipeline = CommentedMap()
        self.job = {}
        
        self.data_pipeline["name"] = descsription
        self.data_pipeline["on"] = {}
        self.data_pipeline["on"]["workflow_dispatch"] = None
        
        path_workflow = Path(".github/workflows/")
        path_workflow.mkdir(parents=True, exist_ok=True)
        self.pipeline_file = Path(path_workflow) / self.pipeline_file
        
        logging.debug("Workflow directory: %s", path_workflow.resolve())
    
    def add_job(self, job_name: str, runs_on: str, needs: str = "") -> JobBuilder:
        
        logging.info("Adding job %s to the pipeline %s",  job_name, self.pipeline_file)
        
        self.job[job_name] = JobBuilder(job_name=job_name, runs_on=runs_on, needs=needs)
        self.data_pipeline["jobs"] = self.job[job_name].return_data_job()

        return self.job[job_name]
        
    def write_pipeline(self) -> CommentedMap:
        
        logging.info("Starting pipeline file generation %s", self.pipeline_file)
        
        yaml = YAML()
        
        self.data_pipeline.yaml_set_comment_before_after_key("on", before="\n")
        self.data_pipeline.yaml_set_comment_before_after_key("jobs", before="\n")
        
        logging.info("Witring data in %s \n%s", self.pipeline_file, json.dumps(self.data_pipeline, indent=2))
        
        with open(self.pipeline_file, "w") as f:
            yaml.dump(self.data_pipeline, f)
            
        logging.info("Pipeline successfully written")
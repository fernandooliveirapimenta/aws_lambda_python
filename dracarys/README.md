docker build -t fernando107/dracarys:latest
docker push fernando107/dracarys:latest

docker run -p 8083:8083 --env-file aws-stepfunctions-local-credentials.txt amazon/awsstepfunctions-local

### Aws step functions
```

  "Comment": "A Hello World example of the Amazon States Language using Pass states",
  "StartAt": "Hello",
  "States": {
    "Hello": {
      "Type": "Pass",
      "Result": "Pass",
      "Next": "DracarysJob"
    },
    "DracarysJob": {
      "Type": "Task",
      "Resource": "arn:aws:states:::batch:submitJob.sync",
      "Parameters": {
        "JobName": "ExecStepFunctionJob",
        "JobQueue": "arn:aws:batch:us-east-1:046741928853:job-queue/dracarysFila",
        "JobDefinition": "arn:aws:batch:us-east-1:046741928853:job-definition/dracarysDefinicao:1",
         "ContainerOverrides": {
           "Environment": [ 
               { 
                  "Name": "FERNANDO",
                  "Value": "stepFunction"
               }
            ]
        }
      },
      "End": true
    }
    
  }
}
```
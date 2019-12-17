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

### Aws batch 

```
Ambiente Compu.
Visão geral
Nome do ambiente computacional: dracarysAmbienteComputacional
Nome de região da Amazon (ARN) do ambiente computacional: arn:aws:batch:us-east-1:046741928853:compute-environment/dracarysAmbienteComputacional
Nome do cluster do ECS: arn:aws:ecs:us-east-1:046741928853:cluster/dracarysAmbienteComputacional_Batch_8a23809e-6d41-3c6f-a5d9-d144b7630d07
Tipo: MANAGED
Status: VALID
Estado: ENABLED
Função de serviço: arn:aws:iam::046741928853:role/service-role/AWSBatchServiceRole
Recursos computacionais
Mínimo de vCPUs: 0
vCPUs desejados: 0
Máximo de vCPUs: 4
Tipos de instância: optimal
Estratégia de alocação: BEST_FIT
Modelo de execução--
Versão do modelo de execução
Função da instância: arn:aws:iam::046741928853:instance-profile/ecsInstanceRole

Def trabalho.
Requisitos de recurso
Função de trabalho: arn:aws:iam::046741928853:role/ecsTaskAdm
Imagem do contêiner: fernando107/dracarys
vCPUs: 2
Memória: 1024 MiB
```
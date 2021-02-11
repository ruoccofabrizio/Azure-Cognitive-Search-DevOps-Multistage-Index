# Azure-Cognitive-Search-DevOps-Multistage-Index

Azure DevOps YAML pipeline to deploy an Azure Cognitive Search index in multiple environments (DEV, TEST, PROD)
The scripts creates specified indexes or updates (with additional fields) existing indexes. Field removal is not allowed.

![Azure DevOps Stages](/images/stages.PNG)
![Azure DevOps Jobs](/images/jobs.PNG)



| Azure DevOps Variable                          | Value                                                      | Note                                           |
|------------------------------------------------|---------------------------------------------------------|------------------------------------------|
| --ENV_SERVICE          			| Azure Cognitive Search Service              								 | Required					    |
| --ENV_SERVICE_KEY      			| Azure Cognitive Search Service Key 								 | Required                        |
| --ENV_INCLUDE            			| Indexes to create / modify (COMMA SEPARATED e.g. index1,index2,index3)				 | OPTIONAL - If not specified it applies to all indexed not present in the ENV_ESCLUDE variable|
| --ENV_ESCLUDE          			| Indexes to exclude from update (COMMA SEPARATED e.g. index1,index2,index3) |  |
| --ENV_INDEX_FILE_PATH      			| File path fot the index json definition  								 | Required |

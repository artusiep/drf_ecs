APP_NAME 			?=
AWS_REGION			?=
ENVIRONMENT 		?=
AWS_CLI				?=
GITHUB_REPO_OWNER 	?=
GITHUB_REPO_NAME 	?=
GITHUB_DEPLOYMENT_BRANCH ?=

PHONY += init-repo check_aws_profile_environment_var
PHONY += verify_elastic_container_registries_stack create_elastic_container_registries_stack
PHONY += verify_s3_codepipeline_artifact_bucket_stack create_s3_codepipeline_artifact_bucket_stack
PHONY += verify_cluster_security_groups_stack create_cluster_security_groups_stack
PHONY += verify_cluster_ecs_stack create_cluster_ecs_stack
PHONY += verify_ecs_container_draining_lambda_stack create_ecs_container_draining_lambda_stack
PHONY += verify_cluster_load_balancer_stack create_cluster_load_balancer_stack
PHONY += verify_ecs_resources_stack create_ecs_resources_stack
PHONY += verify_deployment_pipeline_stack create_deployment_pipeline_stack
PHONY += verify_CI_stack create_CI_stack
PHONY += create_cloud_formation_stacks

.PHONY: $(PHONY)

.EXPORT_ALL_VARIABLES:

init-repo:
	python3 -m venv venv
	( \
		. venv/bin/activate; \
		pip3 install --quiet --no-cache-dir --upgrade pip; \
		pip3 install --quiet --no-cache-dir --requirement requirements.txt; \
	)

check_aws_profile_environment_var:
	[ ! -z "$${AWS_PROFILE}" ] || \
		(echo "Authenticate to AWS using aws-mfa and set AWS_PROFILE!" && exit 1)


verify_elastic_container_registries_stack: check_aws_profile_environment_var
	$(AWS_CLI) cloudformation validate-template --template-body file://stacks/elastic-container-registries.yaml

create_elastic_container_registries_stack: verify_elastic_container_registries_stack
	$(AWS_CLI) cloudformation create-stack \
		--template-body file://stacks/elastic-container-registries.yaml \
		--parameters ParameterKey=Environment,ParameterValue=${ENVIRONMENT} \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		--region ${AWS_REGION} \
		--stack-name "${ENVIRONMENT}-${APP_NAME}-elastic-container-registries-${AWS_REGION}"
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "${ENVIRONMENT}-${APP_NAME}-elastic-container-registries-${AWS_REGION}" \
		--region ${AWS_REGION} \



verify_s3_codepipeline_artifact_bucket_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/s3-codepipeline-artifact-bucket.yaml

create_s3_codepipeline_artifact_bucket_stack: verify_s3_codepipeline_artifact_bucket_stack
	${AWS_CLI} cloudformation create-stack \
		--template-body file://stacks/s3-codepipeline-artifact-bucket.yaml \
		--parameters ParameterKey=Environment,ParameterValue=${ENVIRONMENT} \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		--region ${AWS_REGION} \
		--stack-name "${ENVIRONMENT}-${APP_NAME}-s3-codepipeline-artifact-bucket-stack-${AWS_REGION}"
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "${ENVIRONMENT}-${APP_NAME}-s3-codepipeline-artifact-bucket-stack-${AWS_REGION}" \
		--region ${AWS_REGION} \



verify_cluster_security_groups_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/cluster-security-groups.yaml

create_cluster_security_groups_stack: verify_cluster_security_groups_stack
	${AWS_CLI} cloudformation create-stack \
		--template-body file://stacks/cluster-security-groups.yaml \
		--parameters ParameterKey=Environment,ParameterValue=${ENVIRONMENT} \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		--capabilities CAPABILITY_IAM \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-cluster-security-groups-stack-$(AWS_REGION)"
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-cluster-security-groups-stack-$(AWS_REGION)"



verify_cluster_ecs_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/cluster-ecs.yaml

create_cluster_ecs_stack: verify_cluster_ecs_stack
	${AWS_CLI} cloudformation create-stack \
		--template-body file://stacks/cluster-ecs.yaml \
		--parameters ParameterKey=Environment,ParameterValue=${ENVIRONMENT} \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		ParameterKey=CustomAmiId,ParameterValue=${CUSTOM_AMI_ID} \
		--capabilities CAPABILITY_IAM \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-cluster-ecs-stack-$(AWS_REGION)"
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-cluster-ecs-stack-$(AWS_REGION)"



verify_bastion_host_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/bastion-host.yaml

create_bastion_host_stack: verify_bastion_host_stack
	${AWS_CLI} cloudformation create-stack \
		--template-body file://stacks/bastion-host.yaml \
		--parameters ParameterKey=Environment,ParameterValue=${ENVIRONMENT} \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		ParameterKey=CustomAmiId,ParameterValue=${CUSTOM_AMI_ID} \
		--capabilities CAPABILITY_IAM \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-bastion-host-$(AWS_REGION)"
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-bastion-host-$(AWS_REGION)"



verify_ecs_container_draining_lambda_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/ecs-container-draining-lambda.yaml

create_ecs_container_draining_lambda_stack: verify_ecs_container_draining_lambda_stack
	${AWS_CLI} cloudformation create-stack \
		--template-body file://stacks/ecs-container-draining-lambda.yaml \
		--parameters ParameterKey=Environment,ParameterValue=${ENVIRONMENT} \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		--capabilities CAPABILITY_IAM \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-ecs-container-draining-lambda-$(AWS_REGION)"
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-ecs-container-draining-lambda-$(AWS_REGION)"



verify_cluster_load_balancer_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/cluster-load-balancer.yaml

create_cluster_load_balancer_stack: verify_cluster_load_balancer_stack
	${AWS_CLI} cloudformation create-stack \
		--template-body file://stacks/cluster-load-balancer.yaml \
		--parameters ParameterKey=Environment,ParameterValue=$(ENVIRONMENT) \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-cluster-load-balancer-stack-$(AWS_REGION)" \
		--capabilities CAPABILITY_IAM
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-cluster-load-balancer-stack-$(AWS_REGION)"



verify_ecs_resources_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/ecs-resources.yaml

create_ecs_resources_stack: verify_ecs_resources_stack
	${AWS_CLI} cloudformation create-stack \
		--template-body file://stacks/ecs-resources.yaml \
		--parameters ParameterKey=Environment,ParameterValue=${ENVIRONMENT} \
		 ParameterKey=AppName,ParameterValue=${APP_NAME} \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-ecs-resources-stack-$(AWS_REGION)" \
		--capabilities CAPABILITY_IAM
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-ecs-resources-stack-$(AWS_REGION)"



verify_deployment_pipeline_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/deployment-pipeline.yaml

create_deployment_pipeline_stack: verify_deployment_pipeline_stack
	${AWS_CLI} cloudformation create-stack \
		--parameters \
		ParameterKey=Environment,ParameterValue=$(ENVIRONMENT) \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		ParameterKey=GitHubRepoName,ParameterValue=${GITHUB_REPO_NAME} \
		ParameterKey=GitHubDeploymentBranch,ParameterValue=${GITHUB_DEPLOYMENT_BRANCH} \
		ParameterKey=GitHubRepoOwner,ParameterValue=${GITHUB_REPO_OWNER} \
		--template-body file://stacks/deployment-pipeline.yaml \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-deployment-pipeline-$(AWS_REGION)" \
		--capabilities CAPABILITY_IAM
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "$(ENVIRONMENT)-${APP_NAME}-deployment-pipeline-$(AWS_REGION)"



verify_CI_stack: check_aws_profile_environment_var
	${AWS_CLI} cloudformation validate-template --template-body file://stacks/continuous-integration.yaml

create_CI_stack: verify_CI_stack
	${AWS_CLI} cloudformation create-stack \
		--parameters \
		ParameterKey=AppName,ParameterValue=${APP_NAME} \
		ParameterKey=GitHubRepoName,ParameterValue=${GITHUB_REPO_NAME} \
		ParameterKey=GitHubRepoOwner,ParameterValue=${GITHUB_REPO_OWNER} \
		--template-body file://stacks/continuous-integration.yaml \
		--stack-name "${APP_NAME}-CI-$(AWS_REGION)" \
		--capabilities CAPABILITY_IAM
	${AWS_CLI} cloudformation wait stack-create-complete \
		--stack-name "${APP_NAME}-CI-$(AWS_REGION)"



create_cloud_formation_stacks:
	$(MAKE) create_elastic_container_registries_stack
	$(MAKE) create_s3_codepipeline_artifact_bucket_stack
	$(MAKE) create_cluster_security_groups_stack
	$(MAKE) create_cluster_ecs_stack
	$(MAKE) create_ecs_container_draining_lambda_stack
	$(MAKE) create_cluster_load_balancer_stack
	$(MAKE) create_ecs_resources_stack
	$(MAKE) create_deployment_pipeline_stack
	$(MAKE) create_CI_stack

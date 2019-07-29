# DRF-ECS

DRF-ECS is a project connecting Django Rest Framework with highly scalable AWS ECS service.
It reduce lots of development time by providing ready to use CICD pipeline on AWS development 
tools like Code Build and CodePipeline which are fairly cheep for small teams development.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

It is needed to have installed [pip](https://pypi.org/project/pip/) and [docker](https://docs.docker.com/install/)

### Installing

TODO 

## Running the tests

TODO

## Deployment

TODO

## Databases

For now Django is using sqlite3 for all Environments. 
Future work will include adding dockerized mysql and postgres on local development stage.

`dev`, `qa`, `prod` environments will be using RDS instances. 


## Built With

* [Django](https://www.djangoproject.com/) - Framework upon which Django Rest Framework was created.
* [DRF](https://www.django-rest-framework.org) - ramework is a powerful and flexible toolkit for building Web APIs.
* [AWS Cloudformation](https://aws.amazon.com/cloudformation/) - AWS functionality for [Infrastructure as Code](https://en.wikipedia.org/wiki/Infrastructure_as_code).
* [AWS ECS](https://aws.amazon.com/ecs/) - Amazon Elastic Container Service (Amazon ECS) is a highly scalable, high-performance container orchestration service that supports Docker containers and allows you to easily run and scale containerized applications on AWS.



## Contributing

Please read [CONTRIBUTING.md](https://github.com/artusiep/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Artur Siepietowski** - *Initial work* - [artusiep](https://github.com/artusiep)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* 

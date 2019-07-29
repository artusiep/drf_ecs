APP_NAME 			?= drf_ecs
VERSION				?= 0.0.1

.EXPORT_ALL_VARIABLES:

init-repo:
	python3 -m venv venv
	( \
		. venv/bin/activate; \
		pip3 install -r drf_ecs/requirements.txt; \
	)

build_drf_ecs_image:
	docker build \
	-t "${APP_NAME}:latest" \
	-t "${APP_NAME}:${VERSION}" \
	drf_ecs/

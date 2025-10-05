set -eo pipefail # 밑으로 실행 하다가 실패하면 더이상 진행하지 않음 (0: 성공, 0 X: 실패)

COLOR_GREEN=`tput setaf 2;` # 성공했을때 색을 초록으로
COLOR_NC=`tput sgr0;` # No Color

echo "Starting black"
poetry run black .
echo "OK"

echo "Starting ruff"
poetry run ruff check --select I --fix # 인포트 정렬을 수행해라
poetry run ruff check --fix # linter을 수행해라
echo "OK"

echo "Starting mypy"
poetry run mypy .
echo "OK"

echo "Starting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
echo "OK"

echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"
# 모든 테스트 끝나면 초록색으로 문자 나오기
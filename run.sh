
# shellcheck disable=SC2164
cd tests
while [ -n "$1" ]
do
    pytest -vv -n2 --driver chrome --url $1 --alluredir=../allure-results
shift
done

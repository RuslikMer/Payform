
# shellcheck disable=SC2164
cd tests
while [ -n "$1" ]
do
    pytest -vv -n4 --driver chrome --url https://payform.ru/
shift
done

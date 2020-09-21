#!/bin/bash

SOURCE_DIR=$( cd $(dirname $0) ; pwd -P )
source "${SOURCE_DIR}/.colors.sh"

GRADE="${SOURCE_DIR}/grade.tsv"

function finish {
  echo -e "\e[0m"
}
trap finish EXIT

function grade {
    if [[ "${2}" -eq 0 ]]; then
	echo -e -n "${Bold_Green}${3}"
	echo -n "${3}" >> "${GRADE}"
    else
	echo -e -n "${Bold_Red}0"
	echo -n "0" >> "${GRADE}"
    fi
    echo -e -n "${Bold_Black}/${3} points" 1>&2
    echo -e    "\t${Color_Off}${1}" 1>&2
    echo -e "\t${3}\t${1}" >> "${GRADE}"
}

rm -f ${GRADE}

grade "Does the file hello.sh exist?" $(if [[ -f "${SOURCE_DIR}/hello.sh" ]]; then echo 0 ; else echo 1 ; fi) 2

grade "Does the file hello.sh start with a bash shebang?" "$(head -n 1 ${SOURCE_DIR}/hello.sh 2> /dev/null | grep -q '#!/bin/bash' &> /dev/null && echo 0 || echo 1)" 2

grade "Is the file hello.sh executable?" $(if [[ -x "${SOURCE_DIR}/hello.sh" ]]; then echo 0 ; else echo 1 ; fi) 2

grade "Do you have a comment (that is at least 7 words long) on line 2 describing how the script works?" $(if [[ $(tail -n +2 hello.sh | head -n 1 | grep "^#") ]] && (( $(tail -n +2 hello.sh | head -n 1 | sed 's,^#,,' | wc -w) >= 7 )) ; then echo 0 ; else echo 1 ; fi) 2

grade "Does the script produce the expected output?" $(if [[ "$(bash ${SOURCE_DIR}/hello.sh 2> /dev/null)" == $"Hello, world" ]]; then echo 0 ; else echo 1 ; fi) 2

grade "Have you added and committed your work to git using a meaningful commit message?" $(if [[ $(git rev-list --all --count 2> /dev/null) -gt 1 ]] && [[ $(git log -1 --pretty=%B 2> /dev/null | wc -w) -gt 1 ]]; then echo 0 ; else echo 1 ; fi) 2

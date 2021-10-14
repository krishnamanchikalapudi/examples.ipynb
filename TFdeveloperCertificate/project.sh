#!/bin/bash
arg=${1}

default(){
    echo "Action argument length is ZERO. So, executing default action: Clean, Build"

    clean
        
    build
}

code_coverage() {
    # ref: https://github.com/marketplace/actions/github-action-for-pylint
    pylint --confidence=HIGH --exit-zero -v -E -s y -f json -j 4 scripts/ tests/
    # pylint --confidence=HIGH --exit-zero -v -E -s y -j 4 scripts/ tests/
}
clean() {
    find . -type f -name .DS_Store -exec rm -r {} \+
    find . -type d -name __pycache__ -exec rm -r {} \+
}
build() {
    python3 -q setup.py clean
    python3 -q setup.py install

    dependency
    compile   
}
dependency() {
    pip3 install -r requirements.txt
}
compile() {
    python3 -m compileall .
}
tests() {
    python3 -m unittest tests/utils/FileExtenTests.py 
    python3 -m unittest tests/utils/ConvolutionalNeuralNetworksTests.py
}

# -n string - True if the string length is non-zero.
if [[ -n $arg ]] ; then
    arg_len=${#arg} 
    # uppercase the argument
    arg=$(echo ${arg} | tr [a-z] [A-Z] | xargs)


    echo "Action: ${arg} and length is NOT ZERO: ${arg_len}"
    echo "Python version: {`python3 -V`}"
    echo "PIP version: {`pip3 -V`}"

    if  [[ "CLEAN" == "${arg}" ]] ; then # Clean Python __pycache__ folders
        clean

    elif  [[ "BUILD" == "${arg}" ]] ; then  # compile code before excute commands
        build

    elif  [[ "DEPENDENCY" == "${arg}" ]] ; then  # compile 
        dependency
        
    elif  [[ "COMPILE" == "${arg}" ]] ; then  # compile 
        compile

    elif  [[ "LINT" == "${arg}" ]] ; then
        code_coverage

    elif [[ "TEST" == "${arg}" ]] || [[ "TESTS" == "${arg}" ]] ; then   # TEST
        tests
    
    else
       default
    fi
else 
    default
fi
#!/bin/bash

for i in $(find . -type f -name \*.png);
do
    echo "## Processing ${i}";

    ollama run moondream "describe this image ${i}" \
        > "${i//.png/_generated.txt}";

    echo "summarize this text so that it can be used as alt text for an image: $(cat ${i//.png/_generated.txt})" \
        | ollama run tinyllama > "${i//.png/.txt}";

    echo "## Comparing texts"
    cat "${i//.png/_generated.txt}"
    echo "-------------------"
    cat "${i//.png/.txt}"
    echo
    echo
    echo
    echo
done


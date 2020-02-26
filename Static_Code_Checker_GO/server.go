package main

import (
	"fmt"
	"net/http"
)

// HelloServer a basic server implement
func HelloServer(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}

// compareStrings compares 2 strings and returns them as pretty printed
func compareStrings(original string, generated string) {
	var comparison = ""
	var length = 0

	if len(original) > len(generated) {
		length = len(original)
	} else {
		length = len(generated)
	}

	for i := 0; i < length; i++ {
		if i < len(original) && i < len(generated) {

		}

	}
}

func main() {
	http.HandleFunc("/", HelloServer)
	http.ListenAndServe(":8080", nil)
}

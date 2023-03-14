#include <stdio.h>
#include <curl/curl.h>
#include <string.h>
#include <stdlib.h>

size_t write_callback(char *ptr, size_t size, size_t nmemb, void *userdata) {
    size_t num_bytes = size * nmemb;
    char *response = (char *) ptr;
    printf("%s", response);
    printf("OK");
    //printf("%.*s", (int) num_bytes, response);
    return num_bytes;
}

char *getcont(char user[], char day[]) {
    char *url = NULL;
    url = malloc(strlen("https://github.com/") + strlen(user) + 1);
    if (url == NULL) {
        printf("Failed to allocate memory.");
        return NULL;
    }
    strcat(url, "https://github.com/");
    strcat(url, user);
    CURL *curl;
    CURLcode res;
    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            return curl_easy_strerror(res);
        }
        curl_easy_cleanup(curl);
    }
    return "";
}



int main() {
    char *test = getcont("An013r", "23-03-13");
    //printf("%s", test);
    return 0;
}
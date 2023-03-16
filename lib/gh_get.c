// I don't know C so I use ChatGPT to translate the python code to C. 
// it is currently not memory safe and will crash if you use an invalid user.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

long len = 0;

int getcont(char* user, char* day, int returnformalday);

size_t write_callback(void *contents, size_t size, size_t nmemb, void *userp) {
    char **data = (char **)userp;
    size_t realsize = size * nmemb;
    char *ptr = realloc(*data, len + realsize + 1);
    if(ptr == NULL) {
        fprintf(stderr, "realloc() failed\n");
        return 0;
    }
    *data = ptr;
    memcpy(&((*data)[len]), contents, realsize);
    len += realsize;
    (*data)[len] = '\0';
    return realsize;
}

int getcont(char* user, char* day, int returnformalday) {
    CURL *curl;
    CURLcode res;
    char *url = malloc(strlen(user) + 20);
    sprintf(url, "https://github.com/%s", user);
    char *data = NULL;
    long len = 0;
    int cont = 0;
    int formalday = 0;
    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &data);
        res = curl_easy_perform(curl);
        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
                    curl_easy_strerror(res));
        }
        else {
            char *p = strstr(data, "js-calendar-graph-svg");
            char *q = strstr(p, "</g>  </svg>");
            if (p != NULL && q != NULL) {
                len = q - p;
                p[len] = '\0';
                char *line = strtok(p, "\n");
                while (line != NULL) {
                    if (strstr(line, day) != NULL) {
                        char *cont_str = strstr(line, "\">") + 2;
                        char *cont_end = strstr(cont_str, " contribution");
                        if (cont_end != NULL) {
                            *cont_end = '\0';
                            cont = atoi(cont_str);
                        }
                        if (returnformalday) {
                            char *formalday_str = strstr(line, "contribution") + 16;
                            char *formalday_end = strstr(formalday_str, "</rect>");
                            if (formalday_end != NULL) {
                                *formalday_end = '\0';
                                formalday = atoi(formalday_str);
                            }
                        }
                        break;
                    }
                    line = strtok(NULL, "\n");
                }
            }
        }
        curl_easy_cleanup(curl);
        free(url);
        free(data);
    }
    return returnformalday ? formalday : cont;
}

int main() {
    int cont = getcont("An013r", "0af3-18", 0);
    printf("%d\n", cont);
    return 0;
}
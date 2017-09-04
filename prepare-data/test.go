// Copyright 2016 Jun Zhou <zhoujun06@gmail.com>. All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	//"encoding/json"
	"flag"
	"fmt"
	"github.com/google/go-github/github"
	"golang.org/x/oauth2"
	//"io/ioutil"
	"os"
	"strings"
	"time"
)

const GitKeeperToken string = "278fe67e76634258f6cde89e341364d4145d672d"

const xFile = "./data3-x.json"
const yFile = "./data3-y.json"

type Result struct {
	Title  string
	Body   string
	Labels []string
}

func NewClient(token string) *github.Client {
	flag.CommandLine.Parse([]string{})

	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: token},
	)

	tc := oauth2.NewClient(oauth2.NoContext, ts)
	client := github.NewClient(tc)
	return client
}

func main() {

	results := []Result{}
	client := NewClient(GitKeeperToken)
	xf, err := os.OpenFile(xFile, os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		panic(err)
	}
	yf, err := os.OpenFile(yFile, os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		panic(err)
	}
	defer xf.Close()
	defer yf.Close()

	//Since:     time.Date(2016, time.January, 1, 0, 0, 0, 0, time.UTC),
	page := 0
	for len(results) < 50000 {
		page = page + 1
		ops := github.IssueListByRepoOptions{
			State:     "all",
			Direction: "asc",
			ListOptions: github.ListOptions{
				Page:    page,
				PerPage: 100,
			},
		}

		issues, _, err := client.Issues.ListByRepo("kubernetes", "kubernetes", &ops)
		if err != nil {
			fmt.Println(err)
		}
		if len(issues) == 0 {
			break
		}
		fmt.Printf("number: %d\n", len(issues))
		for _, issue := range issues {
			labels := []string{}
			fmt.Println(*issue.Number)
			if len(issue.Labels) > 0 && issue.Title != nil && issue.Body != nil {
				for _, l := range issue.Labels {
					if strings.HasPrefix(*l.Name, "area") ||
						strings.HasPrefix(*l.Name, "sig") ||
						strings.HasPrefix(*l.Name, "kind") {
						labels = append(labels, *l.Name)
					}
				}

				if len(labels) == 0 {
					continue
				}

				res := Result{
					Title:  *issue.Title,
					Body:   *issue.Body,
					Labels: labels,
				}

				results = append(results, res)
				xf.WriteString(strings.Replace(strings.Replace((res.Title+" "+res.Body), "\r\n", " ", -1), "\n", " ", -1) + "\n")
				yf.WriteString(strings.Join(res.Labels, ",") + "\n")
			}
		}

		fmt.Println("sleep 1 seconds before next api call")
		time.Sleep(1 * time.Second)
	}

	//data, err := json.MarshalIndent(results, "", "    ")

	if err != nil {
		fmt.Println(err)
	}

	//ioutil.WriteFile(resultFile, data, 0644)
	//	for _, issue := range issues {
	//		fmt.Printf("Title: %d, %s\n", *issue.ID, *issue.Title)
	//		if issue.Labels != nil {
	//			for _, l := range issue.Labels {
	//				fmt.Printf("Label: \t%s\n", *l.Name)
	//			}
	//		}
	//	}
}

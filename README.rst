PyAWS Lambda
============

Amazon published AWS Lambda and API Gateway service which runs a simple function providing managed scalability. Developer can focus on writing code without concerns of server, includes auto-scaling, deploy automation, etc.

But currently AWS Lambda has a poor UI. Developer should write a function, ZIP codes, upload via API, wire the function with API Gateway endpoint. If you need several functions, it's hard to maintain it by hand.

Here PyAWS-Lambda comes in. Our purpose is automate the process. Finally, if a developer wants to build a web service, write a set of functions in a shape of micro web framework, just like flask, and simple deploy it with one command line execution.

There is already an evolving framework, Serverless (formerly JAWS), but it supports only Javascript for now and uses CloudFormation which is heavy to understand. PyAWS-Lambda aims a lightweight script-like tool also for python.

Below is an example of project.

Directory structure:

- Project root
    - project.yaml
    - urls.yaml
    - modules
        - function1.py
        - function2.py
        - function3
            - __init__.py
            - run.py

project.yaml

.. code-block:: yaml

    project-name: test-lambda
    domain: test-lambda.mydomain.com
    depedencies:
       - django==1.8.0
    functions:
       - function_name: series
         role: arn:aws:iam::<iam>:role/lambda_basic_execution
         handler: series.json
         publish: true
       - function_name: hello
         role: arn:aws:iam::<iam>:role/lambda_basic_execution
         handler: hello.say
         publish: true

urls.yaml

.. code-block:: yaml

    urls:
      - path: /series
        method: GET
        function:
          handler: series.json
          role: lambda_basic_execution
      - path: /hello
        method: GET
        function:
          handler: hello.say

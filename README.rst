PyAWS Lambda
============

Background
----------

Amazon published AWS Lambda and API Gateway service which runs a simple function providing managed scalability. Developer can focus on writing code without concerns of server, includes auto-scaling, deploy automation, etc.

But currently AWS Lambda has a poor UI. Developer should write a function, ZIP codes, upload via API, wire the function with API Gateway endpoint. If you need several functions, it's hard to maintain it by hand.

Here PyAWS-Lambda comes in. Our purpose is automate the process. Finally, if a developer wants to build a web service, write a set of functions in a shape of micro web framework, just like flask, and simple deploy it with one command line execution.

There is already an evolving framework, Serverless (formerly JAWS), but it supports only Javascript for now and uses CloudFormation which is heavy to understand. PyAWS-Lambda aims a lightweight script-like and python friendly tool.


Take a look
-----------

Directory structure::

   Project root/
      project.yaml
      urls.yaml
      modules/
         function1.py
         function2.py
         function3/
            __init__.py
            run.py

project.yaml

.. code-block:: yaml

    name: test-lambda
    depedencies:
       - django==1.8.0
    configurations:
       defaults:
          role: arn:aws:iam::<iam>:role/lambda_basic_execution
    functions:
       - function_name: series
         handler: series.json
         publish: true
       - function_name: hello
         handler: hello.say
         publish: true
    domain: test-lambda.mydomain.com
    urls:
      - path: /series
        method: GET
        function: series
      - path: /hello
        method: GET
        function: hello


Usage (planned)::

    pyaws-lambda createproject <project-name>
    pyaws-lambda deploy


Alternatives
------------

There are some serverless frameworks leveraging AWS Lambda and API Gateway.

* Serverless_: Built on node.js and only support javascript runtime for now.
* Apex_: Built on Go and supports node.js, go, python.
* Zappa_: Serverless WSGI with AWS lambda + API Gateway

.. _Serverless: https://github.com/serverless/serverless
.. _Apex: https://github.com/apex/apex
.. _Zappa: https://github.com/Miserlou/django-zappa


TODO
----

* Add API gateway setup part
* Separate layers to enchance testability

# Dagster Cloud CI/CD GitHub Action Quickstart

Template to get started with the [Dagster Cloud CI/CD GitHub Action](https://github.com/dagster-io/dagster-cloud-cicd-action).

For complete documentation on the CI/CD action, see [Continuous Integration in the Cloud docs](https://docs.dagster.cloud/guides/continuous-integration).

## Create a new repository from this template

Click the `Use this Template` button and provide details for your new repo.

![Creating a copy of the Template repo](https://user-images.githubusercontent.com/10215173/138138429-7a81e4d7-8fdf-4988-9758-2babcc90af5f.png)

## Modify GitHub Workflow

Edit the [GitHub Workflow](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#create-an-example-workflow) at
[`/.github/workflows/dagster-cloud-cicd.yml`](./.github/workflows/dagster-cloud-cicd.yml) to set up Docker registry access. Uncomment the step associated with your
registry (ECR, DockerHub, GCR etc.)

## Set up secrets

Set up the secrets listed in the Docker registry access step, as well as `DAGSTER_CLOUD_ORGANIZATION`, `DAGSTER_CLOUD_DEPLOYMENT`, and `DAGSTER_CLOUD_AGENT_TOKEN`,
in your GitHub repository's Settings page.

`DAGSTER_CLOUD_ORGANIZATION` and `DAGSTER_CLOUD_DEPLOYMENT` should specify the deployment to target, e.g. `hooli` and `prod`. `DAGSTER_CLOUD_AGENT_TOKEN` should contain an [agent token](https://docs.dagster.cloud/auth#managing-user-and-agent-tokens), e.g. `agent:hooli:1193cb69aaa34cfz83d44adcfe89b057`.

![GitHub settings page](https://user-images.githubusercontent.com/10215173/164542909-78f7b580-96e4-44a2-990e-d85cb1ec9319.png)

## Modify `locations.yaml`

The `locations.yaml` file in the root of the repository specifies the code locations to build and
the Docker registries to push the built images to. Modify the `registry` field to point to your
Docker registry, and update the location's name as desired.

The default code location builds using the Python `requirements.txt` file, using the `base_image`
listed in the locations file. You may alternatively provide your own Dockerfile, removing the
`base_image` field.

You may also want to move your code to a subdirectory. In this case, simply point the `build` field
at the new directory containing either your `requirements.txt` file or Dockerfile.

```yaml
locations:
  # Code location name
  github_action_template_foo:
    # Path to build directory, which must contain a Dockerfile or
    # requirements.txt file, relative to the locations.yaml folder
    build: .

    # The base Docker image to install your code in
    # If providing a custom Dockerfile, this line is not needed
    base_image: python:3.8-slim

    # Fill in your Docker registry here, on Dockerhub, ECR, GCR, etc.
    registry: REGISTRY_HERE

    # Python file containing the job repo
    # Can alternatively supply python_module
    python_file: repo.py
```

## Verify Builds are Successful

At this point, the Workflow should complete successfully. If builds are failing, ensure that your
secrets are properly set up the Workflow properly sets up Docker regsitry access.

![Screen Shot 2021-10-20 at 10 02 55 AM](https://user-images.githubusercontent.com/10215173/138138556-d147000f-c42d-4ab1-8187-3d6be3786142.png)

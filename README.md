# Dagster Cloud CI GitHub Action Quickstart

Template to get started with the [Dagster Cloud CI GitHub Action](https://github.com/dagster-io/dagster-cloud-ci-action).

## Create a new repository from this template

Click the `Use this Template` button and provide details for your new repo

## Modify GitHub Workflow

Edit the [GitHub Workflow](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#create-an-example-workflow) at
[`/.github/workflows/dagster-cloud-ci.yml`](./.github/workflows/dagster-cloud-ci.yml) to set up Docker registry access. Uncomment the step associated with your
registry (ECR, DockerHub, GCR etc.)

Next, update the `dagit-url` to point to your Dagster Cloud deployment. This should have
the format `https://{organization}.dagster.cloud/{deployment}`.

## Set up secrets

Set up the secrets listed in the Docker registry access step, as well as the `DAGSTER_AGENT_TOKEN`,
in your GitHub repository's Settings page.

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
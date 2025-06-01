import argparse
import json
import requests
import time
import random

WORKFLOW_PATH = "api.json"
COMFY_URL = "http://localhost:8188"


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Process ComfyUI prompts")

    # Add arguments
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="The main prompt for generation",
    )
    parser.add_argument(
        "--neg-prompt",
        type=str,
        required=False,
        help="The negative prompt for generation",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=50,
        help="Number of steps for generation (default: 50)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Seed for generation (if not provided, will generate random)",
    )

    # Parse arguments
    args = parser.parse_args()

    # Load the workflow
    with open(WORKFLOW_PATH, "r") as f:
        workflow = json.load(f)

    # Get the prompt
    workflow["6"]["inputs"]["text"] = args.prompt

    # Get the negative image
    workflow["7"]["inputs"]["text"] = args.neg_prompt

    # Get the steps
    workflow["3"]["inputs"]["steps"] = args.steps

    # Handle seed
    if args.seed is not None:
        # Use command line seed if provided
        workflow["3"]["inputs"]["seed"] = args.seed
    else:
        workflow["3"]["inputs"]["seed"] = random.randint(0, 2**32 - 1)

    print("Parameters:")
    print(f"Prompt: {args.prompt}")
    print(f"Negative Prompt: {args.neg_prompt}")
    print(f"Steps: {args.steps}")
    print(f"Seed: {workflow['3']['inputs']['seed']}")
    print("--------------------------------")

    response = requests.post(
        f"{COMFY_URL}/prompt", json={"prompt": workflow, "client_id": "script_runner"}
    )
    data = response.json()

    prompt_id = data["prompt_id"]
    # Check the history for the results
    while True:
        r = requests.get(f"{COMFY_URL}/history/{prompt_id}")
        result = r.json()
        if prompt_id in result:
            outputs = result[prompt_id]["outputs"]
            output_image = outputs["9"]["images"][0]["filename"]

            break
        time.sleep(1)

    print(f"Output image: ComfyUI/output/{output_image}")


if __name__ == "__main__":
    main()

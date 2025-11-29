# config.py  (complete file)
# Central model and parameter configuration used by your app.

from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# Model parameters (same as you originally used)
PARAMETERS = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
}

# Model IDs
LLAMA3_MODEL_ID = "meta-llama/llama-3-2-11b-vision-instruct"
GRANITE_MODEL_ID = "ibm/granite-3-8b-instruct"

# Updated Mixtral model ID — replaced mistralai/mistral-large (unsupported) with
# mistralai/mistral-medium-2505 which is supported in your environment.
MIXTRAL_MODEL_ID = "mistralai/mistral-medium-2505"

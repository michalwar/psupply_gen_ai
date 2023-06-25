# %%
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

import pandas as pd


# ============================================================
# %%
df = pd.read_csv("data/raw_orders_df.csv")

df.head()


# %%
# ============================================================
model_type = "tiiuae/falcon-40b"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained(model)


# %%
# ============================================================
model = AutoModelForCausalLM.from_pretrained(
    model_type, 
    trust_remote_code=True,
    low_cpu_mem_usage=True)


pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    device=0,
)


# %%
# ============================================================
# Prompt Engineering

main_task = f"Identify potential risk related to the order delievery based on the order details and the customer details."
context_prompt = f"Take into consideration Key Risk Indication (KRI) and Key Performance Indication (KPI) to identify potential risk related to the order delievery based on the order details and the customer details."
base_context_raw_data = df.to_dict('records')

main_prompt = main_task + "\n" + context_prompt + "\n" + str(base_context_raw_data) 


sequences = pipeline(
    main_prompt,
    max_length=300,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")









model = r"C:\Users\micha\.cache\huggingface\hub\models--tiiuae--falcon-40b\snapshots\c47b371b31a68349c233104050ac76680b8485db"


"""
model = AutoModelForCausalLM.from_pretrained(
    model, 
    trust_remote_code=True,
    low_cpu_mem_usage=True).to(torch.device('cpu'))
"""


"""


"""
import streamlit as st
import requests

st.set_page_config(page_title="Cloud Storage Misconfiguration Scanner", page_icon="🔐")

st.title("🔐 Cloud Storage Misconfiguration Scanner")
st.markdown("""
Check AWS S3 buckets and Azure Blob containers for potential **public exposure**.

Paste a list of bucket/container URLs below — one per line.
""")

def check_s3_bucket(url):
    """Check if an S3 bucket is publicly accessible."""
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return "❌ PUBLIC — Objects may be listed or downloaded"
        elif r.status_code == 403:
            return "✅ Private — Access correctly restricted"
        elif r.status_code == 404:
            return "⚠️ Bucket not found"
        else:
            return f"ℹ️ Unexpected response: {r.status_code}"
    except Exception:
        return "⚠️ Error connecting to bucket"


def check_azure_blob(url):
    """Check if an Azure Blob container is public."""
    if not url.endswith("/"):
        url = url + "/"
    test_url = url + "?restype=container&comp=list"

    try:
        r = requests.get(test_url, timeout=5)
        if r.status_code == 200:
            return "❌ PUBLIC — Container listing enabled"
        elif r.status_code == 403:
            return "✅ Private — No anonymous access"
        elif r.status_code == 404:
            return "⚠️ Container not found"
        else:
            return f"ℹ️ Unexpected response: {r.status_code}"
    except Exception:
        return "⚠️ Error connecting to container"


# ------------------------------------
# INPUT SECTION
# ------------------------------------

urls_input = st.text_area(
    "Enter S3 or Azure Blob URLs (one per line)",
    height=200,
    placeholder="https://mybucket.s3.amazonaws.com\nhttps://mycontainer.blob.core.windows.net",
)

if st.button("Scan Buckets"):
    if not urls_input.strip():
        st.warning("Enter at least one URL.")
    else:
        urls = [u.strip() for u in urls_input.split("\n") if u.strip()]

        st.subheader("📊 Scan Results")

        for url in urls:
            st.write(f"### 🔍 {url}")

            if "s3.amazonaws.com" in url or ".s3." in url:
                result = check_s3_bucket(url)
            elif "blob.core.windows.net" in url:
                result = check_azure_blob(url)
            else:
                result = "❓ Unknown service — must be S3 or Azure Blob"

            st.write(result)

        st.markdown("---")
        st.subheader("🛡️ Security Recommendations")

        st.markdown("""
        - Disable **public access** unless absolutely required  
        - For AWS:  
          - Block Public Access at the **account** and **bucket** level  
          - Use least privilege IAM policies  
        - For Azure:  
          - Disable public container access  
          - Use SAS tokens for controlled sharing  
        - Always enable logging + monitoring for storage access  
        """)

st.markdown("---")
st.caption("Built by Frank Garcia · Cloud Security Demo Project")

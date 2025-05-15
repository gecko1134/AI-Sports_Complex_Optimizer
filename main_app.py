import streamlit as st
import importlib.util
from pathlib import Path

st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin Suite")

categories = {
    "Memberships": "memberships",
    "Dome Usage": "dome_usage",
    "Governance": "governance",
    "Personnel": "personnel",
    "Finance": "finance",
    "AI Engine": "ai_engine",
    "Events": "events"
}

category = st.sidebar.selectbox("Choose Category", list(categories.keys()))
selected_folder = categories[category]
tool_dir = Path(__file__).parent / selected_folder

if tool_dir.exists():
    tool_files = [f for f in tool_dir.glob("*.py") if f.name != "__init__.py"]
    tool_names = [f.stem for f in tool_files]
    selected_tool = st.sidebar.selectbox("Choose Tool", tool_names)

    tool_path = tool_dir / f"{selected_tool}.py"
    if tool_path.exists():
        spec = importlib.util.spec_from_file_location("module", str(tool_path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.run()
    else:
        st.error(f"Tool not found: {tool_path}")
else:
    st.error(f"Folder not found: {tool_dir}")
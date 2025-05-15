import streamlit as st
import importlib.util
from pathlib import Path

st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin Suite")

categories = {
    "Membership Tools": "memberships",
    "Dome Usage & Events": "dome_usage",
    "Governance Tools": "governance",
    "Personnel & Leagues": "personnel",
    "Finance & Risk": "finance",
    "NIL + AI Tools": "ai_engine"
}

selection = st.sidebar.selectbox("Choose Tool Category", list(categories.keys()))
selected_folder = categories[selection]
tool_dir = Path(__file__).parent / selected_folder

if tool_dir.exists():
    module_files = [f for f in tool_dir.glob("*.py") if f.name != "__init__.py"]
    tool_names = [f.stem for f in module_files]
    selected_tool = st.sidebar.selectbox("Tool", tool_names)

    module_path = tool_dir / f"{selected_tool}.py"
    if module_path.exists():
        spec = importlib.util.spec_from_file_location("module", str(module_path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.run()
    else:
        st.error(f"Module file not found: {module_path}")
else:
    st.error(f"Directory not found: {tool_dir}")
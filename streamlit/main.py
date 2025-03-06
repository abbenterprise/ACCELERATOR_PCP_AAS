import streamlit as st
import json
st.set_page_config(layout="wide")

class FileReader:
    def __init__(self, filename: str, filetype: None|str = None) -> None:
        self.filename = filename
        self.filetype = filetype if filetype != None else filename.split(".")[-1]
        self._data = None

    def read_json(self) -> dict:
        with open(self.filename, "r") as file:
            data = json.load(file)

        return data

    def read(self):
        match self.filetype:
            case "json":
                self._data = self.read_json()
            case _:
                raise Exception("This file type is currently not supported.")
    @property
    def data(self):
        return self._data
        

# -------------------------------------------- VIEW LAYER ---------------------------------------------------

# -------------------------------------------- Template LAYER ---------------------------------------------------

# -------------------------------------------- Template LAYER ---------------------------------------------------

st.title("PCP AAS Accelerator App")

main_tab, template_tab, data_mapping_tab, download_tab = st.tabs(["Main Page", "Template", "Data Mapping", "Download AAS"])
template = FileReader("template.json")
template.read()

with main_tab:
    st.subheader("#TODO - BLA BLA BLA BLA. Input test")

with template_tab:
    st.write(template.data)

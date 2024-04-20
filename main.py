import streamlit as st
import pandas as pd


st.title("Toto je metoda: title")
st.header("Toto je metoda: header")
st.subheader("Toto je metoda: subheader")
st.text("Toto je metoda text")
st.markdown("Ukázka **tučného** písma.")
st.markdown("Toto je *kurzíva*.")
st.markdown("# Ukázka nadpisu h1")
st.markdown("## Ukázka nadpisu h2")
st.markdown("### Ukázka nadpisu h3")
st.markdown("Tady bude odkaz na [Google](https://www.google.com). Klikni zde.")
json={"a":123,"b":789}
st.json(json)
st.markdown("---")
program="""
def nějaka_funkce():
    print("Pozdrav")
    return 0
"""
st.code(program,language="python", line_numbers=True)
st.metric(label="Rychlost",value="25 m/s", delta="2,5 m/s")
st.markdown("---")
tabulka=pd.DataFrame({"Sloupec 1":[1,2,3,4],"Sloupec 2":[11,12,13,14]})
tabulka.index += 1
st.table(tabulka)
st.markdown("---")
nakup = [["rohlik", 10, "kusu"],

          ["jablka", 8, "kusu"],

          ["maslo", 1, "kusu"],

          ["sunka", 200, "gramu"],

          ["mleko", 1, "litru"],

          ["vejce", 15, "kusu"]
        ]
df = pd.DataFrame(nakup, columns =["Typ", "Mnozstvi", ""])
df.index += 1
st.table(df)
st.title("Čtení dat ze souboru csv")
df=pd.read_csv("cedok.csv",sep=";")
st.table(df)
st.dataframe(df)
st.image("louvre.jpg",caption="Obrázek Louvru v Paříži")
st.video("pocasi.mp4")





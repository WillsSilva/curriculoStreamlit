import streamlit as st

# Definindo o título da página
st.set_page_config(page_title="Currículo Willian Andreola", page_icon="📄")

# Sidebar com a imagem e menu de navegação
with st.sidebar:
    st.image("EU.jpg", width=200)
    page = st.radio("Selecione uma seção", ("Início", "Cursos", "Contato", "Experiência", "Habilidades"))

sobre = ('''Desenvolvedor Back-End com 4 anos de experiência focado em ERP

Sou um desenvolvedor com 4 anos de experiência, especializado em back-end, com forte envolvimento no desenvolvimento de sistemas ERP. Ao longo da minha trajetória, tenho contribuído ativamente para a resolução de bugs e criação de novos módulos, garantindo a evolução e estabilidade de sistemas críticos. Além disso, participei da criação de APIs do zero e no desenvolvimento de aplicações para integrar diversas APIs, permitindo uma comunicação eficaz entre diferentes sistemas.

Tenho uma sólida experiência em análise e desenvolvimento de consultas SQL e sou familiarizado com bancos de dados como Microsoft SQL Server e DB2, o que me permite otimizar a performance de sistemas complexos. Minha expertise inclui tecnologias como Node.js, Python, Django, e CSS/JavaScript, com grande foco no desenvolvimento back-end.

Além de minhas habilidades técnicas, também tenho experiência com metodologias ágeis, como Scrum e Kanban, o que me ajuda a trabalhar de forma eficiente em equipes multifuncionais. Sou versátil no uso de Git e em versionamento de código, garantindo que os projetos sejam mantidos organizados e seguros.

Estou sempre aberto a desafios e novas oportunidades, com grande paixão pelo desenvolvimento, especialmente em Python, e com um interesse crescente em treinamento de LLM e LangChain. Tenho como objetivo continuar me desafiando tanto no aspecto profissional quanto pessoal, buscando sempre aprender novas tecnologias e aprimorar minhas habilidades.''')

if page == "Início":
    st.write("# Willian Andreola da Silva")
    st.markdown("## Sobre Mim")
    st.write("")
    
elif page == "Cursos":
    st.write("# 📚 Cursos")
    st.markdown("[Django Master](https://link-do-curso-django) - Curso avançado de Django.")
    st.markdown("[IA Master](https://link-curso-ia) - Curso de Inteligência Artificial.")
    
elif page == "Contato":
    st.write("# 📞 Contato")
    st.markdown("**E-mail:** wills.andreola@gmail.com")
    st.markdown("**Telefone:** +55 45 991313371")
    st.markdown("**LinkedIn:** [Perfil LinkedIn](https://www.linkedin.com/in/willian-andreola-da-silva-972a60173/)")

elif page == "Experiência":
    st.write("# 🏆 Experiência Profissional")
    st.write("**Empresa:** Group Sistemas")
    st.write("**Função:** Desenvolvedor de sistemas")
    st.write("**Período:** 2 anos em desenvolvimento de sistemas ERP.")

elif page == "Habilidades":
    st.write("# 🛠️ Habilidades")
    st.markdown("**Técnicas:** Python, Django, Git, HTML, CSS, JavaScript, SQL, Node.js")
    st.markdown("**Bancos de Dados:** SQL Server, DB2")


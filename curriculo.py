import streamlit as st

# Definindo o título da página
st.set_page_config(page_title="Currículo Willian Andreola", page_icon="📄")

# Sidebar com a imagem e menu de navegação
with st.sidebar:
    st.image("EU.jpg", width=200)
    page = st.radio("Selecione uma seção", ("Início", "Cursos", "Experiência", "Habilidades"))
    
    st.write("# Contatos:")
    email = "wills.andreola@gmail.com"
    telefone = "5545991313371"  
    linkedin = "willian-andreola-da-silva-972a60173"    

    st.link_button("💬 WhatsApp", f"https://wa.me/{telefone}")
    st.link_button("🔗 LinkedIn", f"https://www.linkedin.com/in/{linkedin}/") 
    st.link_button("📧 E-mail", f"(mailto:{email})")     

sobre = ('''Desenvolvedor Back-End com 4 anos de experiência focado em ERP

Sou um desenvolvedor com 4 anos de experiência, especializado em back-end, com forte envolvimento no desenvolvimento de sistemas ERP. Ao longo da minha trajetória, tenho contribuído ativamente para a resolução de bugs e criação de novos módulos, garantindo a evolução e estabilidade de sistemas críticos. Além disso, participei da criação de APIs do zero e no desenvolvimento de aplicações para integrar diversas APIs, permitindo uma comunicação eficaz entre diferentes sistemas.

Tenho uma sólida experiência em análise e desenvolvimento de consultas SQL e sou familiarizado com bancos de dados como Microsoft SQL Server e DB2, o que me permite otimizar a performance de sistemas complexos. Minha expertise inclui tecnologias como Node.js, Python, Django, e CSS/JavaScript, com grande foco no desenvolvimento back-end.

Além de minhas habilidades técnicas, também tenho experiência com metodologias ágeis, como Scrum e Kanban, o que me ajuda a trabalhar de forma eficiente em equipes multifuncionais. Sou versátil no uso de Git e em versionamento de código, garantindo que os projetos sejam mantidos organizados e seguros.

Estou sempre aberto a desafios e novas oportunidades, com grande paixão pelo desenvolvimento, especialmente em Python, e com um interesse crescente em treinamento de LLM e LangChain. Tenho como objetivo continuar me desafiando tanto no aspecto profissional quanto pessoal, buscando sempre aprender novas tecnologias e aprimorar minhas habilidades.''')

if page == "Início":
    st.write("# Willian Andreola da Silva")
    st.markdown("## Sobre Mim")
    st.write(sobre)
    
elif page == "Cursos":
    st.write("# 📚 Cursos")
    st.write("### Django Master - Curso avançado de Django.")
    st.write('''Aprendizado:
             
    ✅ Construção de aplicações completas com Django, do backend ao frontend      
    ✅ Implementação de sistemas de autenticação e controle de acesso
    ✅ Técnicas de deploy e otimização de performance
    ✅ Melhores práticas de segurança e escalabilidade
    ✅ Implementação da API de IA do Groq para automação de descrições e criação de conteúdo dinâmico ''')
    
    st.write("---")
    st.write("### IA Master - Curso avançado de IA.")
    st.write('''Aprendizado:
             
    ✅ Integração de IA com APIs da OpenAI (como GPT).
    ✅ Utilização de LangChain para a criação de pipelines inteligentes.
    ✅ Desenvolvimento de Agentes capazes de executar tarefas complexas de forma automatizada.
    ✅ Implementação de RAG (Retrieval-Augmented Generation), combinando bancos de dados com IA para respostas contextuais.
    ✅ Criação de aplicações interativas com Streamlit.
    ✅ Desenvolvimento de ChatBots inteligentes utilizando as melhores práticas de IA.
    ✅ Ferramentas e truques para potencializar a produtividade em projetos de IA.             
             
             ''')
    
elif page == "Experiência":
    st.write("# 🏆 Experiência Profissional")
    st.write("### **Empresa:** Group Sistemas")
    st.write("**Função:** Desenvolvedor full stack")
    st.write("**Período:** 2 anos.")
    st.write("**Atividades:**")
    st.write('''Desenvolvimento de sistemas ERP, manutenção de sistemas legados, criação de APIs, integração de sistemas, desenvolvimento de aplicações web.
            Implementação de melhorias em toda stack de módulos ERP: contas a receber, contas a
            pagar, cadastros gerais, pedidos, faturamento, contabilidade, BI, expedição e estoque, Correção de bugs, auxiliando a estabilidade, disponibilidade e integridade do sistema em
geral. Desenvolvimento de novos módulos e desenvolvimento de APIs RESTful para integração com sistemas externos. Desenvolvimento de aplicações web para integração com APIs de terceiros.          
             ''')

elif page == "Habilidades":
    st.write("# 🛠️ Habilidades")
    st.markdown("**Técnicas:** Python, Django, Git, HTML, CSS, JavaScript, SQL, Node.js")
    st.markdown("**Bancos de Dados:** SQL Server, DB2")
        


import streamlit as st
import requests 

URL = 'https://viacep.com.br/ws/{cep}/json/'


st.set_page_config(page_title='Busca CEP', page_icon='📬', layout='wide')

st.title('Busca CEP')

cep = st.text_input('Digite o CEP:')
buscar = st.button('Buscar CEP')

if buscar: 
    if cep.isdigit() and len(cep) == 8:
        try:
            resp = requests.get(URL.format(cep=cep))
            if resp.status_code == 200:
                dados = resp.json()
                
                if 'erro' in dados:
                    st.warning('CEP não encontrado. Verifique se digitou corretamente.')
                else:    
                    st.success('CEP encontrado com sucesso!')
                    st.write(f"📍 **Logradouro:** {dados.get('logradouro', 'Não informado')}")
                    st.write(f"🏘️ **Bairro:** {dados.get('bairro', 'Não informado')}")
                    st.write(f"🏙️ **Cidade:** {dados.get('localidade', 'Não informado')} - {dados.get('uf', '')}")
                    st.write(f"📮 **CEP:** {dados.get('cep', '')}")

            else:
                st.warning(f'Error - Code:  {resp.status_code} ')
                
        except Exception as e:
            st.error(f'Erro ao buscar o CEP: {e}')
    else: 
        st.error('CEP inválido. Digite o CEP somente com números e 8 digitos.')
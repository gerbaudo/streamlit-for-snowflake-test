import streamlit as st

st.title('Hierarchical data viewer')
st.header('This is a header')
st.subheader('subheader')
st.caption('capt')

st.write('write text')
st.text('just text')

st.code('var = "value"', 'python')
st.markdown('**bold**\n* item1 \n* item2')

st.divider()

st.latex('\chi^2')

st.error('error')
st.warning('warning')
st.info('info')
st.success('success')

#st.balloons()
#st.snow()
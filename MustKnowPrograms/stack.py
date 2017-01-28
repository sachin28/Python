class stack:
    list = []

    def push(self, input):
        self.list.append(input)

    def pop(self):
        print self.list.pop()


st = stack()

st.push('Sachin')
st.push('Sandeep')
st.pop()

import { createStore } from 'vuex'

export default createStore({
    state: {
        selectedUser: ""
    },
    mutations: {
        setSelectedUser(state, payload) {
            state.selectedUser = payload;
        }
    }
})
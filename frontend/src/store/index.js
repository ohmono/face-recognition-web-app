import Vue from 'vue'
import Vuex from 'vuex'
import app from "./app.module"

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    app
  }
})

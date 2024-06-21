<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">

    <ParticipantsView />

    <DrawFormView />

    <DrawsView />
  </div>
</template>

<script>
import DrawFormView from '@/views/DrawFormView.vue'
import ParticipantsView from '@/views/ParticipantsView.vue'
import DrawsView from '@/views/DrawsView.vue'

export default {
  name: 'HomeView',
  components: {
    ParticipantsView,
    DrawFormView,
    DrawsView
  }
}
</script>
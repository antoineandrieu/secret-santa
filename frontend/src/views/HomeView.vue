<template>
  <div class="home">
    <img alt="Secret Santa logo" src="../assets/secret-santa.webp">

    <ParticipantsView @update:selected="handleSelectedParticipants" />

    <DrawFormView :selected-participants="selectedParticipants" />

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
  },
  data() {
    return {
      selectedParticipants: []
    };
  },
  methods: {
    handleSelectedParticipants(participants) {
      this.selectedParticipants = participants;
    }
  }
}
</script>

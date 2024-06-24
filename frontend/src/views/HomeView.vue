<template>
  <div class="home">
    <div class="logo-container">
      <img alt="Secret Santa logo" src="../assets/secret-santa.webp" class="logo">
    </div>

    <div class="top-components">
      <ParticipantsView 
        @update:selected="handleSelectedParticipants" 
        class="participants"
      />
      <DrawFormView 
        :selected-participants="selectedParticipants" 
        class="draw-form"
      />
    </div>

    <DrawsView class="draws" />
  </div>
</template>



<style scoped>
.home {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto;
  gap: 20px;
  padding: 20px;
}

.logo-container {
  display: flex;
  justify-content: center;
}

.top-components {
  display: flex;
  gap: 20px;
}

.participants, .draw-form {
  flex: 1 1 auto;
  padding: 10px;
  background-color: #f4f4f4;
  border-radius: 8px;
  min-width: 0;
}

.draws {
  padding: 10px;
  background-color: #f4f4f4;
  border-radius: 8px;
  grid-column: 1 / -1;
}

@media (max-width: 768px) {
  .top-components {
    flex-direction: column;
  }
}
</style>



<script>
import DrawFormView from '@/views/DrawFormView.vue';
import DrawsView from '@/views/DrawsView.vue';
import ParticipantsView from '@/views/ParticipantsView.vue';

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

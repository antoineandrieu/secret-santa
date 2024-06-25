<template>
    <div class="participants-container">
        <h2>Participants</h2>
        <ul>
            <li v-for="participant in participants" :key="participant.id" class="participant-item">
                <div class="participant-info">
                    <input type="checkbox" :value="participant" v-model="selectedParticipants"
                        @change="updateSelectedParticipants">
                    {{ participant.name }} ({{ participant.email }})
                </div>
                <button @click="openBlacklistModal(participant)" class="manage-blacklist-btn">Manage Blacklist</button>
            </li>
        </ul>
        <form @submit.prevent="addParticipant" class="add-participant-form">
            <input v-model="participant.name" placeholder="Name" required class="input-field">
            <input v-model="participant.email" type="email" placeholder="Email" required class="input-field">
            <button type="submit" class="submit-btn">Add</button>
        </form>
        <blacklist-modal
            :isVisible="showModal"
            :currentParticipant="currentParticipant"
            :participants="participants"
            @close="closeModal"
            @update-success="handleSuccess"
            @update-error="handleError"
        ></blacklist-modal>
    </div>
</template>

<style scoped>
.participants-container {
    max-width: 500px;
    margin: auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h2 {
    color: #333;
}

ul {
    padding: 0;
    list-style-type: none;
    text-align: left;
}

.participant-item {
    padding: 10px;
    border-bottom: 1px solid #eee;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.participant-info {
    display: flex;
    align-items: center;
    gap: 10px;
}

.input-field {
    margin: 10px 5px 10px 0;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.submit-btn {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
}

.manage-blacklist-btn {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 8px 16px;
    font-size: 14px;
    cursor: pointer;
    border-radius: 4px;
    outline: none;
}

.add-participant-form {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
}
</style>

<script>
import axios from 'axios';
import BlacklistModal from './BlacklistModal.vue';

export default {
    components: {
        BlacklistModal
    },
    created() {
        this.fetchParticipants();
    },
    data() {
        return {
            participant: { name: '', email: '', blacklist: [] },
            participants: [],
            selectedParticipants: [],
            showModal: false,
            currentParticipant: null
        };
    },
    methods: {
        async fetchParticipants() {
            try {
                const response = await axios.get('http://localhost:8000/api/participants/');
                this.participants = response.data;
            } catch (error) {
                console.error('Error fetching participants:', error);
            }
        },
        async addParticipant() {
            try {
                const response = await axios.post('http://localhost:8000/api/participants/', this.participant);
                this.participants.push(response.data);
                this.participant = { name: '', email: '' };  // Reset form fields
            } catch (error) {
                alert('Error adding participant');
                console.error(error);
            }
        },
        updateSelectedParticipants() {
            this.$emit('update:selected', this.selectedParticipants);
        },
        openBlacklistModal(participant) {
            this.currentParticipant = participant;
            this.showModal = true;
        },
        closeModal() {
            this.showModal = false;
        },
        handleSuccess(message) {
            console.log(message);
        },
        handleError(error) {
            console.error(error);
        },
    },
}
</script>

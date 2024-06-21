<template>
    <div>
        <h1>Participants</h1>
        <ul>
            <li v-for="participant in participants" :key="participant.id">
                <input type="checkbox" :value="participant" v-model="selectedParticipants"
                    @change="updateSelectedParticipants">
                {{ participant.name }} ({{ participant.email }})
            </li>
        </ul>
        <form @submit.prevent="addParticipant">
            <input v-model="participant.name" placeholder="Name" required>
            <input v-model="participant.email" type="email" placeholder="Email" required>
            <button type="submit">Add</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            participant: {
                name: '',
                email: ''
            },
            participants: [],
            selectedParticipants: []
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
    },
    created() {
        this.fetchParticipants();
    }
}
</script>

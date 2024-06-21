<template>
    <div>
        <h1>Participants</h1>
        <ul>
            <li v-for="participant in participants" :key="participant.id">
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
            participants: []
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
                this.participant = { name: '', email: '' };
            } catch (error) {
                alert('Error adding participant');
                console.error(error);
            }
        }
    },
    created() {
        this.fetchParticipants();
    }
}
</script>

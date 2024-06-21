<template>
    <div>
        <h2>Create a Draw</h2>
        <ul>
            <li v-for="participant in selectedParticipants" :key="participant.id">
                {{ participant.name }} ({{ participant.email }})
            </li>
        </ul>
        <button @click="createDraw">Create Draw</button>

        <div v-if="draw && !errorMessage">
            <h3>Draw Created Successfully!</h3>
            <ul>
                <li v-for="result in draw.results" :key="result.id">
                    {{ result.name }} ({{ result.email }})
                </li>
            </ul>
        </div>

        <div v-if="errorMessage">
            <h3>Error Creating Draw:</h3>
            <p>{{ errorMessage }}</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    props: ['selectedParticipants'],
    data() {
        return {
            draw: null,
            errorMessage: ''
        };
    },
    methods: {
        async createDraw() {
            this.errorMessage = '';
            try {
                const response = await axios.post('http://localhost:8000/api/draws/', {
                    participants: this.selectedParticipants.map(p => p.id)
                });
                this.draw = response.data;
                console.log('Draw created:', this.draw);
            } catch (error) {
                console.error('Error creating draw:', error);
                if (error.response && error.response.status === 400) {
                    this.errorMessage = error.response.data.join(", "); // Assuming error messages are returned as an array
                } else {
                    this.errorMessage = 'An error occurred while creating the draw. Please try again.';
                }
            }
        }
    }
}
</script>

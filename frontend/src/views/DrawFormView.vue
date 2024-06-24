c<template>
    <div class="draw-container">
        <h2>Create a Draw</h2>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div> <!-- Display error messages -->
        <ul class="participant-list">
            <li v-for="participant in selectedParticipants" :key="participant.id">
                {{ participant.name }} ({{ participant.email }})
            </li>
        </ul>
        <div class="draw-results">
            <ul v-if="draws.length">
                <li v-for="draw in draws" :key="draw.id">
                    <h3>{{ formatDate(draw.date) }}</h3>
                    <ul>
                        <li v-for="participant in draw.participants" :key="participant.id">
                            {{ participant.giver.name }} is giving to {{ participant.receiver.name }}
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
        <button @click="createDraw" class="submit-btn">Create Draw</button>
    </div>
</template>


<style scoped>
.draw-container {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

h2 {
    color: #333;
}

.participant-list, .draw-results ul {
    padding: 0;
    list-style-type: none;
    text-align: left;
}

.participant-list li, .draw-results li {
    padding: 10px;
    border-bottom: 1px solid #eee;
}

.submit-btn {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: block;
    font-size: 16px;
    cursor: pointer;
    border-radius: 4px;
    margin: 2px 4px 8px 4px;
}

.error-message {
    color: red;
    margin: 10px 0;
}

</style>



<script>
import axios from 'axios';

export default {
    props: ['selectedParticipants'],
    data() {
        return {
            draws: [],
            errorMessage: ''  // Added to store potential error messages
        };
    },
    methods: {
        async createDraw() {
            try {
                const response = await axios.post('http://localhost:8000/api/draws/', {
                    participants: this.selectedParticipants.map(p => p.id)
                });
                this.draws.push(response.data);
                this.errorMessage = '';  // Clear any previous errors on success
                console.log(response);
            } catch (error) {
                if (error.response && error.response.status === 400) {
                    // Set the error message from response data if it's a 400 error
                    this.errorMessage = error.response.data[0];
                } else {
                    this.errorMessage = 'An unexpected error occurred.';  // Generic error message for other errors
                }
                console.error(error);
            }
        },
        formatDate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString(undefined, {
                year: 'numeric', month: 'long', day: 'numeric',
                hour: '2-digit', minute: '2-digit'
            });
        }
    }
}
</script>


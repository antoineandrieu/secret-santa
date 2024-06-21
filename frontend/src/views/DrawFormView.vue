<template>
    <div>
        <h1>Create a Draw</h1>
        <ul>
            <li v-for="participant in selectedParticipants" :key="participant.id">
                {{ participant.name }} ({{ participant.email }})
            </li>
        </ul>
        <button @click="createDraw">Create Draw</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    props: ['selectedParticipants'],
    methods: {
        async createDraw() {
            try {
                const response = await axios.post('http://localhost:8000/api/draws/', {
                    participants: this.selectedParticipants.map(p => p.id)
                });
                console.log(response);
            } catch (error) {
                console.error(error);
            }
        }
    }
}
</script>

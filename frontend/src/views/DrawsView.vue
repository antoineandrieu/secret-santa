<template>
    <div>
        <h2>Recent Draws</h2>
        <ul>
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
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            draws: []
        };
    },
    methods: {
        async fetchDraws() {
            try {
                const response = await axios.get('http://localhost:8000/api/draws/');
                this.draws = response.data;
            } catch (error) {
                console.error('Error fetching draws:', error);
            }
        },
        formatDate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString(undefined, {
                year: 'numeric', month: 'long', day: 'numeric',
                hour: '2-digit', minute: '2-digit'
            });
        }
    },
    created() {
        this.fetchDraws();
    }
}
</script>
